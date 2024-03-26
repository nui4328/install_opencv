import cv2
import numpy as np

# เปิดกล้อง
cap = cv2.VideoCapture(0)

# ตรวจสอบว่ากล้องถูกเปิดหรือไม่
if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องได้")
    exit()

# วนลูปอ่านภาพจากกล้อง
while True:
    # อ่านภาพจากกล้อง
    ret, frame = cap.read()

    # ตรวจสอบว่าอ่านภาพได้สำเร็จหรือไม่
    if not ret:
        print("ไม่สามารถอ่านภาพจากกล้องได้")
        break

    # แปลงภาพจาก BGR เป็น HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # กำหนดช่วงสีที่ต้องการจับ (ในที่นี้เป็นสีแดง)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # สร้างมาส์ค (mask) โดยใช้ช่วงสีที่กำหนด
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # ค้นหาเส้นขอบ
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # วาดกรอบรอบวัตถุที่พบ
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # แสดงภาพต้นฉบับและมาส์ค
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)

    # รอการกดปุ่ม 'q' เพื่อออกจากการแสดงภาพ
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดกล้องเมื่อเสร็จสิ้น
cap.release()
cv2.destroyAllWindows()