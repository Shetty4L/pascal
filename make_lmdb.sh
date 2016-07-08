#./extract_data.sh VOCtrainval_25-May-2011.tar

#mkdir lmdb

GLOG_logtostderr=1 ~/caffe/build/tools/convert_imageset --resize_height=128 --resize_width=128 data/VOCdevkit/VOC2011/JPEGImages/ train.txt lmdb/train_lmdb

GLOG_logtostderr=1 ~/caffe/build/tools/convert_imageset --resize_height=128 --resize_width=128 data/VOCdevkit/VOC2011/JPEGImages/ val.txt lmdb/val_lmdb
