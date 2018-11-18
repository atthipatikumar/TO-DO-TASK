#from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from TODO_project.db import query


def register1(request):
    ID = request.POST.get('ID', '')
    title = request.POST.get('title', '')

    if ID != '':
        sql = "SELECT * from todo_title WHERE ID = %s"
        param_for_user_details = [ID]

    elif title != '':
        sql = "SELECT * from todo_title WHERE title= %s"
        param_for_user_details = [title]

    else:
        sql = "SELECT * from todo_title"
        param_for_user_details = []
    results = query(sql, *param_for_user_details)
    final_test_map = []
    metadata_totalcount = 0
    # result is constructed in the expected format
    for result in results:
        metadata_totalcount = metadata_totalcount + 1
        response_map = {}
        response_map['ID'] = result['ID']
        response_map['title'] = result['title']
        final_test_map.append(response_map)
    metadata = {"total_count": metadata_totalcount}
    response = {"metadata": metadata, 'data_test': final_test_map}
    data = json.dumps(response, encoding='ISO-8859-1')
    http_response = HttpResponse(data, content_type="application/json")
    #kwargs['encoding'] = 'safe-utf-8'
    return http_response

def register2(request):
    task_id = request.POST.get('task_id', '')
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    date_time = request.POST.get('date_time', '')
    status = request.POST.get('status', '')
    created = request.POST.get('created', '')
    date_modified = request.POST.get('date_modified', '')

    if task_id != '':
        sql = "SELECT * from todo_fields WHERE task_id= %s"
        param_for_user_details = [task_id]

    elif title != '':
        sql = "SELECT * from todo_fields WHERE title= %s"
        param_for_user_details = [title]
    elif description != '':
        sql = "SELECT * from todo_fields WHERE description= %s"
        param_for_user_details = [description]
    elif date_time != '':
        sql = "SELECT * from todo_fields WHERE date_time= %s"
        param_for_user_details = [date_time]
    elif status != '':
        sql = "SELECT * from todo_fields WHERE status= %s"
        param_for_user_details = [status]
    elif created != '':
        sql = "SELECT * from todo_fields WHERE created= %s"
        param_for_user_details = [created]
    elif date_modified != '':
        sql = "SELECT * from todo_fields WHERE date_modified= %s"
        param_for_user_details = [date_modified]
    else:
        sql = "SELECT * from todo_fields"
        param_for_user_details = []
    results = query(sql, *param_for_user_details)
    final_test_map = []
    metadata_totalcount = 0
    for result in results:
        metadata_totalcount = metadata_totalcount + 1
        response_map = {}
        response_map['task_id'] = result['task_id']
        response_map['title'] = result['title']
        response_map['description'] = result['description']
        response_map['date_time'] = result['date_time']
        response_map['status'] = result['status']
        response_map['created'] = result['created']
        response_map['date_modified'] = result['date_modified']
        final_test_map.append(response_map)
    metadata = {"total_count": metadata_totalcount}
    response = {"metadata": metadata, 'data_test': final_test_map}
    data = json.dumps(response, encoding='ISO-8859-1')
    http_response = HttpResponse(data, content_type="application/json")
    # kwargs['encoding'] = 'safe-utf-8'
    return http_response


