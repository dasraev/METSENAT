from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sponsors/',views.SponsorsListCreateView.as_view()),
    path('sponsors/<int:pk>/', views.SponsorsDetailView.as_view()),
    # path('students/', views.StudentListCreateView.as_view()),
    path('set-sponsors/<int:student_id>',views.SponsorByStudentListCreateView.as_view()),
    path('sponsor-by-student/<int:id_sponsor_by_student>/', views.SponsorByStudentUpdateDeleteView.as_view())

    # path('school/', views.SchoolView.as_view()),
    # path('pupil/', views.PupilView.as_view()),
]

