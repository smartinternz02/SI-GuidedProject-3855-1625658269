import cv2
import os
data_file_path = "available_objects"
i=0
classifiers = {
    file_name.replace(".xml",""):cv2.CascadeClassifier(
        os.path.join(data_file_path,file_name)
    )
    for file_name in os.listdir(data_file_path)
    }

cam = cv2.VideoCapture(0)

assert cam.isOpened(),"Camera is not available."

while cam.isOpened():
    is_frame, frame = cam.read()
    for classifier_name in classifiers.keys():
        pred = classifiers[classifier_name].detectMultiScale(
            frame, 1.3, 5
        )
        for (x,y,w,h) in pred:
            frame = cv2.rectangle(frame,(x,y),
            (x+w,y+h),(0,255,0), thickness=2)
            frame = cv2.putText(frame,classifier_name,(x,y-3),
            cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,
            thickness=2,
            color=(0,0,255))
    cv2.imshow("Object Detection System",frame)
    cv2.imwrite(f"scrnshts_{i}.png",frame,)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    i+=1
cam.release()
cv2.destroyAllWindows()