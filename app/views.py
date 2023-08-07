from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.exceptions import MethodNotAllowed
from .serializers import *
from rest_framework.pagination import PageNumberPagination
import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .query_params import *


class Custompagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class SponsorsListCreateView(generics.ListCreateAPIView):
    serializer_class = SponsorSerializer
    pagination_class = Custompagination
    pagination_class.page_size = 10

    def get_queryset(self):
        queryset = Sponsor.objects.all()
        created_at = self.request.query_params.get('created_at', None)
        application_status = self.request.query_params.get('application_status', None)
        payment_amount = self.request.query_params.get('payment_amount', None)

        if created_at:
            created_at_from = datetime.datetime.strptime(created_at.split("-")[0], "%d.%m.%Y")
            created_at_to = datetime.datetime.strptime(created_at.split("-")[1], "%d.%m.%Y")

            queryset = queryset.filter(Q(created_at__gte=created_at_from) & Q(created_at__lte=created_at_to))
        if application_status:
            queryset = queryset.filter(application_status=application_status)
        if payment_amount:
            queryset = queryset.filter(payment_amount=payment_amount)
        return queryset

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=sponsor_filter_by())
    def get(self, request, format=None):
        paginatior = self.pagination_class()
        sponsors = paginatior.paginate_queryset(queryset=self.get_queryset(), request=request)
        serializer = self.serializer_class(sponsors, many=True)
        return paginatior.get_paginated_response(serializer.data)

        # return Response(serializer.data)


class SponsorsDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    pagination_class = Custompagination

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return StudentWriteSerializer
        else:
            return StudentReadSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        university_id = self.request.query_params.get('university_id')
        education_type = self.request.query_params.get('education_type')
        if university_id:
            queryset = queryset.filter(university=university_id)
        if education_type:
            queryset = queryset.filter(education_type=education_type)
        return queryset

    @swagger_auto_schema(manual_parameters=student_filter_by())
    def get(self, request):
        paginator = self.pagination_class()
        students = paginator.paginate_queryset(self.get_queryset(), request=request)
        serializer = self.get_serializer(students, many=True)
        return paginator.get_paginated_response(serializer.data)

class SponsorByStudentListCreateView(generics.ListCreateAPIView):
    serializer_class = SponsorByStudentSerializer

    def get_queryset(self):
        return SponsorByStudent.objects.filter(student_id=self.kwargs['student_id'])

    def post(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs['student_id'])
        serializer = self.serializer_class(data=request.data,context={'student':student})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SponsorByStudentUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = SponsorByStudent
    serializer_class = SponsorByStudentSerializer

    def get_object(self):
        return get_object_or_404(SponsorByStudent, pk=self.kwargs['id_sponsor_by_student'])
    def update(self, request, *args, **kwargs):
        student = self.get_object().student

        serializer = self.get_serializer(self.get_object(),data=request.data,context={'student':student})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

