import os

from docx.shared import Inches
from docx import Document
from docxtpl import DocxTemplate
from report_app.report_users.modules_users.equipment_staff import DEPO, SYSTEMS, НОМЕР_ВАГОНА_СЕКЦИИ, TYPE_TRAINS

# этот код работает не так как надо
from report_app.report_users.modules_users.equipment_staff import ТИПЫ_ВИДЕОКАРТ, ТИПЫ_ПРОЦЕССОРОВ, ТИПЫ_ОС, БУЛЕВО
from report_app.report_users.modules_users.типы_мониторов import ТИП_МОНИТОРА


def function_report2(results):
    directory = '/home/alex/report_maker/report_project/media/отчёты'
    doc = DocxTemplate(directory + '/' + 'demo.docx')

    context = {'СЛД': str(dict(DEPO).get(int(results[0]))),
               'ТИП_ЛОКОМОТИВА': dict(TYPE_TRAINS).get(int(results[1])),
               'СИСТЕМЫ': dict(SYSTEMS).get(int(results[2])),
               'НОМЕР_УСТРОЙСТВА': dict().get(int(results[3])),
               'типпроцессора': dict(ТИПЫ_ПРОЦЕССОРОВ).get(int(results[4])),
               'маркамонитора': dict(ТИП_МОНИТОРА).get(int(results[6])),
               'видеокарта': dict(ТИПЫ_ВИДЕОКАРТ).get(int(results[7])),
               'номер телефона': results[8],
               'ОС': dict(ТИПЫ_ОС).get(int(results[9])),
               'диагональ_монитора': results[10],
               'принтер_локальный': dict(БУЛЕВО).get(int(results[12])),
               'инвпринтера': results[11]
               }
    doc.render(context)
    doc.save(directory + '/' + 'report.docx')

    return doc
