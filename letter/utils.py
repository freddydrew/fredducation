from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from subscriber.models import subscriber
import queue

def sendEmail(object):
    from_email = 'slickfredwin@gmail.com'

    to = [from_email]
    for obj in subscriber.objects.all():
        to.append(obj.email)

    context = {
        'object': object
        }
    html_message = render_to_string('letter/letter.html', context=context)
    plain_message = strip_tags(html_message)
    
    mail.send_mail(
        object.title, 
        plain_message, 
        from_email, 
        to, 
        html_message=html_message
        )
    
def sendNewsLetter(object):

    # Building the queue of email address of subscribers
    mailQueue = queue.Queue()
    for obj in subscriber.objects.all():
        mailQueue.put(obj.email)

    while mailQueue.empty() != True:
        from_email = 'slickfredwin@gmail.com'
        to = None
        bcc = [from_email]
        count = 0
        while count < 15 and mailQueue.empty() != True:
            bcc.append(mailQueue.get())
            count += 1

        context = {
            'object': object
            }
        html_message = render_to_string('letter/letter.html', context=context)
        plain_message = strip_tags(html_message)
        
        mail.send_mail(
            object.title, 
            plain_message, 
            from_email, 
            bcc,
            html_message=html_message
            )