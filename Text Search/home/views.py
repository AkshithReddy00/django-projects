from django.shortcuts import render
from .models import Product
from django.contrib.postgres.search import (SearchVector, SearchQuery, SearchRank,
                                            TrigramSimilarity
                                            )
from django.db.models import Q
import time
from django.views.decorators.cache import cache_page
from django.core.cache import cache



def index(request):
    pass

# @cache_page(60 * 1)
# def index(request):

#     search = request.GET.get('search')

#     if search:
#         query = SearchQuery(search)
#         vector = SearchVector('title','category','brand')
#         rank = SearchRank(vector,query)
#         results = Product.objects.annotate(
#             rank = rank
#         ).filter(rank__gte = 0.05).order_by('-rank')
#     else:
#         results = Product.objects.all()

#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')

#     if min_price and max_price:
#         results = results.filter(price__gte = min_price,price__lte = max_price).order_by('price')

#     brand = request.GET.get('brand')
#     category = request.GET.get('category')

#     if brand or category:
#         results = results.filter(Q(brand = brand)|Q(category = category))

#     brands = Product.objects.all().distinct('brand').order_by('brand')
#     categories = Product.objects.all().distinct('category').order_by('category')

#     return render(request,'index.html',{'results':results,'search':search,'brands':brands,'categories':categories})