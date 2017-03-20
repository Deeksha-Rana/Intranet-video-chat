import vidStream
import server
import client


status = int(raw_input("Enter server = 0 or client = 1\n"))
if status == 0:
    serv = server.Server(vidStream.exitFlg)
    serv.start()
    cam = vidStream.Camera()
    mic = vidStream.Microphone()
    while vidStream.exitFlg == False:
        if serv.started == False:
            continue
        serv.setMySoundSample(mic.getFrame())
        serv.setMyImageFrame(cam.getFrame())
        imageFrame = serv.getClientImageFrame()
        soundSample = serv.getClientSoundSample()
        try:
            cam.showFrame(imageFrame)
            mic.playSoundSample(soundSample)
        except:
            continue

if status == 1:
    ip = raw_input("Enter the IP address you want to connect")
    port = int(raw_input("Enter the port number"))
    cli = client.Client((ip, port))
    cli.start()
    cam = vidStream.Camera()
    mic = vidStream.Microphone()
    while vidStream.exitFlg == False:
        if cli.started == False:
            continue
        cli.setMySoundSample(mic.getFrame())
        cli.setMyImageFrame(cam.getFrame())
        imageFrame = cli.getServImageFrame()
        soundSample = cli.getServSoundSample()
        try:
            cam.showFrame(imageFrame)
            mic.playSoundSample(soundSample)
        except:
            continue
