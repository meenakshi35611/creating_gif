import os
import imageio.v3 as iio
filenames = [r'Your_file _path\nyan-cat1.png', 
             r'Your_file_path\nyan-cat2.png',
             r'Your_file path\nyan-cat3.png']  # add your file path
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('cat_nyan.gif',images,duration = 500,loop=0)
os.startfile("cat_nyan.gif")
'''
P.S:
if the code isn't working the problem maybe with the file path or its name. 
smtimes the terminal considers '/' symbol for inbuilt operation from library such as /n,/t etc so its better to use 'r' before the path 
also it should actually create the gif file where the code file is situated 
but if not found then os.startfile helps to open the file independant of the file location or the file type.
'''
