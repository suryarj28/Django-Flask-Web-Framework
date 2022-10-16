from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Please start with letter 'z' ")


class Form_name(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean_data(self):
        all_clean = super().clean()
        email = all_clean["email"]
        vmail = all_clean["verify_email"]

        if email != vmail:
            raise forms.ValidationError("make sure both emails are same")

    def __init__(self, *args, **kwargs):
        super(Form_name, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
