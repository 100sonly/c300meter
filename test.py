import picamera
import time
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = false
time.sleep(2)
camera.capture("/home/Desktop/C300-read/img.jpg")
print("Done.")
