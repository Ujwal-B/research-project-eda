import cv2
import os
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

path = "../../data-analysis/Mango/"
all_dir = os.listdir(path)

euclidean_dist_y = []
x_axis = []

# calculates the histogram value for the test image
image = cv2.imread(path + all_dir[50])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
# calchist(image_to_calculate_histogram_on, channel_no, mask, no_of_bins, range)

# Calculates the histogram value for each image and compares it with the 50th image
for file in all_dir:
    image = cv2.imread(path + file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram1 = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    c1 = 0
   
    # Euclidean Distace between file and all_dir[50]
    i = 0
    while i<len(histogram) and i<len(histogram1):
        c1+=(histogram[i]-histogram1[i])**2
        i+= 1
    c1 = c1**(1 / 2)
    euclidean_dist_y.append(round(float(c1), 2))
      
print(euclidean_dist_y)
for i in range(len(euclidean_dist_y)):
    x_axis.append(i+1)
print(x_axis)

# plt.plot(x_axis, euclidean_dist_y)
# plt.bar(x_axis, euclidean_dist_y, align='center', alpha=0.5)
plt.scatter(x_axis, euclidean_dist_y)
plt.xlabel('Image number')
plt.ylabel('Euclidean distance')
plt.title('ScatterPlot of Mango Image Variation')
plt.show()

###########################################################
   
