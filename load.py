import numpy as np
import time
import matplotlib.pylab as plt
from sklearn.utils import shuffle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import simplejson


files=['event_type.txt','log_feature.txt','severity_type.txt','resource_type.txt','trainp1.txt','test.txt','trainp2.txt']

for File in files:
    f=open(File,'r')
    data=simplejson.load(f)
    print 'data from ',File,' is ',data,
    f.close()
    print 'data size is ',len(data)
    print '\n\n'
    time.sleep(5)
    
