#pritilata_biswas
import cv2
import numpy as np

im = cv2.imread('input_2.jpg', cv2.IMREAD_GRAYSCALE)


im = 255 - im


proj = np.sum(im,1)


m = np.max(proj)
w = 500
result = np.zeros((proj.shape[0],500))


for row in range(im.shape[0]):
   cv2.line(result, (0,row), (int(proj[row]*w/m),row), (255,255,255), 1)


cv2.imwrite('output_2.jpg', result)

########## showing output  ##########
cv2.imshow('image', result)
#####################################

############ save output ##############
k = cv2.waitKey(0) & 0xFF
# press ESC to close  
if k == 27:  
    cv2.destroyAllWindows() 
# press s to save the output     
elif k == ord('s'):  
    cv2.imwrite('output_2.jpg',rotated) 
    cv2.destroyAllWindows() 
#########################################