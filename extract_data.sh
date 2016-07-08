#!/bin/bash

tarfile=$1
if [ -z $tarfile ]; then
	echo "Please enter a tar file"
	exit 1
fi

tar -xvf $tarfile

mv TrainVal/ data/

cd data/VOCdevkit/VOC2011

rm -rf SegmentationClass Annotations SegmentationObject

cd ImageSets

rm -rf Action Layout Segmentation

mv Main original

cd original 

ls | grep -v _trainval | xargs rm

cd ..

mkdir formatted

for line in $(ls original | grep _trainval)
do
	STR="$(cat original/${line} | tr -s " ")"
	echo "${STR// /,}" > formatted/${line}
done

ls formatted > filenames.txt

cd ../../../..

echo "Labels: "
python label_processing.py train

