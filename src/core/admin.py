from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Sentiment

# admin.site.register(Sentiment)

# admin.site.register(item)
@admin.register(Sentiment)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)
