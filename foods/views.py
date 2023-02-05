from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
""" def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request, 'foods/index.html', context) """

# same as index but this one is class based
class IndexClassView(ListView):
    model = Item;
    template_name = 'foods/index.html'
    context_object_name = 'item_list'


# def items(request):
#     return HttpResponse('This is an item view')


""" def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }

    return render(request, 'foods/detail.html', context) """


class FoodDetail(DetailView):
    model = Item
    template_name = 'foods/detail.html'
    
    

def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'foods/item-form.html', {'form': form })


# This is a class based view for create_item
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'foods/item-form.html'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)
    



def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'foods/item-form.html',{'form':form, 'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if request.method == 'POST':
        item.delete()
        return redirect('foods:index')
    
    return render(request, 'foods/item-delete.html', {'item':item})