import re
import random
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotAuthenticated, NotAcceptable

from apps.user.models import SMS, User, Address
from .utils import generate_password


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    class Meta:
        model = SMS
        fields = [
            "phone",
        ]

    def validate_phone(self, phone):
        pattern = "^\+998([0-9]{9})$"
        phone = re.match(pattern, phone)
        if not phone:
            raise serializers.ValidationError(_("Phone number isn't allowed"))
        return phone.group()

    def validate_attempt(self, phone):
        sms = SMS.objects.filter(phone=phone).first()
        if sms and timezone.now() - sms.updated_at <= timedelta(minutes=1):
            raise serializers.ValidationError(
                _("You can only request a code once a minute")
            )

    def validate(self, data):
        self.validate_attempt(data["phone"])
        return data

    def save(self, **kwargs):
        sms = SMS.objects.filter(phone=self.validated_data["phone"]).first()
        code = random.randint(100000, 999999)

        if sms:
            sms.code = code
            sms.save()
        else:
            sms = SMS.objects.create(phone=self.validated_data["phone"], code=code)
            sms.save()

        return sms


class VerifySerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    code = serializers.CharField(required=True)

    class Meta:
        fields = ["phone", "code"]

    def validate_phone(self, phone):
        pattern = "^\+998([0-9]{9})$"
        phone = re.match(pattern, phone)
        if not phone:
            raise ValidationError(_("Phone number isn't allowed"))
        return phone.group()

    def validate_code(self, code):
        if len(code) != 6:
            raise ValidationError(_("Validation code incorrect"))
        return code

    def validate(self, data):
        phone = data["phone"]
        code = data["code"]
        sms = SMS.objects.filter(phone=phone).first()

        if not sms:
            raise ValidationError(_("Phone number not verified"))

        if timezone.now() - sms.updated_at > timedelta(seconds=90):
            raise NotAuthenticated(_("Verification timed out"))

        if str(sms.code) != code:
            raise NotAcceptable(_("Validation code incorrect"))

        return data

    def save(self, **kwargs):
        phone = self.validated_data["phone"]
        user, __ = User.objects.get_or_create(phone=phone)
        if __:
            user.set_password(generate_password())
            user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone", "first_name", "last_name"]
        read_only_fields = ["id", "phone"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ["user"]
