# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agregat(models.Model):
    agregat_id = models.IntegerField(primary_key=True)
    name_agr = models.TextField(blank=True, null=True)
    serial_num = models.TextField(blank=True, null=True)
    current_quality = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_production = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agregat'


class ProductsA(models.Model):
    producta_no = models.IntegerField(primary_key=True)
    namea = models.TextField(blank=True, null=True)
    batch_numa = models.IntegerField(blank=True, null=True)
    agr = models.ForeignKey(Agregat, models.DO_NOTHING, blank=True, null=True)
    data_prod_a = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_a'


class ProductsB(models.Model):
    productb_no = models.IntegerField(primary_key=True)
    nameb = models.TextField(blank=True, null=True)
    batch_numb = models.IntegerField(blank=True, null=True)
    agr = models.ForeignKey(Agregat, models.DO_NOTHING, blank=True, null=True)
    data_prod_b = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_b'
