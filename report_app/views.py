from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.edit import CreateView

import datetime
from django.http import HttpResponse
import os
import re
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
directory = BASE_DIR.joinpath('media')

# Create your views here.
cloud = "https://e1.ru"


def index(request):

    date_time = str(datetime.datetime.now().date())
    '''print(diag_device)'''
    d_time = date_time.split('-')[2] + '.' + date_time.split('-')[1] + '.' + date_time.split('-')[0] + ' г.'

    return render(request, 'report_app/index.html', {'title': d_time, 'ss': cloud, })
