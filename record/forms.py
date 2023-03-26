from django import forms
from record.models import Daily_Objective
from datetime import date

class DailyRecordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        daily_objectives = Daily_Objective.objects.all()
         # Adicione os campos do modelo ao formulário
        for daily_objective in daily_objectives:
            self.fields[daily_objective.name] = forms.BooleanField(
                                                                required= False, 
                                                                widget= forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                                                                label= daily_objective.name
                                                                )

    # Adicione os campos adicionais ao formulário
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), label= 'Date', initial=date.today().strftime('%Y-%m-%d'))
    

