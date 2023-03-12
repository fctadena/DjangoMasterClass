from .views import Item
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView



app_name = 'foods'
urlpatterns = [
    #/food/
    path('', views.IndexClassView.as_view(),name='index'),
    #/food/1
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # path('items/', views.items,name='items'),
    # add items
    #path('add', views.CreateItem.as_view(), name='create_item'),
    path('add/', login_required(CreateView.as_view(model=Item, fields=['item_name', 'item_desc', 'item_price', 'item_image'], template_name='foods/item-form.html')), name='create_item'),


    # edit items
    path('update/<int:id>/', views.update_item,name='update_item'),
    # delete
    path('delete/<int:id>/', views.delete_item,name='delete_item'),
    
]


