from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PredictionForm
from .ml_model.predict import predict_result
from django.shortcuts import render
import json

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def predict_view(request):
    prediction = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Collecting the data from the form (converted to integers for Boolean fields)
            cd = form.cleaned_data
            input_data = [
                int(cd['none_symptom']),
                int(cd['fever']),
                int(cd['tiredness']),
                int(cd['dry_cough']),
                int(cd['difficulty_in_breathing']),
                int(cd['sore_throat']),
                int(cd['pains']),
                int(cd['nasal_congestion']),
                int(cd['runny_nose']),
                int(cd['diarrhea']),
            ]

            # Making prediction
            result = predict_result(input_data)
            
            #prediction = "COVID Positive" if result == 1 else "COVID Negative"
            prediction = "COVID-19 Positive" if result == "COVID-19 Positive" else "COVID-19 Negative"
    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form, 'prediction': prediction})

@login_required
def dashboard_view(request):
    # Example data
    total_records = "316,800"
    total_features = 10
    target_distribution = "85.51% Positive,14.49% Negative"
    model_accuracy = "85.48"
    confusion_matrix = [[9199, 0], [7655, 46506]]

    # Data for charts
    target_labels = ['85.51% Positive', '14.49% Negative']
    target_data = [85.51, 14.49]
    performance_labels = ['Jan', 'Feb', 'Mar', 'Apr']
    performance_data = [85, 88, 90, 92.5]

    context = {
        'total_records': total_records,
        'total_features': total_features,
        'target_distribution': target_distribution,
        'model_accuracy': model_accuracy,
        'confusion_matrix': json.dumps(confusion_matrix),
        'target_labels': json.dumps(target_labels),
        'target_data': json.dumps(target_data),
        'performance_labels': json.dumps(performance_labels),
        'performance_data': json.dumps(performance_data),
    }
    return render(request, 'dashboard.html', context)
