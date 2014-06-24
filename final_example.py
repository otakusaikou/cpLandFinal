#/usr/bin/python2.7
import Image
import os

def resize_image(img, size, file_name):
    """This function can resize input image object with given size and new file name
Define of input parameters are as follows: 
 img -> an image object
 size -> new width and height, it must be tuple of integers, like (width, height)
 file_name -> new file name, string type
"""
    #Triple quotation marks are used to specify doc string. Doc string can be accessed by the following command: <function name>.__doc__
    
    new_img = img.resize(size)
    new_img.save(file_name)
    print "New file '" + file_name + "' has been created."

def rotate_image(img, angle, file_name):
    """This function can rotate input image object with given size and new file name
Define of input parameters are as follows: 
 img -> an image object
 angle -> rotate angle, it can be integer or float type
 file_name -> new file name, string type
"""
    #Triple quotation marks are used to specify doc string. Doc string can be accessed by the following command: <function name>.__doc__
    
    new_img = img.rotate(angle)
    new_img.save(file_name)
    print "New file '" + file_name + "' has been created."

def main():
    fin = open("files.txt")
    all_image = fin.readlines()  #Read all file names to variable all_image
    
    #----------For question1----------#
    size = [(3.0 / 4), (1.0 / 2), (1.0 / 4)]  #Create resize ratio list. Make sure that the type of numerator is float
    
    #Use for loop to create new image with all input filenames
    for i in range(len(all_image)):
        image_name = all_image[i].replace("\r", "").replace("\n", "")  #Replace invalid characters with empty string
        img = Image.open(image_name)  #Variable img is an image object
        width, height = img.size  #Get image size
        
        #Use for loop to create new image with different resize ratio
        for j in range(len(size)):
            new_size = int(width * size[j]), int(height * size[j])  #The input height and width must be integer
            f, e = os.path.splitext(image_name)  #This function can split filename into a base name and it's extension. Old extension name should not be used
            new_file_name = f + '_%dx%d' % new_size  #Use string formatting to create new filename automatically
            resize_image(img, new_size, new_file_name + ".jpg")
            resize_image(img, new_size, new_file_name + ".tif")
    
    #----------for question2----------#
    angle = [45, 90, 135, 180]  #Create rotate angle list
    image_name = all_image[0].replace("\r", "").replace("\n", "")  #Use first image name as input file name. Replace invalid characters with empty string
    for i in range(len(angle)):  #Use for loop to create new image with different rotate angles
        f, e = os.path.splitext(image_name)  #This function can split filename into a base name and it's extension
        new_file_name = f + ('_rot_%d' % angle[i]) + e  #Use string formatting to create new filename automatically
        img = Image.open(image_name)  #Variable img is an image object
        rotate_image(img, angle[i], new_file_name)
            
if __name__ == "__main__":
    main()
    #print resize_image.__doc__   #uncomment this line to see the function definition of resize_image
    #print rotate_image.__doc__   #uncomment this line to see the function definition of rotate_image
