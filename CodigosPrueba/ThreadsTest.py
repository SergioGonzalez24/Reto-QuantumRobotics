import threading
import time

def holaMundo(nombre):
    print("Hola mundo "+nombre)
    time.sleep(5)
    
def holaSergio(edad):
    print("Hola sergio tengo "+str(edad)+"\n")
    time.sleep(5)

if __name__ == '__main__':
    #Segundo Hilo
    thread = threading.Thread(target=holaMundo, args=("Codi",))
    thread.start()

    #Tercer Hilo
    thread = threading.Thread(target=holaSergio, args=(20,))
    thread.start()



    thread.join()

    print("Hilo Principal")
