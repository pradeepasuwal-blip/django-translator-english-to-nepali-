from django.shortcuts import render
from deep_translator import GoogleTranslator
from rest_framework.decorators import api_view
from rest_framework.response import Response

# HTML form view
def home(request):
    translation = ""
    if request.method == "POST":
        text = request.POST.get("translate")
        translation = GoogleTranslator(source="en", target="ne").translate(text)
    return render(request, "main/index.html", {"translation": translation})

# REST API view using deep_translator
@api_view(["POST"])
def translate_api(request):
    text = request.data.get("text", "")
    target = request.data.get("target", "ne")  # default Nepali
    if not text:
        return Response({"error": "No text provided"}, status=400)

    translation = GoogleTranslator(source="en", target=target).translate(text)
    return Response({"translated": translation})


