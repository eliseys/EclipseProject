from planetaryimage import PDS3Image
#import pdr

import matplotlib.pyplot as plt

testfile = 'test.img'
# testfile = 'tests/mission_data/2p129641989eth0361p2600r8m1.img'
image = PDS3Image.open(testfile)
#print(image) 

#data = pdr.read(testfile)
print(data)



