import os
os.environ['GLOG_minloglevel'] = '2' 
import caffe
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from caffe.proto import caffe_pb2

def main():

	mean_blob = caffe_pb2.BlobProto()
	with open('lmdb/mean_file.binaryproto') as f:
		mean_blob.ParseFromString(f.read())

	mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape((3,128,128))

	model = 'model3/deploy.prototxt'
	weights = 'model3/snapshot/model3_iter_10000.caffemodel'

	# caffe.set_device(0)
	caffe.set_mode_cpu()

	net = caffe.Net(model, weights, caffe.TEST, )

	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_mean('data', mean_array)
	transformer.set_transpose('data', (2,0,1))
	transformer.set_raw_scale('data',255)
	transformer.set_channel_swap('data', (2,1,0))

	# images = os.listdir('plots/incorrect')

	images = ['horse.jpg','sheep.jpg','aeroplane.jpg','boat.jpg']
	true_labels = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable','dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']
	
	print 'Actual images: ',images
	print 'Predicated labels: '
	for image_name in images:
		image_name = 'test_data/%s'%image_name
		image = caffe.io.load_image(image_name,color=True)
		image = caffe.io.resize_image(image,(128,128))
		net.blobs['data'].data[...] = transformer.preprocess('data', image)
		result = net.forward()
		output = result['prob'][0]

		# plt.figure()
		# plt.imshow(mpimg.imread(image_name))
		# plt.show()

		print image_name, true_labels[output.argmax()]

if __name__ == '__main__':
	main()
