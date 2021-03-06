# from allauth.account.adapter import get_adapter
# from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
# from rest_framework.authtoken.models import Token
#
from .models import User
#
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_customer', 'is_worker')

#
# class CustomRegisterSerializer(RegisterSerializer):
#     is_customer = serializers.BooleanField()
#     is_worker = serializers.BooleanField()
#
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password', 'is_customer', 'is_worker')
#
#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'password2': self.validated_data.get('password2', ''),
#             'email': self.validated_data.get('email', ''),
#             'is_customer': self.validated_data.get('is_customer', ''),
#             'is_worker': self.validated_data.get('is_worker', '')
#         }
#
#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         user.is_customer = self.cleaned_data.get('is_customer')
#         user.is_worker = self.cleaned_data.get('is_worker')
#         user.save()
#         adapter.save_user(request, user, self)
#         return user
#
#
