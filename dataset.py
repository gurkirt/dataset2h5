import os
import numpy as np
import h5py as h5

class hmdb:
    def __init__(self):
        self.basedir = "/mnt/jupiter-alpha/HMDB51/"
        self.imagedir = "/mnt/jupiter-alpha/HMDB51/images/";
        self.videodir = "/mnt/jupiter-alpha/HMDB51/videos/";
        self.flowdir = "/mnt/jupiter-alpha/HMDB51/motion-images/";
        self.splitdir = "/mnt/jupiter-alpha/HMDB51/testTrainsplits/";
        self.classnames = ['wave','sword_exercise','flic_flac','sit','fall_floor','walk','eat','push','shoot_bow','smoke','shoot_gun','kick',
                           'laugh','ride_horse','pour','pullup','sword','chew','kick_ball','dive','stand','fencing','run','drink','climb_stairs',
                           'hug','catch','hit','shake_hands','shoot_ball','clap','turn','kiss','pushup','talk','situp','golf','ride_bike','smile',
                           'climb','punch','draw_sword','handstand','somersault','swing_baseball','throw','brush_hair','dribble','cartwheel','pick','jump'];
    def saveAsH5(self):
        imgcount = 0;
        mydict = dict();
        with h5py.File( self.basedir + '/data.h5', 'w') as f:
            for aidx,action in enumerate(self.classnames):
                videoFolderlist = os.listdir(self.imagedir+'/'+action);
                numVideos = len(videoFolderlist);
                mydict[aidx]['numVideos'] = numVideos;
                mydict[aidx]['actionName'] = action
                mydict[aidx]['actionDir'] = self.imagedir+'/'+action
                for split in np.arange(1,4):
                    train[split],valid[split],test[split] = actionSplit(action,split);
                trainlist = []; validlist = []; testlist = [];
                for vidx,vid in videos:
                    imglist = os.listdir(mydict[aidx]['actionDir']+'/'+action);
                    numImages = len(imglist);
                    mydict[aidx][vidx]['numImages'] = numImages;
                    mydict[aidx][vidx]['initIndex'] = imgcount;
                    mydict[aidx][vidx]['videoName'] = vid
                    if vid in trainlist:
                        trainlist.append(vidx)
                    elif vid in trainlist:
                        validlist.append(vidx)
        # f['data']['action']['video'][]
    
        
    def actionSplit(action,split):
        filename = self.splitdir+action+'_test_split'+str(split)+'.txt'
        with open(filename,'r') as f:
            lines = f.readlines()
        trainvideos = []
        testvideos = []
        for line in lines:
            temp = line.split(' ');
            if temp[1] == '1':
               trainvideos.append(temp[0])
            elif temp[1] == '2':
                testvideos.append(temp[0])
        validvideos = trainvideos[60:]
        trainvideos = trainvideos[:60]
        return trainvideos,validvideos,testvideos