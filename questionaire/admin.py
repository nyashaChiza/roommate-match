from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'is_active', 'created', 'updated')
    list_filter = ('is_active', 'created')
    search_fields = ('text', 'user__username')
    raw_id_fields = ('user',)
    readonly_fields = ('created', 'updated')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer_text', 'created')
    list_filter = ('created',)
    search_fields = ('answer_text', 'user__username', 'question__text')
    raw_id_fields = ('user', 'question')
    readonly_fields = ('created',)
