from django.db import models
from django.forms import ModelChoiceField

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length = 100, null = True, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "polls"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"{self.id}. {self.question}. {self.created_at}"


class Choice(models.Model):
    text = models.CharField(max_length = 400, null = True, blank = False)
    poll_id = models.ForeignKey("poll.Poll", on_delete=models.CASCADE, related_name="Choice", null=False, blank=False)

    class Meta:
        db_table = "choices"
        verbose_name = "Вариант_ответа"
        verbose_name_plural = "Варианты_ответа"

    def __str__(self):
        return f"{self.id}. {self.text}. {self.poll_id}"


class Answer(models.Model):
    poll_id = models.ForeignKey("poll.Poll", on_delete=models.CASCADE, related_name="Answer", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    choice_id = models.ForeignKey("poll.Choice", on_delete=models.CASCADE, related_name="Answer", null=False, blank=False)

    class Meta:
        db_table = "answers"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"{self.id}. {self.poll_id}. {self.choice_id}"