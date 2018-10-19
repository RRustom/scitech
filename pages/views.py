from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/index.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class SchedulePageView(TemplateView):
    template_name = 'pages/schedule.html'

class SpeakersPageView(TemplateView):
    template_name = 'pages/speakers.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

class TicketsPageView(TemplateView):
    template_name = 'pages/tickets.html'
