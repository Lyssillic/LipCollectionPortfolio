from django.shortcuts import render


def home(request):
    return render(request, 'LipCollection/home.html')


def about(request):
    return render(request, 'LipCollection/about.html')


def balm(request):
    return render(request, 'LipCollection/balm.html')


def gloss(request):
    return render(request, 'LipCollection/gloss.html')


def scrub(request):
    return render(request, 'LipCollection/scrub.html')
