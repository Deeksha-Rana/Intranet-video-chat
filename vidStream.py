import numpy as np # numpy: used by cv2 the OpenCV
import cv2 # cv2: the python binding for OpenCV for fetching video from camera
import threading
import pyaudio

exitFlg = False

'''
    This module will be used to send the data recorded by the camera,
    the video, the audio and then finally the multiplexed output.

'''

class Camera:
    '''
        This class will work in 1 thread, i.e. thread using showStream
        will keeps on working till 'q' button is pressed, and the
        getFrame method will return the frame information, the image
        at the time of calling of the function.

        Though this technique will have some lagging but it will be a
        better solution for the modern fast computers
    '''
    def __init__(self):
        self.frame = 0
        streamer = threading.Thread(target = self.startVideoStream)
        streamer.start()

    def startVideoStream(self):
        global exitFlg
        camera = cv2.VideoCapture(0)
        while True:
            ret, self.frame = camera.read()
            cv2.imshow("Stream", self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                exitFlg = True
                break
        cv2.destroyAllWindows()
        camera.release()

    def getFrame(self):
        return self.frame
    def showFrame(self, frame):
        cv2.imshow("Stream", frame)


class Microphone:
    '''
        This class will be used to get the sound from the microphone
        this class too will save the frames, the momentry frames then
        these frames will be multiplexed with the video frames
        It also uses a thread
    '''
    def __init__(self):
        self.frame = 0
        streamer = threading.Thread(target = self.startAudioStream)
        self.stream = 0
        streamer.start()
    def startAudioStream(self):
        global exitFlg
        CHUNK = 1024
        RATE = 44100
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        p = pyaudio.PyAudio()
        self.stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        output = True,
                        frames_per_buffer = CHUNK)
        while exitFlg == False:
            self.frame = self.stream.read(CHUNK)
        self.stream.stop_stream()
        self.stream.close()
        p.terminate()
    def getFrame(self):
        return self.frame

    def playSoundSample(self, sample):
        self.stream.write(sample, 1024)

