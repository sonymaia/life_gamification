from django import forms
from record.models import Daily_Objective
from datetime import datetime
from record.core import daily_goals_check
from record.models import Category


class DailyRecordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        daily_objectives = Daily_Objective.objects.all()
        current_date = datetime.now().strftime('%Y-%m-%d')

        dict_daily_goals = daily_goals_check(user=self.user, date=current_date)

        # Adicione os campos do modelo ao formulário
        for daily_objective in daily_objectives:
            field_attrs_checkbox = {
                'class': 'form-check-input', 'id': daily_objective.id}
            self.fields[daily_objective.name] = forms.BooleanField(
                required=False,
                widget=forms.CheckboxInput(attrs=field_attrs_checkbox),
                label=daily_objective.name,
                initial=dict_daily_goals[daily_objective.id]
            )

        # Adicione os campos adicionais ao formulário
        field_attrs_date = {'type': 'date',
                            'class': 'form-control', 'id': 'date'}
        self.fields['date'] = forms.DateField(widget=forms.DateInput(
            attrs=field_attrs_date), label='Date', initial=current_date)


class CategoryRecordForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select'}),
                                      empty_label=None,
                                      required=True)

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                           initial=datetime.now().strftime('%Y-%m-%d'),
                           required=True)

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
                                  required=True)


