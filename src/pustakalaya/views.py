import os
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import FeedBackForm
from django.conf import settings


def change_language(request):
    return HttpResponse("Change language")


def feedback(request):
    if request.method == 'GET':
        form = FeedBackForm()
    else:
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            location = form.cleaned_data['address']
            suggestion = form.cleaned_data['suggestion']
            html_message = """
                <p>From: {0}</p>
                <p>Location: {1}</p>
                <p>Sender Email: {2}</p>
                <p>Country: {3}</p>
                <br><br>
                <b>
                {4}
                </b>

            """.format(name, location, email, country, suggestion)

            print(name, location, email, country, suggestion)

            try:
                # send_mail(
                #     subject="Feedback Message",
                #     message=html_message,
                #     from_email=email,
                #     recipient_list=os.getenv("FEEDBACK_EMAIL"),
                #     fail_silently=False,
                # )

                send_mail(
                    'Feedback message',
                    """
                    From: {}\n Email: {} \n Location: {} \n Country: {}\n Message: {}
                    """.format(name, email, location, country, suggestion ),
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_FEEDBACK])


            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect("/")
    return render(request, "static_pages/feedback.html", {'form': form})
