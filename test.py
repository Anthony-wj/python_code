import pymysql
dt = "2022-03-17 16:28:59"
prov = "长沙"
isp = "电信"
bandwidth = 69


db = pymysql.connect(host='123.56.3.24',
                         user='sc',
                         password='123456',
                         database='python')
print(dir(db))
cursor = db.cursor()
sql = "INSERT INTO nginx_log(log_dt, province, isp, bandwidth) VALUES (%s, %s, %s, %s)"
cursor.execute(sql, (dt, prov, isp, bandwidth))
db.commit()
db.close()