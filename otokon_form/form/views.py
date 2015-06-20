from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Form
from .forms import FormCreateForm


class FormCreateView(CreateView):
    model = Form
    form_class = FormCreateForm
    template_name = "form_create.html"

    def form_valid(self, form):
        instance = form.instance
        instance.save()
        messages.success(self.request, "Form created successfully!")
        return HttpResponseRedirect(reverse("create"))
