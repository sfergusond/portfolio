# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:37:03 2020

@author: sferg
"""
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class Contact(forms.Form):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'First'
      }
    ),
    label='Name',
    required=True
  )

  last_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'Last'
      }
    ),
    label='',
    required=False
  )

  email = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
        'type': 'email',
      }
    ),
    label=f'Email',
    required=True
  )

  message = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control shadow-sm'
      }
    ),
    label='Message',
    required=True
  )

  captcha = ReCaptchaField(
    widget=ReCaptchaV2Invisible(
      attrs={
        'data-theme': 'dark',
      }
    )
  )

class Hire(forms.Form):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'First'
        }
    ),
    label='Name',
    required=True
  )

  last_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'Last'
      }
    ),
    label='',
    required=True
  )

  email = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
        'type': 'email',
      }
    ),
    label=f'Email',
    required=True
  )

  title = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control shadow-sm',
      }
    ),
    label='Project Title',
    required=True
  )

  budget = forms.IntegerField(
    widget=forms.NumberInput(
      attrs={
        'class': 'form-control shadow-sm'
      }
    ),
    label='Proposed Budget',
    required=True
  )

  payment_type = forms.ChoiceField(
    widget=forms.Select(
      attrs={
        'class': 'form-control shadow-sm'
      }
    ),
    choices=[('hourly', 'Hourly'), ('fixed', 'Fixed Price')],
    label='',
    required=True
  )

  deadline = forms.DateField(
    widget=forms.DateInput(
      attrs={
        'class': 'form-control shadow-sm',
        'type': 'date',
        'placeholder': 'DD/MM/YYYY'
      }
    ),
    label='Deadline',
    required=False
  )

  description = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control shadow-sm'
      }
    ),
    label='Project Description',
    required=True
  )

  #captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)