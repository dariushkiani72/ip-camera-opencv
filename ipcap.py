import cv2

#  video capture object
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('rtsp://admin:1234@192.168.1.***/1')


while (True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()