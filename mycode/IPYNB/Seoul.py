# 현재 시각을 가져오자
import requests
import pandas as pd
import sqlite3
import json
import schedule
import time
import pytz
from datetime import datetime as dt

# 날씨 데이터를 매일 오전 8시에 요청해서 DB에에 저장해보자
MY_API_KEY='56fe2da71ee4a88b467102c987fc2673'
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_API_KEY}&units=metric"
    
def fetch_weather():
    local_tz = pytz.timezone("Asia/Seoul")
    tnow = dt.now(local_tz).strftime("%D %T")

    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]

    # daily_weather.db
    conn = sqlite3.connect("daily_weather.db")
    curs = conn.cursor()
    sql_table = """
          CREATE TABLE IF NOT EXISTS Seoul
          (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temp FLOAT NOT NULL,
            time DATETIME
          )
          """
    curs.execute(sql_table)
    conn.commit()
    curs.close()
    conn.close()

    conn = sqlite3.connect("daily_weather.db")
    curs = conn.cursor()
    # 현재 서울의 기온을 Seoul에 Insert
    sql = f"""
    INSERT INTO Seoul(temp, time)
    VALUES ({temp}, '{tnow}')
    """
    curs.execute(sql)
    conn.commit()

    curs.close()
    conn.close()

task_test_30s = schedule.every(30).seconds.do(fetch_weather)
# task1d = schedule.every().day.at("08:00").do(fetch_weather)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
finally:
    # schedule.cancel_job(task1d)
    schedule.cancel_job(task_test_30s)
    print("프로그램 종료")