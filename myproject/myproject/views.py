from django.shortcuts import render
from .forms import ImageUploadForm
from .model import model # Import your model
import numpy as np

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            processed_image = preprocess_image(uploaded_image)
            result = model.predict(processed_image)
            predicted_label = np.argmax(result)
            return render(request, 'result.html', {'predicted_label': predicted_label})
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})
