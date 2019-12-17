import cv2 as cv

cv.namedWindow('track_bar')


def th1f(bri):
    return 6*(10**(-7))*(bri**3)-0.0012*(bri**2)+0.7355*bri-66.587


def th2f(bri):
    return 6*(10**(-7))*(bri**3)-0.0013*(bri**2)+0.9212*bri-33.5


def nothing():
    pass


def auto_canny(vid_name):
    capture = cv.VideoCapture(vid_name)

    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        bri = cv.getTrackbarPos('bri', 'track_bar')
        frame_canny = cv.Canny(frame, th1f(bri), th2f(bri))
        cv.imshow('Frame', frame_canny)
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break


cv.createTrackbar('bri', 'track_bar', 0, 255, nothing)
cv.setTrackbarPos('bri', 'track_bar',0)
auto_canny("1.mp4")