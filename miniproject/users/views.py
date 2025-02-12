from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

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

def logout_view(request):
    response = Response({"message": "Logged out successfully"})
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response