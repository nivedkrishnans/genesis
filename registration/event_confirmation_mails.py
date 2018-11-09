from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages

#sends the event confirmation mail to both the team email and the user email, unless they are the same. if they are the same, only one email is sent
def event_confirmation_mail(event_name,email,request,email2=False,email3=False,email4=False,name2=False,name3=False,name4=False,):
    #email confirmation
    base_location = "{0}://{1}".format(request.scheme, request.get_host())
    subject = event_name + " Registration Successful"
    name = str(request.user)
    tempName = ""
    html_content = render_to_string('registration/email_templates/event_registered.html', {'event_name':event_name,'base_location':base_location,'name':name}) # render with dynamic value
    #for text version of mail
    text_content = '''\n
                    Hello, {2}.
                    \n\n
                    You have successfully registered for {3}
                    \n\n Best wishes,
                    \n Pravega Team.
                    '''.format(request.scheme, request.get_host(),name,event_name)
    success=True
    try:
        msg1 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [request.user.email])
        msg1.attach_alternative(html_content, "text/html")
        msg1.send()
        if email != request.user.email:
            msg2 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [email])
            msg2.attach_alternative(html_content, "text/html")
            msg2.send()
        if email2:
            if (email2 != request.user.email) and (email2 != email):
                msg3 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [email2])
                if name2:
                    tempName = name2
                else:
                    tempName = name
                html_content = render_to_string('registration/email_templates/event_registered.html', {'event_name':event_name,'base_location':base_location,'name':tempName}) # render with dynamic value
                msg3.attach_alternative(html_content, "text/html")
                msg3.send()
        if email3:
            if (email3 != request.user.email) and (email3 != email):
                msg4 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [email3])
                if name3:
                    tempName = name3
                else:
                    tempName = name
                html_content = render_to_string('registration/email_templates/event_registered.html', {'event_name':event_name,'base_location':base_location,'name':tempName}) # render with dynamic value
                msg4.attach_alternative(html_content, "text/html")
                msg4.send()
        if email4:
            if (email4 != request.user.email) and (email4 != email):
                msg5 = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [email4])
                if name4:
                    tempName = name4
                else:
                    tempName = name
                html_content = render_to_string('registration/email_templates/event_registered.html', {'event_name':event_name,'base_location':base_location,'name':tempName}) # render with dynamic value
                msg5.attach_alternative(html_content, "text/html")
                msg5.send()
    except:
        success=False
        messages.add_message(request, messages.INFO, 'We are facing some difficulty sending the confirmation mail.')

    return success
