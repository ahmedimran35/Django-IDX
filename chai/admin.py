from django.contrib import admin
from .models import Chaivarity, ChaiReview, Store, Certificate

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cha_type')
    inlines = [ChaiReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    filter_horizontal = ('chai_varity',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai_name', 'certificate_number', 'issue_date')

    def chai_name(self, obj):
        return obj.chai.name






admin.site.register(Chaivarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Certificate, ChaiCertificateAdmin)

