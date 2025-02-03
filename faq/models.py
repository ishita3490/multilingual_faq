from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()  # English question
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    answer = RichTextField(blank=True, null=True)  # English Answer
    answer_hi = RichTextField(blank=True, null=True)  # Hindi Answer
    answer_bn = RichTextField(blank=True, null=True)  # Bengali Answer

    def save(self, *args, **kwargs):
        """Automatically translate question and answer when saving."""
        if self.question:
            if not self.question_hi:
                translated_hi = translator.translate(self.question, src='en', dest='hi')
                self.question_hi = translated_hi.text if translated_hi and translated_hi.text else self.question

            if not self.question_bn:
                translated_bn = translator.translate(self.question, src='en', dest='bn')
                self.question_bn = translated_bn.text if translated_bn and translated_bn.text else self.question

        # ✅ Now, Auto-Translate the Answers
        if self.answer:
            if not self.answer_hi:
                translated_hi = translator.translate(self.answer, src='en', dest='hi')
                self.answer_hi = translated_hi.text if translated_hi and translated_hi.text else self.answer

            if not self.answer_bn:
                translated_bn = translator.translate(self.answer, src='en', dest='bn')
                self.answer_bn = translated_bn.text if translated_bn and translated_bn.text else self.answer

        super().save(*args, **kwargs)  # Save model changes
