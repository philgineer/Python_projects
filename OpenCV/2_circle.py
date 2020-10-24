import cv2
img = cv2.imread('D:/python/udemy_cv/dog_backpack.jpg')

def circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,0,255), 6)


cv2.namedWindow('image')
cv2.setMouseCallback('image', circle)
        
while True:
    cv2.imshow('image', img)
    
    if cv2.waitKey(2) & 0xFF==27:
        break
        
cv2.destroyAllWindows()