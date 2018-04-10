import cv2,time

video=cv2.VideoCapture(0)
i=0
while True:
    i=i+1

    check,frame=video.read()

    print(check)
    print(frame)
    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  Converting to grayscale
    cv2.imshow("Capturing",frame)    #frame represents color image grey represents grey image
    key=cv2.waitKey(1)

    if key == 27:
        break

print (i)
video.release()

cv2.destroyAllWindows()
