from django.contrib import admin
from .models import ChaiVariety , chaireview,store,chaicertificate

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = chaireview
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('Name' , 'type' , 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varities',)

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')

admin.site.register(ChaiVariety,ChaiVarityAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(chaicertificate,chaiCertificateAdmin)
