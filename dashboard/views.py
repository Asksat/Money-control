from django.views.generic import ListView

from dashboard.models import Category


class HomePageView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'
