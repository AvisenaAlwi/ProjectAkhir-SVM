# SVM
## Reuirement
1. Pyhton 3.x
2. Numpy
3. Pandas
4. Matplotlib (optional)
5. xlrd

## How to Use
1. Run ```pip list``` on your terminal or cmd
2. Check is numpy, matplotlib, pandas and xlrd installed or not

## How to Install
1. Install numpy. ```pip install numpy```
2. Install pandas. ```pip install pandas```
3. Install matplotlib. ```pip install matplotlib```
4. Install xlrd. ```pip install xlrd```

*nb : matplotlib is optional. But if you run ```main_vis.py```, matplotlib is required.
## Files
* main.py - Main file
* main_vis.py - SVM Visualisation of main.py
	* Red marker : positive class
	* Blue marker : negative class
	* Green marker : data test
		* if the green marker is above the hyperplane, the test data includes a positive class, otherwise include a negative class
