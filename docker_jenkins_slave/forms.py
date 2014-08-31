from django import forms

class DockerfileRequestForm(forms.Form):
    OSs = (
        ('centos6', 'CentOS 6'),
        ('centos5', 'CentOS 5'),
        ('centos5', 'SUSE')
        )
    os = forms.ChoiceField(label='OS', choices=OSs)
