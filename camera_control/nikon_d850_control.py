from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

import schedule

# def job_that_executes_once():

#     #print("TEST SCHEDULE", datetime.now())
#     print(datetime.now())
#     subprocess.call("./test.sh", shell=True)

#     #return schedule.CancelJob
#     return 0


# schedule.every().day.at('15:07:10').do(job_that_executes_once)
# schedule.every().day.at('15:07:15').do(job_that_executes_once)
# schedule.every().day.at('15:07:20').do(job_that_executes_once)




# while True:
#     schedule.run_pending()



# www.astropix.com
# Don't take any exposures longer than 1/30th of a second in the 10 seconds after second contact or in the 10 seconds before third contact.


# If you connect more than one camera to the PC, you can control them independently from gPhoto2. The gphoto2 --auto-detect command provides a list of the detected cameras. You can use the displayed name to control the camera with:
# gphoto2 --camera="displayed_name"  --capture-image-and-download
# If you open a separate terminal window for each camera and record the image in separate directories, you can get a parallel series of frames from each camera. Figure 3 shows the process.



# Если для параметра [52: Автоотключение] выбрано значение [Запрещено], то съемка в режиме
# Live View прекратится автоматически через 30 минут (питание камеры будет включено).


# if camera busy
# kill output of the following
# ps aux | grep gphoto


# gp("--auto-detect")



# settings

gp("--set-config", "capturetarget=1") # Capture Target Memory card
print(gp("--get-config", "capturetarget"))

# imgsettings

gp("--set-config", "imagesize=7") # Image Size 8256x5504
print(gp("--get-config", "imagesize"))


gp("--set-config", "imagequality=7") # Image Quality NEF
print(gp("--get-config", "imagequality"))


gp("--set-config", "iso=5") # ISO 100 
print(gp("--get-config", "iso"))

gp("--set-config", "whitebalance=1") # WhiteBalance Daylight
print(gp("--get-config", "whitebalance"))

# capturesettings

gp("--set-config", "exposurecompensation=15") # Exposure Compensation
print(gp("--get-config", "exposurecompensation"))

gp("--set-config", "highisonr=0") # High ISO Noise Reduction (0=off) Nikon
print(gp("--get-config", "highisonr"))

print(gp("--get-config", "capturemode")) # READ ONLY (Ch on ring for Burst)

gp("--set-config", "bracketing=On") # Bracketing
print(gp("--get-config", "bracketing"))

gp("--set-config", "bracketmode=Flash/speed") # Bracketing
print(gp("--get-config", "brackemode"))




gp("--set-config", "f-number=f/1.4" ) # Aperture
print(gp("--get-config", "aperture"))

gp("--set-config", "shutterspeed='1/2'") # Shutter Speed
print(gp("--get-config", "shutterspeed"))

gp("--set-config", "aeb=0") # Auto Exposure Bracketing
print(gp("--get-config", "aeb"))


#######################################





# gp("--set-config", "aeb=0")
#gp("--set-config", "shutterspeed='1/4'")


# gp("--set-config", "viewfinder=1",
#    "--wait-event=1s",
#    "--set-config", "shutterspeed=1/1000",
#    "--set-config", "eosremoterelease=5")

# sleep(3)

# gp("--set-config", "shutterspeed=1/1000",
#    "--set-config", "eosremoterelease=5")

   
   # "--wait-event=2s",
   # "--set-config", "eosremoterelease=4",
   # "--set-config", "shutterspeed=1/1000",
   # "--set-config", "eosremoterelease=5",
   # "--wait-event=3s",   
   # "--set-config", "eosremoterelease=4",
   # "--set-config", "shutterspeed=0.5",
   # "--set-config", "eosremoterelease=5")



# gp("--set-config", "output=0")

