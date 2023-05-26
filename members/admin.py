from django.contrib import admin
from .models import Member, Product

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}

class ProductAdmin(admin.ModelAdmin):
  list_display = ("productname","inventory","productpic","price")

admin.site.register(Member, MemberAdmin)
admin.site.register(Product, ProductAdmin)