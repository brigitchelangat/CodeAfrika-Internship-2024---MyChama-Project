from django.contrib import admin

# Register your models here.
from .models import Member
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','email','phone_number','joining_date','profession']
    list_filter=['email','joining_date']
    search_fields=['first_name','last_name','profession']
    show_facets = admin.ShowFacets.ALWAYS


from .models import Account
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display= ['member_id','account_number','actual_balance','available_balance','account_type']
    list_filter=['account_type']
    search_fields=['account_number']
    show_facets = admin.ShowFacets.ALWAYS