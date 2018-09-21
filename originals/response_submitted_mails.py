from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages

#sends the event confirmation mail to both the team email and the user email, unless they are the same. if they are the same, only one email is sent
def response_submitted_mail(challenge_number ,email,request):
    #email confirmation
    base_location = "{0}://{1}".format(request.scheme, request.get_host())
    subject = " Submitted \'In Other Words\' Responses"
    name = str(request.user)
    html_content = render_to_string('originals/email_templates/responses_submitted.html', {'challenge_number ':challenge_number ,'base_location':base_location,'name':name}) # render with dynamic value
    #for text version of mail
    text_content = '''\n
                    Hello, {2}.
                    \n\n
                    You have successfully submitted your \'In Other Words\' Challenge {3} Responses
                    \n\n Best wishes,
                    \n Pravega Team.
                    '''.format(request.scheme, request.get_host(),name,challenge_number)
    success=True
    try:
        msg1 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [email])
        msg1.attach_alternative(html_content, "text/html")
        msg1.send()
        if email != request.user.email:
            msg2 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [request.user.email])
            msg2.attach_alternative(html_content, "text/html")
            msg2.send()
    except:
        success=False
        messages.add_message(request, messages.INFO, 'We are facing some difficulty sending the confirmation mail.')

    return success
