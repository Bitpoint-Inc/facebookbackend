from django.shortcuts import render
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.views import APIView, csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny

from .forms import UserCreationForm

class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"message": "Successfully logged in"})


@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(APIView):
    permission_classes = (AllowAny,)

    form = UserCreationForm
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            return Response({"message": f"Successfully created"})
        return Response({"message": "Not created"})