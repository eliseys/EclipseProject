from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
import schedule

import threading

import vlc
p = vlc.MediaPlayer("beep-09.mp3")
p.play()

sleep(5)

p.stop()


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

    
def canon_7d2():
    #print("TEST SCHEDULE", datetime.now())
    print(datetime.now())
    subprocess.call("./canon_7d2_control.sh", shell=True)

    #return schedule.CancelJob
    return 0


def canon_rp():
    #print("TEST SCHEDULE", datetime.now())
    print(datetime.now())
    subprocess.call("./canon_rp_control.sh", shell=True)

    return schedule.CancelJob
    #return 0



start_time_7d = '12:59:46' # offset minus 18 s C2=13:00:04
start_time_rp = '12:59:54' # offset minus 10 s C2=13:00:04


schedule.every().day.at(start_time_7d).do(run_threaded, canon_7d2)
schedule.every().day.at(start_time_rp).do(run_threaded, canon_rp)

while True:
    schedule.run_pending()






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



