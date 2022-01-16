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


def users_add(request):
    if request.method == 'POST':
        fioform = FioForm(request.POST) # добавить формы

        ид_пользователя = fioform.data['пользователи']
        date_time = str(datetime.datetime.now().date())
        d_time = date_time.split('-')[2] + '.' + date_time.split('-')[1] + '.' + date_time.split('-')[0] + ' г.'
        выборка = пользователи_все.filter(фио=ид_пользователя)

        '''context = {
            'title': d_time,
            'пользователи': ид_пользователя,

        }
        return render(request, 'maker_reports/us_pivot.html', context)'''
        from report_app.report_modules.report_users import function_report2

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="reports_docx.docx"'
        данные_выборки = [(i.фио,  # 0
                           i.должность,  # 1
                           i.подразделение,  # 2
                           i.тип_оборудования,  # 3
                           i.процессор,  # 4
                           i.инв_принтера,  # 5
                           i.марка_монитора,  # 6
                           i.видеокарта,  # 7
                           i.номер_телефона,  # 8
                           i.установленная_операционная_система,  # 9
                           i.диагональ_монитора,  # 10
                           i.инв_монитора,  # 11
                           i.принтер_локальный,  # 12
                           i.инв_основного_оборудования,  # 13
                           i.источник_бесперебойного_питания,  # 14
                           i.колонки,  # 15
                           i.инв_колонки,  # 16
                           i.телефон_модель,  # 17
                           i.инв_телефона,  # 18
                           i.номер_телефона,  # 19
                           i.тип_монитора,  # 20
                           i.инв_тк,  # 21
                           i.инв_ноутбуков,  # 22
                           i.прочие_устройства,  # 23
                           i.прочие_устройства2,  # 24
                           i.прочие_устройства3,  # 25
                           i.прочие_устройства4,  # 26
                           i.прочие_устройства5,  # 27
                           i.прочие_устройства6,  # 28
                           i.прочие_устройства7,  # 29
                           i.прочие_устройства8,  # 30
                           i.прочие_устройства9,  # 31
                           i.прочие_устройства10,  # 32
                           i.инв_прочего_устройства,  # 33
                           i.инв_прочего_устройства2,  # 34
                           i.инв_прочего_устройства3,  # 35
                           i.инв_прочего_устройства4,  # 36
                           i.инв_прочего_устройства5,  # 37
                           i.инв_прочего_устройства6,  # 38
                           i.инв_прочего_устройства7,  # 39
                           i.инв_прочего_устройства8,  # 40
                           i.инв_прочего_устройства9,  # 41
                           i.инв_прочего_устройства10,  # 42
                           i.инв_ИБП,  # 43
                           i.инв_вебкамера,  # 44
                           i.вебкамера,  # 45

                           ) for i in выборка][0]
        doc = function_report2(данные_выборки)
        doc.save(response)
        return response
    else:
        fioform = FioForm()

        return render(request, 'maker_reports/users_form_maker.html', {'form2': fioform, })
