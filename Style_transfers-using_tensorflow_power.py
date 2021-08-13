import tensorflow_hub as hub 
import tensorflow as tf 
import matplotlib.pyplot as plt 
import numpy as np 
import cv2 

model = hub.load(# put the link of model ----  explore google seatbacks)

## preprocessing image and loading it

def load_image(location);
    img = tf.io.read_file(location)
    img = tf.image.decode_image(img, channels = 1)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]

    return img

content_image = load_image('path_of_img')
style_image = load_image('path_of_img')

## visualise output

content_image.shape

plt.imshow(np.squeeze(content_image))
plt.show()

## Stylize Image

stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

plt.imshow(np.squeeze(stylized_image))
plt.show()

## saving our created image

cv2.imwrite('generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))