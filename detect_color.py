import cv2
import numpy as np

# อ่านภาพ
image = cv2.imread('example.jpg')

# แปลงรูปเป็นระบบสี HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# กำหนดช่วงของสีน้ำเงินในระบบสี HSV
lower_blue = np.array([90, 100, 100])  # ค่าสีน้ำเงินต่ำสุด (Hue, Saturation, Value)
upper_blue = np.array([130, 255, 255])  # ค่าสีน้ำเงินสูงสุด (Hue, Saturation, Value)

# สร้าง binary mask เพื่อแสดงส่วนของภาพที่มีสีน้ำเงินอยู่ในช่วงที่กำหนด
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# แสดงภาพ binary mask
cv2.imshow('Blue Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
