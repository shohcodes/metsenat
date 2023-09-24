from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentListSerializer(serializers.ModelSerializer):
    allocated_amount = serializers.SerializerMethodField('get_allocated_amount', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'type', 'institute', 'allocated_amount', 'contract_amount']

    def get_allocated_amount(self, obj):
        return 0


class StudentDetailSerializer(serializers.ModelSerializer):
    allocated_amount = serializers.SerializerMethodField('get_allocated_amount', read_only=True)

    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'institute', 'type', 'allocated_amount', 'contract_amount']

    def get_allocated_amount(self, obj):
        return 0


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'institute', 'type', 'contract_amount']


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'institute', 'contract_amount']
