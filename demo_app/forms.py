from django import forms


DATE_INPUT_FORMATS = ['%b %d, %Y', '%B %d, %Y']
TIME_INPUT_FORMATS = ['%H:%M %p', '%I:%M %p']
DATETIME_INPUT_FORMATS = ['%b %d, %Y %H:%M %p']


class BasicForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    checks = forms.MultipleChoiceField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three')])
    date_value = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), input_formats=DATE_INPUT_FORMATS)
    time_value = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}), input_formats=TIME_INPUT_FORMATS)
    datetime_value = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'datetimepicker'}), input_formats=DATETIME_INPUT_FORMATS)

    # check_value = forms.BooleanField()  # Does not show. Needs span

    # ===== BELOW DOES NOT WORK!!!!! =====
    # class Meta:
    #     widgets = {
    #         'datetime_value': forms.TextInput(attrs={'class': 'datepicker'}),
    #         }
