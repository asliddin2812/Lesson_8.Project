from django.db import models


class Question(models.Model):
    text = models.TextField(verbose_name="Savol matni")
    number = models.PositiveIntegerField(verbose_name="Savol raqami")

    def __str__(self):
        return f"Savol {self.number}: {self.text[:50]}"

class ImageOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    image = models.ImageField(upload_to='options/', verbose_name="Rasm")
    is_correct = models.BooleanField(default=False, verbose_name="To‘g‘ri javobmi")

    def __str__(self):
        return f"Variant - {self.question.number} - {'To‘g‘ri' if self.is_correct else 'Noto‘g‘ri'}"

class UserAnswer(models.Model):
    user_id = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(ImageOption, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foydalanuvchi {self.user_id} - Savol {self.question.number}"