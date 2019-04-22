import cv2
import sys
import os
from os import listdir
from matplotlib import pyplot as plt
#from PIL import Image
#import datetime as dt

#user supplied values
#imagePath = "111.jpg"
#imagePath = sys.argv[1]

cascPath1 = "haarcascade_frontalface_default.xml"
skiprate = 28 #default skiprate = 28 frames
pOut = pathOut = "./out/"
pIn = pathIn = "./in/"


def crop_faces_from_video (pathIn, pathOut, cascPath1, sr):
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
            print("Cropped {0} faces".format(len(faces)) + ' on frame ' + str(j))
            faces_amount += len(faces)

        j += 1
        ret, frame = cap.read()

    print("::::::\n\tCROPPED FACES TOTAL AMMOUNT: \t"+str(faces_amount))
    print(":::::::::\n\tSKIPRATE: \t"+str(sr))
    print("...........\n..........\n...\n...CROPPER.FIN...\n.........\n......\n...")
    cap.release()
    return(faces_amount)


def crop_faces (pathIn, pathOut, cascPath1):
    i=0
    print("............\n.................\n..........\n...CROPPER.START...\n........\n....\n...\n..\n.")
    plt.rcParams['text.usetex'] = False
    plt.figure(figsize=(2, 2))
    plt.axis('off')


    #create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath1)
    imgIn = [f for f in os.listdir(pathIn)]
    faces_amount=0

    for img in imgIn:
        imagePath = pathIn + img
        #print("..processing "+img)
        #read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
        print("Cropped {0} faces".format(len(faces))+' from: \t' + img)

    print("\n\tPROCESSED IMGS TOTAL AMMOUNT: \t"+str(len(imgIn)))
    print("::::::\n\tCROPPED FACES TOTAL AMMOUNT: \t"+str(faces_amount))
    print("...........\n..........\n...\n...CROPPER.FIN...\n.........\n......\n...")
    return(faces_amount)


while (True):
    Inp=input("*\n* * *\n* * * * * *\n* * * * * * * * *\n* * * * * * * * * * * *\n* * CROPPER * * * * * * * *\n* * * * * * VER. 1.88 * * * * * * * * *\n* * * * * * * * * * * * * * * * * * *\nchose input(v for video mode, q to quit):\t")
    if Inp =='q':
        break
    if Inp =='v':
        Inp = input("\n * * * * * * \n * * * * * *  * * * * * * \n * * * * * * VIDEO MODE ON * * * * * * \n * * * * * * chose video input:\t")
        skiprate = input("\n * * * * * * \n * * * * enter SKIPRATE (28 by default):\t")
        pIn = pathIn + "VID/" + Inp + ".mpg"
        pOut = pathOut + "VID/" + Inp + "/"
        print(pIn)
        crop_faces_from_video(pIn, pOut, cascPath1, skiprate)
    else:
        if not Inp=='':
            pIn = pathIn + Inp + "/"
            pOut = pathOut + Inp + "/"
        crop_faces(pIn, pOut, cascPath1)
    #print("CROPPED FACES TOTAL AMMOUNT: "+str(crop_faces(pIn, pOut,cascPath1)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
