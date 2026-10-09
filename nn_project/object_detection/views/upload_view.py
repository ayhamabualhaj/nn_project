from django.shortcuts import render, redirect

from object_detection.models import Prediction
from object_detection.ml.classifier import classify_image


def upload_view(request):
    # Did the user submit the form WITH an image?
    if request.method == "POST" and request.FILES.get("image"):

        # 1. Save the uploaded image into a new database row.
        #    We save first so the file exists on disk for the network to read.
        prediction = Prediction(image=request.FILES["image"])
        prediction.save()

        # 2. FORWARD PROPAGATION: run the image through the neural network.
        label, confidence = classify_image(prediction.image.path)

        # 3. Store what the network decided.
        prediction.label = label
        prediction.confidence = confidence
        prediction.save()

        # 4. Send the user to the result page for this prediction.
        return redirect("result", pk=prediction.pk)

    # No image yet -> just show the empty upload form.
    return render(request, "object_detection/upload.html")