set datafile separator ','
set xlabel 'Number of Iterations'
set key box linestyle 1 linetype rgb "#000000"
set key spacing 1.5
set term png


directory = 'model3/finetune_only_fc'
train_log = 'model3.log.train'
test_log = 'model3.log.test'

set title 'Plot of Iterations vs Loss'
set ylabel 'Loss'
set output directory.'/loss.png'
set key right top
plot directory.'/'.train_log using 1:5 with line title 'Loss'

set title 'Plot of Iterations vs Accuracy'
set ylabel 'Accuracy'
set output directory.'/accuracy.png'
set key right bottom
plot directory.'/'.train_log using 1:4 with line title 'Training Accuracy' linetype rgb "#FF0000", directory.'/'.test_log using 1:4 with line linetype rgb "#0000FF"title 'Testing Accuracy'

