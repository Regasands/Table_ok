from django.contrib import admin
from django.urls import path, include
from app.homepage.views import HomePageViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('task/', include('app.todo_table.urls')),
    path('setting/', include('app.users.urls')),
    path('', HomePageViews.as_view(), name='homepage'),
]
