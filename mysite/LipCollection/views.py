from django.shortcuts import render
from .models import LipItem


lip_items = LipItem.objects.all()


def home(request):
    return render(request, 'LipCollection/home.html')


def about(request):
    return render(request, 'LipCollection/about.html')


def balm(request):
    lip_balms = lip_items.filter(Category__icontains="Lip Balm").order_by('Name')
    return render(request, 'LipCollection/balm.html', {'lip_balms': lip_balms})


def gloss(request):
    return render(request, 'LipCollection/gloss.html')


def scrub(request):
    return render(request, 'LipCollection/scrub.html')
