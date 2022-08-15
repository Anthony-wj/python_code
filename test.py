from pykafka import KafkaClient
import json
# balanced_consumer = topic.get_balanced_consumer(
#     consumer_group='testgroup',
#     auto_commit_enable=True,
#     zookeeper_connect="nginx-kafka01:2181:,nginx-kafka02:2181"
# )
import requests
import time
import pymysql.cursors
from multiprocessing import Pool

baseurl = "https://ip.taobao.com/outGetIpInfo?accessKey=alibaba-inc&ip="


def ip_parse(ip):
    url = baseurl + ip
    response = requests.get(url)
    if response.status_code:
        message = json.loads(response.text)
        isp = message["data"]["isp"]
        city = message["data"]["regison"]
        return isp, city
    else:
        time.sleep(1)


def time_parse(dt):
    timeArray = time.strptime(dt, "%d/%b/%Y:%H:%M:%S")
    otherTimeStyle = time.strftime("%Y-%m-%d:%H:%M:%S", timeArray)
    return otherTimeStyle


def line_parser(line):
    lines = line.split()
    ip = lines[0]
    isp, city = ip_parse(ip)
    dt = lines[4].split(sep="[")[1]
    dt = time_parse(dt)
    bandwidth = lines[10]
    return dt, city, isp, bandwidth


if __name__ == "__main__":
    client = KafkaClient(hosts="127.0.0.1:9092,192.168.63.111:9092,192.168.63.112:9092,192.168.63.113:9092")
    topic = client.topics['sc-nginx-log']
    consumer = topic.get_simple_consumer()
    p_list = []
    config = {
        "host": '123.56.3.24',
        "user": 'sc',
        "password": '123456',
        "database": 'python'
    }
    db = pymysql.connect(**config)
    with db:
        for message in consumer:
            if message is not None:
                # print(type(message.value))
                result = json.loads(message.value.decode())
                line = result.get("message")
                dt, prov, isp, bandwidth = line_parser(line)
                print(dt, prov, isp, bandwidth)
                cursor = db.cursor()
                sql = "INSERT INTO nginx_log(log_dt, province, isp, bandwidth) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (dt, prov, isp, bandwidth))
                db.commit()
