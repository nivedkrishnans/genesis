import os

def start():
    name_short=input("name short form: ")
    lname=input("capital full name: ")
    sname_code=input("non capitalized name for the code: ")
    lname_code=input("capitalized name for the code: ")

    urlChange(sname_code)
    adminChange(lname_code)
    formsChange(lname_code)
    modelsChange(lname_code)
    viewsChange(lname,sname_code,lname_code)
    htmlChange(name_short,lname,sname_code,lname_code)

def lineNo(text,look):
    ret=0
    for line in text:
        ret+=1
        flag=True
        for i in look:
            if i not in line:
                flag=False
                break
        if flag:
            return ret


def urlChange(sname_code):
    f = open("urls.py", "r")
    contents = f.readlines()
    f.close()
    valueUrls='''    url(r'^'''+sname_code+'''$', views.'''+sname_code+'''Registration, name='''+"'"+sname_code+'''Registration'),
    url(r'^'''+sname_code+'''/$', views.'''+sname_code+'''Registration, name='''+"'"+sname_code+'''Registration'),\n'''
    
    contents.insert(lineNo(contents,["urlpatterns","="]), valueUrls)

    f = open("urls.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def adminChange(lname_code):
    f = open("admin.py", "r")
    contents = f.readlines()
    f.close()
    valueAdmin='''class '''+lname_code+'''RegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'full_name' ,'email','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = '''+lname_code+'''Registration\n
'''

    contents.insert(lineNo(contents,["class PISRegistrationResource(ExportMixin,admin.ModelAdmin):"])-1, valueAdmin)

    f = open("admin.py", "w")
    contents = "".join(contents)
    contents+='''admin.site.register('''+lname_code+'''Registration,'''+lname_code+'''RegistrationResource)'''

    f.write(contents)
    f.close()

def formsChange(lname_code):
    f = open("forms.py", "r")
    contents = f.readlines()
    f.close()
    valueForms='''class '''+lname_code+'''Form(forms.ModelForm):
    class Meta:
        model = '''+lname_code+'''Registration
        fields = ('full_name','institution','city','email','contact','howyouknow')
        labels = {
            "full_name": "Full Name",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact": "Mobile Number",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
            }

'''

    contents.insert(lineNo(contents,["class PISForm(forms.ModelForm):"])-1, valueForms)

    f = open("forms.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def modelsChange(lname_code):
    f = open("models.py", "r")
    contents = f.readlines()
    f.close()
    valueModels='''class '''+lname_code+'''Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details

    #user details
    full_name =  models.CharField(max_length=127)
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20)

    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return str(self.user)\n
'''

    contents.insert(lineNo(contents,["class PISRegistration(models.Model):"])-1, valueModels)

    f = open("models.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def viewsChange(lname,sname_code,lname_code):
    f = open("views.py", "r")
    contents = f.readlines()
    f.close()

    valueViews='''def '''+sname_code+'''Registration(request):

    thisEvent = get_object_or_404(AdminEvent, title='''+"'"+sname_code+"'"+''')
    initialValues={}
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations ='''+lname_code+'''Registration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if thisUserData:
                initialValues={"institution": thisUserData.institution,
                "city":thisUserData.city ,
                "email": thisUserData.email,
                "contact": thisUserData.contact}
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = '''+lname_code+'''Form(initial=initialValues,instance=thisInstance)
                    if request.method == "POST":
                        f = '''+lname_code+'''Form(request.POST, request.FILES,instance=thisInstance,initial=initialValues )
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('''+"'"+lname+"'"+''',request.POST['email'],request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your '''+lname+''' Event Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your '''+lname+''' Event Registration Form')
                                f ='''+lname_code+'''Form(initial=initialValues,instance=thisInstance)
                                return render(request, 'registration/'''+sname_code+'''Registration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = '''+lname_code+'''Form(request.POST, request.FILES,initial=initialValues )
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user

                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('''+"'"+lname+"'"+''',thisUserData.email,request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your '''+lname+''' Event Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your '''+lname+''' Event Registration Form')
                            return render(request, 'registration/'''+sname_code+'''Registration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = '''+lname_code+'''Form(initial=initialValues)
            return render(request, 'registration/'''+sname_code+'''Registration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the '''+lname+"'"+''')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})\n
'''

    contents.insert(lineNo(contents,["def pisRegistration(request):"])-1, valueViews)
    string='''      '''+"'"+sname_code+"':"+lname_code+'''Registration,\n'''
    contents.insert(lineNo(contents,["eventDictionary",'=']),string)

    f = open("views.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def htmlChange(name_short,lname,sname_code,lname_code):
    directory=os.path.join("templates/registration/",sname_code+"Registration.html")
    #directory=directory[:22]+sname_code+directory[22:]

    f=open(directory,'w+')
    valueHtml='''
{% extends 'base.html' %}
<!DOCTYPE html>
{% load staticfiles %}

{% block head %}
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{%static 'css/style.css'%}">
    <link rel="stylesheet" href="{%static 'css/hamburger.css'%}">
    <link rel="icon" href="{%static 'img/logo-gold.gif'%}">

    <title>''' + name_short+''' Registration | Pravega 2019, IISc Bangalore</title>
    <link href="https://fonts.googleapis.com/css?family=Overlock+SC|Raleway:300,400|Titillium+Web" rel="stylesheet">
    <link rel="stylesheet" href="{%static 'css/reg.css'%}">
{% endblock %}

{% block content %}
    <div id="main">
        <div class="heading">'''+lname+''' Registration</div>
        {% if user.is_authenticated %}
          <p>Hi {{ user }}!</p>
          {% if form.errors %}
              <div class="errors">
                  <p>Please fix the following errors</p>
                  <ul>
                      {% for field in form %}
                          {% if field.errors %}
                              {% for error in field.errors %}
                                  <li>{{ error|escape }}</li>
                              {% endfor %}
                          {% endif %}
                      {% endfor %}
                  </ul>
                  {% if form.non_field_errors %}
                      {{ form.non_field_errors }}
                  {% endif %}
              </div>
          {% endif %}
          {% if messages %}
              <div class="messages">
                  <ul>
                  {% for message in messages %}
                      <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
                  {% endfor %}
                  </ul>
              </div>
          {% endif %}
          <p>View the complete details of this event <a href="{% url '''+"'"+sname_code+"Registration'"+'''%}">here</a>.</p>
          <p><a href="{% url 'registration'%}">Click here</a> to go back to the registrations index page.</p>
          <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {% for field in form %}

                <div class="field-space">
                    {{ field.errors }}
                    {{ field.label_tag }}
                    {{ field }}
                </div>
            {% endfor %}
            <div class="messages">
                <p style="margin-bottom:14px;">Important:</p>
                <ul>
                    <li>You have two options, 'save' and 'submit'.</li>
                    <li>If you click save, you will be able to edit the form until you click submit or until the event registration closes, WHICHEVER COMES FIRST.</li>
                    <li>Once you click submit, YOU WILL NOT BE ABLE TO EDIT THE FORM.</li>
                </ul>
            </div>
            <div class="buttonCollection">
                <button type="submit" name="save" value="save">Save</button>
                <button type="submit" name="submit" value="submit">Submit</button>
            </div>
          </form>
        {% else %}
            <p>You have to log in to register for '''+lname+'''</p><br>
            Have an account? <a href="{% url 'login' %}">Click here to Log in</a><br>
            Don't have an account? <a href="{% url 'signup' %}">Click here to sign up</a><br>

        {% endif %}


    </div>

    <script src="{%static 'js/navBar.js'%}"> </script>
{% endblock %}
'''
    f.write(valueHtml)
    f.close()

start()

