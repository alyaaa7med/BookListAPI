from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    category = models.ForeignKey(Category,models.PROTECT,default=1)



class parent(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField()

class child(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    category = models.ForeignKey(parent,models.PROTECT,default=1)# foreign key is a dropbox , if parent has default = 1 it will be placed 



class A(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField()

   

class B(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    # category = models.ForeignKey(A,models.PROTECT,default=1)


class X(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField()

   

class Y(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    category = models.ForeignKey(X,models.PROTECT,null=True)





class tag(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField()
# bookie
class booki(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    category = models.ForeignKey(tag,models.PROTECT)  # no default so the foreign key is a dropbox

class W(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField()

    # def __str__(self) :
    #     return self.title
# v 
class V(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    category = models.ForeignKey(W,models.PROTECT,default=1)


class menu_item(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

