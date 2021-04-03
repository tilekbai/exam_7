from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import get_object_or_404, reverse
from poll.base_views import FormView as CustomFormView

from poll.models import Poll, Choice
from poll.forms import PollForm, SearchForm
# Create your views here.


class MainView(ListView):
    template_name = "poll/poll_list.html"
    model = Poll
    context_object_name = "polls"
    ordering = ("-created_at")
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()

        return super(MainView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_data:
            queryset = queryset.filter(
                Q(summary__icontains = self.search_data) |
                Q(description__icontains = self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search_value"]
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form

        if self.search_data:
            context["query"] = urlencode({"search_value": self.search_data})

        return context
    

class PollView(TemplateView):
    template_name = "poll/poll_view.html"

    def get_context_data(self, **kwargs):
        kwargs ["poll"] = get_object_or_404(Poll, id=kwargs.get("pk"))
        return super().get_context_data(**kwargs)


class PollCreateView(CreateView):
    template_name = "poll/poll_create.html"
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk': self.object.pk})