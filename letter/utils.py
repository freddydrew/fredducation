from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def sendLetter():

    object = '**hello** [freddy](https://www.fredducation.co/) this is a test'
    subject = 'test'
    html_message = render_to_string('/home/freddy/Desktop/myBlog/templates/letter/letter.html', {'object': object})
    plain_message = strip_tags(html_message)
    to = ['freddydrew@gmail.com','justinkoebele@gmail.com','daliayan5@gmail.com']
    from_email = 'slickfredwin@gmail.com'

    mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)