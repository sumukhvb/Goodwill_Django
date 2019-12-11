from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from .models import Section, images, testimonalCard
from .forms import ContactUs
from django.core.mail import send_mail


@csrf_protect
def home(request):
   Sectionobj=Section.objects.all() # Add the content by slug value
   imageobj=images.objects.all()
   testimonalobj=testimonalCard.objects.all()
   form = ContactUs(request.POST)
   if request.method == 'POST':
        if form.is_valid():
            newContact=form.save()
            newContact.user=request.user
            newContact.save()
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            messages.info(request, 'Your Response has been recorded')
            return HttpResponseRedirect('/')
   content={
      "images": imageobj,
      "aboutUsTitle": Sectionobj[0].sectionTitle,
      "aboutUsContent": Sectionobj,
      "testimonal": testimonalobj,
      "form": form,
   }  # Give keywords for calling
   return render(request, 'index.html', content)