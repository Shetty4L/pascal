import pandas as pd
import numpy as np
import sys

def main(argv=None):
	# Should try to append all dataframes into a single dataframe, shuffle it, split it and then export to text file
	i = 0
	data = pd.DataFrame()
	train = pd.DataFrame()
	val = pd.DataFrame()

	DIRECTORY_PREFIX = 'data/VOCdevkit/VOC2011/ImageSets/'
	
	for line in file('%sfilenames.txt'%DIRECTORY_PREFIX):
	    temp = pd.read_table('%sformatted/%s'%(DIRECTORY_PREFIX,line[:-1]),delimiter=',',names=['fname','true'],
	                         header=None,dtype={'fname':object,'true':np.int32})
	    temp = temp[temp['true']==1]
	    temp['fname'] = temp['fname'] + '.jpg'
	    temp['true'] = i
	    data = data.append(temp)
	    i = i + 1

	data = data.drop_duplicates('fname',keep='first')
	data = data.sample(n=data.shape[0],replace=True)
	num_train = int(data.shape[0] * 0.7)
	train = data[:num_train]
	val = data[num_train:]

	train.to_csv('train.txt',sep=' ',index=None,header=None,mode='w')
	val.to_csv('val.txt',sep=' ',index=None,header=None,mode='w')

	# data.to_csv('data.txt',sep=' ',index=None,header=None,mode='w')

	filenames = []
	for line in file('%sfilenames.txt'%DIRECTORY_PREFIX):
	    filenames.append(line[:-1])
	filenames = np.array(filenames)

	for i in range(filenames.shape[0]):
	    print i, filenames[i].split('_')[0]

if __name__ == '__main__':
	main()