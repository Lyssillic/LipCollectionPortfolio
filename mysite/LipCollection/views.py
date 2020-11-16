from django.shortcuts import render
from .models import LipItem


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
    lip_balms = lip_items.filter(Category__icontains="Lip Balm").order_by('Name')
    return render(request, 'LipCollection/balm.html', {'lip_balms': lip_balms})


def gloss(request):
    lip_glosses = lip_items.filter(Category__icontains="Lip Gloss").order_by('Name')
    return render(request, 'LipCollection/gloss.html', {'lip_glosses': lip_glosses})


def scrub(request):
    lip_scrubs = lip_items.filter(Category__icontains="Lip Scrub").order_by('Name')
    return render(request, 'LipCollection/scrub.html', {'lip_scrubs': lip_scrubs})
