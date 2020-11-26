from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

import schedule




def job_that_executes_once():

    for i in range(10):
        print("TEST SCHEDULE", datetime.now())
        sleep(1.0)

    return schedule.CancelJob



def interrupt():
    schedule.cancel_job(job_that_executes_once)




schedule.every().day.at('14:07:05').do(job_that_executes_once)
schedule.every().day.at('14:07:10').do(job_that_executes_once)



while True:
    schedule.run_pending()

