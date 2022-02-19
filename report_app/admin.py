from django.contrib import admin
from report_app.models import Employee, InventoryNumbers, OfficeEquipment


@admin.register(Employee)
class EmpoyeeAdmin(admin.ModelAdmin):
    search_fields = ('emp_name', 'emp_dep', 'emp_pos')
    list_display = ('emp_name', 'emp_dep', 'emp_pos', 'data_of_emp')
    list_filter = ('emp_name', 'emp_dep', 'emp_pos')


@admin.register(OfficeEquipment)
class OfficeEquipmentAdmin(admin.ModelAdmin):
    search_fields = ('off_type', 'off_emp')
    list_display = ('off_type', 'off_type_num', 'off_emp', 'data_install')
    list_filter = ('off_type', 'off_type_num', 'off_emp')


@admin.register(InventoryNumbers)
class InventoryNumbersAdmin(admin.ModelAdmin):
    search_fields = ('data_install', 'inv_emp')
    list_display = ('inv_phones', 'inv_speakers', 'inv_emp',
                    'data_install')
    list_filter = ('inv_phones', 'inv_speakers', 'inv_emp')
