import client
from time import sleep

cam = client.Camera()
mic = client.Microphone()
print "Hello World"
sleep(5)
print cam.getFrame()

