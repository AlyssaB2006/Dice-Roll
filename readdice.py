import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

globs=glob.iglob('**/t*')

d1=d2=d3=d4=d5=d6=0

data = []

for file in globs:
    
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    params = cv2.SimpleBlobDetector_Params()

    params.filterByArea = True
    params.minArea = 30
    params.filterByCircularity = True

    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(img)
    keypoint = len(keypoints)

    if keypoint == 1:
        d1+=1
        data.append(1)
    elif keypoint == 2:
        d2+=1
        data.append(2)
    elif keypoint == 3:
        d3+=1
        data.append(3)
    elif keypoint == 4:
        d4+=1
        data.append(4)
    elif keypoint == 5:
        d5+=1
        data.append(5)
    elif keypoint == 6:
        d6+=1
        data.append(6)
    else:
        print(f"error or above d6 in {file}")
   
#print(f"d1:{d1}\nd2:{d2}\nd3:{d3}\nd4:{d4}\nd5:{d5}\nd6:{d6}")
#optional uncomment ^^ to print exact numbers

bins = np.arange(1, 6 + 1.5) - 0.5
plt.figure(num='Data plot')
plt.hist(data, bins, color="#FC0ECC", edgecolor='black')
plt.title(f'Frequency of dice faces (n={len(data)})', fontweight = 'bold')
plt.show()
