# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline
import numpy as np

f = open('Lumi.2760.csv')
g = f.readlines()
f.close()

h = np.empty((8,12))

for i in range(8):
    h[i] = g[i+1].split(',')[1:]

imshow(h)
colorbar()

f = open('20130524 2760 1 2 3 later.txt')
g = f.readlines()
f.close()

plate_no = 2760

for idx in range(len(g)):
    plate_str = 'Plate:\t'+str(plate_no)
    if plate_str in g[idx]:
        break
print idx

def get_bgal_data(data, idx):
    start_idx = idx + 2
    h = np.empty((8,12))
    h[0] = data[start_idx].strip().replace('\t',' ').split(' ')[1:]
    for i in range(1,8):
        h[i] = data[start_idx+i].strip().replace('\t',' ').split(' ')
    return h

bgal_data = get_bgal_data(g, idx)


imshow(bgal_data)
colorbar()

norm_data = h/(bgal_data-0.07)
imshow(norm_data)

