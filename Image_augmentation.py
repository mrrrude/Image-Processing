#Author:pratikpandey

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=90,
        brightness_range=[0.75,1.25],
        width_shift_range=0.15,
        height_shift_range=0.15,
        shear_range=0.15,
        zoom_range=[0.8,1.2],
        horizontal_flip=True,
        fill_mode='nearest'
        )

import os

path = 'source_directory'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpg' )): # whatever file types you're using...
        filenames.append(filename)

#filenames.sort()





for i in filenames:
    img = load_img('D:\PratikWorkspace\Training400\Cat-vs-Dog'+'/'+i)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,save_to_dir='D:\PratikWorkspace\FakeValidation\Cat-vs-Dog', save_prefix='C', save_format='jpg'):
        i += 1
        if i > 1:
           break  # otherwise the generator would loop indefinitely
