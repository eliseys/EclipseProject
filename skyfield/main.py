import numpy as np
import json

from skyfield.api import load
from skyfield.api import Topos

import eclipseTimes


with open('ec.json', "r") as jf:
    ec = json.load(jf)


#print(ec)

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

r_moon = ec['r_moon_km']
r_sun = ec['r_sun_km']

accuracy_s = ec['accuracy_s']

c1 = eclipseTimes.t_c1(date, p, ephem, r_moon, r_sun, accuracy_s).utc
c2 = eclipseTimes.t_c2(date, p, ephem, r_moon, r_sun, accuracy_s).utc
mid = eclipseTimes.t_center(date, p, ephem, accuracy_s).utc
c3 = eclipseTimes.t_c3(date, p, ephem, r_moon, r_sun, accuracy_s).utc
c4 = eclipseTimes.t_c4(date, p, ephem, r_moon, r_sun, accuracy_s).utc



def tuple_to_json(c):
    return {'year': int(c[0]), 'month': int(c[1]), 'day': int(c[2]), 'hour': int(c[3]), 'minute': int(c[4]), 'second': float(c[5])}

ec['c1'] = tuple_to_json(c1),
ec['c2'] = tuple_to_json(c2),
ec['mid'] = tuple_to_json(mid),
ec['c3'] = tuple_to_json(c3),
ec['c4'] = tuple_to_json(c4)

with open('ec.json', "w") as jf:
    json.dump(ec, jf)
