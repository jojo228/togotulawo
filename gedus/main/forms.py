from django import forms
from main.models.article import Comment
from main.models import Subscribers, MailMessage
from main.models.article import Article



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rate']





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


from entreprise.models import Postuler


class PostuleForm(forms.ModelForm):
    class Meta:
        model = Postuler
        fields = ['nom_du_candidat', 'prenom_du_candidat', 'contact_du_candidat', 'email_du_candidat', 'motivation_du_candidat',]


        widgets = {
            'nom_du_candidat': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_du_candidat': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_du_candidat': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_du_candidat': forms.EmailInput(attrs={'class': 'form-control'}),
            
        }

        labels = {
            "motivation_du_candidat": "Motivation",
            "nom_du_candidat": "Nom",
            "prenom_du_candidat": "Prénoms",
            "contact_du_candidat": "Contact",
            "email_du_candidat": "Email",
            
        }