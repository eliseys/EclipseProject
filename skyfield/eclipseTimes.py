import numpy as np

from skyfield.api import load
from skyfield.api import Topos
import matplotlib.pyplot as plt


def center_angular_separation(t, p, ephem):
    #
    # separation between centers of the moon and the sun
    #
    earth, moon, sun = ephem['earth'], ephem['moon'], ephem['sun']
    observer_location = earth + p  
    apparent_moon = observer_location.at(t).observe(moon)
    apparent_sun = observer_location.at(t).observe(sun)

    return apparent_moon.separation_from(apparent_sun)


def t_center(date, p, ephem, accuracy_s):
    start = 0
    end = 86400
    step = 60
    span = np.arange(start, end+step, step)
        
    while step >= accuracy_s:
        t = load.timescale().utc(date.utc[0], date.utc[1], date.utc[2], 0, 0, span)
        l = center_angular_separation(t, p, ephem)
        t_center = t[np.argmin(l.radians)]
        
        #print(t_center.utc)
        
        start = 3600*t_center.utc[3] + 60*t_center.utc[4] + t_center.utc[5] - step
        end = 3600*t_center.utc[3] + 60*t_center.utc[4] + t_center.utc[5] + step

        if step > 1:
            step = step/60
        elif step <= 1:
            step = step/10

        span = np.arange(start, end+step, step)

    return t_center



def t_c1(date, p, ephem, r_moon, r_sun, accuracy_s):

    t_max = t_center(date, p, ephem, accuracy_s)

    start = 0
    end = 3600*t_max.utc[3] + 60*t_max.utc[4] + t_max.utc[5]
    step = 60
    span = np.arange(start, end+step, step)

    earth, moon, sun = ephem['earth'], ephem['moon'], ephem['sun']

    observer_location = earth + p  

    distance_to_moon_at_t_max = observer_location.at(t_max) - moon.at(t_max)
    distance_to_sun_at_t_max = observer_location.at(t_max) - sun.at(t_max)

    angular_radius_moon = np.arctan(r_moon/distance_to_moon_at_t_max.distance().km)
    angular_radius_sun = np.arctan(r_sun/distance_to_sun_at_t_max.distance().km)

    #delta_angular_radius_moon_sun = angular_radius_moon - angular_radius_sun # for c2 and c3 calculation
    summa_angular_radius_moon_sun = angular_radius_moon + angular_radius_sun # for c1 and c4 calculation
    
    while step >= accuracy_s:
        t = load.timescale().utc(date.utc[0], date.utc[1], date.utc[2], 0, 0, span)
        l = center_angular_separation(t, p, ephem)
        t_c1 = t[np.argmin(abs(l.radians - summa_angular_radius_moon_sun))]
        
        start = 3600*t_c1.utc[3] + 60*t_c1.utc[4] + t_c1.utc[5] - step
        end = 3600*t_c1.utc[3] + 60*t_c1.utc[4] + t_c1.utc[5] + step

        if step > 1:
            step = step/60
        elif step <= 1:
            step = step/10

        span = np.arange(start, end+step, step)

    return t_c1




def t_c4(date, p, ephem, r_moon, r_sun, accuracy_s):

    t_max = t_center(date, p, ephem, accuracy_s)

    start = 3600*t_max.utc[3] + 60*t_max.utc[4] + t_max.utc[5]
    end = 86400
    step = 60
    span = np.arange(start, end+step, step)

    earth, moon, sun = ephem['earth'], ephem['moon'], ephem['sun']

    observer_location = earth + p  

    distance_to_moon_at_t_max = observer_location.at(t_max) - moon.at(t_max)
    distance_to_sun_at_t_max = observer_location.at(t_max) - sun.at(t_max)

    angular_radius_moon = np.arctan(r_moon/distance_to_moon_at_t_max.distance().km)
    angular_radius_sun = np.arctan(r_sun/distance_to_sun_at_t_max.distance().km)

    #delta_angular_radius_moon_sun = angular_radius_moon - angular_radius_sun # for c2 and c3 calculation
    summa_angular_radius_moon_sun = angular_radius_moon + angular_radius_sun # for c1 and c4 calculation
    
    while step >= accuracy_s:
        t = load.timescale().utc(date.utc[0], date.utc[1], date.utc[2], 0, 0, span)
        l = center_angular_separation(t, p, ephem)
        t_c4 = t[np.argmin(abs(l.radians - summa_angular_radius_moon_sun))]
        
        start = 3600*t_c4.utc[3] + 60*t_c4.utc[4] + t_c4.utc[5] - step
        end = 3600*t_c4.utc[3] + 60*t_c4.utc[4] + t_c4.utc[5] + step

        if step > 1:
            step = step/60
        elif step <= 1:
            step = step/10

        span = np.arange(start, end+step, step)

    return t_c4



def t_c3(date, p, ephem, r_moon, r_sun, accuracy_s):

    t_max = t_center(date, p, ephem, accuracy_s)

    start = 3600*t_max.utc[3] + 60*t_max.utc[4] + t_max.utc[5]
    end = 3600*t_max.utc[3] + 60*t_max.utc[4] + t_max.utc[5] + 600
    step = 1
    span = np.arange(start, end+step, step)

    earth, moon, sun = ephem['earth'], ephem['moon'], ephem['sun']

    observer_location = earth + p  

    distance_to_moon_at_t_max = observer_location.at(t_max) - moon.at(t_max)
    distance_to_sun_at_t_max = observer_location.at(t_max) - sun.at(t_max)

    angular_radius_moon = np.arctan(r_moon/distance_to_moon_at_t_max.distance().km)
    angular_radius_sun = np.arctan(r_sun/distance_to_sun_at_t_max.distance().km)

    delta_angular_radius_moon_sun = angular_radius_moon - angular_radius_sun # for c2 and c3 calculation
    #summa_angular_radius_moon_sun = angular_radius_moon + angular_radius_sun # for c1 and c4 calculation
    
    while step >= accuracy_s:
        t = load.timescale().utc(date.utc[0], date.utc[1], date.utc[2], 0, 0, span)
        l = center_angular_separation(t, p, ephem)
        t_c3 = t[np.argmin(abs(l.radians - delta_angular_radius_moon_sun))]
        
        start = 3600*t_c3.utc[3] + 60*t_c3.utc[4] + t_c3.utc[5] - step
        end = 3600*t_c3.utc[3] + 60*t_c3.utc[4] + t_c3.utc[5] + step

        step = step/10

        span = np.arange(start, end+step, step)

    return t_c3



def t_c2(date, p, ephem, r_moon, r_sun, accuracy_s):

    t_max = t_center(date, p, ephem, accuracy_s)

    start = 3600*t_max.utc[3] + 60*t_max.utc[4] + t_max.utc[5] - 600 
    end = 3600*t_max.utc[3] + 60*t_max.utc[4] + t_max.utc[5]
    step = 1
    span = np.arange(start, end+step, step)

    earth, moon, sun = ephem['earth'], ephem['moon'], ephem['sun']

    observer_location = earth + p  

    distance_to_moon_at_t_max = observer_location.at(t_max) - moon.at(t_max)
    distance_to_sun_at_t_max = observer_location.at(t_max) - sun.at(t_max)

    angular_radius_moon = np.arctan(r_moon/distance_to_moon_at_t_max.distance().km)
    angular_radius_sun = np.arctan(r_sun/distance_to_sun_at_t_max.distance().km)

    delta_angular_radius_moon_sun = angular_radius_moon - angular_radius_sun # for c2 and c3 calculation
    #summa_angular_radius_moon_sun = angular_radius_moon + angular_radius_sun # for c1 and c4 calculation
    
    while step >= accuracy_s:
        t = load.timescale().utc(date.utc[0], date.utc[1], date.utc[2], 0, 0, span)
        l = center_angular_separation(t, p, ephem)
        t_c2 = t[np.argmin(abs(l.radians - delta_angular_radius_moon_sun))]
        
        start = 3600*t_c2.utc[3] + 60*t_c2.utc[4] + t_c2.utc[5] - step
        end = 3600*t_c2.utc[3] + 60*t_c2.utc[4] + t_c2.utc[5] + step

        step = step/10

        span = np.arange(start, end+step, step)

    return t_c2



