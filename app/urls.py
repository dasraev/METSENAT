from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()

router.register(r'students', views.StudentViewSet)
urlpatterns = [
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(router.urls)),
    path('sponsors/', views.SponsorsListCreateView.as_view()),
    path('sponsors/<int:pk>/', views.SponsorsDetailView.as_view()),
    path('set-sponsors/<int:student_id>', views.SponsorByStudentListCreateView.as_view()),
    path('sponsor-by-student/<int:id_sponsor_by_student>/', views.SponsorByStudentUpdateDeleteView.as_view()),
    path('university/', views.UniversityView.as_view()),
    path('dashboard/<str:created_at>', views.DashboardView.as_view()),
    path('statistics/', views.StatisticsView.as_view()),

]
