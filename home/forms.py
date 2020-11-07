from django.forms import ModelForm
from .models import Image_for_ML
  
class search_img(ModelForm): 
  
    class Meta: 
        model = Image_for_ML 
        fields = '__all__' 