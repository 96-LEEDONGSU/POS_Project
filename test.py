import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='mydb', charset='utf8')
cur = conn.cursor()
cur.execute("SELECT c_name, c_phone, c_address, c_memo from customer")
result = cur.fetchall()
return_data = {}

for i, v in enumerate(result):
    return_data[i] = v

conn.close()

print(return_data.values())


# 위와 같은 방식으로 mysql에 존재하는 데이터를 불러와 저장할 수 있다.