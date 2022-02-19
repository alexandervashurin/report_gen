from django.shortcuts import render
from report_app.forms import FioForm

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
    d_time = date_time.split(
        '-')[2] + '.' + date_time.split('-')[1] + '.' + date_time.split('-')[
                 0] + ' г.'

    return render(request, 'report_app/index.html',
                  {'title': d_time, 'ss': cloud, })


def users_add(request):
    from report_app.report_users.report_user_gen import function_report2
    if request.method == 'POST':
        fioform = FioForm(request.POST)  # добавить формы

        id_user_dep = fioform.data['users_dep']
        date_time = str(datetime.datetime.now().date())
        d_time = date_time.split(
            '-')[2] + '.' + date_time.split('-')[1] + '.' + \
                 date_time.split('-')[0] + ' г.'
        choices = users_dep_all.filter(name_m_surname=id_user_dep)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument'
                         '.wordprocessingml.document')
        response[
            'Content-Disposition'] = 'attachment; filename="reports_docx.docx"'
        choices_data = [(i.name_m_surname,  # 0
                         i.position_pers,  # 1
                         i.department,  # 2
                         i.type_equip,  # 3
                         i.type_processor,  # 4
                         i.inv_num_printer,  # 5
                         i.brand_monitor,  # 6
                         i.type_video,  # 7
                         i.number_phone,  # 8
                         i.type_os,  # 9
                         i.diagonal_monitor,  # 10
                         i.inv_num_monitor,  # 11
                         i.local_printer,  # 12
                         i.inv_num_main_equip,  # 13
                         i.ups,  # 14
                         i.sound_devices,  # 15
                         i.inv_num_sound_speakers,  # 16
                         i.brand_phone,  # 17
                         i.inv_num_phone,  # 18
                         i.number_phone,  # 19
                         i.type_monitor,  # 20
                         i.inv_num_thin_client,  # 21
                         i.inv_num_notebook,  # 22
                         i.other_devices,  # 23
                         i.other_devices2,  # 24
                         i.inv_num_other_devices,  # 25
                         i.inv_num_other_devices2,  # 26
                         i.inv_num_ups,  # 27
                         i.inv_num_webcam,  # 28
                         i.webcam,  # 29

                         ) for i in choices][0]
        doc = function_report2(choices_data)
        doc.save(response)
        return response
    else:
        fioform = FioForm()

        return render(
            request, 'report_app/users_form_maker.html', {'form2': fioform, })
