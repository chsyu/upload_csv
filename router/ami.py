from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
import time
from db.database import get_db
from db import db_ami

router = APIRouter(
    prefix='/ami',
    tags=['ami']
)

@router.delete('/delete-all')
async def delete_all(db: Session = Depends(get_db)):
    await db_ami.delete_all(db)
    return {"message": "All data deleted"}

@router.post('/upload-csv')
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    start_time = time.time()  # 開始計時
    await db_ami.upload_csv(file, db)
    end_time = time.time()  # 結束計時
    total_time = round(end_time - start_time, 1)  # 計算總耗時

    return {"message": "File uploaded successfully", "time_elapsed": f"{total_time} seconds"}


