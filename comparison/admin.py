<<<<<<< HEAD
from django.contrib import admin

# Register your models here.
=======
from django.contrib import admin

# Register your models here.
from comparison.models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_id', 'comparison_page', 'id_for_anchor')
    search_fields = ('title', 'external_id', 'comparison_page')
    list_filter = ('comparison_page',)
>>>>>>> 02eda6b (2025_1115_mypage_custom)
