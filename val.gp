set datafile separator ','
set xlabel 'Number of Iterations'
set key box linestyle 1 linetype rgb "#000000"
set key spacing 1.5
set term png

set title 'Plot of Iterations vs Validation Accuracies'
set ylabel 'Validation Accuracy'
set output 'accuracies.png'
set key right bottom
plot 'val_accuracies.log' using 1:2 with line title 'Model 1' linetype rgb "#FF0000", 'val_accuracies.log' using 1:3 with line title 'Model 2' linetype rgb "#00FF00", 'val_accuracies.log' using 1:4 with line title 'Model 3' linetype rgb "#0000FF", 'val_accuracies.log' using 1:5 with line title 'Model 4' linetype rgb "#FFFF00", 'val_accuracies.log' using 1:6 with line title 'Model 5' linetype rgb "#FF00FF"

