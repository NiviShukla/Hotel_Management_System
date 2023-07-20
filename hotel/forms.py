from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC', 'AC ROOM'),
        ('NAC', 'NON-AC ROOM'),
        ('DEL', 'DELUXE ROOM'),
        ('KIN', 'KING ROOM'),
        ('QUE', 'QUEEN ROOM'),
        ('STE', 'SUITE ROOM'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES , required= True)
    check_in = forms.DateTimeField(required= True, input_formats=["%Y-%m-%dT%H:%M"],widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(required= True, input_formats=["%Y-%m-%dT%H:%M"],widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))