from django.urls import path
from api.views import MyModelListAPIView,StandardAPIView,CompanyCreateAPIView,OtpVerificationView,SendOtpView

app_name = 'api'
urlpatterns = [
    # Other URL patterns
    path('mymodels/', MyModelListAPIView.as_view(), name='mymodels'),
    path('postapi/',StandardAPIView.as_view(), name='StandardAPIView'),
    path('createapiview/',CompanyCreateAPIView.as_view(), name='createapiview'),
    path('otp-verification/', OtpVerificationView.as_view(), name='otp-verification'),
    path('send-otp/', SendOtpView.as_view(), name='send_otp'),


]