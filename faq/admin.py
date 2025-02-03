from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # ✅ Use 'question' instead of 'question_en'
    search_fields = ('question', 'question_hi', 'question_bn')

admin.site.register(FAQ, FAQAdmin)
