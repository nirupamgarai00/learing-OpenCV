import cv2

cap = cv2.VideoCapture(0)



while True:
    ret , fram = cap.read()
    clear_fram = cv2.GaussianBlur(fram,(5,5),0)
    
    cv2.imshow('original',fram)
    cv2.imshow('cleared',clear_fram)
    if cv2.waitKey(2) == 27:
        break
cap.release()
cv2.destroyAllWindows()