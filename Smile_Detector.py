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

#read current frame from webcam
#returns a tuple
#1st element 'successful_frame' is a boolan
#2nd element is the actual frame that the image runs on
#webcam.read is reading from the webcam
#.read - reads a single webframe
    succesful_frame_read, frame = webcam.read()
    
    #if there is an error, abort
    if not succesful_frame_read:
        break

    #change to grayscale
    # reduces the amount of processing in the video cam
    # which helps define a face
    # cvtColor - convert color to black and white
    # chang the color to grey
    # RGB to grey
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detects face first
    # calls detectMultiScale - tells us where faces are
    # returns an array of points (rectangles)
    # detect faces of every scale
    faces = face_detector.detectMultiScale(frame_grayscale, 1.3, 5)
    
    # print out face locations
    print(faces)
    #name of window
    # show image to screen
    # cv2.imshow('Smile detector', frame)

    #shows gray scale
    cv2.imshow('Smile detector', frame_grayscale)

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