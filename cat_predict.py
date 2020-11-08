import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model


model =tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Conv2D(128, (3,3), activation ='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax')
])

model = load_model('../model/cat')

# sample labels
labels=["apetite_loss","hair_loss", "patch", "ticks", "watery_eyes"]

import numpy as np
from tensorflow.keras.preprocessing import image
# path = input()
# path =uploaded
path="../test/10.jpeg"
img= image.load_img(path,target_size=(150,150))
x= image.img_to_array(img)
x=np.expand_dims(x, axis=0)

images=np.vstack([x])
classes=model.predict(images, batch_size=10)
cout=0
for i in range(4):
    if classes[0][i]>classes[0][i+1]:
        classes[0][i+1]=classes[0][i]
    else:
        cout+=1
print(labels[cout])


