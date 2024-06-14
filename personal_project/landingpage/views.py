from django.shortcuts import render


# Create your views here.
def home_page(request):
    # display the home page

    return render(request, 'landingpage/index.html')