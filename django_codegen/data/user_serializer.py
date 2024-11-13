from djoser.serializers import UserSerializer as BaseUserSeralizer,  UserCreateSerializer as BaseUserCreateSerializer
from django.utils import timezone
from datetime import timedelta


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        # Ajustamos el tiempo límite para verificar el email
        validated_data['verification_deadline'] = timezone.now() + \
            timedelta(days=7)
        return super().create(validated_data)


class UserSerializer(BaseUserSeralizer):
    """
    Aquí hemos sobreescrito los campos que queremos que muestre el endpoint auth/users/me, para que muestre también el nombre y el apellido.
    """
    class Meta(BaseUserSeralizer.Meta):
        fields = ['id', 'email', 'first_name',
                  'last_name', 'role', 'email_verified']
