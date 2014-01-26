from django.contrib import admin
from polls.models import Poll,Choice

class ChoiceInline(admin.TabularInline):
  model=Choice
  extra=4
  
class PollAdmin(admin.ModelAdmin):
  fieldsets=[('Date information',{'fields':['pub_date'],'classes':['collapse']}),(None,{'fields':['question']})]
  inlines=[ChoiceInline]
  list_display=('question','pub_date','was_published_recently')
  list_filter=['pub_date','question']
  search_fields=['question']
  
admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)
# Register your models here.
