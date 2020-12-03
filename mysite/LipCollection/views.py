from django.shortcuts import render
from .models import LipItem
from django.core.paginator import Paginator
from django.db.models import Q


lip_items = LipItem.objects.all()


def home(request):
    count = {"lip_balm": len(lip_items.filter(Category__icontains="Lip Balm")),
             "lip_gloss": len(lip_items.filter(Category__icontains="Lip Gloss")),
             "lip_scrub": len(lip_items.filter(Category__icontains="Lip Scrub"))
             }
    return render(request, 'LipCollection/home.html', {'count': count})


def about(request):
    return render(request, 'LipCollection/about.html')


def detail(request, id):
    item = LipItem.objects.get(pk=id)
    return render(request, 'LipCollection/detail.html', {'item': item})


def balm(request):
    sort = request.GET.get('sort_by')
    if not sort:
        sort = 'Name'

    lip_balms = lip_items.filter(Category__exact="Lip Balm").order_by(sort)
    search_item = request.GET.get('search_item')

    if search_item != '' and search_item is not None:
        lip_balms = lip_balms.filter(Q(Name__icontains=search_item)
                                     |
                                     Q(Brand__icontains=search_item)
                                     |
                                     Q(Flavor__icontains=search_item))

    paginator = Paginator(lip_balms, 8)
    page = request.GET.get('page')
    lip_balms = paginator.get_page(page)
    return render(request, 'LipCollection/balm.html', {'lip_balms': lip_balms})


def gloss(request):
    sort = request.GET.get('sort_by')
    if not sort:
        sort = 'Name'

    lip_glosses = lip_items.filter(Category__exact="Lip Gloss").order_by(sort)
    search_item = request.GET.get('search_item')

    if search_item != '' and search_item is not None:
        lip_glosses = lip_glosses.filter(Q(Name__icontains=search_item)
                                         |
                                         Q(Brand__icontains=search_item)
                                         |
                                         Q(Flavor__icontains=search_item))

    paginator = Paginator(lip_glosses, 8)
    page = request.GET.get('page')
    lip_glosses = paginator.get_page(page)
    return render(request, 'LipCollection/gloss.html', {'lip_glosses': lip_glosses})


def scrub(request):
    sort = request.GET.get('sort_by')
    if not sort:
        sort = 'Name'

    lip_scrubs = lip_items.filter(Category__icontains="Lip Scrub").order_by(sort)
    search_item = request.GET.get('search_item')

    if search_item != '' and search_item is not None:
        lip_scrubs = lip_scrubs.filter(Q(Name__icontains=search_item)
                                       |
                                       Q(Brand__icontains=search_item)
                                       |
                                       Q(Flavor__icontains=search_item))

    paginator = Paginator(lip_scrubs, 6)
    page = request.GET.get('page')
    lip_scrubs = paginator.get_page(page)

    return render(request, 'LipCollection/scrub.html', {'lip_scrubs': lip_scrubs})
