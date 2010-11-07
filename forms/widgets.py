# -*- coding: utf-8 -*-
""" widgets alternatifs et utiles pour le projet """
from django.forms import DateInput

class DatePickerInput(DateInput):

    def __init__(self, attrs=None, format=None):
        self.attrs = {'class': 'datepicker'}
        if attrs:
            self.attrs.update(attrs)
        super(DatePickerInput, self).__init__(self.attrs, format)
