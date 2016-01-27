import numpy as np
import csv
import matplotlib.pylab as plt
from sklearn.utils import shuffle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import simplejson
import re



target=[]
event_type=[]
log_feature=[]
severe=[]
trainp1=[]
trainp2=[]
test=[]
files=['event_type.csv','log_feature.csv','severity_type.csv','resource_type.csv','train.csv','test.csv']

def data():
    
    for datasets in files:
        f=open(datasets,'r')
        readcsv=csv.reader(f)
        data=[]
        i=1
        
        if datasets!='train.csv':
            if datasets=='train.csv':
                continue
            print 'Processing File1 ',datasets
            for line in readcsv: 
                if i==1:
                    i=i+1
                    continue;
                d={}
                a=re.search('\d+$',line[1])
                a=int(a.group(0))
                id1=int(line[0])
                d[id1]=a
                data.append(d)
                i=i+1
                #print 'Processing datasets',datasets,' Line ',i
            print 'size of data is ',len(data)    
            
            if datasets=='event_type.csv':
                print 'assigned event_type'
                event_type=data
                f2=open('event_type.txt','wb')
                f2.write(simplejson.dumps(event_type)) 
                f2.close()
            elif datasets=='log_feature.csv':
                print 'assigned log_feature'
                log_feature=data
                f2=open('log_feature.txt','wb')
                f2.write(simplejson.dumps(log_feature)) 
                f2.close()
            elif datasets=='severity_type.csv':
                print 'assigned severity_type'
                severity_type=data
                f2=open('severity_type.txt','wb')
                f2.write(simplejson.dumps(severity_type)) 
                f2.close()
            elif datasets=='resource_type.csv':
                print 'assigned resource_type'
                resource_type=data
                f2=open('resource_type.txt','wb')
                f2.write(simplejson.dumps(resource_type)) 
                f2.close()
            else:
                test=data
                f2=open('test.txt','wb')
                f2.write(simplejson.dumps(test)) 
                f2.close()
       
            f.close()
            print '\n'
       
       
        else:
            f=open(datasets,'r')
            readcsv=csv.reader(f)
            data1=[]
            data2=[]
            i=1
            print 'Processing File ',datasets
             
            for line in readcsv: 
                if i==1:
                    i=i+1
                    continue;
                d1={}
                d2={}
                a=re.search('\d+$',line[1])
                a=int(a.group(0))
                id1=int(line[0])
                d1[id1]=a
                data1.append(d1)
                d2[id1]=int(line[2].strip())
                data2.append(d2)
                i=i+1
                #print 'Processing datasets ',datasets,'Line ',i
            print 'size of data1 is ',len(data1)  
            print 'size of data2 is ',len(data2)  
            trainp1=data1
            trainp2=data2
            f2=open('trainp1.txt','wb')
            f2.write(simplejson.dumps(data1)) 
            f2.close()
            f2=open('trainp2.txt','wb')
            f2.write(simplejson.dumps(data2)) 
            f2.close()
            f.close()
            print '\n'
            
data()
print 'the size of event is  ',len(event_type)
         
             
       
                
            
