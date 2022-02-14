from django import forms
from report_app.models import ReestrUsers
from report_app.report_users.modules_users.employees_and_departments import \
    STAFF


def users():
    return ReestrUsers.reestr_man.all()


class FioForm(forms.Form):
    users_dep = forms.ChoiceField(label="пользователи", choices=STAFF)
