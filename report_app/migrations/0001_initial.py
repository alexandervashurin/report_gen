# Generated by Django 4.0.1 on 2022-01-21 23:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='documents/%Y/%m')),
            ],
            options={
                'verbose_name': 'ежедневные справки(excel)',
                'verbose_name_plural': 'ежедневные справки(excel)',
                'ordering': ['upload_at'],
            },
        ),
        migrations.CreateModel(
            name='Document2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='documents2/%Y/%m')),
            ],
            options={
                'verbose_name': 'ежедневные справки(word)',
                'verbose_name_plural': 'ежедневные справки(word)',
                'ordering': ['upload_at'],
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('id_problem', models.IntegerField()),
                ('data_problem', models.DateTimeField()),
                ('description_problem', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'проблемы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ReestrUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_m_surname', models.CharField(choices=[('1', 'Фамилия1 Имя1 Отчество1 '), ('2', 'Фамилия2 Имя2 Отчество2 '), ('3', 'Фамилия3 Имя3 Отчество3 '), ('4', 'Фамилия4 Имя4 Отчество4 '), ('5', 'Фамилия5 Имя5 Отчество5 '), ('6', 'Фамилия6 Имя6 Отчество6 '), ('7', 'Фамилия7 Имя7 Отчество7 '), ('8', 'Фамилия8 Имя8 Отчество8 '), ('9', 'Фамилия9 Имя9 Отчество9 '), ('10', 'Фамили10 Имя10 Отчество10 '), ('11', 'Фамилия11 Имя11 Отчество11 '), ('12', 'Фамилия12 Имя12 Отчество12 '), ('13', 'Фамилия13 Имя13 Отчество13 '), ('14', 'Фамилия14 Имя114 Отчество14 ')], max_length=5, verbose_name='ФИО сотрудника')),
                ('name_pc', models.CharField(blank=True, default='', max_length=25, verbose_name='имя компьютера в системе')),
                ('type_pc', models.CharField(choices=[('1', 'Основной'), ('2', 'Дополнительный'), ('3', 'Ноутбук')], default='1', max_length=1, verbose_name='тип рабочей станции')),
                ('department', models.CharField(choices=[('1', 'Дирекция'), ('2', 'Служба финансового директора'), ('3', 'Служба коммерческого директора'), ('4', 'Служба технического директора'), ('5', 'Группа проектного проектирования'), ('6', 'Бухгалтерия')], default='1', max_length=1, verbose_name='подразделение')),
                ('position_pers', models.CharField(blank=True, choices=[('1', 'Генеральный директор'), ('2', 'Советник генерального директора'), ('3', 'Главный бухгалтер'), ('4', 'Финансовый директор'), ('5', 'Комерческий директор'), ('6', 'Технический директор'), ('7', 'Бухгалтер'), ('8', 'Экономист'), ('9', 'Юрисконсульт'), ('10', 'Заместитель технического директора - главный технолог'), ('11', 'Заместитель коммерческого директора'), ('12', 'Заместитель финансового директора'), ('13', 'Главный конструктор'), ('14', 'Секретарь Генерального директора'), ('15', 'Главный специалист по работе персоналом'), ('16', 'Специалист по административно-хозяйственной деятельности'), ('17', 'Ведущий инженер'), ('18', 'Руководитель проекта'), ('19', 'Архитектор проекта'), ('20', 'Ведущий инженер-конструктор'), ('21', 'Инженер-конструктор 1 категории'), ('22', 'Инженер-конструктор 2 категории'), ('23', 'Ведущий специалист по СМБ'), ('24', 'Руководитель отдела сертификации'), ('25', 'Инженер-конструктор по расчетам 2 категории'), ('26', 'Руководитель по управлению качеством'), ('27', 'Специалист по диспетчеризации'), ('28', 'Менеджер по продажам'), ('29', 'Инженер-аналитик')], max_length=5, verbose_name='должность')),
                ('type_equip', models.CharField(choices=[('0', 'нет'), ('1', 'Тонкий клиент'), ('2', 'Системный блок'), ('3', 'Ноутбук1'), ('4', 'Ноутбук2'), ('5', 'Ноутбук3'), ('6', 'Ноутбук-трансформер'), ('7', 'Аппарат-копир'), ('8', 'Плоттер1'), ('9', 'Сканер1'), ('10', 'Телевизор1')], default='1', max_length=2, verbose_name='тип оборудования')),
                ('inv_num_notebook', models.CharField(choices=[('0', 'нет'), ('1', '000001ноут.'), ('2', '000002ноут.'), ('3', '000003ноут.'), ('4', '000004ноут.'), ('5', '000005ноут.'), ('6', '000006ноут.'), ('7', '000007ноут.'), ('8', '000008ноут.'), ('9', '000009ноут.'), ('10', '000010ноут.'), ('11', '000011ноут.'), ('12', '000012ноут.'), ('13', '000013ноут.'), ('14', '000014ноут.'), ('15', '000015ноут.'), ('16', '000016ноут.'), ('17', '000017ноут.'), ('18', '000018ноут.'), ('19', '000019ноут.'), ('20', '000020ноут.'), ('21', '000021ноут.'), ('22', '000022ноут.'), ('23', '000023ноут.'), ('24', '000024ноут.'), ('25', '000025ноут.'), ('26', '000026ноут.'), ('27', '000027ноут.'), ('28', '000028ноут.'), ('29', '000029ноут.'), ('30', '000030ноут.'), ('31', '000031ноут.'), ('32', '000032ноут.'), ('33', '000033ноут.'), ('34', '000034ноут.'), ('35', '000035ноут.'), ('36', '000036ноут.'), ('37', '000037ноут.')], default='1', max_length=2)),
                ('inv_num_thin_client', models.CharField(choices=[('0', 'нет'), ('1', '000001тк'), ('2', '000002тк'), ('3', '000003тк'), ('4', '000004тк'), ('5', '000005тк'), ('6', '000006тк'), ('7', '000007тк'), ('8', '000008тк'), ('9', '000009тк'), ('10', '000010тк'), ('11', '000011тк'), ('12', '000012тк'), ('13', '000013тк'), ('14', '000014тк'), ('15', '000015тк'), ('16', '000016тк'), ('17', '000017тк'), ('18', '000018тк'), ('19', '000019тк'), ('20', '000020тк'), ('21', '000021тк'), ('22', '000022тк'), ('23', '000023тк'), ('24', '000024тк'), ('25', '000025тк'), ('26', '000026тк'), ('27', '000027тк'), ('28', '000028тк'), ('29', '000029тк'), ('30', '000030тк'), ('31', '000031тк'), ('32', '000032тк'), ('33', '000033тк'), ('34', '000034тк'), ('35', '000035тк'), ('36', '000036тк'), ('37', '000037тк')], default='1', max_length=2, verbose_name='инв. номер тонкого клиента')),
                ('inv_num_main_equip', models.CharField(choices=[('0', 'нет'), ('1', 'БП-000001'), ('2', 'БП-000002'), ('3', 'БП-000003'), ('4', 'БП-000004'), ('5', 'БП-000005'), ('6', 'БП-000006'), ('7', 'БП-000007'), ('8', 'БП-000008'), ('9', 'БП-000009'), ('10', 'БП-000010'), ('11', 'БП-000011'), ('12', 'БП-000012'), ('13', 'БП-000013'), ('14', 'БП-000014'), ('15', 'БП-000015'), ('16', 'БП-000016'), ('17', 'БП-000017'), ('18', 'БП-000018'), ('19', 'БП-000019'), ('20', 'БП-000020'), ('21', 'БП-000021'), ('22', 'БП-000022'), ('23', 'БП-000023'), ('24', 'БП-000024'), ('25', 'БП-000025'), ('26', 'БП-000026'), ('27', 'БП-000027'), ('28', 'БП-000028'), ('29', 'БП-000029'), ('30', 'БП-000030'), ('31', 'БП-000031'), ('32', 'БП-000032'), ('33', 'БП-000033'), ('34', 'БП-000034'), ('35', 'БП-000035'), ('36', 'БП-000036'), ('37', 'БП-000037')], default='0', max_length=2, verbose_name='инв. номер основного оборудования')),
                ('type_processor', models.CharField(choices=[('1', 'Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz'), ('2', 'Intel Core i5-8600K CPU 3.10GHz '), ('3', 'Intel Core i5-9600K CPU 3.70GHz ')], default='1', max_length=1, verbose_name='тип процессора')),
                ('ram', models.IntegerField(default='1', verbose_name='объем памяти')),
                ('type_video', models.CharField(choices=[('1', 'Встроенная'), ('2', 'дисректная_1'), ('3', 'дисректная_2'), ('4', 'дисректная_3')], default='1', max_length=1, verbose_name='видеокарта')),
                ('sound_devices', models.CharField(choices=[('1', 'нет'), ('2', 'есть')], default='1', max_length=1, verbose_name='звуковые колонки')),
                ('inv_num_sound_speakers', models.CharField(choices=[('0', 'нет'), ('1', '000001зв.кол.'), ('2', '000002зв.кол.'), ('3', '000003зв.кол.'), ('4', '000004зв.кол.'), ('5', '000005зв.кол.'), ('6', '000006зв.кол.'), ('7', '000007зв.кол.'), ('8', '000008зв.кол.'), ('9', '000009зв.кол.'), ('10', '000010зв.кол.'), ('11', '000011зв.кол.'), ('12', '000012зв.кол.'), ('13', '000013зв.кол.'), ('14', '000014зв.кол.'), ('15', '000015зв.кол.'), ('16', '000016зв.кол.'), ('17', '000017зв.кол.'), ('18', '000018зв.кол.'), ('19', '000019зв.кол.'), ('20', '000020зв.кол.'), ('21', '000021зв.кол.'), ('22', '000022зв.кол.'), ('23', '000023зв.кол.'), ('24', '000024зв.кол.'), ('25', '000025зв.кол.'), ('26', '000026зв.кол.'), ('27', '000027зв.кол.'), ('28', '000028зв.кол.'), ('29', '000029зв.кол.'), ('30', '000030зв.кол.'), ('31', '000031зв.кол.'), ('32', '000032зв.кол.'), ('33', '000033зв.кол.'), ('34', '000034зв.кол.'), ('35', '000035зв.кол.'), ('36', '000036зв.кол.'), ('37', '000037зв.кол.')], default='0', max_length=2, verbose_name='инв. номерколонок')),
                ('serial_num_monitor', models.CharField(blank=True, default='', max_length=70, verbose_name='серийный номер монитора')),
                ('inv_num_monitor', models.CharField(choices=[('0', 'нет'), ('1', '000001мон'), ('2', '000002мон'), ('3', '000003мон'), ('4', '000004мон'), ('5', '000005мон'), ('6', '000006мон'), ('7', '000007мон'), ('8', '000008мон'), ('9', '000009мон'), ('10', '000010мон'), ('11', '000011мон'), ('12', '000012мон'), ('13', '000013мон'), ('14', '000014мон'), ('15', '000015мон'), ('16', '000016мон'), ('17', '000017мон'), ('18', '000018мон'), ('19', '000019мон'), ('20', '000020мон'), ('21', '000021мон'), ('22', '000022мон'), ('23', '000023мон'), ('24', '000024мон'), ('25', '000025мон'), ('26', '000026мон'), ('27', '000027мон'), ('28', '000028мон'), ('29', '000029мон'), ('30', '000030мон'), ('31', '000031мон'), ('32', '000032мон'), ('33', '000033мон'), ('34', '000034мон'), ('35', '000035мон'), ('36', '000036мон'), ('37', '000037мон')], default='0', max_length=2, verbose_name='инв. номер монитора')),
                ('diagonal_monitor', models.IntegerField(default='23', verbose_name='диагональ')),
                ('num_monitor', models.IntegerField(default=1, verbose_name='количество мониторов')),
                ('power_filter', models.CharField(choices=[('1', 'нет'), ('2', 'есть')], default='1', max_length=1, verbose_name='сетевой фильтр')),
                ('local_printer', models.CharField(choices=[('1', 'нет'), ('2', 'есть')], default='1', max_length=1, verbose_name='принтер локальный')),
                ('inv_num_printer', models.CharField(choices=[('0', 'нет'), ('1', '000001п'), ('2', '000002п'), ('3', '000003п'), ('4', '000004п'), ('5', '000005п'), ('6', '000006п'), ('7', '000007п'), ('8', '000008п'), ('9', '000009п'), ('10', '000010п'), ('11', '000011п'), ('12', '000012п'), ('13', '000013п'), ('14', '000014п'), ('15', '000015п'), ('16', '000016п'), ('17', '000017п'), ('18', '000018п'), ('19', '000019п'), ('20', '000020п'), ('21', '000021п'), ('22', '000022п'), ('23', '000023п'), ('24', '000024п'), ('25', '000025п'), ('26', '000026п'), ('27', '000027п'), ('28', '000028п'), ('29', '000029п'), ('30', '000030п'), ('31', '000031п'), ('32', '000032п'), ('33', '000033п'), ('34', '000034п'), ('35', '000035п'), ('36', '000036п'), ('37', '000037п')], default='0', max_length=2, verbose_name='инв. номер принтера')),
                ('webcam', models.CharField(choices=[('1', 'нет'), ('2', 'есть')], default='1', max_length=1, verbose_name='вебкамера')),
                ('inv_num_webcam', models.CharField(choices=[('0', 'нет'), ('1', 'ВК-000001'), ('2', 'ВК-000002'), ('3', 'ВК-000003'), ('4', 'ВК-000004'), ('5', 'ВК-000005'), ('6', 'ВК-000006'), ('7', 'ВК-000007'), ('8', 'ВК-000008'), ('9', 'ВК-000009'), ('10', 'ВК-000010'), ('11', 'ВК-000011'), ('12', 'ВК-000012'), ('13', 'ВК-000013'), ('14', 'ВК-000014'), ('15', 'ВК-000015'), ('16', 'ВК-000016'), ('17', 'ВК-000017'), ('18', 'ВК-000018'), ('19', 'ВК-000019'), ('20', 'ВК-000020'), ('21', 'ВК-000021'), ('22', 'ВК-000022'), ('23', 'ВК-000023'), ('24', 'ВК-000024'), ('25', 'ВК-000025'), ('26', 'ВК-000026'), ('27', 'ВК-000027'), ('28', 'ВК-000028'), ('29', 'ВК-000029'), ('30', 'ВК-000030'), ('31', 'ВК-000031'), ('32', 'ВК-000032'), ('33', 'ВК-000033'), ('34', 'ВК-000034'), ('35', 'ВК-000035'), ('36', 'ВК-000036'), ('37', 'ВК-000037')], default='0', max_length=2, verbose_name='инв. номер вебкамеры')),
                ('other_devices', models.CharField(choices=[('0', 'нет'), ('1', 'Тонкий клиент'), ('2', 'Системный блок'), ('3', 'Ноутбук1'), ('4', 'Ноутбук2'), ('5', 'Ноутбук3'), ('6', 'Ноутбук-трансформер'), ('7', 'Аппарат-копир'), ('8', 'Плоттер1'), ('9', 'Сканер1'), ('10', 'Телевизор1')], default='0', max_length=2, verbose_name='прочие устройства')),
                ('inv_num_other_devices', models.IntegerField(blank=True, null=True, verbose_name='инв. прочего устройства')),
                ('other_devices2', models.CharField(choices=[('0', 'нет'), ('1', 'Тонкий клиент'), ('2', 'Системный блок'), ('3', 'Ноутбук1'), ('4', 'Ноутбук2'), ('5', 'Ноутбук3'), ('6', 'Ноутбук-трансформер'), ('7', 'Аппарат-копир'), ('8', 'Плоттер1'), ('9', 'Сканер1'), ('10', 'Телевизор1')], default='0', max_length=2, verbose_name='прочие устройства_2')),
                ('inv_num_other_devices2', models.IntegerField(blank=True, null=True, verbose_name='инв. прочего устройства')),
                ('ups', models.CharField(choices=[('1', 'нет'), ('2', 'есть')], default='1', max_length=1, verbose_name='источник бесперебойного питания')),
                ('inv_num_ups', models.CharField(blank=True, choices=[('0', 'нет'), ('1', 'ИБП-000001'), ('2', 'ИБП-000002'), ('3', 'ИБП-000003'), ('4', 'ИБП-000004'), ('5', 'ИБП-000005'), ('6', 'ИБП-000006'), ('7', 'ИБП-000007'), ('8', 'ИБП-000008'), ('9', 'ИБП-000009'), ('10', 'ИБП-000010'), ('11', 'ИБП-000011'), ('12', 'ИБП-000012'), ('13', 'ИБП-000013'), ('14', 'ИБП-000014'), ('15', 'ИБП-000015'), ('16', 'ИБП-000016'), ('17', 'ИБП-000017'), ('18', 'ИБП-000018'), ('19', 'ИБП-000019'), ('20', 'ИБП-000020'), ('21', 'ИБП-000021'), ('22', 'ИБП-000022'), ('23', 'ИБП-000023'), ('24', 'ИБП-000024'), ('25', 'ИБП-000025'), ('26', 'ИБП-000026'), ('27', 'ИБП-000027'), ('28', 'ИБП-000028'), ('29', 'ИБП-000029'), ('30', 'ИБП-000030'), ('31', 'ИБП-000031'), ('32', 'ИБП-000032'), ('33', 'ИБП-000033'), ('34', 'ИБП-000034'), ('35', 'ИБП-000035'), ('36', 'ИБП-000036'), ('37', 'ИБП-000037')], default='0', max_length=2, verbose_name='инв. номер ИБП')),
                ('type_os', models.CharField(choices=[('1', 'Windows 7'), ('2', 'Windows 10'), ('3', 'Linux')], default='2', max_length=1, verbose_name='операционная система')),
                ('mac_addresses', models.CharField(choices=[('1', '00:AA:BB:CC:DD:E0'), ('2', '00:AA:BB:CC:DD:E1'), ('3', '00:AA:BB:CC:DD:E2'), ('4', '00:AA:BB:CC:DD:E3'), ('5', '00:AA:BB:CC:DD:E4')], default='33', max_length=5, verbose_name='MAC-адрес')),
                ('brand_phone', models.CharField(choices=[('1', 'телефон_1'), ('2', 'телефон_2')], default='1', max_length=1, verbose_name='модель телефона')),
                ('inv_num_phone', models.CharField(choices=[('0', 'нет'), ('1', '000001тел'), ('2', '000002тел'), ('3', '000003тел'), ('4', '000004тел'), ('5', '000005тел'), ('6', '000006тел'), ('7', '000007тел'), ('8', '000008тел'), ('9', '000009тел'), ('10', '000010тел'), ('11', '000011тел'), ('12', '000012тел'), ('13', '000013тел'), ('14', '000014тел'), ('15', '000015тел'), ('16', '000016тел'), ('17', '000017тел'), ('18', '000018тел'), ('19', '000019тел'), ('20', '000020тел'), ('21', '000021тел'), ('22', '000022тел'), ('23', '000023тел'), ('24', '000024тел'), ('25', '000025тел'), ('26', '000026тел'), ('27', '000027тел'), ('28', '000028тел'), ('29', '000029тел'), ('30', '000030тел'), ('31', '000031тел'), ('32', '000032тел'), ('33', '000033тел'), ('34', '000034тел'), ('35', '000035тел'), ('36', '000036тел'), ('37', '000037тел')], default='0', max_length=2, verbose_name='инв. телефона')),
                ('number_phone', models.IntegerField(blank=True, null=True, verbose_name='номер телефона сотрудника')),
            ],
            options={
                'verbose_name': 'пользователи Информационной системы',
                'verbose_name_plural': 'пользователи_ИС',
                'ordering': ['name_m_surname'],
            },
            managers=[
                ('reestr_man', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddIndex(
            model_name='problem',
            index=models.Index(fields=['title', 'description_problem'], name='report_app__title_c13d62_idx'),
        ),
        migrations.AddIndex(
            model_name='problem',
            index=models.Index(fields=['title'], name='title_idx'),
        ),
    ]