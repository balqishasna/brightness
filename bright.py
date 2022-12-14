# python program to demonstrate the brightness of the image with the brightness_range argument

# we import all our required libraries
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot

# we first load the image
image = load_img('koex.jpeg')
# we converting the image which is in PIL format into the numpy array, so that we can apply deep learning methods
dataImage = img_to_array(image)
# print(dataImage)
# expanding dimension of the load image
imageNew = expand_dims(dataImage, 0)
# now here below we creating the object of the data augmentation class
imageDataGen = ImageDataGenerator(brightness_range=[0.2,1.0])
# because as we alreay load image into the memory, so we are using flow() function, to apply transformation
iterator = imageDataGen.flow(imageNew, batch_size=1)
# below we generate augmented images and plotting for visualization
for i in range(9):
	# we are below define the subplot
	pyplot.subplot(330 + 1 + i)
	# generating images of each batch
	batch = iterator.next()
	# again we convert back to the unsigned integers value of the image for viewing
	image = batch[0].astype('uint8')
	# we plot here raw pixel data
	pyplot.imshow(image)
# visualize the the figure
pyplot.show()