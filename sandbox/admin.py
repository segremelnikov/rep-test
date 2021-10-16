from django.contrib import admin
from .models import Answer

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AnswerAdmin)