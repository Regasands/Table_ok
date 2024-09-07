from django.urls import path
from app.users.views import *

urlpatterns = [
    path('', SettingPageViews.as_view(), name='settingpage'),
    path('group/', ListGroupViews.as_view(), name='listgroup'),
    path('group/delgroup/<int:pk>', UpdateDelGroup.as_view(), name='delgroup'),
    path('group/update/<int:pk>',  UpdateAdminGroup.as_view(), name='updategroup'),
    path('group/createinvite/<int:pk>', CreateInvite.as_view(), name='createinvite'),
    path('profile/', ListUserProfile.as_view(), name='profileuser'),
    path('profile/invite', ListInviteViews.as_view(), name='invite'),
    path('profile/invite/deleteaccept/<int:pk>', DelAndAcceptInviteView.as_view(), name='acceptinvite'),
    path('profile/invite/deletereject/<int:pk>', DelAndRejectInviteView.as_view(), name='reject'),
]