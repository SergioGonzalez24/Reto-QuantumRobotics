import cv2

imagen = cv2.imread("/Users/sergiogonzalez/OneDrive/GitHub/Reto-QuantumRobotics/Recursos/bucks_and_cents_[IMAGEN_4].png")


grises = cv2.cvtColor(imagen, cv2.COLOR_RGBA2GRAY)
gauss = cv2.GaussianBlur(grises,(15,15),0)
_,th = cv2.threshold(gauss,80,200,cv2.THRESH_BINARY)
#canny = cv2.Canny(gauss,15,170)

cnts,_= cv2.findContours(th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen,cnts,-1,(255,0,0),2)

print("CXontornos: ",len(cnts))

cv2.imshow('Imagen',imagen)
cv2.imshow("Gris",grises)
cv2.imshow("Gaus",gauss)
#cv2.imshow("Canny",canny)
cv2.imshow("Canny",th)

cv2.waitKey(0)
cv2.destroyAllWindows()