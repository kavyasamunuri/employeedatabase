from django.urls import path

from salary import views
urlpatterns=[
    path('<int:pk>/',views.employee_details, name='employee_detail'),
]