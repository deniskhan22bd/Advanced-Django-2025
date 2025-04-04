from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserRegistrationSerializer, PasswordResetSerializer
from dj_rest_auth.registration.views import RegisterView

class CustomRegisterView(RegisterView):
    serializer_class = UserRegistrationSerializer

# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data["access"]
            refresh_token = response.data["refresh"]
            res = Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
            res.set_cookie(
                key="access_token", 
                value=access_token, 
                httponly=True, 
                secure=True,
                samesite="None"
            )
            res.set_cookie(
                key="refresh_token", 
                value=refresh_token, 
                httponly=True, 
                secure=True,
                samesite="None"
            )
            return res
        return response
    

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response(
                {"detail": "Refresh token cookie not found."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        request.data['refresh'] = refresh_token
        
        response = super().post(request, *args, **kwargs)
        access_token = response.data['access']
        res = Response({"detail": "Token Refreshed successful"}, status=status.HTTP_200_OK)
        res.set_cookie(
            key="access_token", 
            value=access_token, 
            httponly=True, 
            secure=True,
            samesite="None"
        )
        
        return res
    

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        return Response({"detail": request.data.get('hello')}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    response = Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response

@api_view(['POST'])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"detail" : "User created"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def reset_password(request):
    serializer = PasswordResetSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)