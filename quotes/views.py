import random
import time
from django.shortcuts import render

# Create your views here.
quotes = [
    'Know thy self, know thy enemy. A thousand battles, a thousand victories.',
    'Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.',
    'The supreme art of war is to subdue the enemy without fighting.',
]

image_urls = [
    'https://cdn.britannica.com/36/259536-050-C6DC3D1F/Sunzi-Sun-Tzu-Chinese-strategist-Art-of-War.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/3/37/Enchoen27n3200.jpg',
    'https://www.shambhala.com/media/catalog/category/Sun_Tzu_open_rights.jpg',
]
def quote(request):
    template_name = "quotes/quote.html"
    context = {
        'quote': random.choice(quotes),
        'image_url': random.choice(image_urls),
        'current_time': time.ctime()
    }
    return render(request, template_name, context)

def show_all(request):
    template_name = "quotes/show_all.html"
    
    context = {
        'all_quotes': quotes,
        'all_images': image_urls,
        'current_time': time.ctime()
    }
    
    return render(request, template_name, context)

def about(request):
    template_name = "quotes/about.html"
    
    context = {
        'current_time': time.ctime()
    }
    
    return render(request, template_name, context)