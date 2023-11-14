from django.core.mail import EmailMessage 

# Gives me a heads up that a contact form has been submitted
def newContactSubmission(firstName,lastName,emailAddress,subject,message):
        
    from_email='slickfredwin@gmail.com'
    # Email Contents
    body = f'''
    FROM:           {firstName} {lastName}
    EMAIL:          {emailAddress}
    SUBJECT:        {subject}
    MESSAGE:
    {message}
        '''
        
    emailSubject = f"CONTACT FORM: {subject}"
    emailReplyTo = [emailAddress]
    # Send Email
    msg = EmailMessage(
            subject=emailSubject, 
            body=body,
            from_email=from_email,
            to=[from_email],
            reply_to = emailReplyTo)
    msg.send()
