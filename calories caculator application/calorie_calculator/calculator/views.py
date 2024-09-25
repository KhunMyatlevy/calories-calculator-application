from django.shortcuts import render
from .forms import CalorieForm

def calculator_view(request):
    calories = None  # Initialize calories variable to None

    if request.method == 'POST':
        form = CalorieForm(request.POST)  # Create form instance with submitted data
        if form.is_valid():
            # Get values from the form
            weight = form.cleaned_data['weight']  # General weight
            weight_unit = form.cleaned_data['weight_unit']  # Weight unit (kg or lbs)
            height = form.cleaned_data['height']  # General height
            height_unit = form.cleaned_data['height_unit']  # Height unit (cm or ft)
            inches = form.cleaned_data['inches']  # Inches
            age = form.cleaned_data['age']  # Age
            gender = form.cleaned_data['gender']  # Gender
            activity_level = float(form.cleaned_data['activity'])  # Activity level
            
            # Convert weight to kg if it's in lbs
            if weight_unit == 'lbs':
                weight = weight * 0.453592  # Convert lbs to kg

            # Convert height to cm if it's in feet
            if height_unit == 'ft':
                # Calculate height in cm (feet to cm) + (inches to cm)
                height = (height * 30.48) + (inches * 2.54)  # Convert feet and inches to cm
            elif height_unit == 'cm':
                # If the height is already in cm, just keep it
                height = height  

            # Debugging output to check values
            print(f'Weight: {weight} kg, Height: {height} cm, Age: {age}, Gender: {gender}, Activity Level: {activity_level}')

            # Calculate BMR
            if gender == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            # Calculate maintenance calories
            calories = bmr * activity_level
    else:
        form = CalorieForm()  # Create an empty form if not a POST request

    # Render the calculator template
    return render(request, 'calculator.html', {'form': form, 'calories': calories})
