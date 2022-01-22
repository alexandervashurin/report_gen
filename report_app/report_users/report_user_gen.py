import os

from docx.shared import Inches
from docx import Document
from docxtpl import DocxTemplate
import datetime
from report_app.report_users.modules_users.employees_and_departments import STAFF
from report_app.report_users.modules_users.employees_and_departments import DEPARTMENTS
from report_app.report_users.modules_users.employees_and_departments import POSITIONS
import report_app.report_users.modules_users.equipment_staff as eq

date_time = str(datetime.datetime.now().date())
d_time = date_time.split(
    '-')[2] + '.' + date_time.split('-')[1] + '.' + date_time.split('-')[0] \
         + ' г.'


def function_report(results):
    document = Document()
    run = document.add_paragraph().add_run()
    font = run.font
    font.bold = True
    table = document.add_table(rows=3, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Пользователь'
    hdr_cells[1].text = str(dict(STAFF).get(int(results[0])))
    hdr_cells = table.rows[1].cells
    hdr_cells[0].text = 'Должность'
    hdr_cells[1].text = dict(POSITIONS).get(int(results[1]))
    hdr_cells = table.rows[2].cells
    hdr_cells[0].text = 'Подразделение'
    hdr_cells[1].text = dict(DEPARTMENTS).get(int(results[2]))

    table = document.add_table(rows=1, cols=6)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Номер п/п'
    hdr_cells[1].text = 'Наименование устройства'
    hdr_cells[2].text = 'Характеристика оборудования'
    hdr_cells[3].text = 'Инв.№'
    hdr_cells[4].text = 'Телефон'
    hdr_cells[5].text = 'Подпись'

    row_cells = table.add_row().cells
    row_cells[0].text = '1'
    row_cells[1].text = dict(eq.TYPES_EQUIPMENTS).get(int(results[3]))
    row_cells[2].text = dict(eq.TYPES_PROCESSORS).get(int(results[4]))
    if results[5] is not None:
        row_cells[3].text = str(results[5])
    else:
        row_cells[3].text = ''

    row_cells[5].text = str(results[8])

    table = document.add_table(rows=1, cols=6)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = ''
    hdr_cells[1].text = ''
    hdr_cells[2].text = ''
    hdr_cells[3].text = ''
    hdr_cells[4].text = ''
    hdr_cells[5].text = ''

    row_cells = table.add_row().cells
    row_cells[0].text = '2'
    row_cells[1].text = 'Марка монитора: ' + \
        dict(eq.TYPES_EQUIPMENTS).get(int(results[6]))
    row_cells[2].text = 'Видеокарта: ' + \
        dict(ТИПЫ_ВИДЕОКАРТ).get(int(results[7]))
    row_cells[3].text = ''
    row_cells[4].text = ''
    row_cells[5].text = ''

    document.add_page_break()
    document.save(directory + '/' + 'demo.docx')

    return document


def function_report2(results):
    directory = '/home/alex/report_project/report_project/media/отчёты'
    doc = DocxTemplate(directory + '/' + 'demo.docx')
    inv_OS = dict(ИНВ_ОС).get((results[13]))
    inv_TK = dict(ИНВ_ТК).get((results[21]))
    inv_nout = dict(ИНВ_ТК_Н).get((results[22]))
    if dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])) == 'Системный блок':
        res = inv_OS
    elif dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])) == 'Тонкий клиент НР Flexible':
        res = inv_TK
    elif dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])) == 'Ноутбук Dell Latitude 3510 15.6 ':
        res = inv_nout
    elif dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])) == 'Ноутбук Dell Inspiron 5490':
        res = inv_nout
    elif dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])) == 'Ноутбук HP ProBook 430 G5, 13.3':
        res = inv_nout
    elif dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])) == 'Ноутбук-трансформер  HP Pavilion x360':
        res = inv_nout
    else:
        res = "нет"

    context = {'name_middlename_surname': str(dict(ФИО).get((results[0]))),
               'position_pers': dict(ДОЛЖНОСТИ).get((results[1])),
               'department': dict(ПОДРАЗДЕЛЕНИЯ).get((results[2])),
               'устройство': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[3])),
               'типпроцессора': dict(ТИПЫ_ПРОЦЕССОРОВ).get((results[4])),
               'марка_монитора': dict(МАРКА_МОНИТОРА).get((results[6])),
               'видеокарта': dict(ТИПЫ_ВИДЕОКАРТ).get((results[7])),
               'номер телефона': results[8],
               'ОС': dict(ТИПЫ_ОС).get((results[9])),
               'диагональ_монитора': results[10],
               'принтер_локальный': dict(БУЛЕВО).get((results[12])),
               'инв_принтера': dict(ИНВ_ТК_П).get((results[5])),
               'инв_монитора': dict(ИНВ_ТК_М).get((results[11])),
               'ИБП': dict(БУЛЕВО).get((results[14])),

               'колонки': dict(БУЛЕВО).get((results[15])),
               'инв_колонки': dict(ИНВ_ТК_К).get((results[16])),

               'телефон': dict(МАРКА_ТЕЛЕФОНА).get((results[17])),
               'inv_num_phone': dict(ИНВ_ТК_Т).get((results[18])),
               'number_phone': results[19],

               'тип_монитора': dict(ТИП_МОНИТОРА).get((results[20])),

               'инв_тк': res,

               'пр1': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[23])),
               'пр2': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[24])),
               'пр3': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[25])),
               'пр4': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[26])),
               'пр5': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[27])),
               'пр6': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[28])),
               'пр7': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[29])),
               'пр8': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[30])),
               'пр9': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[31])),
               'пр10': dict(ТИПЫ_ОБОРУДОВАНИЯ).get((results[32])),


               'инв_пр1': results[33],
               'инв_пр2': results[34],
               'инв_пр3': results[35],
               'инв_пр4': results[36],
               'инв_пр5': results[37],
               'инв_пр6': results[38],
               'инв_пр7': results[39],
               'инв_пр8': results[40],
               'инв_пр9': results[41],
               'инв_пр10': results[42],

               'инв_ИБП': dict(ИНВ_ИБП).get((results[43])),

               'инв_вебкам': dict(ИНВ_ВЕБКАМ).get((results[44])),
               'вебкам': dict(БУЛЕВО).get((results[45])),

               'дата': d_time
               }
    doc.render(context)
    doc.save(directory + '/' + 'report.docx')

    return doc
