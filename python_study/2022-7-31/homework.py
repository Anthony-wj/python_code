import requests
import json
import time
import pymysql.cursors
from multiprocessing import Pool
# 时间 省份 运营商 带宽
baseurl = "https://ip.taobao.com/outGetIpInfo?accessKey=alibaba-inc&ip="

def ip_parser(ip):
    url = baseurl + ip
    for i in range(1):
        response = requests.get(url)
        if response.status_code:
            result = json.loads(response.text)
            prov = result["data"]["city"]
            isp = result["data"]["isp"]
            return prov, isp
        else:
            time.sleep(1)

def line_parser(line):
    lines = line.split()
    ip_port = lines[0].split(sep=":")
    ip = ip_port[0]
    dt = lines[3].replace("[", "")
    bandwidth = int(lines[9])
    ip_parser(ip)
    prov, isp = ip_parser(ip)
    dt = time_parser(dt)
    # connect_mysql(dt, prov, isp, bandwidth)
    return dt, prov, isp, bandwidth

def connect_mysql(dt, prov, isp, bandwidthh):
    db = pymysql.connect(host='123.56.3.24',
                         user='sc',
                         password='123456',
                         database='python')
    cursor = db.cursor()
    sql = "INSERT INTO nginx_log(log_dt, province, isp, bandwidth) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (dt, prov, isp, bandwidthh))
    db.commit()
    db.close()

def time_parser(dt):
    timeArray = time.strptime(dt, "%d/%b/%Y:%H:%M:%S")
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


if __name__ == "__main__":
    r_list = []
    with open("access2.log", "r") as fp:
        p = Pool(processes=4)
        for line in fp:
            r = p.apply_async(func=line_parser, args=(line,))
            r_list.append(r)
        p.close()
        p.join()
    config = {
         "host": '123.56.3.24',
         "user": 'sc',
         "password": '123456',
         "database": 'python'
    }
    db = pymysql.connect(**config)
    with db:
        cursor = db.cursor()
        for r in r_list:
            # print(r.get())
            dt, prov, isp, bandwidthh = r.get()
            sql = "INSERT INTO nginx_log(log_dt, province, isp, bandwidth) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (dt, prov, isp, bandwidthh))
            db.commit()


# '''
#     CREATE TABLE nginx_log(
#         id int auto_increment primary key not null,
#         log_dt datetime,
#         province varchar(128) not null,
#         isp varchar(128) not null,
#         bandwidth int
#     )
# '''

