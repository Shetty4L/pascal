import caffe
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from caffe.proto import caffe_pb2

def main():

	mean_blob = caffe_pb2.BlobProto()
	with open('data/pascal_mean.binaryproto') as f:
		mean_blob.ParseFromString(f.read())

	mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape((3,224,224))

	model = 'deploy.prototxt'
	weights = 'snapshot/pascal_iter_2000.caffemodel'

	caffe.set_mode_cpu()

	net = caffe.Net(model, weights, caffe.TEST, )

	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_mean('data', mean_array)
	transformer.set_transpose('data', (2,0,1))

	image_name = 'car.jpg'
	image = caffe.io.load_image(image_name,color=True)
	image = caffe.io.resize_image(image,(224,224))
	net.blobs['data'].data[...] = transformer.preprocess('data', image)
	result = net.forward()
	output = result['prob']

	plt.figure()
	plt.imshow(mpimg.imread(image_name))
	plt.show()

	print output,output.argmax()

if __name__ == '__main__':
	main()