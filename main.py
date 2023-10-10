# คำสั่งเปิดเซิฟเวอร์ uvicorn main:app --port 8003 --reload

import numpy as np
import cv2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# อนุญาตให้เข้าถึง API จากทุกๆ โดเมนหรือ URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return '<Geeleed/> สวัสดีครับ api นี้ใช้ประมวลผลภาพ สามารถดูรายละเอียดได้ที่ /docs'
