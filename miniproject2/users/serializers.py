from rest_framework import serializers
from .models import User
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def save(self, request):
        # You can perform any request-specific logic here if needed.
        return self.create(self.validated_data)
    
from rest_framework import serializers

class PasswordResetSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['current_password'] == attrs['new_password']:
            raise serializers.ValidationError("New password must be different from the current password.")
    
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        if not user.check_password(self.validated_data['current_password']):
            raise serializers.ValidationError(
                {'current_password': 'The provided current password is incorrect.'}
            )

        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        return user
