from django.shortcuts import render
from caching_app.models import Food
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @cache_page(CACHE_TTL)
def item(request):
    print(cache.__str__(),'kk')
    if 'data'in cache:
        print("cache data")
        d = cache.get('data')
        return render(request, 'index.html', {"data":d})
    else:
        print("non cache")
        data = Food.objects.all()
        cache.set(data,data, timeout=CACHE_TTL)
        return render(request,"index.html",{"data":data})


#caching on specific row of database
def item_id(request, id):
    if cache.get(id):
        print("cache")
        data = cache.get(id)
        print(data)
        return render(request, 'index.html', {"data":data})
    else:
        print("non cache")
        data = Food.objects.get(id=id)
        print(data)
        cache.set(id,data, timeout=CACHE_TTL)
    return render(request,"index.html",{"data":data})

