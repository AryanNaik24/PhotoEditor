from PIL import Image , ImageEnhance , ImageFilter
import os

#path from where images are taken to edit
path="./imgs"
#path to which the edited images will be stored 
savePath="/editedImgs"


#loop to go through all the images present in the folder
for filename in os.listdir(path):
    
    #stores every image in the variable
    img = Image.open(f"{path}/{filename}")
    
    #sharpens the image
    edit = img.filter(ImageFilter.SHARPEN)
    
    #factor to enhance by
    factor = 1.2
    
    #enhances the image by increasing contrast by 1.2 times
    enchancer = ImageEnhance.Contrast(edit)
    #applies the filter to edit
    edit = enchancer.enhance(factor)
    
    
    
    #cleanout the name
    clean_name = os.path.splitext(filename)[0]
    
    #saves the edited name
    edit.save(f".{savePath}/{clean_name}_edited.jpg")
    
    
    
    