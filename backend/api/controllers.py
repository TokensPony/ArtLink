#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *
from api.serializer import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

import bleach

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
from django.core.validators import *
import requests


def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

def xss_example(request):
  """
  Send requests to xss-example/ to the insecure client app
  """
  return render_to_response('dumb-test-app/index.html',
              {}, RequestContext(request))

class Register(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, *args, **kwargs):
        # Login
        username = bleach.clean(request.data.get('username')) #you need to apply validators to these
        print username
        password = request.data.get('password') #you need to apply validators to these
        print password
        email = request.data.get('email') #you need to apply validators to these
        commstatus = request.data.get('commstatus')
        description = "Hello everybody! I'm an artist, and this is my test description!"
        artstyle = request.data.get('artstyle')
        willdraw = request.data.get('willdraw')
        wontdraw = request.data.get('wontdraw')

        try:
            validate_email(email)
        except:
            return Response({'email': 'Email is Invalid.', 'status': 'error'})
        print request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'username': 'Username is taken.', 'status': 'error'})
        elif User.objects.filter(email=email).exists():
            return Response({'email': 'Email is taken.', 'status': 'error'})

        #especially before you pass them in here
        newuser = User.objects.create_user(email=email, username=username, password=password)
        newuser.save()
        #Profile

        newprofile = Profile(user=newuser, commstatus=commstatus, description=description,
                            artstyle=artstyle, willdraw=willdraw, wontdraw=wontdraw)
        newprofile.save()

        #, 'profile': newprofile.id
        return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})

class Session(APIView):
    permission_classes = (AllowAny,)
    #parser_classes = (parsers.JSONParser,)
    def form_response(self, isauthenticated, userid, username, error=""):
        serializer = ''
        profileData = ''
        if(userid is not None):
            serializer = ProfileSerializer(Profile.objects.get(pk=userid))
            profileData = serializer.data
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username,
            'profile': profileData
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class Events(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        events = Event.objects.all()
        json_data = serializers.serialize('json', events)
        content = {'events': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):
        print 'REQUEST DATA'
        print str(request.data)

        eventtype = request.data.get('eventtype')
        timestamp = int(request.data.get('timestamp'))
        userid = request.data.get('userid')
        requestor = request.META['REMOTE_ADDR']
        commstatus = request.data.get('commstatus')
        description = request.data.get('description')
        name = request.data.get('name')


        newEvent = Event(
            eventtype=eventtype,
            timestamp=datetime.datetime.fromtimestamp(timestamp/1000, pytz.utc),
            userid=userid,
            requestor=requestor,
            commstatus=commstatus,
            description = description,
            name = name
        )

        try:
            newEvent.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newEvent.save()
        print 'New Event Logged from: ' + requestor
        return Response({'success': True}, status=status.HTTP_200_OK)

class EventDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get_object(self, pk):
        try:
            print 'Attempt Get ' + pk
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Profiles
'''
class Profiles(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print 'REQUEST DATA'
        print str(request.data)

        commstatus = request.data.get('commstatus')
        description = request.data.get('description')
        user = request.data.get('user')#name = request.data.get('name')


        newProfile = Profile(
            commstatus=commstatus,
            description = description,
            user=user
        )

        try:
            newProfile.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newProfile.save()
        #print 'New Profile Logged from: ' + requestor
        return Response({'success': True}, status=status.HTTP_200_OK)

#ProfileDetail

class ProfileDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get_object(self, pk):
        try:
            print 'Attempt Get ' + pk
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        profiles = Profile.objects.filter(user = user)
        #profile = self.get_object(pk)
        #json_data = serializers.serialize('json', [profile, ])
        #json_data = ProfileSerializer('json', profiles)
        #content = {'profile': json_data}
        #return HttpResponse(json_data, content_type='json')
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        profile = Profile.objects.filter(user = user)
        #profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CommissionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    #parser_classes = (parsers.JSONParser,)
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer

    #@detail_route(methods=['post'])
    def create(self, request, *args, **kwargs):
        print 'REQUEST DATA'
        print str(request.data.get('profile'))

        commtype = bleach.clean(request.data.get('commtype'))
        description = bleach.clean(request.data.get('description'))
        profile = Profile.objects.get(pk= (request.data.get('profile').get('id')))
        price_min = request.data.get('price_min')
        price_max = request.data.get('price_max')
        slots = request.data.get('slots')
        newCommission = Commission(
            commtype=commtype,
            description = description,
            profile=profile,
            price_min = price_min,
            price_max = price_max,
            slots = slots
        )

        if(price_max < price_min):
            return Response({'price_max': 'Max must be greater than or equal to min', 'status': 'error'})
        try:
            newCommission.clean_fields()
        except ValidationError as e:
            print e
            print str(request.data.get('profile'))
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newCommission.save()
        #Return serialized object
        #print 'New Profile Logged from: ' + requestor
        newData = CommissionSerializer(newCommission)
        return Response(newData.data, status=status.HTTP_200_OK)
    #def create(self, request)
        #Use custome post

    #Enter edit
    #Tighten
    # Reject things on the API side
'''
class Commissions(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        commissions = Commission.objects.all()
        serializer = CommissionSerializer(commissions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print 'REQUEST DATA'
        print str(request.data)

        commtype = request.data.get('commstatus')
        description = request.data.get('description')
        user = request.data.get('user')#name = request.data.get('name')
        price_min = request.data.get('price_min')
        price_max = request.data.get('price_max')
        slots = request.data.get('slots')
        newCommission = Commission(
            commtype=commstatus,
            description = description,
            user=user,
            price_min = price_min,
            price_max = price_max,
            slots = slots
        )

        try:
            newCommission.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newCommission.save()
        #print 'New Profile Logged from: ' + requestor
        return Response({'success': True}, status=status.HTTP_200_OK)

#ProfileDetail

class CommissionDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get_object(self, pk):
        try:
            print 'Attempt Get ' + pk
            #user = User.objects.get(pk=pk)
            #return Commission.objects.get(user = user)
            return Commission.objects.get(pk=pk)
        except Commission.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        commissions = Commission.objects.filter(user = user)
        serializer = CommissionSerializer(commissions, many=True)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        #user = User.objects.get(pk=pk)
        #commission = Commission.objects.filter(user = user)
        commission = self.get_object(pk)
        serializer = CommissionSerializer(commission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

class ActivateIFTTT(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )
    def post(self,request):
        print 'REQUEST DATA'
        print str(request.data)

        eventtype = request.data.get('eventtype')
        timestamp = int(request.data.get('timestamp'))
        requestor = request.META['REMOTE_ADDR']
        api_key = ApiKey.objects.all().first()
        event_hook = "test"

        print "Creating New event"

        newEvent = Event(
            eventtype=eventtype,
            timestamp=datetime.datetime.fromtimestamp(timestamp/1000, pytz.utc),
            userid=str(api_key.owner),
            requestor=requestor
        )

        print newEvent
        print "Sending Device Event to IFTTT hook: " + str(event_hook)

        #send the new event to IFTTT and print the result
        event_req = requests.post('https://maker.ifttt.com/trigger/'+str(event_hook)+'/with/key/'+api_key.key, data= {
            'value1' : timestamp,
            'value2':  "\""+str(eventtype)+"\"",
            'value3' : "\""+str(requestor)+"\""
        })
        print event_req.text

        #check that the event is safe to store in the databse
        try:
            newEvent.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        #log the event in the DB
        newEvent.save()
        print 'New Event Logged'
        return Response({'success': True}, status=status.HTTP_200_OK)
