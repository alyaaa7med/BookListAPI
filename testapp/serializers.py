from .models import Category , Book , booki,tag , parent , child ,A , B,X,Y,W,V , menu_item
from rest_framework import serializers 

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Category
        fields = ['id','title']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name='category-detail'
        )
    class Meta : 
        model = Book 
        fields =['id','title','author','price','category']




















class tagSerializer(serializers.ModelSerializer):
    class Meta : 
        model = tag
        fields = ['id','title']



class parentSerializer(serializers.ModelSerializer):
    class Meta : 
        model = parent
        fields = ['id','title']



class childSerializer(serializers.ModelSerializer):
    class Meta : 
        model = child 
        fields =['id','title','author','price','category']


class ASerializer(serializers.ModelSerializer):
    class Meta : 
        model = A
        fields = ['id','title']

class BSerializer(serializers.ModelSerializer):
    class Meta : 
        model = B 
        fields =['id','title','author','price']


class XSerializer(serializers.ModelSerializer):
    class Meta : 
        model = X
        fields = ['id','title']

class YSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Y 
        fields =['id','title','author','price','category']


class WSerializer(serializers.ModelSerializer):
    class Meta : 
        model = W
        fields = ['id','title']

class VSerializer(serializers.ModelSerializer):
    category = WSerializer(read_only=True)
    # categoryk = serializers.IntegerField(write_only =True) not work :) 
    category_id = serializers.IntegerField(write_only=True) # as it is a field , will be serialized and deserialized , so add write only 
    class Meta : 
        model = V
        # fields =['id','title','author','price','category','category_id']
        fields = '__all__' # will serialize  all data of model and serializer ^_^


class bookiSerializer(serializers.ModelSerializer):
    class Meta : 
        model = booki 
        fields =['id','title','author','price','category']


class menu_item_Serializer(serializers.ModelSerializer):
    class Meta : 
        model = menu_item
        fields = '__all__'
        extra_kwargs = {
                  'price': {'min_value': 2},
                  }