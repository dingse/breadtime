#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

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
	return render(request, 'bread/bread_list.html', {})