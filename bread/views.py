#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Bread

# Create your views here.
def single_bread(request, bread_id):
	bread = get_object_or_404(Bread, pk = bread_id)

	respons_text = '<p>{bread_id}번 빵은 곧 나옵니다.</p>'
	respons_text += '<p><img src = "{bread_url}" /></p>'
	return HttpResponse(respons_text.format(
		bread_id = bread_id,
		bread_url = bread.image_file.url)
	)

def bread_list(request):
	#breads = Bread.objects.filter(release_at=timezone.now()).order_by('release_at')
	breads = Bread.objects.all()
	return render(request, 'bread/bread_list.html', {'breads':breads})

def bread_boot(request):	
	#breads = Bread.objects.filter(release_at=timezone.now()).order_by('release_at')
	#breads = Bread.objects.all()
	
	breads = Bread.objects.order_by("release_at")
	# breads.objects.order_by("release_at")
	nowTime = timezone.now()
	limitTime = timezone.now() + timezone.timedelta(hours = -1)

	return render(request, 'bread/bread_boot.html', {'breads':breads, 
													'nowTime':nowTime, 
													'limitTime':limitTime})


def bread_html(request):	
	return render(request, 'bread/bread_intro.html')