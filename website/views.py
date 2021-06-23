from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from django.shortcuts import render , get_object_or_404
from service import models as models_service
from . import models


def index(request):
    is_index =True
    category = request.GET.get('category')
    if not category :
        articles = models_service.Article.objects.filter(status=True)
    else:
        articles = models_service.Article.objects.filter(categorie__nom= category)

    return render(request, 'index.html',locals())

def cart(request):
    is_cart =True
    return render(request, 'cart.html',locals())

def checkout(request):
    is_checkout =True
    return render(request, 'checkout.html',locals())


def shop(request):
    is_shop =True
    category = request.GET.get('category')
    if not category :
        articles = models_service.Article.objects.filter(status=True)
    else:
        articles = models_service.Article.objects.filter(categorie__nom__icontains = category)

    categories = models_service.Categorie.objects.filter(status=True)
    paginator = Paginator(articles,4)
    page = request.GET.get('page')
    try:
        articles_albums = paginator.page(page)
    except PageNotAnInteger : 
        articles_albums = paginator.page(1)
    except EmptyPage :
        articles_albums = paginator.page(paginator.num_pages)

    return render(request, 'shop.html', locals())

def product_detail(request,id):

    article = get_object_or_404(models_service.Article , id=id)
    images = models_service.Image.objects.filter(status=True)
    return render(request, 'product-details.html',locals())


def search(request):
    query = request.GET.get('query')
    if not query:
        articles = models_service.Article.objects.all
    else:
        articles = models_service.Article.objects.filter(categorie__nom__icontains=query)
        
    return render(request ,'index.html', locals())  
# Create your views here.