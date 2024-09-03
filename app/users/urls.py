from django.urls import path
from app.users.views import SettingPageViews

urlpatterns = [
    path('', SettingPageViews.as_view(), name='settingpage'),
]