from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Avg
from crm.forms import RatingForm
from crm.models import Opinion

# Create your views here.


class HomePage(View):
    """
    First web when user into to website
    """
    def get(self, request):

        avg_opinion = Opinion.objects.aggregate(avg=Avg('rated'))
        avg_rating = round(avg_opinion['avg'], 2)
        return render(request, 'dashboard.html', locals())


class OpinionPage(View):
    """
    Feedback from customer about ours products <3
    """
    def get(self, request):
        search_type = 'dateOpinion'
        test_check = [1, 2, 3, 4, 5]

        form = RatingForm(request.GET)

        if form.is_valid():
            search_type = form.cleaned_data.get('search_option')
            test_check = form.cleaned_data.get('rated')

        if search_type == 'dateOpinion' or search_type == 'rated':
            search_all = "-" + search_type
            result = Opinion.objects.filter(rated__in=test_check).order_by(search_all, "-dateOpinion")

        elif search_type == 'dateOpinion_reverse':
            search_all = "-" + 'dateOpinion'
            result = Opinion.objects.filter(rated__in=test_check).order_by(search_all, "dateOpinion").reverse()

        elif search_type == 'rated_reverse':
            search_all = "-" + 'rated'
            result = Opinion.objects.filter(rated__in=test_check).order_by(search_all, "rated").reverse()

        form = RatingForm(initial={"search_option": search_type, "rated": test_check})
        return render(request, 'opinion.html', locals())


