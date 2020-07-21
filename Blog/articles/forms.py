from django import forms
from . models import Comments, SubComments
from crispy_forms.helper import FormHelper

class CommentsForm(forms.ModelForm):
    text = forms.CharField(label='text', widget=forms.Textarea(attrs={'placeholder': 'Type your comment here...'}))
    class Meta:
        model = Comments
        fields = ['article','author','text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class SubCommentsForm(forms.ModelForm):
    text = forms.CharField(label='text', widget=forms.Textarea(attrs={'placeholder': 'Type your respond here...'}))
    class Meta:
        model = SubComments
        fields = ['comment','author','text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

