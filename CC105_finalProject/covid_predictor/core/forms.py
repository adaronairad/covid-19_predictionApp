from django import forms

class PredictionForm(forms.Form):
    none_symptom = forms.BooleanField(required=False, label="None Symptom")
    fever = forms.BooleanField(required=False, label="Fever")
    tiredness = forms.BooleanField(required=False, label="Tiredness")
    dry_cough = forms.BooleanField(required=False, label="Dry Cough")
    difficulty_in_breathing = forms.BooleanField(required=False, label="Difficulty in Breathing")
    sore_throat = forms.BooleanField(required=False, label="Sore Throat")
    pains = forms.BooleanField(required=False, label="Pains")
    nasal_congestion = forms.BooleanField(required=False, label="Nasal Congestion")
    runny_nose = forms.BooleanField(required=False, label="Runny Nose")
    diarrhea = forms.BooleanField(required=False, label="Diarrhea")
    
