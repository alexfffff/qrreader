1. I isolated the first 3 pictures, but couldn't get the 4th one with code so to continue i cropped it manually
, and after the sticher class didn't work out so I just put it together on google slides, 
the code is 0106 took around umm 6 hours

2. My code for the extraction is in main.py, the 1,2,3,4.jpg are original images, roi_0,1,2,3,4 are the images extracted everything else is debugging, the paste.py
doesn't work well

3. you just simply run main.py, and it will create roi_0,1,2,3 corresponding to the order of the original jpg. i dont really know how to do the stiching, 
( i noticed there was overlap between the pictures but for somereason the stiching class said it needed more pictreus/ or it would say requires argument 'masks' pos2 which 
I could find nothing about in the documentation/stackoverflow) so I just did it in google slides

4. I couldn't isolate the fourth picture because there was a glare on the qr code so my method where I change all the white pixels to
black didn't work on that section. The main problem is that there was an area of the background that was darker than the area in the qr code so it would mess with 
the contour detection algorithm so it coudl never detect the qr code byitself, I started doing soemthing with cv2.canny becasue 
if it can identify 2 edges it can get the whole rectangle, but I tried for a while and could never find a way to make the 
code isolate the two edges i needed. so I cropped only the 4th png and saved it as roi_4.jpeg (roi_3.jpeg was what i got when i ran the 4th picture through ). 
then I tried to implement the stiching but even if i rotated the pictures the right way I still couldn't stich it, the final code for paste.py has me rotating them 
manually ( normally i would either use the black bar as a reference point or just try every combination, its only 4^4) and trying to the bottom 2 together like a panorama 
(which is what people normally use stich for) but even then it threw a error code 1 which says need more pictures. I haven't found another way to stich them toghere
so I stopped here. Maybe there are other libraries for stiching but I haven't found any that were better than opencv. If i were given more time, I would implement a way to
universally get the qr code, rn since 2.jpg is brighter i need to use different thresholds and different ways to isolate the qr code, so I would do something about the lighting
and or implement it in such  a way that gets rid of the bias of lighting. and for the qr decoder, i would consdier using a program to covert the picture to a qr in the form 
of an array then I could just implement something to see if the qr codes' edges are equal and if they are i would stich them togehter. 