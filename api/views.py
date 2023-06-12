from rest_framework import generics,serializers
from rest_framework.views import APIView
from .models import MyModel,Company
from .serializers import MyModelSerializer, StandardSerializer,CompanySerializer,OtpSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_otp.oath import totp
from phonenumbers import parse as parse_phone_number, is_valid_number
from twilio.rest import Client
import random
from django.conf import settings


#from .decorators import  require_authentication


class MyModelListAPIView(generics.ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
   #permission_classes = [IsAuthenticated]
   # custom permission
    permission_classes = [IsAuthenticatedOrReadOnly]


class StandardAPIView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        serailizer = StandardSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'data': serailizer.data})
        else:
            return Response({'errors':serailizer.errors},status=status.HTTP_400_BAD_REQUEST)

class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]



class OtpVerificationView(generics.GenericAPIView):
    serializer_class = OtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        otp = serializer.validated_data.get('otp')

        if otp:
            
            if verify_otp(phone_number, otp):
               
                return Response({'message': 'Authentication successful!'})
            else:
                
                return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        else:
           
            if send_otp(phone_number):
                return Response({'message': 'OTP sent!'})
            else:
                return Response({'message': 'Failed to send OTP'}, status=status.HTTP_400_BAD_REQUEST)

def send_otp(phone_number):
    otp = str(random.randint(100000, 999999))

    try:
      
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    
        message = client.messages.create(
            body=f"Your OTP is: {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        
        return True
    except Exception as e:
        # Log any errors or handle them as needed
        print(f"Failed to send OTP to {phone_number}: {e}")
        
    return True

def verify_otp(phone_number, otp):
    # here i have to write logic for verife the otp 
    return otp == '123456'

class OtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField()



class OtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

class SendOtpView(generics.GenericAPIView):
    serializer_class = OtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        otp = str(random.randint(100000, 999999))
        try:
            send_otp(phone_number, otp)
            return Response({'message': 'OTP sent!', 'otp': otp})
        except Exception as e:
            return Response({'message': 'Failed to send OTP'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def send_otp(self, phone_number, otp):
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=f"Your OTP is: {otp}",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            return True
        except Exception as e:
            # Log any errors or handle them as needed
            print(f"Failed to send OTP to {phone_number}: {e}")
            raise