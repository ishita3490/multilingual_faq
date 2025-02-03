from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'answer']

    def get_translated_question(self, obj):
        lang = self.context.get('request').GET.get('lang', 'en')
        return obj.get_question(lang)
