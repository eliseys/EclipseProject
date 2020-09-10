import numpy as np
from skyfield.api import load
from skyfield.api import Topos
import matplotlib.pyplot as plt


R_moon = 1737.4 #km
R_sun = 696000.0 #km


planets = load('de421.bsp')
earth, moon, sun = planets['earth'], planets['moon'], planets['sun']

ts = load.timescale()
#t = ts.now()
t = ts.utc(2020, 12, 14, 16, 7, np.arange(0, 240, 0.01))
#t = ts.utc(2020, np.arange(0, 12, 0.1))

print(len(t))

obs_location = earth + Topos('39.88836 S', '69.87577 W', elevation_m=449)  
#obs_location = earth + Topos('39.84835 S', '69.87581 W')  

m = obs_location.at(t).observe(moon)
s = obs_location.at(t).observe(sun)

separ = m.separation_from(s).radians*206265

T_center = t[np.argmin(separ)]
print(T_center.utc)


distance_to_moon = obs_location.at(T_center) - moon.at(T_center)
distance_to_sun = obs_location.at(T_center) - sun.at(T_center)

R_apparent_moon = (R_moon/distance_to_moon.distance().km)*206265
R_apparent_sun = (R_sun/distance_to_sun.distance().km)*206265


#print('%d' % distance_to_moon.distance().km)

rr = R_apparent_moon - R_apparent_sun

for i in range(len(separ)-1):
    if (separ[i] - rr)*(separ[i+1] - rr) <= 0:
        print(t[i].utc)


plt.grid()
plt.plot((t.tt - t[0].tt)*86400, separ)

plt.show()


