from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index.html')

def all_actus(request):

	return render(request, 'more.html', {'actus':True})

def all_videos(request):
	return render(request, 'more.html', {'videos':True})

def all_photos(request):
	return render(request, 'more.html', {'photos':True})

def all_albums(request):
	return render(request, 'more.html', {'albums':True})

def about(request):
	return render(request, 'index.html')