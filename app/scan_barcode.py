import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
camera=True
isCaptured = False
i = 1
# while camera==True:
#     success, frame = cap.read()
#
#     if decode(frame) and isCaptured == False:
#         print(str(i))
#         i = i + 1
#         for code in decode(frame):
#             print(code.type)
#             print(code.data.decode('utf-8'))
#         isCaptured = True
#     elif len(decode(frame)) == 0 and isCaptured == True:
#         isCaptured = False
#     cv2.imshow('Testing-code-scan', frame)
#     x = cv2.waitKey(1)

while camera == True:
    success, frame = cap.read()
    x = cv2.waitKey(50)
    print(x)
    if x == 113:
        for code in decode(frame):
            print(code.type)
            print(code.data.decode('utf-8'))
    elif x == 27: camera = False
    cv2.imshow('Testing-code-scan', frame)
