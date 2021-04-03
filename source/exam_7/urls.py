"""exam_7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from poll.views import MainView, PollView, PollCreateView, PollUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="poll-list"),
    path('<int:pk>/', PollView.as_view(), name="poll-view"),
    path('add_poll/', PollCreateView.as_view(), name="poll-create"),
    path('<int:pk>/update_poll/', PollUpdateView.as_view(), name="poll-update"),
]
