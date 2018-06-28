DjREST
======

DjREST is a lightweight library that provides basics of what is needed to create RESTful APIs on top of Django.

NOTE: This is fork of https://github.com/croach/django-simple-rest with some improvements.


Installation
------------

1. Install using pip

    $ pip install djrest


Sample Project Setup
-------------------

    # ===================
    # example/resources.py
    # ===================

    import json

    from djrest import Resource
    from django.http import JsonResponse

    from example.models import Email

    class ContactResource(Resource):

        def post(self, request):
            meta = {
                item: request.META.get(item)
                for item in ['HTTP_ACCEPT_LANGUAGE', 'HTTP_REFERER', 'HTTP_USER_AGENT']
            }

            e = Email(name=request.POST.get('name'),
                      email=request.POST.get('email'),
                      subject='Test Subject',
                      message=request.POST.get('message'),
                      meta=json.dumps({'cookies': request.COOKIES, 'meta': meta}))
            e.save()
            return JsonResponse({'status': 200,
                                 'message': 'Thanks for subscribing'}, status=200)


    # ===================
    # example/models.py
    # ===================

    from django.db import models

    class Email(models.Model):

        name = models.CharField(max_length=255, blank=True, null=True)
        email = models.EmailField()
        subject = models.CharField(max_length=255)
        message = models.TextField()
        meta = models.TextField(blank=True, null=True)
