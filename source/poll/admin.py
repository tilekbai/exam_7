from django.contrib import admin
from poll.models import Poll, Choice, Answer

# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "created_at"]
    list_filter = ["id", "question", "created_at"]
    list_search = ["question", "created_at"]
    fields = ["id", "question", "created_at"]
    readonly_fields = ["id", "created_at"]

admin.site.register(Poll, PollAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "poll_id"]
    list_filter = ["id", "text", "poll_id"]
    list_search = ["text", "poll_id"]
    fields = ["id", "text", "poll_id"]
    readonly_fields = ["id"]

admin.site.register(Choice, ChoiceAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "poll_id", "choice_id"]
    list_filter = ["id", "poll_id", "choice_id"]
    list_search = ["poll_id","choice_id"]
    fields = ["id", "poll_id", "choice_id"]
    readonly_fields = ["id", "created_at"]

admin.site.register(Answer, AnswerAdmin)