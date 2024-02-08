from django.shortcuts import render
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from .models import Book , Category , tag , booki , child , parent , A, B,X,Y,W,V , menu_item
from .serializers import CategoriesSerializer ,WSerializer , VSerializer , ASerializer  , menu_item_Serializer, BSerializer, BookSerializer , tagSerializer , bookiSerializer ,childSerializer, parentSerializer ,XSerializer,YSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator , EmptyPage
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes  , throttle_classes 
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle 
from .throttles import TenCallsPerMinute 
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

# class MenuView(generics.ListCreateAPIView ):
#     queryset = menu_item.objects.all()
#     serializer_class = menu_item_Serializer
class MenuView(ModelViewSet):
    queryset = menu_item.objects.all()
    serializer_class = menu_item_Serializer
    

@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
     items = Category.objects.all()
     serialized_item = CategoriesSerializer(items, many=True)
     return Response({'data':serialized_item.data}, template_name='book-items.html')

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    
    
    
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategoriesSerializer(category)
    return Response(serialized_category.data) 


class tagView(generics.ListCreateAPIView):
    queryset = tag.objects.all()
    serializer_class = tagSerializer    

class  childView(generics.ListCreateAPIView):
    queryset = child.objects.all()
    serializer_class = childSerializer    

class parentView(generics.ListCreateAPIView):
    queryset = parent.objects.all()
    serializer_class = parentSerializer  


class  AView(generics.ListCreateAPIView):
    queryset = A.objects.all()
    serializer_class = ASerializer    

class BView(generics.ListCreateAPIView):
    queryset = B.objects.all()
    serializer_class =BSerializer  


class  XView(generics.ListCreateAPIView):
    queryset = X.objects.all()
    serializer_class = XSerializer    

class YView(generics.ListCreateAPIView):
    queryset = Y.objects.all()
    serializer_class =YSerializer  
    
class  WView(generics.ListCreateAPIView):
    queryset = W.objects.all()
    serializer_class = WSerializer    



#booki
class bookiView(generics.ListCreateAPIView):
    queryset = booki.objects.all()
    serializer_class = bookiSerializer    


#v
    
    ##___________________________________________________________________________________________##
# django-filters package is mostly used with class-based views while you were working with function
#-based views so you can take advantage of Django's native sorting methods
    ##___________________________________________________________________________________________##


# @api_view(['GET','POST'])
# def VView(request):
#     if request.method == 'GET' :
#         items = V.objects.select_related('category').all()
#         cat_name = request.query_params.get('category')
#         to_price = request.query_params.get('to_price')
#         search = request.query_params.get('search')
#         ordering = request.query_params.get('ordering')
#         per_page = request.query_params.get('per_page',default= 2)
#         page = request.query_params.get('page',default=2)

#         # for filtering 
#         if cat_name : 
#             items = items.filter(category__title = cat_name) # title of the category (field of foreign key )
#         if to_price :
#             items = items.filter(price__tle = to_price)

#         # for searching 
#         if search :
#             items = items.filter(title__startswith=search) # title of the book , #contains , icontains
#         # for ordering 
#         if ordering : 
#             items = items.order_by(ordering) # http://127.0.0.1:8000/api/V/?ordering=-price
#         # pagination 
            
#         # per_page=2&page = 2 : this means that the client may request some page which is empty  , so add 
#         # a try catch block 
#         paginator =  Paginator(items, per_page= per_page) # http://127.0.0.1:8000/api/V/?per_page=2&page=3
#         try : 
#             items = paginator.page(number=page)
#         except EmptyPage: 
#             items = []

#         serialized_item = VSerializer(items, many= True)
#         return Response(serialized_item.data)
#     if request.method == 'POST' : 
#         serialized_item = VSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception=True)
#         serialized_item.save()
#         return Response(serialized_item.data, status.HTTP_200_OK)

class VView (generics.ListCreateAPIView):
    queryset = V.objects.all()
    serializer_class = VSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    ordering_fields=['price']
    search_fields=['title']
    
#___________________________________________________________
#authentication => token  and authorization => groups  ^_^  |
#___________________________________________________________|
#secured endpoint 
@api_view()
@permission_classes([IsAuthenticated])
def secret(request) :
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"you are authorized !"})
    else : 
        return Response({"message":"you are not authorized! "},403)

@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([AnonRateThrottle,UserRateThrottle])
@throttle_classes([TenCallsPerMinute]) # for authenticated user ==> 10 calls 
def throttle_check(request):
    return Response({"message":"successful"})