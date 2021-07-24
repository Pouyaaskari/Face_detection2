import cv2
import mtcnn

face_detector = mtcnn.MTCNN(min_face_size=20)
image=cv2.imread("cr7.jpg")
threshold =0.99

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
detect=face_detector.detect_faces(image_rgb)
print(detect)

for item in detect:
    x1,y1,width,height=item['box']
    x1,y1=abs(x1),abs(y1)
    x2,y2=x1+width,y1+height
    confidence=item["confidence"]
    if confidence<threshold:
        continue
    key_points=item["keypoints"].values()
    
    cv2.rectangle(image,(x1,y1),(x2,y2),(255,0,0),2)
    cv2.putText(image,f"conf:{confidence:.3f}",(x1, y1), cv2.FONT_ITALIC,1,(255,0,255),1)
    for point in key_points:
        cv2.circle(image,point,5,(0,255,0),-1)
cv2.imshow("CR7",image)
cv2.waitKey(0)    