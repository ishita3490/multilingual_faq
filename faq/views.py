from django.utils.html import strip_tags
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from googletrans import Translator  # Google Translate for automatic translations
from .models import FAQ
from .serializers import FAQSerializer

translator = Translator()

def clean_html(html_text):
    """ Remove HTML tags from CKEditor content """
    return strip_tags(html_text).replace("&nbsp;", " ").strip()

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  
        cache_key = f"faqs_{lang}"  

        # Check if cached data exists
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)  # Return cached data instantly

        # Fetch all FAQs from the database
        faqs = FAQ.objects.all()
        translated_faqs = []

        for faq in faqs:
            translated_question = faq.question
            translated_answer = clean_html(faq.answer)  # Remove HTML tags from the answer

            if lang != "en":
                try:
                    translated_question = translator.translate(faq.question, dest=lang).text
                    translated_answer = translator.translate(translated_answer, dest=lang).text
                except Exception as e:
                    print(f"Translation error: {e}")  # Handle translation errors gracefully
                    translated_question = faq.question
                    translated_answer = faq.answer

            translated_faqs.append({
                "id": faq.id,
                "question": faq.question,
                "translated_question": translated_question,
                "answer": faq.answer,
                "translated_answer": translated_answer,
            })

        # Cache the translated FAQs for 1 hour
        cache.set(cache_key, translated_faqs, timeout=60*60)  
        return Response(translated_faqs)

class FAQDetailView(APIView):
    """ Fetch a single FAQ based on its ID """

    def get(self, request, faq_id):
        lang = request.GET.get("lang", "en")
        cache_key = f"faq_{faq_id}_{lang}"

        # Check if the FAQ is in cache
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        try:
            faq = FAQ.objects.get(id=faq_id)
        except FAQ.DoesNotExist:
            return Response({"error": "FAQ not found"}, status=404)

        translated_question = faq.question
        translated_answer = clean_html(faq.answer)

        if lang != "en":
            try:
                translated_question = translator.translate(faq.question, dest=lang).text
                translated_answer = translator.translate(translated_answer, dest=lang).text
            except Exception as e:
                print(f"Translation error: {e}")

        faq_data = {
            "id": faq.id,
            "question": faq.question,
            "translated_question": translated_question,
            "answer": faq.answer,
            "translated_answer": translated_answer,
        }

        # Cache the translated FAQ for 1 hour
        cache.set(cache_key, faq_data, timeout=60*60)
        return Response(faq_data)
