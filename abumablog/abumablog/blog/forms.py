from django import forms
from .models import Comment, Reply

class PostSearchForm(forms.Form):

    key_word = forms.CharField(
        label='検索キーワード'
        required=False,
    )


class CommentCreateForm(forms.ModelForm):

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
