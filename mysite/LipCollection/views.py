from django.shortcuts import render
from .models import LipItem
from django.core.paginator import Paginator


lip_items = LipItem.objects.all()


def home(request):
    count = {"lip_balm": len(lip_items.filter(Category__icontains="Lip Balm")),
             "lip_gloss": len(lip_items.filter(Category__icontains="Lip Gloss")),
             "lip_scrub": len(lip_items.filter(Category__icontains="Lip Scrub"))
             }
    return render(request, 'LipCollection/home.html', {'count': count})


def about(request):
    return render(request, 'LipCollection/about.html')


def balm(request):
    lip_balms = lip_items.filter(Category__exact="Lip Balm").order_by('Name')
    balm_name = request.GET.get('balm_name')

    if balm_name != '' and balm_name is not None:
        lip_balms = lip_balms.filter(Name__icontains=balm_name)

    paginator = Paginator(lip_balms, 8)
    page = request.GET.get('page')
    lip_balms = paginator.get_page(page)
    return render(request, 'LipCollection/balm.html', {'lip_balms': lip_balms})


def gloss(request):
    lip_glosses = lip_items.filter(Category__exact="Lip Gloss").order_by('Name')
    gloss_name = request.GET.get('gloss_name')

    if gloss_name != '' and gloss_name is not None:
        lip_glosses = lip_glosses.filter(Name__icontains=gloss_name)

    paginator = Paginator(lip_glosses, 8)
    page = request.GET.get('page')
    lip_glosses = paginator.get_page(page)
    return render(request, 'LipCollection/gloss.html', {'lip_glosses': lip_glosses})


def scrub(request):
    lip_scrubs = lip_items.filter(Category__icontains="Lip Scrub").order_by('Name')
    scrub_name = request.GET.get('scrub_name')

    if scrub_name != '' and scrub_name is not None:
        lip_scrubs = lip_scrubs.filter(Name__icontains=scrub_name)

    paginator = Paginator(lip_scrubs, 6)
    page = request.GET.get('page')
    lip_scrubs = paginator.get_page(page)

    return render(request, 'LipCollection/scrub.html', {'lip_scrubs': lip_scrubs})
