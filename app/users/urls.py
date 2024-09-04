from django.urls import path
from app.users.views import SettingPageViews, ListGroupViews, UpdateDelGroup

urlpatterns = [
    path('', SettingPageViews.as_view(), name='settingpage'),
    path('group/', ListGroupViews.as_view(), name='listgroup'),
    path('group/delgroup/<int:pk>', UpdateDelGroup.as_view(), name='delgroup')
]