import cv2
import numpy as np
total = 0
for x in range(1,5):
    img = cv2.imread( str(x) + '.jpg')
    #img = cv2.imread('4.jpg')
    print(x)
    imgtemp = img.copy()
    if x == 2:
        (thresh, img_bin) = cv2.threshold(img, 240, 255,cv2.THRESH_BINARY)
        img[img_bin == 255] = 0
        (thresh, img_bin) = cv2.threshold(img, 110, 255,cv2.THRESH_BINARY)
    elif x == 4:
        (thresh, img_bin) = cv2.threshold(img, 200, 255,cv2.THRESH_BINARY)
        
        img[img_bin == 255] = 0
        
        (thresh, img_bin) = cv2.threshold(img, 50, 255,cv2.THRESH_BINARY)
        
        
    else:
        (thresh, img_bin) = cv2.threshold(img, 240, 255,cv2.THRESH_BINARY)
        img[img_bin == 255] = 0
        (thresh, img_bin) = cv2.threshold(img, 49, 255,cv2.THRESH_BINARY)

    


    
    lower_black = np.array([0,0,0], dtype = "uint16")
    upper_black = np.array([70,70,70], dtype = "uint16")
    black_mask = cv2.inRange(img_bin, lower_black, upper_black)  


    if x == 2:

        kernel = np.ones((5,5),np.uint8)
        black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
        black_mask = 255- black_mask
        black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
    elif x == 4:
        kernel = np.ones((10,10),np.uint8)
        black_mask = 255- black_mask
        black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
        cv2.imwrite('Image_bin2.png',black_mask)
        #black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)

    else:
        black_mask = 255- black_mask
        kernel = np.ones((10,10),np.uint8)
        black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
    
    

    contours, hierarchy = cv2.findContours(black_mask, 1, 2)

    def subimage(image, center, theta, width, height):

        ''' 
        Rotates OpenCV image around center with angle theta (in deg)
        then crops the image according to width and height.
        '''

        # Uncomment for theta in radians
        #theta *= 180/np.pi

        shape = ( image.shape[1], image.shape[0] ) # cv2.warpAffine expects shape in (length, height)

        matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
        image = cv2.warpAffine( src=image, M=matrix, dsize=shape )

        x = int( center[0] - width/2.0  )
        y = int( center[1] - height/2.0 )

        image = image[ y:y+int(height), x:x+int(width) ]

        return image
    edge = cv2.Canny(black_mask, 100, 200)
    cv2.imwrite('Image_bin.png',edge)
    (cnts, _) = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    areamin = 40000
    areamax = 70000
    for c in cnts:

        if cv2.contourArea(c) > areamin:
            print(cv2.contourArea(c))
            epsilon = 0.1 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            box = cv2.minAreaRect(approx)
            print(box)
            if(box[1][1] != 0.0):
                tempimg = subimage(imgtemp, box[0], theta=box[2], width=box[1][0], height=box[1][1])
                cv2.imwrite('ROI_{}.jpeg'.format(total),tempimg)
                total += 1
    
