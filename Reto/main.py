##Codigo desarrollado por Sergio Gonzalez
#Reto para el Area de Control 

import cv2
import threading
import time
import re
import linecache

def leerArchivo(line):
    lineaL = linecache.getline("nombres.txt",line)
    lineaC = re.sub("\\n|\''","",lineaL)
    lineaC = list(lineaC.split(" "))

    for word in lineaC:
        if ("_" in word):
            return(word+".png")

def reconocimiento(nombreImagen):
    imagen = cv2.imread(nombreImagen)
    grises = cv2.cvtColor(imagen, cv2.COLOR_RGBA2GRAY)
    gauss = cv2.GaussianBlur(grises,(15,15),0)
    
    if ("4" in nombreImagen):
        _,th = cv2.threshold(gauss,80,200,cv2.THRESH_BINARY)
        cnts,_= cv2.findContours(th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    else:
        canny = cv2.Canny(gauss,15,170)
        cnts,_= cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return(f"Yo soy el hilo que analizo la imagen {nombreImagen} y encontre {len(cnts)} objetos")


def hilo(num):
    print(reconocimiento(leerArchivo(num)))
    time.sleep(5)



if __name__ == '__main__':
    #Hilo Principal
    print("Reto Area de Control Quantum Robotics \n")
    
    thread = threading.Thread(target=hilo, args=(1,))
    thread.start()
    time.sleep(1)

    thread = threading.Thread(target=hilo, args=(2,))
    thread.start()
    time.sleep(1)

    thread = threading.Thread(target=hilo, args=(3,))
    thread.start()
    time.sleep(1)

    thread = threading.Thread(target=hilo, args=(4,))
    thread.start()
    time.sleep(1)

    thread = threading.Thread(target=hilo, args=(5,))
    thread.start()
    time.sleep(1)

    thread = threading.Thread(target=hilo, args=(6,))
    thread.start()
    time.sleep(1)

    thread = threading.Thread(target=hilo, args=(7,))
    thread.start()
    time.sleep(1)

    thread.join()