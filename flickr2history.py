#!/usr/bin/python


__author__ = "pkolarov@gmail.com"

import dbhash,anydbm
import sys, os, shelve, logging,string
import threading, Queue
import flickr

user = None
uploaded = None
lock = None


#get one and only one photo for the given tags or None
#this works only if we previously tagged all the pics on Flickr with uploader tool automaticaly
#
#Plus delete images that contain the same TAGS !!!!
def getPhotoIDbyTag(tag):
  
    
    retries = 0
    photos = None
    while (retries < 3):
        try:
                logging.debug(user.id)
                photos = flickr.photos_search(user_id=user.id, auth=all, tags=tag,tag_mode='any')
                break
        except:
                logging.error("flickr2history: Flickr error while searching ....retrying")
                logging.error(sys.exc_info()[0])
                
        retries = retries + 1
        
    if (not photos or len(photos) == 0):
        logging.debug("flickr2history: No image in Flickr (yet) with tags %s (possibly deleted in Flickr by user)" % tag)
        return None
    
    logging.debug("flickr2history: Tag=%s found %d" % (tag, len(photos)))
    while (len(photos)>1):
        logging.debug( "flickr2history :Tag %s matches %d images!" % (tag, len(photos)))
        logging.debug("flickr2history: Removing other images")
        try:
            photos.pop().delete()
        except:
            logging.error("flickr2history: Flickr error while deleting duplicate image")
            logging.error(sys.exc_info()[0])
   
    return photos[0]


class ReshelfThread (threading.Thread):
    def __init__(self, threadID, imageDir, imageQueue, historyFile):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.imageDir = imageDir 
        self.imageQueue = imageQueue
        self.historyFile = historyFile

    def has_key(self, image):
        global lock
        global uploaded
        with lock:
            return uploaded.has_key(str(image)) 
    
    def update(self, image, photo):
        global lock
        global uploaded
        with lock:
            uploaded[ str(image)] = str(photo.id)
            uploaded[ str(photo.id) ] =str(image)
            uploaded.close();
            uploaded = shelve.open(self.historyFile )   #its better to always reopen this file

    def run(self):
        logging.debug( "Starting ReshelfThread %d " % self.threadID )

        while True:
            try:
                image = self.imageQueue.get_nowait()
                logging.debug( "ReshelfThread %d qSize: %d processing %s" % (self.threadID, self.imageQueue.qsize(), image) )

                image = image[len(self.imageDir):] #remove absolute directory
                if ( not self.has_key(str(image) ) ):
                    #each picture should have one id tag in the folder format with spaces replaced by # and starting with #
                    flickrtag = '#' + image.replace(' ','#')
                    logging.debug(flickrtag)
                    photo = getPhotoIDbyTag(flickrtag)
                    logging.debug(image)
                    if not photo:
                        #uploaded.close()  # flush the DB file
                        continue
                    logging.debug("ReshelfThread: Reregistering %s photo in local history file" % image)

                    self.update(image, photo)
            except Queue.Empty:
                break
        logging.debug( "Exiting ReshelfThread %d " % self.threadID )


#store image reference in the history file if its not there yet and if we actually can
#find it on Flickr
def reshelf(images,  imageDir, historyFile, numThreads):
     
    logging.debug('flickr2history: Started flickr2history')
    try:
        global user
        user = flickr.test_login()
        logging.debug(user.id)
    except:
        logging.error(sys.exc_info()[0])
        return None 

    imageQueue = Queue.Queue();
    for image in images:
        imageQueue.put_nowait(image)

    global uploaded
    uploaded = shelve.open( historyFile )   #its better to always reopen this file

    global lock
    lock = threading.Lock()
    threads = []
    for i in range(numThreads):
        thread = ReshelfThread(i, imageDir, imageQueue, historyFile)
        threads.append(thread) 
        thread.start()

    for thrd in threads:
        thrd.join()

    uploaded.close()

    logging.debug('flickr2history: Finished flickr2history')
   
