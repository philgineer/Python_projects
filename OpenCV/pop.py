import cv2

img = cv2.imread('D:/python/udemy_cv/00-puppy.jpg')

while True:
    cv2.imshow('puppy', img)
    
    # if we've waited at least 1 ms AND we've passed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()