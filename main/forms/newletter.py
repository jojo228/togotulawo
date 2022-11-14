from django import forms
from main.models import Subscribers, MailMessage
from main.models.article import Article


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'


class CustomerMailing(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'subtitle')
