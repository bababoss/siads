from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):

    list_display = ['title','publish_in',]

#    def get_name(self, obj):
#        return obj.title
#    get_name.admin_order_field  = 'title'  #Allows column order sorting
#    get_name.short_description = 'blog title'  #Renames column head


    #serializers= Blog
    class Meta:
        model = Blog


admin.site.register(Blog)