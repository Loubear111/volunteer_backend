from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from volunteer.models import event, user, organization

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
	response = event.objects.filter(latitude__gte=min_lat).filter(latitude__lte=max_lat).filter(longitude__gte=min_long).filter(longitude__lte=max_long).values()
	longitudes = []
	latitudes = []
	names = []
	start_times = []
	end_times = []
	pphs = []
	eids = []
	organizers = []
	
	for entry in response:
		longitudes.append(entry["longitude"])
		latitudes.append(entry['latitude'])
		names.append(entry['name'])
		start_times.append(entry['start_time'])
		end_times.append(entry['end_time'])
		pphs.append(entry['pph'])
		eids.append(entry['eid'])
		#organizers = organizers.append(entry['host_org'])
	return JsonResponse([{'eids':eids,'longitudes':longitudes,'latitudes':latitudes,'names':names,'start_times':start_times,'end_times':end_times,'pphs':pphs}],safe=False)

def login(request,uname):
	response = user.objects.filter(username=uname).values()
	
	if not response:
		return JsonResponse({"exists": False})
	else:
		for entry in response:
			return JsonResponse({"exists": True})

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
