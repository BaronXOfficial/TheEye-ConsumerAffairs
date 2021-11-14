from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='event_home'),
    path('api/', views.EventAPIView.as_view()),
    path('api/event/', views.add_webapp_data, name='event_api'),
    path("click_1", views.click_1, name='click_1'),
    path("click_2", views.click_2, name='click_2'),
    path("click_3", views.click_3, name='click_3'),
    ]