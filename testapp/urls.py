from django.urls import path 
from .views import BookView ,secret, throttle_check,menu,CategoriesView,category_detail,MenuView, tagView,XView,WView, VView, YView, bookiView , parentView , childView,AView , BView
urlpatterns = [
    path('categories/',CategoriesView.as_view()),
    path('books/',BookView.as_view()), 
    path('parent/',parentView.as_view()),
    path('child/',childView.as_view()),
    path('A/',AView.as_view()),
    path('B/',BView.as_view()),
    path('X/',XView.as_view()),
    path('Y/',YView.as_view()),
    path('W/',WView.as_view()),
    path('tag/',tagView.as_view()),
    path('V/',VView.as_view()),
    path('booki/',bookiView.as_view()) ,
    path('category/<int:pk>',category_detail, name='category-detail'),
    path('menu/',menu ),
    # path('MenuView/',MenuView.as_view()),
    path('MenuView/', MenuView.as_view({'get': 'list', 'post': 'create'}), name='your-model-list'),
    path('MenuView/<int:pk>/', MenuView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='your-model-detail'),
    path('secret/',secret),
    path('throttle_check/',throttle_check),

]
