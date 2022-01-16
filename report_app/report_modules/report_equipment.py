from docx import Document
from docxtpl import DocxTemplate
from report_app.templates_for_report.список_устройств import SYSTEMS


def function_report2(res1, res2, equip):
    doc = DocxTemplate('/' + 'template_equipment.docx')

    context = {'устройства_уст': res1,
               'устройства_снят': res2,
               'equip': equip
               }
    doc.render(context)
    doc.save('/' + 'report_equipment.docx')

    return doc
