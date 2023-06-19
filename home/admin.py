from django.contrib import admin
from.models import  Category,Product,Cart,Order,OrderItem,Profile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug',)  
    
class catA(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug',)  
        
      
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,catA)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
# admin.site.register(Amodel)