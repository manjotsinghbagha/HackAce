# VetAce
#### Just Click and Get Your Pet Analysed
In this project we provide user with feature to examine their pets just by uploading a picture of their pet, that to at the ease of your bed and get the result for cure and also expert advice if subscription mode is on.  

All you need to do is simply click a picture of your pet if its suffering from any disease and just uplaod it. We will provide you with the best related output.

## To run/ Setup over local system 
1.) Clone the repo using command:
```bash
git clone https://github.com/manjotsinghbagha/HackAce.git
```
2.) Download model to main directory from link:                                    
2.) Create a virtual environment in python and run following
```bash
pip install -r requirements.txt
python manage.py runserver
```
Congratulation you are all set :partying_face:

## Problem solved and Solution:

### Problem
Imagine your pet is suffering from any knid of disease. What are the biggest challenges you think you'll face at this time of COVID-19 being spread all over the world?
1.) Taking a risk to take take your pet outside to a VETfor consultation.  

2.) Waiting for your turn for longer duration of time.  

3.) Stressing your pet all our the journey to take to VET to home.  


And Even if the COVID-19 is gone, still many would be having time constrains or hate to wait in the long long qeues. 

These are the most common challenges that would be faced during this time even if your pet is suffering from any small kind of disease.
So what if we give you a solution to solve all the majors challenges. Sitting just at your place you can identify your pet's problem in just few seconds with all the details 
how it can be cured. 

### Solution:

VetAce is a web based app solution in which a user can:  
  1.) Click the pic of pet and upload to the disease predicted over our algorithm.  

  2.) Our Web App will also suggest initial curing.  

  3.) Can explore any disease by visiting discription page or clicking over hyperlinks.  

  4.) Can get advice from VET experts over our site.  


In this project we provide user with feature to examine their pets just by uploading a picture of their pet, that to at the ease of your bed and get the result for cure and also expert advice if subscription mode is on.  

All you need to do is simply click a picture of your pet if its suffering from any disease and just uplaod it. We will provide you with the best related output.  
Just on single click user can upload the the image of thier pet and our application will use machine learning model to generate the report of the disease from which your pet is suffering and will also tell the required cure that can be taken.  
You can easily have a pre treatment and a knowledge about the disease and can easily consult the VET for further information.

#### Machine learning part

We had trained a Multi Class Classifier Convolution neural network model over 5 broad categories (Hair loss, Loss of Apetite, Ticks, patches on body, watery eyes).  The model is trained over 75 epochs, Adam optimizer with 0.001 learning rate and used 6 layered CNN. We had trained 2 different models, one for Dogs and other for cats. Further we could expand it to as many as you want.  

In future we can train the machine learning model with more number of images so that the prediction accuracy of the model improves.  

Currently we can classify the diseases in animal in 5 categories but later on we can use more data and computational power to train a better model which can
classify more diseases with respect the different animals.  

Along with this application is full of information. It provides the user with all the information related to the diseases commonly found in domestic animal(cat and dog).  


## Market feasibility and Buisness model
This website/software can generate revenue through these models:

### Software as a service Model for Vet
The software or website will be given as a service to various veterinary doctor to track development and improvement in animals of their potential coutomers.
VET can look after them regularly with physical meeting and can provide with the best treatment possible. they can provide suggestions to owner how they can look after and cure the disease in minimal time. through our portal.  
We will use django-tenant-model to register every VET as a tenant and every tenant will have his/her private patients.  
This dieticians will be asked to pay for our service.

### Advertisement Model
Here we could advertise some shops from where pet goods, medicine or curing material could be bought and also could promote specific VET on basis of their subscription and requrement.
