for f in *.jpg;
do
	convert -flop $f "flip_$f"
done

for f in *.jpg;
do
	read w h < <(convert $f -format "%w %h" info:)
	((x=RANDOM % (w-256) ))
	((y=RANDOM % (h-256) ))
	convert $f -crop 256x256+0+0 "crop1_$f" 
	convert $f -crop 256x256+${x}+0 "crop2_$f"
	convert $f -crop 256x256+0+${y} "crop3_$f"
	convert $f -crop 256x256+${x}+${y} "crop4_$f"
done