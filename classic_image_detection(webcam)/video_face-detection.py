import cv2

cap=cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret ,frame=cap.read()
    if not ret: 
        break
    boxes = detector.detectMultiScale(frame)
    for box in boxes:
        x1, y1, width, height = box
        x2, y2 = x1 + width, y1 + height
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("pouya",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


