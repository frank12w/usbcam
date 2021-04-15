import numpy as np
import time
import cv2

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

for dev_index in [1, 2, 3, 4, 0]:
    if cv2.VideoCapture(dev_index).isOpened():
        print("dev%d is available" %dev_index)
        dev = dev_index
        fourcc = cv2.VideoCapture(dev).get(cv2.CAP_PROP_FOURCC)
        codec = decode_fourcc(fourcc)
        if codec=="YUYV":
            break
        
cap = cv2.VideoCapture(dev)
print("use dev%d" %dev)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 20)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
#print(" %dx%d, fps=%d" %(width, height, fps))


fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print(codec, " %dx%d, fps=%d" %(width, height, fps))

t_tep = time.ctime().split()[-2].split(':')
# XVID(pi no support)
name = 'test'+t_tep[0]+t_tep[1]+t_tep[2]+'.avi'
out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MJPG'), fps, (width, height))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        #cv2.imshow('frame',frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()