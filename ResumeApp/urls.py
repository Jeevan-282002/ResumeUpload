from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('all_candidates/', views.all_candidates.as_view(),name='all_candidates'),

]
