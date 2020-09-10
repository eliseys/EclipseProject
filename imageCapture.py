from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess




detect_cameras = ["--auto-detect"]

lockup_mirror = ["--set-config", "viewfinder" + "=1"]
release_mirror = ["--set-config", "viewfinder" + "=0"]

#lockup_mirror = ["--capture-preview"]



#set_parameters = [""]

time = "=1.0s" #
frames = "=2f"

wait_time = ["--wait-event" + time]
wait_frames = ["--wait-event" + frames]

wait_0 = ["--wait-event" + "=100ms"]


capture = ["--trigger-capture"]


#burst_shooting = ["--set-config", "eosremoterelease" + "=2", "--wait-event" + time, "--set-config", "eosremoterelease" + "=4"]


#burst_shooting_start = ["--set-config", "eosremoterelease" + "=5", "--wait-event" + "=5"] # Immediate

burst_shooting_start = ["--set-config", "eosremoterelease" + "=5"] # Immediate
#burst_shooting_start = ["--set-config", "eosremoterelease" + "=2"] # Press Full

burst_shooting_stop = ["--set-config", "eosremoterelease" + "=4"]



liveview = ["--set-config", "output" + "=1"]

liveview_off = ["--set-config", "output" + "=0"]


remoterelease = ["--set-config", "eosremoterelease" + "=5"]
remoterelease_press_full = ["--set-config", "eosremoterelease" + "=2"]

#bulb?


iso = "=100"

set_iso = ["--set-config", "iso" + iso]


shutterspeed = "=1/500"
set_shutterspeed = ["--set-config", "shutterspeed" + shutterspeed]


drivemode_single = ["--set-config", "drivemode" + "=0"] 
drivemode_high_speed = ["--set-config", "drivemode" + "=1"] 

#print(gp(detect_cameras))#




#gp(capture)#
#gp(lockup_mirror)


#gp(capture)
#sleep(2)

#gp(set_shutterspeed)
#gp(burst_shootingx)
#gp(set_iso)

#gp(lockup_mirror)
#sleep(1)
#gp(release_mirror)

#gp(liveview, drivemode_high_speed, wait_time, remoterelease, wait_time, burst_shooting_stop)
#sleep(1.0)
#gp(drivemode_single, liveview, wait_time, "--wait-event=1s", gp(remoterelease_press_full), "--wait-event=1s", gp(remoterelease_press_full))
#gp(drivemode_single, liveview, "--wait-event=2s", capture, "--wait-event=FILEADDED", capture, )




# /main/actions/syncdatetime


# /main/actions/eosremoterelease
# # Label: Canon EOS Remote Release
# # Readonly: 0
# # Type: RADIO
# # Current: None
# # Choice: 0 None
# # Choice: 1 Press Half
# # Choice: 2 Press Full
# # Choice: 3 Release Half
# # Choice: 4 Release Full
# # Choice: 5 Immediate
# # Choice: 6 Press 1
# # Choice: 7 Press 2
# # Choice: 8 Press 3
# # Choice: 9 Release 1
# # Choice: 10 Release 2
# # Choice: 11 Release 3



# /main/settings/output

# Choice: 0 Off
# Choice: 1 TFT




# /main/imgsettings/iso
# Label: ISO Speed


# autoexposuremode

# 3 Manual




# drivemode

# aperture

# shutterspeed


t = 0.25


#gp("--set-config", "output=1", "--wait-event", "1.0s", "--capture-image", "-I 10s", "-F 5", "--set-config", "output=0")

#gp("--set-config", "drivemode=1", "--set-config", "output=1", "--set-config", "eosremoterelease=5", "--wait-event", "2.0s", "--set-config", "eosremoterelease=4", "--wait-event", "3s",\
#"--set-config", "drivemode=2", "--set-config", "eosremoterelease=5", "--wait-event", "10.0s", "--set-config", "eosremoterelease=4", "--wait-event", "3s",\
   
#"--set-config", "drivemode=1", "--set-config", "eosremoterelease=5", "--wait-event", "2.0s", "--set-config", "eosremoterelease=4", "--wait-event", "3s", "--set-config", "output=0")


#gp("--trigger-image", "--wait-event", "2.0s", "--trigger-image")

gp("--set-config", "drivemode=1", "--set-config", "output=1",\
   "--set-config", "shutterspeed=1/4000", "--set-config", "eosremoterelease=5", "--wait-event", "4s", "--set-config", "eosremoterelease=4",\
   "--wait-event", "2s",\
   "--set-config", "aeb=3",\
   "--set-config", "shutterspeed=1/1000", "--set-config", "eosremoterelease=5", "--wait-event", "2s", "--set-config", "eosremoterelease=4",\
   "--set-config", "shutterspeed=1/8", "--set-config", "eosremoterelease=5", "--wait-event", "2s", "--set-config", "eosremoterelease=4")

#11.020 total


# gp("--capture-image")
# sleep(t)
# gp("--capture-image")
# sleep(t)
# gp("--capture-image")
# sleep(t)
# gp("--capture-image")


#sleep(1.000)
#gp(burst_shooting_stop, liveview)


# gp(lockup_mirror, burst_shooting_start)
# sleep(0.500)
# gp(lockup_mirror, burst_shooting_stop)
#sleep(1)
#gp(release_mirror)


# k = 0
# while k<5:

#     gp(capture)
#     k = k + 1
#     sleep(0.1)
