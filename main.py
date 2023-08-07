info = ['장준혁','동국대','캡스']
find1 = '장준혁'
if find1 in info:
    print('%s는 %s안에 있어요'%(find1,info))
find2 = '홍길동'
if find2 not in info:
    print('%s는 %s안에 없어요'%(find2,info))