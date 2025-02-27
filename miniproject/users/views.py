from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.shortcuts import redirect, render 
from .forms import RegistrationForm
from .models import User
from rest_framework.decorators import api_view, renderer_classes

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data["access"]
            refresh_token = response.data["refresh"]
            res = Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            res.set_cookie(
                key="access_token", 
                value=access_token, 
                httponly=True, 
                secure=True,
                samesite="Lax"
            )
            res.set_cookie(
                key="refresh_token", 
                value=refresh_token, 
                httponly=True, 
                secure=True,
                samesite="Lax"
            )
            return res
        return response

@api_view(('GET',))
def logout_view(request):
    response = Response({"message": "Logged out successfully"})
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response


def user_registration(request): 
    if request.method == "POST": 
        form = RegistrationForm(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username'] 
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('/login')
    else: 
        form = RegistrationForm() 
    return render(request, 'users/contact.html', {'form': form})

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        return render(request, 'users/profile.html', {'user': user})
    
    def post(self, request):
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            user = request.user
            user.profile_picture = profile_picture
            user.save()
        return redirect('profile')