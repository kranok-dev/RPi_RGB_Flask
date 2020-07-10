import cv2
import time

vid = cv2.VideoCapture(0)

while(True):
    _,image = vid.read()
    cv2.imshow("Live",image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(0.05)

cv2.destroyAllWindows()
vid.release()
    
