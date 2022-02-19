from report_app.report_users.modules_users.employees_and_departments import \
    STAFF
from report_app.report_users.modules_users.employees_and_departments import \
    DEPARTMENTS
from report_app.report_users.modules_users.employees_and_departments import \
    POSITIONS
from report_app.report_users.modules_users.equipment_staff import \
    TYPES_EQUIPMENTS
from report_app.report_users.modules_users.equipment_staff import \
    INVENTORY_NUMBER_MAIN_EQUIPMENTS
from report_app.report_users.modules_users.equipment_staff import \
    INVENTORY_NUMBER_PHONES
from report_app.report_users.modules_users.equipment_staff import \
    INVENTORY_NUMBER_SOUND_SPEAKERS
from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(blank=True, max_length=100, null=True,
                                choices=STAFF)
    emp_dep = models.CharField(blank=True, max_length=100, null=True,
                               choices=DEPARTMENTS)
    emp_pos = models.CharField(blank=True, max_length=100, null=True,
                               choices=POSITIONS)
    data_of_emp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Сотрудник'


class OfficeEquipment(models.Model):
    off_id = models.IntegerField(primary_key=True)
    off_type = models.CharField(blank=True, max_length=100, null=True,
                                choices=TYPES_EQUIPMENTS)
    off_type_num = models.CharField(blank=True, max_length=100, null=True,
                                    choices=INVENTORY_NUMBER_MAIN_EQUIPMENTS)
    off_emp = models.ForeignKey(Employee, models.DO_NOTHING, blank=True,
                                null=True)
    data_install = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'офисная техника'


class InventoryNumbers(models.Model):
    inv_id = models.IntegerField(primary_key=True)
    inv_phones = models.CharField(blank=True, max_length=100, null=True,
                                  choices=INVENTORY_NUMBER_PHONES)
    inv_speakers = models.CharField(blank=True, max_length=100, null=True,
                                    choices=INVENTORY_NUMBER_SOUND_SPEAKERS)
    inv_emp = models.ForeignKey(Employee, models.DO_NOTHING, blank=True,
                                null=True)
    data_install = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'инвентарные номера остальной техники'
