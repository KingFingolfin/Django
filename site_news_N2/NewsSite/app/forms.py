from django import forms
from .models import Contact, Gmails, Comment


class ContactForm(forms.ModelForm):
    Name = forms.CharField(label="",
                           widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))
    Email = forms.CharField(label="",
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
    Phone = forms.CharField(label="",
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Phone Number"}))
    Subject = forms.CharField(label="",
                              widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}))
    Message = forms.CharField(label="",
                              widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Message"}))

    class Meta:
        model = Contact
        fields = ('Name', 'Email', 'Phone', 'Subject', 'Message')


class GmailsForm(forms.ModelForm):
    Email = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter your email address", "type": "text"}))

    class Meta:
        model = Gmails
        fields = ('Email',)


class CommentForm(forms.ModelForm):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))

    text = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Message"}))

    class Meta:
        model = Comment
        fields = ('username', 'text')
