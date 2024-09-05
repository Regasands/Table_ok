from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from crispy_forms.layout import Layout, Row, Div, HTML, Submit, Button
from crispy_forms.helper import FormHelper
from app.users.models import GroupUsers

class UpdateFormsGroupUsers(forms.ModelForm):
    '''
    Обновление настроек группы
    '''
    group_user = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Удалить участников  группы'
    )
    admin_user = forms.ModelChoiceField(
        label='Назначить администратора группы',
        queryset=User.objects.all(),
        widget=forms.RadioSelect,
        required=False,
    )

    class Meta:
        model = GroupUsers
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['group_user'].queryset = self.instance.group_user.all()
            self.initial['group_user'] = []
            self.fields['admin_user'].queryset = self.instance.group_user.all()

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Row('group_user'),
                Row('name'),
                Row('description'),
                Row('admin_user'),
                Row(
                    Submit('submit', 'Отправить', css_class='col-2'),
                    Button(
                        'button',
                        'Назад',
                        css_class='btn btn-secondary col-2',
                        onclick='window.history.back()'
                        ),
                    css_class='d-flex gap-4 mx-auto justify-content-center'
                    ),
                css_class='form_block'
            )
        )
        
    def clean(self):
        cleaned_data = super().clean()
        admin_user = self.cleaned_data.get('admin_user')
        admin_last_user = self.instance.admin_user
        group_user = self.cleaned_data.get('group_user', [])
        if admin_user:
            if admin_user in group_user:
                raise forms.ValidationError({'group_user': 'Администратора нельзя удалить из группы!'})
        else:
            if admin_last_user in group_user:
                raise forms.ValidationError({'group_user':'Администратора нельзя удалить из группы!'})
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'group_user' in self.cleaned_data:
            users_to_remove = self.cleaned_data['group_user']
            instance.group_user.remove(*users_to_remove)
        if commit:
            instance.save()
        return instance

    