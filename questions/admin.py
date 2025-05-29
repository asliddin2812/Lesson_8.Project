from django.contrib import admin
from .models import Question, ImageOption, UserAnswer

class ImageOptionInline(admin.TabularInline):
    model = ImageOption
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['number', 'text']
    inlines = [ImageOptionInline]

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'question', 'selected_option', 'timestamp']

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
