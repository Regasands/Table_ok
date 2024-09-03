from django.contrib import admin
from django.urls import path, include
from app.homepage.views import HomePageViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', include('app.todo_table.urls')),
    path('', HomePageViews.as_view(), name='homepage')
]
