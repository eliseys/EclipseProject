import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.transform import Rotation as R

degrees = np.pi/180.0

latitude_libration = -6.749
longitude_librarion = 1.520
R_moon = 1737.4 


def libration(v, latitude_libration, longitude_librarion, degrees=True):
    r_y = R.from_euler('y', latitude_libration, degrees=degrees)
    r_z = R.from_euler('x', longitude_librarion, degrees=degrees)
    return r_z.apply(r_y.apply(v))


def v2s(v):
    r       =  np.sqrt(v[:,0]*v[:,0] + v[:,1]*v[:,1] + v[:,2]*v[:,2])
    theta   =  np.arccos(v[:,2]/r) 
    phi     =  np.arctan2(v[:,1], v[:,0])
    s = np.array([r, theta, phi])
    return np.transpose(s)


def s2v(s):
    x = s[:,0] * np.sin(s[:,1]) * np.cos(s[:,2])
    y = s[:,0] * np.sin(s[:,1]) * np.sin(s[:,2])
    z = s[:,0] * np.cos(s[:,1])
    v = np.array([x, y, z])
    return np.transpose(v)



def h(s):
    
    return np.ones(len(s)) * R_moon




o = np.array([1.0, 0.0, 0.0]) 
o = libration(o, latitude_libration, longitude_librarion)


N = 360
limb_angle = np.linspace(0.0, 2.0 * np.pi, N)
limb_phi = -(np.pi/2) * np.sign(np.sin(limb_angle))

x_0 = np.zeros(N)
y_0 = R_moon * np.sin(limb_angle) * np.sin(limb_phi)
z_0 = R_moon * np.cos(limb_angle)

l_0 = np.transpose(np.array([x_0, y_0, z_0]))

l_0 = libration(l_0, latitude_libration, longitude_librarion)

M = 20
L = 100.0


o = np.resize(o, np.shape(l_0))


H = []

for dx in np.linspace(-L, L, 2 * M + 1):
    l = l_0 + o * dx
    s = v2s(l)
    H.append(h(s) * np.cos(np.arctan2(np.ones(len(s)) * dx, np.ones(len(s)) * R_moon)))

H = np.array(H)

H = np.transpose(H)


limb = []

for u in H:
    limb.append(np.amax(u))




    
print(np.transpose(np.array([limb_angle, limb])))


