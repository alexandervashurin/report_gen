from django.shortcuts import render
from report_app.forms import FioForm
from report_app.models import ReestrUsers

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
пользователи_все = ReestrUsers.reestr_man.all()


def index(request):
    date_time = str(datetime.datetime.now().date())
    '''print(diag_device)'''
    d_time = date_time.split(
        '-')[2] + '.' + date_time.split('-')[1] + '.' + date_time.split('-')[
                 0] + ' г.'

    return render(request, 'report_app/index.html',
                  {'title': d_time, 'ss': cloud, })


def users_add(request):
    from report_app.report_users.report_user_gen import function_report2
    if request.method == 'POST':
        fioform = FioForm(request.POST)  # добавить формы

        ид_пользователя = fioform.data['users_dep']
        date_time = str(datetime.datetime.now().date())
        d_time = date_time.split(
            '-')[2] + '.' + date_time.split('-')[1] + '.' + \
                 date_time.split('-')[0] + ' г.'
        выборка = пользователи_все.filter(фио=ид_пользователя)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument'
                         '.wordprocessingml.document')
        response[
            'Content-Disposition'] = 'attachment; filename="reports_docx.docx"'
        данные_выборки = [(i.name_middlename_surname,  # 0
                           i.position_pers,  # 1
                           i.department,  # 2
                           i.type_equip,  # 3
                           i.процессор,  # 4
                           i.инв_принтера,  # 5
                           i.марка_монитора,  # 6
                           i.видеокарта,  # 7
                           i.number_phone,  # 8
                           i.type_os,  # 9
                           i.диагональ_монитора,  # 10
                           i.инв_монитора,  # 11
                           i.принтер_локальный,  # 12
                           i.инв_основного_оборудования,  # 13
                           i.источник_бесперебойного_питания,  # 14
                           i.колонки,  # 15
                           i.инв_колонки,  # 16
                           i.brand_phone,  # 17
                           i.inv_num_phone,  # 18
                           i.number_phone,  # 19
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
                           i.webcam,  # 45

                           ) for i in выборка][0]
        doc = function_report2(данные_выборки)
        doc.save(response)
        return response
    else:
        fioform = FioForm()

        return render(
            request, 'report_app/users_form_maker.html', {'form2': fioform, })
