from django import forms
from .models import Comment, Reply, EmailPush
from .fields import SimpleCaptchaField

class PostSearchForm(forms.Form):

    key_word = forms.CharField(
        label='検索キーワード'
        required=False,
    )


class CommentCreateForm(forms.ModelForm):

    captcha = Simple

    class Meta:
        model = Comment
        exclude = ('target', 'created_at')
        widgets = {
            'text': forms.Textarea
        }


class ReplyCreateForm(forms.ModelForm):

    class Meta:
        model = Reply
        exclude = ('target', 'created_at')
        widgets = {
            'text': forms.Textarea
        }

class EmailForm(forms.ModelForm):

    class Meta:
        model = EmailPush
        fields = ('mail',)
        widgets = {
            'mail': forms.EmailInput(attrs={'placeholder': 'メールアドレス'})
        }
        error_messages = {
            'mail': {
                'unique': 'メールアドレスは登録済みです！',
            }
        }

    def clean_email(self):
        mail = self.cleaned_data['mail']
        EmailPush.objects.filter(mail=mail, is_active=False).delete()
        return
