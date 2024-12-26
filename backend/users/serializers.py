from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import serializers

from django.core.mail import send_mail
from django.core.cache import cache

from users.models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    second_name = serializers.CharField(allow_blank=True, allow_null=True)
    is_staff = serializers.BooleanField(default=False)
    is_authenticated = serializers.BooleanField(default=False, read_only=True)

    def create(self, validated_data):
        try:
            user = CustomUser.objects.get(email=validated_data['email'])
            if not user.is_authenticated:
                verification_code = self.generate_verification_code()
                cache.set(f"email_verification_{user.email}", verification_code, timeout=3600)  # код действует 1 час
                self.send_verification_email(user, verification_code)
                return user
            else:
                raise serializers.ValidationError("User with this email already exists and is active.")

        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(**validated_data)
            user.is_authenticated = False  # Initially inactive until email is verified
            user.save()
            verification_code = self.generate_verification_code()
            cache.set(f"email_verification_{user.email}", verification_code, timeout=3600)  # код действует 1 час
            self.send_verification_email(user, verification_code)
            return user

    @staticmethod
    def generate_verification_code():
        import random
        return str(random.randint(100000, 800000))

    @staticmethod
    def send_verification_email(user, code):
        subject = 'Подтверждение Email КомбоБрокер'
        html_message = render_to_string('email/verification_email.html', {'code': code})  # Используем шаблон
        plain_message = strip_tags(html_message)  # Текстовая версия для клиентов, не поддерживающих HTML

        send_mail(
            subject,
            plain_message,  # Текстовая версия для спам-фильтров и клиентов без HTML-поддержки
            '',
            [user.email],
            html_message=html_message,  # HTML-версия
            fail_silently=False,
        )

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if hasattr(instance, key):
                setattr(instance, key, value)

        instance.save()
        return instance


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)