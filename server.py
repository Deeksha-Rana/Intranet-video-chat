import threading
import socket
import sys

def getMyIP():
    mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySock.connect(('8.8.8.8', 80))
    ip = mySock.getsockname()[0]
    mySock.close()
    return ip

class Server(threading.Thread):
    def __init__(self, exitStatus):
        threading.Thread.__init__(self)
        self.frame = self.sample = None
        self.clFrame = self.clSample = None
        self.exitStatus = exitStatus
        self.started = False

    def run(self):
        print 'Server started'
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP = getMyIP()
        print 'Your IP is ' + str(IP)
        HOST = 8888
        serverSock.bind((IP, HOST))
        serverSock.listen(1)
        clientSock, addr = serverSock.accept()
        counter = 0
        size = sys.getsizeof((self.getMySoundSample(), self.getMyImageFrame()))
        while True:
            if counter % 2 == 0:
                clientSock.send((self.getMySoundSample(), self.getMyImageFrame()))
            else:
                soundSample, imageFrame = clientSock.recv(size)
                self.setClientImageFrame(imageFrame)
                self.setClientSoundSample(soundSample)
            counter += 1
            self.started = True

    def setMySoundSample(self, sample):
        self.sample = sample

    def getMySoundSample(self):
        return self.sample

    def setMyImageFrame(self, frame):
        self.frame = frame

    def getMyImageFrame(self):
        return self.frame

    def getClientImageFrame(self):
        return self.clFrame

    def getClientSoundSample(self):
        return self.clSample

    def setClientImageFrame(self, frame):
        self.clFrame = frame

    def setClientSoundSample(self, sample):
        self.clSample = sample

