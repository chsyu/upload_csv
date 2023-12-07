from sqlalchemy.orm import Session
from fastapi import UploadFile
from io import StringIO
import csv
from .models import Ami

async def upload_csv(file: UploadFile, db: Session):
    # 讀取 CSV 檔案
    content = await file.read()
    file_content = StringIO(content.decode())
    reader = csv.reader(file_content, delimiter=',', quotechar='"')

    # 批量插入設定
    batch_size = 1000  # 每批處理的資料量
    records = []

    # 跳過標題行
    next(reader)

    db.query(Ami).delete()
    db.commit()

    # 插入資料
    for index, row in enumerate(reader):
        record = Ami(cust_id=row[0], meter_id=row[1], ratio=row[2], read_time=row[3], del_kwh=row[4], rec_kwh=row[5], del_kvarh_lag=row[6])
        records.append(record)

        # 當累積到一定數量的記錄時進行批量插入
        if (index + 1) % batch_size == 0:
            db.bulk_save_objects(records)
            db.commit()
            records = []  # 清空記錄以釋放記憶體

    # 插入剩餘的記錄
    if records:
        db.bulk_save_objects(records)
        db.commit()

    db.close()

async def delete_all(db: Session):
    db.query(Ami).delete()
    db.commit()
    db.close()
