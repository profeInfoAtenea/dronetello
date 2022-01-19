from djitellopy import Tello
import cv2
#### https://www.youtube.com/watch?v=vDOkUHNdmKs

##############################################
width = 320 # width of the image
height = 240 # heigh of the image
startCounter = 1  # 0 for FLIGHT - 1 FOR TESTING
##############################################

# Creamos objeto Dron e inicilizamos parametros.
dron = Tello()
dron.connect()
dron.for_back_velocity = 0.0
dron.left_right_velocity = 0.0
dron.up_down_velocity = 0.0
dron.yaw_velocity = 0.0
dron.speed = 0.0

print(dron.get_battery())

dron.streamoff()
dron.streamon()


while True:
    # GET THE IMAGE FROM TELLO_
    frame_read = dron.get_frame_read()
    my_frame = frame_read.frame
    img = cv2.resize(my_frame, (width, height))

    #TO GO UP IN THE BEGINNING
    if startCounter == 0:
        dron.takeoff()
        dron.move_left(20)
        dron.rotate_clockwise(90)
        startCounter= 1

    # DISPLAY IMAGE 
    cv2.imwrite("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == cv2.ord('q'):
        print("fin")
        dron.land()
        break

# sudo lsof -i -P -n 
