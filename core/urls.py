from django.contrib import admin
from django.urls import path
from bot.views import webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", webhook.urls)
]
