from django.contrib import admin
from main.models import UserData, UserEntry, AnonEntry

class UserDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserData, UserDataAdmin)


class UserEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserEntry, UserEntryAdmin)

class AnonEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(AnonEntry, AnonEntryAdmin)