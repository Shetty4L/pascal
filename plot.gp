set datafile separator ','
set xlabel 'Number of Iterations'
set key off
set term png

train_log = directory.'.log.train'
test_log = directory.'.log.test'

set title 'Plot of Iterations vs Loss'
set ylabel 'Loss'
set output directory.'/loss.png'
plot directory.'/'.train_log using 1:5 with line

set title 'Plot of Iterations vs Accuracy'
set ylabel 'Accuracy'
set output directory.'/accuracy.png'
plot directory.'/'.train_log using 1:4 with line title 'Training Accuracy', directory.'/'.test_log using 1:4 with line title 'Testing Accuracy'

