import django.conf.locale
from rest_framework import serializers
from .models import *


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
        read_only_fields = ['id', 'spent_money', 'created_at']

    def validate(self, attrs):
        print(333, attrs)
        if not attrs.get('legal_entity') and attrs.get('organization_name'):
            raise serializers.ValidationError('legal_entity should be true when there is organization_name')
        if attrs.get('legal_entity') and not attrs.get('organization_name'):
            raise serializers.ValidationError('There should be organization_name when legal_entity is true')
        return attrs

    # def update(self, instance, validated_data):
    #     print('VAL',validated_data)
    #     Sponsor.objects.filter(pk=instance.pk).update(**validated_data)
    #     return Sponsor.objects.get(pk=instance.pk)


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class StudentReadSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['allocated_money']


class StudentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['allocated_money']


class SponsorByStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorByStudent
        fields = '__all__'
        read_only_fields = ['student']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        sponsor = Sponsor.objects.get(pk=representation['sponsor'])
        representation['sponsor'] = {"id": sponsor.id, "fullname": sponsor.fullname}
        representation.pop('student')
        return representation

    def validate(self, attrs):
        student = self.context.get('student')
        print(991,self.context,student)
        sponsor = attrs.get('sponsor')
        sponsor_money = attrs.get("sponsor_money")
        if student.allocated_money + sponsor_money > student.contract_fee:
            raise serializers.ValidationError(
                f"Student's allocated_money exceeds contract_fee. Maximum sponsor_money can be {student.contract_fee - student.allocated_money}")
        if sponsor.spent_money + sponsor_money > sponsor.payment_amount:
            raise serializers.ValidationError(
                f"Sponsor does not have enough money. Left money in sponsor's wallet:{sponsor.payment_amount - sponsor.spent_money}")
        return attrs

    def create(self, validated_data):
        student = self.context.get('student')
        sponsor = validated_data.get('sponsor')
        student.allocated_money += validated_data.get('sponsor_money')
        student.save()
        sponsor.spent_money += validated_data.get('sponsor_money')
        sponsor.save()
        return SponsorByStudent.objects.create(student=student, **validated_data)
