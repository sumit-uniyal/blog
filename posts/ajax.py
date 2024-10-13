from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.conf import settings
from blog.comman_functions import *
from .models import *

# msg_code = '00' For Success
# msg_code = '01' For Error

def dynamic_ajax(request):
    response_data = {}
    if request.method == 'POST':
        if request.POST.get('tab') == 'add_posts':
            try:
                title= request.POST.get('title')
                description= request.POST.get('description')
                image= request.FILES.get('image')

                if not title:
                    response_data['msg_code'] = '01'
                    response_data['msg'] = 'Please Enter the title'
                elif not description:
                    response_data['msg_code'] = '01'
                    response_data['msg'] = 'Please Enter the Description'
                elif not image:
                    response_data['msg_code'] = '01'
                    response_data['msg'] = 'Please upload an Image'
                else:
                    post = Posts(
                        title = title,
                        description = description,
                        image = image,
                        created_by = request.user
                    )
                    post.save()
                    response_data['msg_code'] = '00'
                    response_data['msg'] = 'Post Added Successfully'

            except Exception as e:
                response_data['msg_code'] = '01'
                response_data['msg'] = f'Failed '+str(e)

            return JsonResponse (response_data)

        else:
            response_data['msg_code'] = '01'
            response_data['msg'] = 'Tab Not Found.'
            return JsonResponse (response_data)
    else:
        response_data['msg_code'] = '01'
        response_data['msg'] = 'Please Send the POST Request.'
        return JsonResponse (response_data)