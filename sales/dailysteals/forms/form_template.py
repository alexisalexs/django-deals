from crispy_forms.helper import FormHelper
from django.forms import forms
from crispy_forms.layout import Column,Div,HTML,Layout,Row
from crispy_forms.bootstrap import StrictButton
from django.conf import Settings
from django.contrib.auth.models import Group
from django.forms import ModelForm, inlineformset_factory, modelformset_factory
from django.urls import reverse
from django.utils.text import format_lazy
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from parsley.decorators import parsleyfy

#
# @parsleyfy
# class ExampleModelForm(ModelForm):
#     def __init__(self, request=None, *args, **kwargs):
#         orgs = kwargs.pop('users_orgs', None)
#         sub_orgs = kwargs.pop('sub_orgs', None)
#         super(ExampleModelForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_action = request.path
#         self.helper.form_method = "POST"
#         self.helper.form_id = "custom_id"
#         self.helper.form_class = ""
#         self.helper.attrs = {"data-parsley-validate": ""}
#
#         self.helper.layout = Layout(
#             Div(
#                 Column("example", css_class="col-md-4"),
#                 css_class='row'
#             ),
#
#             Div(
#                 StrictButton(
#                     'Cancel',
#                     css_class=''
#                 ),
#                 StrictButton('Save', type='submit',
#                              css_class=''
#                              ),
#                 css_class=''
#             )
#         )
#
#     def clean(self):
#
#
#         return cleaned_data
#
#     class Meta:
#         model =
#         fields = (
#
#         )
#         labels = {
#
#         }
#
#
