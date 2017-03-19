import vidStream
import server

cam = vidStream.Camera()
mic = vidStream.Microphone()

status = int(raw_input("Enter server = 0 or client = 1"))
if status == 0:
    serv = server.Server(vidStream.exitFlg)
    serv.start()
    while vidStream.exitFlg == False:
        if serv.started == False:
            continue
        serv.setMySoundSample(mic.getFrame())
        serv.setMyImageFrame(cam.getFrame())
        imageFrame = serv.getClientImageFrame()
        soundSample = serv.getClientSoundSample()
        cam.showFrame(imageFrame)
        mic.playSoundSample(soundSample)
        print 'hello'
