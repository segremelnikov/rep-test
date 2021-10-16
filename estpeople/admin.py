from django.contrib import admin
from .models import Page, Estimation

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)

class EstimationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Estimation, EstimationAdmin)