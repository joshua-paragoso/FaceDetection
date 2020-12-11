import cv2

# face classifier
# some kind input in classifier, output would give a 0 (no) or 1 (yes)
# smile or not smile
# finds faces to find smile
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#grab webcam feed
webcam = cv2.VideoCapture(0)
#shows the current frame
#after getting webcam variable
while True:

    succesful_frame_read, frame = webcam.read()

# #name of window
# # show image to screen
    cv2.imshow('Smile detector', frame)

# # keeps webcam open till key is pressed
# # stays on with real time
# # display
    cv2.waitKey(1)

# # release webcam
# # let OS know the app is done with webcam
webcam.release()

# # closes all windows
cv2.destroyAllWindows()

print("code complete")