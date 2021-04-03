from django import forms
from poll.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("question",)

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=70, required=False, label="Поиск")


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('text',)


class SearchChoiceForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label="Поиск")