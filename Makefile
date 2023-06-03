main.pdf: main.tex hello-world.py img/hello-world.png img/saturn.png
	lualatex $<
img/hello-world.png: hello-world.py
	python $<
img/saturn.png: hello-world.py
	python $<

