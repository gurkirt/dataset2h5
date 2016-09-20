import cv2,os
import numpy as np
imgdir = '/mnt/jupiter-alpha/HMDB51/images/'
actionlist = os.listdir(imgdir);
vidcount = 0;
outliers1 = 0;
outliers2 = 0;
for action in actionlist:
	videolist = os.listdir(imgdir+action+'/')
	for vid in videolist:
		img = cv2.imread(imgdir+action+'/'+vid+'/00001.jpg')
		size = np.shape(img)
		vidcount+=1
		if size:	
			#if (size[1]-320)>240:
				outliers1+=size[0]
				outliers2+=size[1]
				#print imgdir+action+'/'+vid

print ' vidcount ', vidcount, ' percentage is ', outliers1/vidcount, ' width ',outliers2/vidcount
			
