from django.contrib import admin
from blog.models import userinfo,userstest,rank
# Register your models here.


class showuserinfo(admin.ModelAdmin):
    list_display = ('id','username','gender','birth','weight','height','registerdate','choice_id')
    search_fields = ('username','id','gender')
    list_filter = ('gender','choice_id')
    ordering = ('id',)


admin.site.register(userinfo,showuserinfo)
admin.site.register(userstest)
admin.site.register(rank)