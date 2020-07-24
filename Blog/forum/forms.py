from django import forms
from . models import Discussions
from crispy_forms.helper import FormHelper
from captcha.fields import ReCaptchaField
from ckeditor.widgets import CKEditorWidget

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class DiscussionForm(forms.ModelForm):

    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
        attrs={
            
            
            'required' : 'required',
        }
    )
    )

    class Meta:
        model = Discussions
        fields = ['title','discussion','tags','captcha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False   