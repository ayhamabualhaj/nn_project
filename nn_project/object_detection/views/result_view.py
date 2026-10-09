from django.shortcuts import render, get_object_or_404

from object_detection.models import Prediction


def result_view(request, pk):
    # Find the prediction with this id, or show a 404 page if it doesn't exist.
    prediction = get_object_or_404(Prediction, pk=pk)

    # Grab the 10 most recent predictions for a little history table.
    history = Prediction.objects.order_by("-created_at")[:10]

    return render(
        request,
        "object_detection/result.html",
        {"prediction": prediction, "history": history},
    )