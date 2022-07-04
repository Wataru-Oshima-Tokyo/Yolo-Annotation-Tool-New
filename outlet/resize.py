import os
from PIL import Image
# directory_files = "Images/outlet/"
directory_files = os.listdir()
multiple_images = [file for file in directory_files if 'outlet' in file and file.endswith(('.jpg', '.png'))]
# multiple_images = [file for file in directory_files]
print(multiple_images)

# Looping over all of the images:

for image in multiple_images:
    img = Image.open(image)
    img.thumbnail(size=(300,300))
    print(img)
    img.save('./resized/resized-image_'+image, optimize=True, quality=30)

    # We would run the command below to save the images:
    # img.save('resized-image_'+image, optimize=True)