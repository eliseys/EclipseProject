import numpy as np

from scipy.spatial.transform import Rotation as R
from astropy.coordinates import cartesian_to_spherical, spherical_to_cartesian

degrees = np.pi/180.0

latitude_libration = -6.749
longitude_librarion = 1.520




#v = np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])
v = np.array([1.0, 0.0, 0.0])

delta_v = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.1]])

v = np.resize(v, np.shape(delta_v)) + delta_v


r_x = R.from_euler('x', latitude_libration, degrees=True)
r_y = R.from_euler('y', longitude_librarion, degrees=True)


v_libr = r_y.apply(r_x.apply(v))

print(v_libr)
print(cartesian_to_spherical(v_libr[0], v_libr[1], v_libr[2]))














