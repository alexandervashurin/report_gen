
from django.db import models


class Agregat(models.Model):
    agregat_id = models.IntegerField(primary_key=True)
    name_agr = models.CharField(blank=True, null=True)
    serial_num = models.CharField(blank=True, null=True)
    current_quality = models.CharField(blank=True, null=True)  # This field type is a guess.
    data_production = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Изделие'


class ProductsA(models.Model):
    producta_no = models.IntegerField(primary_key=True)
    namea = models.CharField(blank=True, null=True)
    batch_numa = models.IntegerField(blank=True, null=True)
    agr = models.ForeignKey(Agregat, models.DO_NOTHING, blank=True, null=True)
    data_prod_a = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'компонент_1'


class ProductsB(models.Model):
    productb_no = models.IntegerField(primary_key=True)
    nameb = models.CharField(blank=True, null=True)
    batch_numb = models.IntegerField(blank=True, null=True)
    agr = models.ForeignKey(Agregat, models.DO_NOTHING, blank=True, null=True)
    data_prod_b = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'компонент_2'
