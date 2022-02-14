from django.db import models
from django.utils.timezone import now
import report_app.report_users.modules_users.employees_and_departments as emp
import report_app.report_users.modules_users.equipment_staff as eq
import report_app.report_users.modules_users.mac_addresses as mac


# Create your models here.
class Document2(models.Model):
    description = models.CharField(max_length=255, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents2/%Y/%m')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["upload_at"]
        verbose_name = "ежедневные справки(word)"
        verbose_name_plural = "ежедневные справки(word)"


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/%Y/%m')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["upload_at"]
        verbose_name = "ежедневные справки(excel)"
        verbose_name_plural = "ежедневные справки(excel)"


class Problem(models.Model):
    title = models.CharField(max_length=250)
    id_problem = models.IntegerField()
    data_problem = models.DateTimeField()
    description_problem = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "проблемы"
        indexes = [
            models.Index(fields=['title', 'description_problem']),
            models.Index(fields=['title'], name='title_idx'),
        ]


class ReestrUsers(models.Model):
    # Фамилия Имя Отчество сотрудника
    name_m_surname = models.CharField("ФИО сотрудника", max_length=5,
                                      blank=False,
                                      choices=emp.STAFF)  # 0
    # имя компьютера
    name_pc = models.CharField("имя компьютера в системе", max_length=25,
                               default="", blank=True)

    # тип рабочей машины
    type_pc = models.CharField("тип рабочей станции", max_length=1,
                               blank=False,
                               default='1',
                               choices=eq.TYPES_PCS)
    # подразделение
    department = models.CharField("подразделение", max_length=1, blank=False,
                                  default='1',
                                  choices=emp.DEPARTMENTS)  # 2
    # position_pers
    position_pers = models.CharField("должность", max_length=5, blank=True,
                                     choices=emp.POSITIONS)  # 1

    # тип оборудования
    type_equip = models.CharField("тип оборудования", max_length=2,
                                  blank=False,
                                  default='1',
                                  choices=eq.TYPES_EQUIPMENTS)  # 3

    # тип оборудования
    brand_monitor = models.CharField("марка монитора", max_length=2,
                                  blank=False,
                                  default='1',
                                  choices=eq.BRAND_MONITORS)  # 3

    # тип оборудования
    type_monitor = models.CharField("тип монитора", max_length=2,
                                  blank=False,
                                  default='1',
                                  choices=eq.TYPES_MONITORS)  # 3

    # инв. номер ноутбука
    inv_num_notebook = models.CharField(max_length=2, blank=False, default='1',
                                        choices=eq.INVENTORY_NUMBER_NOTEBOOK)  # 22
    # инв. номер тонкого клиента
    inv_num_thin_client = models.CharField("инв. номер тонкого клиента",
                                           max_length=2,
                                           blank=False,
                                           default='1',
                                           choices=eq.INVENTORY_NUMBER_THIN_CLIENT)  # 21
    # инв. номер основного оборудования
    inv_num_main_equip = models.CharField("инв. номер основного "
                                          "оборудования",
                                          max_length=2, blank=False,
                                          default='0',
                                          choices=eq.INVENTORY_NUMBER_MAIN_EQUIPMENTS)  # 13
    # тип процессора
    type_processor = models.CharField("тип процессора",
                                      max_length=1,
                                      blank=False, default='1',
                                      choices=eq.TYPES_PROCESSORS)  # 4
    # объем памяти
    ram = models.IntegerField("объем памяти", blank=False, default='1')

    # видеокарта
    type_video = models.CharField("видеокарта", max_length=1, blank=False,
                                  default='1',
                                  choices=eq.TYPE_VIDEOS)
    # звуковые колонки
    sound_devices = models.CharField("звуковые колонки", max_length=1,
                                     blank=False, default='1',
                                     choices=eq.AVAILABILITY)  # 15
    # инв. номер звуковых колонок
    inv_num_sound_speakers = models.CharField("инв. номер колонок",
                                              max_length=2, blank=False,
                                              default='0',
                                              choices=eq.INVENTORY_NUMBER_SOUND_SPEAKERS)  # 16
    # серийный номер монитора
    serial_num_monitor = models.CharField("серийный номер монитора",
                                          max_length=70, default="",
                                          blank=True)
    # инв. номер монитора
    inv_num_monitor = models.CharField("инв. номер монитора", max_length=2,
                                       blank=False, default='0',
                                       choices=eq.INVENTORY_NUMBER_MONITORS)  # 11
    # диагональ монитора
    diagonal_monitor = models.IntegerField("диагональ", blank=False,
                                           default='23')

    # колчество мониторов у пользователя
    num_monitor = models.IntegerField("количество мониторов", default=1)

    # сетевой фильтр (да/нет)
    power_filter = models.CharField("сетевой фильтр", max_length=1,
                                    blank=False,
                                    default='1', choices=eq.AVAILABILITY)
    # принтер локальный подключен (да/нет)
    local_printer = models.CharField("принтер локальный", max_length=1,
                                     blank=False,
                                     default='1', choices=eq.AVAILABILITY)
    # инв. номер принтера
    inv_num_printer = models.CharField("инв. номер принтера", max_length=2,
                                       blank=False,
                                       default='0',
                                       choices=eq.INVENTORY_NUMBER_PRINTERS)  # 5
    # webcam (да/нет)
    webcam = models.CharField("вебкамера", max_length=1, blank=False,
                              default='1',
                              choices=eq.AVAILABILITY)  # 45
    # инв. номер вебкамеры
    inv_num_webcam = models.CharField("инв. номер вебкамеры",
                                      max_length=2, blank=False,
                                      default='0',
                                      choices=eq.INVENTORY_NUMBER_WEBCAM)  # 44
    # прочие устройства
    other_devices = models.CharField("прочие устройства", max_length=2,
                                     blank=False,
                                     default='0',
                                     choices=eq.TYPES_EQUIPMENTS)  # 23
    # инв. прочего устройства
    inv_num_other_devices = models.IntegerField("инв. прочего устройства",
                                                blank=True, null=True)  # 33

    #
    other_devices2 = models.CharField("прочие устройства_2",
                                      max_length=2,
                                      blank=False,
                                      default='0',
                                      choices=eq.TYPES_EQUIPMENTS)  # 24
    #
    inv_num_other_devices2 = models.IntegerField("инв. прочего устройства",
                                                 blank=True, null=True)  # 34

    # источник бесперебойного питания
    ups = models.CharField("источник бесперебойного питания",
                           max_length=1,
                           blank=False,
                           default='1',
                           choices=eq.AVAILABILITY)  # 14
    # инв. номер ИБП
    inv_num_ups = models.CharField("инв. номер ИБП",
                                   max_length=2, blank=True, default='0',
                                   choices=eq.UPS)  # 43
    # операционная система
    type_os = models.CharField("операционная система",
                               max_length=1,
                               blank=False,
                               default='2',
                               choices=eq.TYPE_OSES)
    # мак-адрес
    mac_addresses = models.CharField("MAC-адрес", max_length=5, default="33",
                                     blank=False,
                                     choices=mac.MACADDRESSES)
    # модель телефона
    brand_phone = models.CharField("модель телефона", max_length=1,
                                   blank=False,
                                   default='1',
                                   choices=eq.NAME_PHONES)  # 17
    # инв. телефона
    inv_num_phone = models.CharField("инв. телефона", max_length=2,
                                     blank=False, default='0',
                                     choices=eq.INVENTORY_NUMBER_PHONES)  # 18
    # номер телефона сотрудника
    number_phone = models.IntegerField("номер телефона сотрудника",
                                       blank=True, null=True)  # 19

    reestr_man = models.Manager()

    def __str__(self):
        return self.name_m_surname

    class Meta:
        ordering = ['name_m_surname']
        verbose_name = "пользователи Информационной системы"
        verbose_name_plural = "пользователи_ИС"


# Класс зарплатная ведомость

class SalaryEmployers(models.Model):
    employee = models.ForeignKey(ReestrUsers, on_delete=models.CASCADE)
    salary_position = models.CharField("Ставка по окладу", max_length=7,
                                       blank=False, default='--',
                                       choices=emp.POSITIONS)
    procents = models.IntegerField("процентная надбавка", blank=True, null=True)