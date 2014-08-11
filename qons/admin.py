from django.contrib import admin
from qons.models import Qon, Quest, Answer

class QuestInline(admin.TabularInline):
    model = Quest
    extra = 3

class QonAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name']
    inlines = [QuestInline]

class QonAnswer(admin.ModelAdmin):
	pass

admin.site.register(Qon, QonAdmin)
admin.site.register(Answer, QonAnswer)
