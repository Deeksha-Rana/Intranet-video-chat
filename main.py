import client
from time import sleep

cam = client.Camera()
print "Hello World"
sleep(5)
print cam.getFrame()

