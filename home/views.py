from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from django.http import HttpResponse

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
modelcat=model
modeldog=model

modeldog = load_model('model/dog')
modelcat = load_model('model/cat')
labels=["apetite_loss","hair_loss", "patch", "ticks", "watery_eyes"]
# sample labels
import numpy as np
from tensorflow.keras.preprocessing import image

def pridictdog(path):
    path=path
    img= image.load_img(path,target_size=(150,150))
    x= image.img_to_array(img)
    x=np.expand_dims(x, axis=0)

    images=np.vstack([x])
    classes=modeldog.predict(images, batch_size=10)
    cout=0
    for i in range(4):
        if classes[0][i]>classes[0][i+1]:
            classes[0][i+1]=classes[0][i]
        else:
            cout+=1
    return labels[cout]




def pridictcat(path):
    path=path
    img= image.load_img(path,target_size=(150,150))
    x= image.img_to_array(img)
    x=np.expand_dims(x, axis=0)

    images=np.vstack([x])
    classes=modelcat.predict(images, batch_size=10)
    cout=0
    for i in range(4):
        if classes[0][i]>classes[0][i+1]:
            classes[0][i+1]=classes[0][i]
        else:
            cout+=1
    return labels[cout]


def home(request):
    return render(request, 'home/home.html')

def sub(request):
    return render(request, 'home/subscription.html') 

def uploadcat(request):
    if request.method == 'POST':
        print(request)
        print (request)
        print (request.POST.dict())
        fileObj=request.FILES['filePath']

        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name,fileObj)
        print('+/'*100,filePathName)
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('*'*100,BASE_DIR)
        a=pridictcat(BASE_DIR+'/media/'+filePathName)
        print('+'*100,a)
        filePathName=fs.url(filePathName)
        # ["","hair_loss", "patch", "ticks", ""]
        if a == 'apetite_loss' :
            result = 'Apetite Loss'
            info = 'Need to deworm '
        elif a== 'hair_loss' :
            result = 'Hair Loss'
            info = 'Dermatitis but medicine is based on weight. Immediate relief with lotion '
        elif a == 'patch' :
            result = 'Patch'
            info = 'Dermatitis but medicine is based on weight. Immediate relief with lotion '
        elif a == 'ticks':
            result = 'Ticks'
            info = 'Dermatitis but medicine is based on weight. Immediate relief with lotion '
        else :
            result = 'Watery Eyes'
            info = 'Need to deworm '

        return render(request, 'home/uploadcat.html',{'result':result,'info':info,'filePathName':filePathName})
    else:
        return render(request, 'home/uploadcat.html')
def uploaddog(request):
    if request.method == 'POST':
        print(request)
        print (request)
        print (request.POST.dict())
        fileObj=request.FILES['filePath']

        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name,fileObj)
        print('+/'*100,filePathName)
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('*'*100,BASE_DIR)
        a=pridictdog(BASE_DIR+'/media/'+filePathName)
        print('+'*100,a)
        filePathName=fs.url(filePathName)
        if a == 'apetite_loss' :
            result = 'Apetite Loss'
            info = 'Need to deworm '
        elif a== 'hair_loss' :
            result = 'Hair Loss'
            info = 'Dermatitis but medicine is based on weight. Immediate relief with lotion '
        elif a == 'patch' :
            result = 'Patch'
            info = 'Dermatitis but medicine is based on weight. Immediate relief with lotion '
        elif a == 'ticks':
            result = 'Ticks'
            info = 'Dermatitis but medicine is based on weight. Immediate relief with lotion '
        else :
            result = 'Watery Eyes'
            info = 'Need to deworm '

        return render(request, 'home/uploaddog.html',{'result':result,'info':info,'filePathName':filePathName})
    else:
        return render(request, 'home/uploaddog.html')

def about(request):
    return render(request, 'home/aboutus.html')

def dogdescription(request):
    return render(request, 'home/dogdescription.html')

def catdescription(request):
    return render(request, 'home/catdescription.html')    

