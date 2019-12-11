from django.contrib import admin
from .models import Section, testimonalCard, images, Hysteroscopy, Arthroscopy, ContactUs
# Register your models here.

admin.site.register(Section)
admin.site.register(testimonalCard)
admin.site.register(images)
admin.site.register(Hysteroscopy)
admin.site.register(Arthroscopy)
admin.site.register(ContactUs)