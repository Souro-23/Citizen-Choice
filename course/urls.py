from django.urls import path
from .views import Create_Course_View


urlpatterns = [
    path('add/',Create_Course_View.as_view(),name = 'create_course'),

]
