import pandas as pd
import numpy as np


# Should try to append all dataframes into a single dataframe, shuffle it, split it and then export to text file
i = 0
data = pd.DataFrame()
train = pd.DataFrame()
val = pd.DataFrame()
for line in file('filenames.txt'):
    temp = pd.read_table('formatted/%s'%line[:-1],delimiter=',',names=['fname','true'],
                         header=None,dtype={'fname':object,'true':np.int32})
    temp = temp[temp['true']==1]
    temp['fname'] = temp['fname'] + '.png'
    temp['true'] = i
    temp2 = pd.DataFrame()
    temp2['fname'] = 'crop1_' + temp['fname']
    temp2['true'] = i
    temp3 = pd.DataFrame()
    temp3['fname'] = 'crop2_' + temp['fname']
    temp3['true'] = i
    temp4 = pd.DataFrame()
    temp4['fname'] = 'crop3_' + temp['fname']
    temp4['true'] = i
    temp5 = pd.DataFrame()
    temp5['fname'] = 'crop4_' + temp['fname']
    temp5['true'] = i
    temp6 = pd.DataFrame()
    temp6['fname'] = 'flip_' + temp['fname']
    temp6['true'] = i
    temp = temp.append(temp2)
    temp = temp.append(temp3)
    temp = temp.append(temp4)
    temp = temp.append(temp5)
    temp = temp.append(temp6)
    data = data.append(temp)
    i = i + 1

data = data.drop_duplicates('fname',keep='first')
data = data.sample(n=data.shape[0],replace=True)
num_train = int(data.shape[0] * 0.7)

train = data[:num_train]
val = data[num_train:]

train.to_csv('../train.txt',sep=' ',index=None,header=None,mode='w')
val.to_csv('../val.txt',sep=' ',index=None,header=None,mode='w')

filenames = []
for line in file('filenames.txt'):
    filenames.append(line[:-1])
filenames = np.array(filenames)

for i in range(filenames.shape[0]):
    print i, filenames[i].split('_')[0]
