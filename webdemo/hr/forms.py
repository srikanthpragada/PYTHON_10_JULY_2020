import django.forms as forms


class EmployeeForm(forms.Form):
    # Fields
    name = forms.CharField(label='Name', max_length=30)
    job = forms.CharField(label='Job', max_length=10)
    salary = forms.IntegerField(label='Salary')
