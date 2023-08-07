import pymysql
from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
    

@app.route('/marker')
def show_marker():
    db = pymysql.connect(
        user='admin',
        password='jjang486',
        host='database-1-instance-1.comumtztjsvx.ap-northeast-2.rds.amazonaws.com',
        db='wheelsafe',
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
select * FROM marker
""")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)