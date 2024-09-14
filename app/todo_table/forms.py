from django import forms
from app.todo_table.models import TemaModels
from app.users.models import GroupUsers


# class ChooseGroup(forms.Form):
#     group = forms.ChoiceField(choices=[])
#     team = forms.ChoiceField(choices=[])

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#         groups = user.groupysers.all()
#         team = user.gro
#         self.fields['group'] = [(group, group.name)  for group in groups]
#         self.fields['nam']