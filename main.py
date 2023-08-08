import threading
from camera import Camera
from windows import First,Second,Third


camera = Camera()

t1 = threading.Thread(target=First(camera).show)
t2 = threading.Thread(target=Second(camera).show)
t3 = threading.Thread(target=Third(camera).show)

t2.daemon = True
t3.daemon = True

t1.start()
t2.start()
t3.start()

t1.join()



