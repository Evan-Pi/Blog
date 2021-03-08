from django import forms
from . models import Articles, Comments, SubComments
from crispy_forms.helper import FormHelper
from froala_editor.widgets import FroalaEditor

class EditArticleForm(forms.ModelForm):
    article = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Articles
        fields = '__all__'



class CommentsForm(forms.ModelForm):

    text = forms.CharField(label='text', widget=FroalaEditor(plugins=('fullscreen','align','emoticons','link','char_counter','table',)))
    class Meta:
        model = Comments
        fields = ['article','author','text']

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['article'].label = False
        self.fields['author'].label = False
        self.fields['text'].label = False


        



class SubCommentsForm(forms.ModelForm):
    text = forms.CharField(label='text', widget=FroalaEditor(plugins=('fullscreen','align','emoticons','link','char_counter','table',)))
    class Meta:
        model = SubComments
        fields = ['comment','author','text']

    def __init__(self, *args, **kwargs):
        super(SubCommentsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['comment'].label = False
        self.fields['author'].label = False
        self.fields['text'].label = False

