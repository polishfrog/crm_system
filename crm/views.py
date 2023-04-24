from django.views import View
from django.shortcuts import render, redirect


# Create your views here.


class HomePage(View):
    """
    First web when user into to website
    """
    def get(self, request):
        return render(request, 'base.html', locals())

