from django.contrib import admin
from report_app.models import Problem, Document, Document2, ReestrUsers


@admin.register(Document)
class DocAdmin(admin.ModelAdmin):
    list_display = ('upload_at', 'description')
    list_filter = ('upload_at', 'description')

    search_fields = ('upload_at', 'description')


@admin.register(Document2)
class DocAdmin2(admin.ModelAdmin):
    list_display = ('upload_at', 'description')
    list_filter = ('upload_at', 'description')

    search_fields = ('upload_at', 'description')


admin.site.register(Problem)


@admin.register(ReestrUsers)
class ReestrUsersAdmin(admin.ModelAdmin):
    list_display = (
        'department',
        'position_pers',
        'type_equip',
        'inv_num_main_equip',
        'type_video',
        'number_phone',
    )
    list_filter = ('department', 'position_pers',)
    search_fields = ('фио', 'position_pers')
