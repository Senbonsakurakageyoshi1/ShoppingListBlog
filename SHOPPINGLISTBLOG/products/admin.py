from django.contrib import admin
from .models import Produits, Category, Company,  Comment
from django.contrib.auth.models import Group

# admin.register() decorator
@admin.register(Produits)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nom', 'description')
    list_filter = ('category', )


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Comment)


admin.site.unregister(Group)

admin.site.site_header = "Product Review Admin"




