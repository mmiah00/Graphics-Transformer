run: main.py display.py draw.py matrix.py parsing.py
	python main.py
	# convert pic.ppm pic.png
	# imdisplay pic.png

clean:
	rm *.pyc
	rm *~
