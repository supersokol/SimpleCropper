import cv2
import sys
import os
from matplotlib import pyplot as plt
import argparse
import logging

def crop_faces_from_video (pathIn, pathOut, cascPath1, sr, log):
    cap=cv2.VideoCapture(pathIn)
    faceCascade = cv2.CascadeClassifier(cascPath1)
    ret, frame = cap.read()
    faces_amount = 0
    i=0
    j=0
    while ret:
        if j % int(sr) == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30)
            )
            # cropping faces into files
            for (x, y, w, h) in faces:
                plt.imshow(gray[y: y + h, x: x + w],
                           cmap='gray', interpolation='bilinear')
                if not os.path.exists(pathOut+str(sr) + '/'):
                    os.makedirs(pathOut + str(sr) + '/')
                plt.savefig(pathOut + str(sr) + '/' + "_plt%d_%03d.png" % (i, i))
                i += 1
            log.info("Cropped {0} faces".format(len(faces)) + ' on frame ' + str(j))
            faces_amount += len(faces)
        j += 1
        ret, frame = cap.read()
    cap.release()
    return(faces_amount)


def crop_faces (pathIn, pathOut, cascPath1, log):
    i=0
    plt.rcParams['text.usetex'] = False
    plt.figure(figsize=(2, 2))
    plt.axis('off')


    #create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath1)
    imgIn = [f for f in os.listdir(pathIn)]
    faces_amount=0

    for img in imgIn:
        imagePath = pathIn + img
        log.info(f"..processing image file: {img}")
        #read the image
        image = cv2.imread(imagePath)
        log.info('imread complete')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        log.info('greyscale complete')
        #detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(15, 15)
        )
        #cropping faces into files
        for (x, y, w, h) in faces:
                plt.imshow	(gray [ y: y + h, x: x + w ],
                cmap = 'gray', interpolation = 'bilinear')
                if not os.path.exists(pathOut):
                    os.makedirs(pathOut)
                plt.savefig(pathOut+"_plt%d_%03d.jpg" % (i,i))
                i+=1

        faces_amount += len(faces)
        log.info("Cropped {0} faces".format(len(faces))+' from: \t' + img)

    log.info("\n\tPROCESSED IMGS TOTAL AMMOUNT: \t"+str(len(imgIn)))
    return(faces_amount)

# do all stuff
if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input_path',    default=None,                                   type=str,   help='Path to a image, directory containig images or video. (str, default: None)')
    argparser.add_argument('-o', '--output_path',   default="./out/",                               type=str,   help='output path, str, defaults to \"output\" directory')
    argparser.add_argument('-v', '--video_input',   default=False,                                  type=bool,  help='Video input (bool, default is False).')
    argparser.add_argument('-s', '--skiprate',      default=28,                                     type=int,   help='optional skiprate (int, for video only, default is 28).')
    argparser.add_argument('-c', '--cascade_path',  default="haarcascade_frontalface_default.xml",  type=str,   help='haar cascade filename path.')
    argparser.add_argument('-l', '--log_path',      default='./new_log.log',                        type=str,   help='optional log filename.')
    
    args = argparser.parse_args()
    log_file = args.log_path
    if log_file:
        logging.basicConfig(filename = log_file,
                            filemode = 'a',
                            format = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt = '%H:%M:%S',
                            level = logging.INFO)
    else:
        logging.basicConfig(level = logging.INFO)
    
    log = logging.getLogger("opencv_haar_cascade_face_cropping_script")

    if args.video_input:
        log.info('Video mode is on')
        log.info(f'Chosen skiprate is {args.skiprate}.')
        try:
            faces_amount = crop_faces_from_video(
                args.input_path, args.output_path, args.cascade_path, args.skiprate, log)
            log.info('Success!')
            log.info(f"CROPPED FACES TOTAL AMOUNT: {faces_amount}.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            sys.exit(0)
        except Exception as err:
            log.info('Error occured!')
            log.info(' %s' % err)
            sys.exit(1)
    else: 
        try:
            if os.path.isdir(args.input_path):
                args.input_path += '\\'
            faces_amount = crop_faces(
                args.input_path, args.output_path, args.cascade_path, log)
            log.info('Success!')
            log.info(f"CROPPED FACES TOTAL AMOUNT: {faces_amount}.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            sys.exit(0)
        except Exception as err:
            log.info('Error occured!')
            log.info(' %s' % err)
            sys.exit(1)