from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Tramites

# Create your views here.


def index(request):
    latest_question_list = Tramites.objects.order_by('-pub_date')[:5]
    template = loader.get_template('guide/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
