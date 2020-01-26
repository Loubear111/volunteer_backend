from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from volunteer.models import event, user, organization, event_user_junction

# Create your views here.
def index(request):
	return HttpResponse("Welcome to the index page!")

def home(request):
	response = user.objects.all().values('username')
	for entry in response:
		return JsonResponse(entry)

def user_stats(request, uname):
	response = user.objects.filter(username=uname).values()
	for entry in response:	
		return JsonResponse(entry)

def event_details(request,eventid):
	response = event.objects.filter(eid=eventid).values()
	for entry in response:
		return JsonResponse(entry)

def org_stats(request,uname):
	response = organization.objects.filter(username=uname).values()
	for entry in response:
		return JsonResponse(entry)

"""def event_history(request,uname):
	response = event_user_junction.objects.filter(username=uname)
	for entry in response:
		inner_response = event.objects.filter(eid=entry[eid])
		for entry2 in inner_response:"""			

"""def leaderboard(request):
	response = user.objects.order_by(points,DESC)
	return response"""

def events(request,min_lat,max_lat,min_long,max_long):
	response = event.objects.filter(latitude>=min_lat).filter(latitude<=max_lat).filter(longitude>=min_long).filter(longitude<=max_long)
	for entry in response:
		longitudes = longitudes + enty[longitude]
		latitudes = latitudes + entry[latitude]
		names = names + entry[name]
		start_times = start_times + entry[start_times]
		end_times = end_times + entry[end_time]
		pphs = pphs + entry[pph]
		eids = eids + entry[eid]
		organizers = organizers + entry[organizer]
	return JsonResponse([{'organizers':organizers},{'eids':eids},{'longitudes':longitudes},{'latitudes':latidues},{'names':names},{'start_times':start_times},{'end_times':end_times},{'pphs':pphs}])

def login(request,uname):
	response = user.objects.filter(username=uname).values()
	print(response)
	for entry in response:
		return JsonResponse(entry)

def insert_user(request,uname,nm,loc):
	b = user(username=uname,name=nm,points=0,location=loc)
	b.save()
	return HttpResponse()

def insert_org(request,nm,uname,loc):
	b = organization(username=uname,name=nm,location=loc)
	b.save()
	return HttpResponse()

def create_event(request,longi,lati,people,stm,etm):
	b = event(longitude = longi, latidue = lati, num_people = people, pph = 10, start_time = stm, end_time = etm, eid = 1)
	b.save()
	return HttpResponse()
