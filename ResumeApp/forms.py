from django import forms
from.models import ResumeModel

# value - label
gender_choices = [("male","male"),("female", 'female'), ('other', 'other')]

city_choics = [("Thane", 'Thane'), ("vashi", 'vashi'), ("kurla",'kurla')]

state_choices = [("Maharashtra","Maharashtra"), ("Mp", "Mp"), ("up", "up")]

language_choices = [("Hindi", 'Hindi'), ("Marathi", "Marathi"), ("english", "english"), ('gujrati', 'gujrati'), ("tamil", "tamil")]

prog_lang_choices = [('C#', 'C#'), ("C", "C"), ("C++", "C++"),("Java", "java"), ("Python", "Python"), ('Asp.net', 'Asp.net')]

#education_choices = [("BSC", "BSC"), ('BSC-IT',"BSC-IT"), ("BE", "BE"), ("BCom", 'BCome'), ("BSC-CS", "BSC-CS")]

preferred_loc_choices = [('Vashi', "vashi"),("Thane", 'Thane'), ("Kurla", "kurla"), ("kalyan", "kalyan")]



class ResumeForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=gender_choices, label = "Gender", widget = forms.RadioSelect)
    city = forms.ChoiceField(choices=city_choics, label='Select city', widget=forms.Select(attrs={'class':'form-control'}))
    state = forms.ChoiceField(choices=state_choices, label = "State", widget= forms.Select(attrs={'class':'form-control'}))

    language = forms.MultipleChoiceField(choices=language_choices, label = "Select Language", widget= forms.CheckboxSelectMultiple)

    programming_language= forms.MultipleChoiceField(choices=prog_lang_choices, label = 'Select Programming Language', widget=forms.CheckboxSelectMultiple)

    #education = forms.ChoiceField(choices=education_choices, label = "Select Education", widget=forms.RadioSelect)

    prefered_loc = forms.ChoiceField(choices=preferred_loc_choices, label = 'Select Preferred Location', widget=forms.Select(attrs={'class':'form-control'}))



    class Meta:
        model = ResumeModel
        fields = ['id','fname','lname','email','contact','gender','dob','city','state','language','programming_language','education','prefered_loc','prof_image','project']

        labels= {
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'email' : 'Email ID',
            'contact' : 'Contact number',
            #'gender' : 'Gender',
            'dob' : 'Date of Birth',
            'city' : 'City',
            'state': 'State',
            'language' : 'Languages',
            'programming_language' : 'Technical Skills',
            'education' : 'Education',
            'prefered_loc' : 'Prefered Location',
            'prof_image' : ' Upload Profile Photo',
            'project' : 'Project'
        }

        widgets = {
            'fname' : forms.TextInput(attrs={"class": "form-control"}),
            'lname' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': "form-control"}),
            'dob' : forms.DateInput(attrs={'class':'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'prof_image' : forms.FileInput(attrs={'class':'form-control'}),
            'project': forms.Textarea(attrs={'class':'form-control'})

            

        }





# for dateinput add jquery datepicker in base.html