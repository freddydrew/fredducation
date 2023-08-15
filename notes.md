**How this blog was created, a memoir**

### Tue Jul 18 10:05:31 AM -05 2023
- **Steps to create a virtual enviroment, activate it, install django in it, then make a django project in it**
    - go to directory
    - type: python3 -m venv .
    - type: source bin/activate
    - type: pip install django
    - type: django-admin startproject freducation .
- **How I moved all important info to an environment variables file**
    - create .env file under myBlog/
    - move all setting.py info and API key info to env file
    - pip install django-dotenv
    - in manage.py
        - import dotenv and pathlib and load env file using read_dotenv()
    - in settings.py load from os.environ 
- **I'm setting up a views.py, a basic base.html, and home page to see if I've correctly established my env file** 
    - I created some basic html files in a templates folder
    - I made a views.py and made a homeView function
    - I imported the homeView function to my urls.py
    - I added the path to my templates in the settings.py folder and after that everything is in order just fine.
- **I'm setting up an admin acount for myself that I can use going forward to interact with the site**
    - python3 manage.py createsuperuser --username USERNAME
        - pretty straigh forward and worked like a charm
- **I'm adding about, contact pages and some base bootstrap 5 styling to everything**
    - So I created some empty html files with some test messages in the mentioned pages that extend the base
    - Then I installed bootstrap5 using pip install django-bootstrap-v5
    - Then I added it under installed apps in settings.py
    - Then I loaded the bootstrap5 tag library, css and JS code into my base.html
    - Then I copy and pasted some boiler plate started code from their site to my base.html that I think suites my needs.
    - I also added some empty views for the contact and the about page.
    - All is working just fine
**I'm moving my contact form over from my other projects that were never realized**
    - first created a forms.py, there wont be many forms on my site, I dont think at least
    - I made a form model including all the things I wanted the person to be able to submit
    - Then I went to settings and entered in all the SMTP (Simple mail transfer protocol) stuff django needs to send mail,
    all that was more or less copied from [here](https://youtu.be/1DcySa35fXw)
    - I also generated an app password through google to send myself the email. This was saved in my env file
    - In my views I imported my new from and passed it in as a piece of the context to the html where I rendered it as a paragraph
    - In the contact html I made a form tag with the POST method and included the csrf token so people can submit stuff
    - In the views I needed to include the request.METHOD if statement that checks if anything has been sent as POST so we know when to call the submit and email function

### Wed Jul 19 10:12:58 AM -05 2023
**Creating the articles app**
    - python3 manage.py startapp articles
    - I added a ton to the model
    - also installed Unidecode so I can handle non-ascii chars 
    - Dropped a copy of a slugify function in the utils.py file I made, I'm going to slugify the titles and move on with my life, easy

### Thu Jul 20 09:47:52 AM -05 2023
**Register the article app**
    - add under installed apps in settings.py
    - register in the admin so I can see it 
    - make the migrations
**Auto Generate Slug**
    - post save function import
    - overwrite default save behavior in the model 
        - checks if anything has been updated, if it has it runs setters from the post save function
**Adding Image with Foreign Key**
    - in virtual env: pip install pillow
    - add new class called article image with foreign key set as article class
    - Under the admin I made a new class which inherits from the stacked inline admin class
        - this is so I can add and remove images to article models as I see fit and don't need to make a set number

### Fri Jul 21 07:04:04 AM -05 2023
**Organizing Templates**
    - changes settings.py to reflect that all templates are now kept at the BASE_DIR level under templates
    - creating a folder specific to article model templates, at the moment it includes allArticles and oneArticle html files
**Setting Up articles app urls**
    - make a urls.py under the articles folder, set up in the same style as that of the freducation folder
        - all paths included for each view will be appeneded onto the 'articles/' path, so they are relative to that
    - under the urls.py included in the freducation folder, I inlcuded the articles.urls file as a path, keeping stuff in the app folder
**Setting up reverse url in article model**
    - the oneArticle view has its own name that can be used to do a reverse lookup
    - I'm creating a fucntion which will return the absolute url of a given article object and its slug
    - I've included the slug as a kwarg in the view and the url
        - typing the slug into the address bar renders the correct page atm
**Setting up all articles view**
    - added a boolean field called publish to filter what posts are ready to go, under the model
    - in the allArticles view I query all posts that are ready to be published and off to the races I go
    - confirmed reverse lookup with slug in address for single articles works
    - on all articles view I can click on single articles and be brought to that oneArticle page
**Setting up basic search**
    - So first on the base.html page, 
        - I included a search form with a action set to the /articles/search/ address.
        - I made the method set to GET
        - I gave the query a name value of q, which will be referenced later in the view
    - Then I set up a search.html 
        - under templates/articles/
        - this will be where the user gets redirected after the search
    - I made the search method under my view
        - from the request it selectes request.GET.get('q')
        - then it uses that to search for matches amongst existing articles and returns the queryset in the context
        - I set up the url routing under articles.urls
    - confirmed it works
**Add pycountry for better slug and search**
    - installed pycountry, upadted requirements
    - wrote setAlpha3 method under model which searches country name, and then applies alpha 3
    - setAlpha3 gets called in post save signal
    - everything works fine still

### Mon Jul 24 09:24:21 AM -05 2023
**Custom model manager search functions**
    - 