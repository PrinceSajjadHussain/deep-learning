from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
import tensorflow as tf
import numpy as np
import pickle
from PIL import Image
import os

# Load the model
with open(os.path.join(settings.BASE_DIR, 'fashion_mnist_model.pkl'), 'rb') as model_file:
    model = pickle.load(model_file)

def home(request):
    return render(request, 'mlapp/home.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        file_path = default_storage.save(os.path.join('images', image.name), image)
        file_url = default_storage.url(file_path)

        # Preprocess the uploaded image
        img = Image.open(os.path.join(settings.MEDIA_ROOT, file_path)).convert('L')
        img = img.resize((28, 28))
        img = np.array(img) / 255.0
        img = img.reshape(-1, 28*28)

        # Predict the class of the image
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction, axis=1)[0]
        classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
        predicted_label = classes[predicted_class]

        return render(request, 'mlapp/upload.html', {
            'predicted_label': predicted_label,
            'image_url': file_url
        })

    return render(request, 'mlapp/upload.html')
