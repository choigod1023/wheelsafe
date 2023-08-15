// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
const request = require('request')
var d = new Date();
var hours = d.getHours();
var PM_or_AM = 'AM'
if (hours > 12) {
    hours = `${hours - 12}`
    PM_or_AM = 'PM'
}
else if (hours == 12) {
    hours = '12'
    PM_or_AM = 'PM'
}
else
    hours = `${hours}`
var minutes = d.getMinutes();
if (minutes < 10)
    minutes = '0' + minutes
var month = d.getMonth();
var date = d.getDate();
var day = d.getDay();
var week = ['일', '월', '화', '수', '목', '금', '토'];
var clock = document.getElementById("clock")
clock.innerHTML += `<div id="clocks">${hours} : ${minutes} ${PM_or_AM}</div>` + `<div id="day">${month + 1}월 ${date}일 ${week[day]}요일</div>`
function return_img(current_dt, sunrise, sunset, weather, clouds) {
    if ('Rain' == weather) {
        return './img/rainy.png'
    }
    else if ('Clouds' == weather && (clouds > 60)) {
        return './img/cloud.png'
    }
    else if ('Clouds' == weather && (current_dt < sunrise || current_dt > sunset)) {
        return './img/night_cloud.png'
    }
    else if ('Clouds' == weather && (sunrise < current_dt < sunset)) {
        return './img/sun_cloud.png'
    }
    else if ('Snow' == weather) {
        return './img/snow.png'
    }
    else if ('Thunderstorm' == weather) {
        return './img/storm.png'
    }
    else if ('Mist' == weather || 'Haze' == weather || 'Fog' == weather) {
        return './img/fog.png'
    }
    else if ('Clear' == weather && (current_dt < sunrise || current_dt > sunset)) {
        return './img/night_clear.png'
    }
    else if ('Clear' == weather && (sunrise < current_dt < sunset)) {
        return './img/sun_clear.png'
    }

}
request('https://m.stock.naver.com/api/json/search/searchListJson.nhn?keyword=apple', (err, res, body) => {
    stock_json = JSON.parse(body)
    var result = stock_json.result.d
    for (var i = 0; i < result.length; i++) {
        var stock = result[i]
        var stock_name = stock.nm
        var int_stock_rate = parseFloat(stock.cr).toFixed(2)
        var stock_code = stock.cd
        if (int_stock_rate > 0) {
            var stock_rate = '+' + int_stock_rate.toString()
        }
        if (stock.cd == "AAPL.O") {
            stock_code = "AAPL"
            var stock = document.getElementById('stock_name')
            var rate = document.getElementById('stock_rate')
            stock.innerHTML += `${stock_name}(${stock_code})`
            rate.innerHTML += `(${stock_rate}%)`
            if (int_stock_rate > 0) {
                rate.style.color = 'red'
            }
            else {
                rate.style.color = 'blue'
            }
        }
    }
})
request('https://api.openweathermap.org/data/2.5/onecall?lat=37.636731897070234&lon=127.03512399778694&appid=4ada87268facd87550e6a5126401fda4&units=metric', (err, res, body) => {
    weather_json = JSON.parse(body)
    var weather_hours = weather_json.hourly
    var weather_current = weather_json.current
    var weather_tomorrow = weather_json.daily[1]
    var current_dt = weather_current.dt
    var sunrise = weather_current.sunrise
    var sunset = weather_current.sunset
    if (current_dt > sunset) {
        sunrise = weather_tomorrow.sunrise
        sunset = weather_tomorrow.sunset
    }
    for (var i = 1; i < 6; i++) {
        forecast_weather_docs = weather_hours[i]
        hh = new Date(forecast_weather_docs.dt * 1000)
        forecast_hour = hh.getHours()
        if (forecast_hour > 12) {
            forecast_hour = `오후 ${forecast_hour - 12}`
        }
        else if (forecast_hour == 12) {
            forecast_hour = '오후 12'
        }
        else
            forecast_hour = `오전 ${forecast_hour}`
        forecast_weather = forecast_weather_docs.weather[0].main
        forecast_temp = Math.round(parseInt(forecast_weather_docs.temp)).toString()
        forecast_cloud = forecast_weather_docs.clouds
        forecast_hum = forecast_weather_docs.humidity
        var forecast_img = return_img(forecast_weather_docs.dt, sunrise, sunset, forecast_weather, parseInt(forecast_cloud))
        var hours = document.getElementById("hours")
        hours.innerHTML += `<li id="forecast"><div id="forecast_hour">${forecast_hour}시</div>` + `<img id="forecast_img" src = "${forecast_img}">` + `<div id="forecast_temp">${forecast_temp}°</div><div id = "forecast_cloud">${forecast_hum}%</div></li>`
    }
    var current_weather_docs = weather_current
    var current_weather = current_weather_docs.weather[0].main
    var current_temp = current_weather_docs.temp
    var current_cloud = current_weather_docs.clouds
    var current = document.getElementById("current")
    var current_hum = current_weather_docs.humidity
    var current_img = return_img(current_dt, sunrise, sunset, current_weather, parseInt(current_cloud))
    current.innerHTML += `<img id="current_img" src="${current_img}">` + `<span id = "current_info"><div id="current_temp">${current_temp}°</div><div id="current_cloud">${current_hum}%</div></div></span>`

})