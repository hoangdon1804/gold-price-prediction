from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
import time
import csv
import os

START_DATE = datetime(2024, 12, 31)
END_DATE   = datetime(2005, 1, 1)

CSV_FILE = "gia_vang_sjc.csv"

driver = webdriver.Chrome()

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Ngày", "Giá crawl được"])

print("📁 CSV sẵn sàng:", CSV_FILE)

current_date = START_DATE

while current_date >= END_DATE:
    date_str = current_date.strftime("%d-%m-%Y")
    url = f"https://webgia.com/gia-vang/sjc/{date_str}.html"
    print("🔎 Đang crawl:", date_str)

    driver.get(url)
    time.sleep(2)

    try:
        # x = table
        x = driver.find_element(
            By.CSS_SELECTOR,
            "table.table.table-bordered.table-hover"
        )

        # x / tbody
        tbody = x.find_element(By.TAG_NAME, "tbody")

        # lấy tr gần cuối
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        if len(rows) < 2:
            raise Exception("Không đủ dòng")

        y = rows[-2]

        # td cuối của y
        value = y.find_elements(By.TAG_NAME, "td")[-1].text

        # ghi vào CSV (append)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date_str, value])

        print(f"✅ {date_str} -> {value}")

    except NoSuchElementException:
        print(f"⛔ {date_str} -> không có bảng, bỏ qua")
    except Exception as e:
        print(f"⚠ {date_str} -> lỗi: {e}")

    current_date -= timedelta(days=1)

driver.quit()
print("🎯 HOÀN TẤT CRAWL")
