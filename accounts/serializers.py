from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('A user with that username already exists.')
        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('A user with that email already exists.')
        return value

    def validate_password(self, value):
        if not any(c.isupper() for c in value):
            raise serializers.ValidationError('Password must contain at least one uppercase letter.')
        if not any(c.isdigit() for c in value):
            raise serializers.ValidationError('Password must contain at least one number.')
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Accepts email instead of username for the JWT login endpoint."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField()
        self.fields.pop(self.username_field, None)

    def validate(self, attrs):
        email = attrs.get('email', '')
        try:
            user_obj = User.objects.get(email__iexact=email)
            attrs[self.username_field] = user_obj.username
        except User.DoesNotExist:
            attrs[self.username_field] = ''
        attrs.pop('email', None)
        return super().validate(attrs)
