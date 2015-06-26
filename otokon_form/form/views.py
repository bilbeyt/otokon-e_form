from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Form
from .forms import FormCreateForm
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.views import logout


def custom_login(request, *args, **kwargs):
    c = csrf(request)
    return render(request, "login.html", c)


def custom_logout(request):
    logout(request)
    messages.success(request, _("You are successfully logged out"))
    return HttpResponseRedirect(reverse("login"))


def auth_view(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
       auth.login(request, user)
       messages.success(request, _("You are successfully logged in"))
       return HttpResponseRedirect(reverse("create"))
    else:
       messages.error(request, _("Username and password mismatch"))
       return HttpResponseRedirect(reverse("login"))


class FormCreateView(CreateView):
    model = Form
    form_class = FormCreateForm
    template_name = "form.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FormCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.instance
        instance.save()
        messages.success(self.request, _("Form created successfully!"))
        return HttpResponseRedirect(reverse("base"))
