import numpy as np


def bracket_info_output(longest_exposure, step, N_steps, fps):
    start = np.log2(longest_exposure)
    end = start - N_steps * step
    ev_range = N_steps * step
    #print(start, end, step)
    
    summa = 0
    for i in np.arange(start, end, -step):
        summa = summa + (2**i)
        if i < 0:
            print("{:.1f}".format(i), "\t", "1/" + "{:.1f}".format(2**(-i)))
        else:
            print("{:.1f}".format(i), "\t", "{:.1f}".format(2**(i)))


            #if i >= 0:
        #    print(i, "\t", str(2**i), "\t\t", 2**i)

    print('Exposure time summa: ', "{:.3f}".format(summa), ' s')
    print('EV range: ', "{:.1f}".format(abs(ev_range)), ' steps')
    print('Estimated shooting time: ', "{:.3f}".format(summa + (1/fps)*N_steps), ' s')



N_steps = 7
step = 1 
longest_exposure_seconds = 1
fps = 4.0



bracket_info_output(longest_exposure_seconds, step, N_steps, fps)


