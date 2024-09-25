from django import forms

class CalorieForm(forms.Form):
    # Weight field with options for kg or lbs
    WEIGHT_CHOICES = [
        ('kg', 'Kilograms'),
        ('lbs', 'Pounds'),
    ]
    weight = forms.FloatField(label='Weight', required=True)  # General weight field
    weight_unit = forms.ChoiceField(label='Weight Unit', choices=WEIGHT_CHOICES)  # Unit for weight

    # Height fields with options for cm or ft + inches
    HEIGHT_CHOICES = [
        ('cm', 'Centimeters'),
        ('ft', 'Feet'),
    ]
    height = forms.FloatField(label='Height', required=True)  # General height field
    inches = forms.FloatField(label='Inches', required=False)  # Inches field, not required by default
    height_unit = forms.ChoiceField(label='Height Unit', choices=HEIGHT_CHOICES)  # Unit for height

    age = forms.IntegerField(label='Age', required=True)  # Age field
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')], required=True)
    activity = forms.ChoiceField(label='Activity Level', choices=[
        (1.2, 'Sedentary'),
        (1.375, 'Lightly active'),
        (1.55, 'Moderately active'),
        (1.725, 'Very active'),
        (1.9, 'Super active')
    ], required=True)
