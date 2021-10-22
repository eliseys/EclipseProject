import numpy as np
import json

#from scipy import optimize
from lmfit import minimize, Parameters, fit_report
from scipy.optimize import Bounds, minimize_scalar, fmin

from skyfield.api import load
from skyfield.api import Topos

from skyfield.searchlib import find_maxima, find_minima
from datetime import timedelta

import matplotlib.pyplot as plt

with open('ec.json', "r") as jf:
    ec = json.load(jf)


date = load.timescale().utc(
    ec['date']['year'],
    ec['date']['month'],
    ec['date']['day']
)
p = Topos(
    ec['gps']['latitude'],
    ec['gps']['longitude'],
    elevation_m = ec['gps']['elevation_m']
)
ephem = load(ec['ephem'])


print(p)

r_moon = ec['r_moon_km']
r_sun = ec['r_sun_km']

accuracy_s = ec['accuracy_s']


earth, moon, sun = ephem['earth'], ephem['moon'], ephem['sun']
observer_location = earth + p  


load.download('finals2000A.all')

ts = load.timescale(builtin=False)
#ts = load.timescale(delta_t=71.0)




def center_angular_separation(tau):
    # separation between centers of the moon and the sun

    t = ts.utc(date.utc.year, date.utc.month, date.utc.day, 0, 0, tau)
    
    apparent_moon = observer_location.at(t).observe(moon).apparent()
    apparent_sun = observer_location.at(t).observe(sun).apparent()

    return abs(apparent_moon.separation_from(apparent_sun).degrees)


# params = Parameters()
# params.add('tau', value=500.0, min=0.0, max=86400.0)

# #out = minimize(center_angular_separation, params, method="lbfgsb")
# out = minimize(center_angular_separation, params)

# print(fit_report(out))



#res = optimize.minimize(center_angular_separation, x0=500.0, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})


res = fmin(center_angular_separation, x0=500, xtol=0.001)


print(res)
print(date.utc_strftime('%Y-%m-%d %H:%M:%S'), date.delta_t)

# t1 = date
# t2 = ts.utc(t1.utc_datetime() + timedelta(days=1))

# center_angular_separation.step_days = 10
# #center_angular_separation.rough_period = 1

# #t_center, values = find_minima(t1, t2, center_angular_separation, epsilon=0.01/86400.0)
# t_center, values = find_minima(t1, t2, center_angular_separation)

# for ti, vi in zip(t_center, values):
#     print(ti.utc_strftime('%Y-%m-%d %H:%M:')+'%2.4f' % ti.utc.second , "\t",  '%.9f' % vi)
#     #print(ti.ut1_strftime('%Y-%m-%d %H:%M:'),'%2.4f' % ti.utc.second , '%.9f' % vi)

#     #print(ti.utc_jpl(), '%.5f' % vi)


# #print(ts.utc(2016).delta_t)
# print(t_center.delta_t)


# distance_to_moon_at_t_center = observer_location.at(t_center) - moon.at(t_center)
# distance_to_sun_at_t_center = observer_location.at(t_center) - sun.at(t_center)

# angular_radius_moon = np.arctan(r_moon/distance_to_moon_at_t_center.distance().km)
# angular_radius_sun = np.arctan(r_sun/distance_to_sun_at_t_center.distance().km)



# print(angular_radius_moon, angular_radius_sun)

# c2c3_t, values = find_maxima(t1, t2, 0.25 - center_angular_separation)


# for ti, vi in zip(t_center, values):
#     print(ti.utc_strftime('%Y-%m-%d %H:%M:'), '%.4f' % ti.utc.second, '%.5f' % vi)
#     #print(ti.utc_jpl(), '%.5f' % vi)



# c1 = eclipseTimes.t_c1(date, p, ephem, r_moon, r_sun, accuracy_s).utc
# c2 = eclipseTimes.t_c2(date, p, ephem, r_moon, r_sun, accuracy_s).utc
#mid = eclipseTimes.t_center(date, p, ephem, accuracy_s)
# c3 = eclipseTimes.t_c3(date, p, ephem, r_moon, r_sun, accuracy_s).utc
# c4 = eclipseTimes.t_c4(date, p, ephem, r_moon, r_sun, accuracy_s).utc

#print(mid)

# def tuple_to_json(c):
#     return {'year': int(c[0]), 'month': int(c[1]), 'day': int(c[2]), 'hour': int(c[3]), 'minute': int(c[4]), 'second': float(c[5])}

# ec['c1'] = tuple_to_json(c1),
# ec['c2'] = tuple_to_json(c2),
# ec['mid'] = tuple_to_json(mid),
# ec['c3'] = tuple_to_json(c3),
# ec['c4'] = tuple_to_json(c4)

# with open('ec.json', "w") as jf:
#     json.dump(ec, jf)
