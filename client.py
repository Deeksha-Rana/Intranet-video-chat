import threading
import socket
import sys

class Client(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.addr = addr
        self.frame = self.sample = 0
        self.servFrame = self.servSample = 0
        self.started = False
    def run(self):
        print 'Client started'
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSock.connect(self.addr)
        counter = 0
        SIZES = sys.getsizeof(self.getMySoundSample())
        SIZEF = sys.getsizeof(self.getMyImageFrame())
        while True:
            if counter % 2 == 0:
                soundSample = clientSock.recv(SIZES)
                imageFrame = clientSock.recv(SIZEF)
                self.setServImageFrame(imageFrame)
                self.setSetSoundSample(soundSample)
            else:
                clientSock.send((self.getMySoundSample(), self.getMyImageFrame()))
            self.started = True

    def setMySoundSample(self, sample):
        self.sample = sample

    def getMySoundSample(self):
        return self.sample

    def setMyImageFrame(self, frame):
        self.frame = frame

    def getMyImageFrame(self):
        return self.frame

    def getServImageFrame(self):
        return self.servFrame

    def getServSoundSample(self):
        return self.servSample

    def setServImageFrame(self, frame):
        self.servFrame = frame

    def setSetSoundSample(self, sample):
        self.servSample = sample

