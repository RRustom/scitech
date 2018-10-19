from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.AboutPageView.as_view(), name='contact'),
    path('speakers/', views.SpeakersPageView.as_view(), name='speakers'),
    path('schedule/', views.SchedulePageView.as_view(), name='schedule'),
    path('tickets/', views.TicketsPageView.as_view(), name='tickets'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
]
