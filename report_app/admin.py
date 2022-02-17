from django.contrib import admin
from report_app.models import Agregat, ProductsA, ProductsB


@admin.register(ProductsA)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('namea', 'batch_numa')
    list_display = ('producta_no', 'namea', 'batch_numa', 'data_prod_a')
    list_filter = ('data_prod_a', 'namea')


@admin.register(ProductsB)
class ProductBadmin(admin.ModelAdmin):
    search_fields = ('nameb', 'batch_numb')
    list_display = ('productb_no', 'nameb', 'batch_numb', 'data_prod_b')
    list_filter = ('data_prod_b', 'nameb')


@admin.register(Agregat)
class AgregatAdmin(admin.ModelAdmin):
    search_fields = ('name_agr', 'data_production')
    list_display = ('serial_num', 'current_quality', 'data_production', 'name_agr')
    list_filter = ('serial_num', 'data_production')