# คำสั่งเปิดเซิฟเวอร์ uvicorn main:app --port 8003 --reload

import numpy as np
# import cv2
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
# from io import BytesIO
# from PIL import Image

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

# # รับภาพมาคำนวณสัดส่วนแสงสี
# @app.post('/photo-value/')
# async def photoValue(file:UploadFile):
#     image_data = await file.read()
#     # img = Image.open(BytesIO(image_data))
#     img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
#     img_array = np.array(img)
#     # คำนวณปริมาณของสีแต่ละสีในภาพ
#     red_mean = np.mean(img_array[:, :, 0])  # สีแดง
#     green_mean = np.mean(img_array[:, :, 1])  # เขียว
#     blue_mean = np.mean(img_array[:, :, 2])  # น้ำเงิน
#     # คำนวณความสว่างของภาพในช่วง 0-1
#     brightness_normalized = np.mean(img_array) / 255.0
#     return {
#         "red_percentage": (red_mean / 255) * 100,
#         "green_percentage": (green_mean / 255) * 100,
#         "blue_percentage": (blue_mean / 255) * 100,
#         "brightness_normalized": brightness_normalized
#     }

# def compute_histogram(image_np):
#     if image_np.shape[-1] == 3:
#         image_gray = np.dot(image_np[...,:3], [0.2989, 0.5870, 0.1140])
#     else:
#         image_gray = image_np
#     hist = np.histogram(image_gray, bins=256, range=(0, 256))[0]
#     mean = np.mean(hist)
#     sd = np.std(hist)
#     skewness = ((hist - mean) ** 3).sum() / (len(hist) * sd ** 3)
#     kurtosis = ((hist - mean) ** 4).sum() / (len(hist) * sd ** 4)
#     return {
#         "mean": mean,
#         "sd": sd,
#         "skewness": skewness,
#         "kurtosis": kurtosis,
#         "histogram": hist.tolist()
#     }

# # วิเคราะห์ histogram ของภาพ
# @app.post('/photo-hist-data/')
# async def photoHistData(file: UploadFile):
#     image_bytes = await file.read()
#     # image_np = np.array(Image.open(BytesIO(image_bytes)))
#     image_np = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    
#     result = {
#         "grayscale": compute_histogram(image_np),
#         "red": compute_histogram(image_np[..., 0]),
#         "green": compute_histogram(image_np[..., 1]),
#         "blue": compute_histogram(image_np[..., 2])
#     }

#     return result