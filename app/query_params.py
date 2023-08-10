from drf_yasg import openapi

def student_filter_by():
    university_id = openapi.Parameter('university_id',openapi.IN_QUERY,description='enter university_id',type=openapi.TYPE_STRING)
    education_type = openapi.Parameter('education_type',openapi.IN_QUERY,description='bachelor or master',type=openapi.TYPE_STRING)
    return [university_id,education_type]


def sponsor_filter_by():
    application_status = openapi.Parameter('application_status',openapi.IN_QUERY,description='enter application status',type=openapi.TYPE_STRING)
    payment_amount = openapi.Parameter('payment_amount',openapi.IN_QUERY,description='Payment amount',type=openapi.TYPE_INTEGER)
    created_at = openapi.Parameter('created_at',openapi.IN_QUERY,description='d.m.Y-d.m.Y(*date.month.year)',type=openapi.TYPE_STRING)
    return [application_status,payment_amount,created_at]

def get_date():
    created_at = openapi.Parameter('created_at',openapi.IN_QUERY,description='d.m.Y(*date.month.year)',type=openapi.TYPE_STRING)
    return [created_at]
