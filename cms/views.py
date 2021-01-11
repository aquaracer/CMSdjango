from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import IndexPage, Product
from .forms import EmailForm
from .service import send_message


class IndexPageView(ListView):
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('created')
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = IndexPage.objects.first()
        context['form'] = EmailForm()
        return context


class ProductDetailView(DetailView):
    model = Product
    slug_field = "url"


class SendEmailView(View):
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['email'])
        return redirect(reverse('index'))
