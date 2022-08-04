from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    obj_phones = Phone.objects.all()
    context = {'phones': list(obj_phones)}
    srt = request.GET.get('sort', None)
    if srt == 'name':
        context['phones'].sort(key=lambda x: x.name)
    elif srt == 'min_price':
        context['phones'].sort(key=lambda x: x.price, reverse=False)
    elif srt == 'max_price':
        context['phones'].sort(key=lambda x: x.price, reverse=True)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    obj_phones = Phone.objects.all()
    for i in obj_phones:
        if i.slug == slug:
            context['phone'] = i
            break
    return render(request, template, context)
