from django.urls import path
from . import views

app_name = 'customerRegistration'
urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('viewFeedback/', views.viewFeedback, name='viewFeedback'),
]