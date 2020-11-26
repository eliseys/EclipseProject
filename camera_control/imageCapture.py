from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

import schedule




# def job_that_executes_once():

#     print("TEST SCHEDULE", datetime.now())
    
#     return schedule.CancelJob



# schedule.every().day.at('17:36:40').do(job_that_executes_once)

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

gp("--set-config", "imageformat=RAW") # Image Format 
print(gp("--get-config", "imageformat"))
gp("--set-config", "imageformatsd=RAW") # Image Format SD
print(gp("--get-config", "imageformat"))
gp("--set-config", "imageformatcf=RAW") # Image Format CF
print(gp("--get-config", "imageformat"))

gp("--set-config", "iso=100") # ISO
print(gp("--get-config", "iso"))

gp("--set-config", "whitebalance=Daylight") # WhiteBalance
print(gp("--get-config", "whitebalance"))

# capturesettings

gp("--set-config", "exposurecompensation=0") # Exposure Compensation
print(gp("--get-config", "exposurecompensation"))

gp("--set-config", "highisonr=2") # High ISO Noise Reduction (2=off)
print(gp("--get-config", "highisonr"))

gp("--set-config", "drivemode=1") # Drive Mode Continuous high speed
print(gp("--get-config", "drivemode"))

gp("--set-config", "drivemode=2") # Drive Mode Continuous low speed
print(gp("--get-config", "drivemode"))

gp("--set-config", "picturestyle=Neutral") # Picture Style
print(gp("--get-config", "picturestyle"))

#gp("--set-config", "aperture") # Aperture
print(gp("--get-config", "aperture"))

gp("--set-config", "shutterspeed") # Shutter Speed
print(gp("--get-config", "shutterspeed"))

gp("--set-config", "aeb=0") # Auto Exposure Bracketing
print(gp("--get-config", "aeb"))


#######################################










#burst_shooting = ["--set-config", "eosremoterelease" + "=2", "--wait-event" + time, "--set-config", "eosremoterelease" + "=4"]

#burst_shooting_start = ["--set-config", "eosremoterelease" + "=5", "--wait-event" + "=5"] # Immediate

burst_shooting_start = ["--set-config", "eosremoterelease" + "=5"] # Immediate
#burst_shooting_start = ["--set-config", "eosremoterelease" + "=2"] # Press Full

burst_shooting_stop = ["--set-config", "eosremoterelease" + "=4"]



liveview = ["--set-config", "output" + "=1"]

liveview_off = ["--set-config", "output" + "=0"]


remoterelease = ["--set-config", "eosremoterelease" + "=5"]
remoterelease_press_full = ["--set-config", "eosremoterelease" + "=2"]



#gp("--set-config", "output=1", "--wait-event", "1.0s", "--capture-image", "-I 10s", "-F 5", "--set-config", "output=0")

#gp("--set-config", "drivemode=1", "--set-config", "output=1", "--set-config", "eosremoterelease=5", "--wait-event", "2.0s", "--set-config", "eosremoterelease=4", "--wait-event", "3s",\
#"--set-config", "drivemode=2", "--set-config", "eosremoterelease=5", "--wait-event", "10.0s", "--set-config", "eosremoterelease=4", "--wait-event", "3s",\
   
#"--set-config", "drivemode=1", "--set-config", "eosremoterelease=5", "--wait-event", "2.0s", "--set-config", "eosremoterelease=4", "--wait-event", "3s", "--set-config", "output=0")


#gp("--trigger-image", "--wait-event", "2.0s", "--trigger-image")

# gp("--set-config", "drivemode=1", "--set-config", "output=1",\
#    "--set-config", "shutterspeed=1/4000", "--set-config", "eosremoterelease=5", "--wait-event", "4s", "--set-config", "eosremoterelease=4",\
#    "--wait-event", "2s",\
#    "--set-config", "aeb=3",\
#    "--set-config", "shutterspeed=1/1000", "--set-config", "eosremoterelease=5", "--wait-event", "2s", "--set-config", "eosremoterelease=4",\
#    "--set-config", "shutterspeed=1/8", "--set-config", "eosremoterelease=5", "--wait-event", "2s", "--set-config", "eosremoterelease=4")

#11.020 total


