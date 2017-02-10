# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from common.mymako import render_json
from blueking.component.shortcuts import get_client_by_request



def home(request):
    client = get_client_by_request(request)

    kwargs = {'app_id': 3}

    result = client.cc.get_app_host_list(kwargs)
    _ip_list = result.get('data', []) if result.get('result', False) else []
    ip_list = [_ip['InnerIP'] for _ip in _ip_list]

    taskresult = client.job.get_task(kwargs)
    print taskresult
    task_list = [{'id': str(i['id']), 'name': i['name']} for i in taskresult.get('data', [])]
    print type(task_list)

    countext = {'listsip': ip_list, 'liststask': task_list}

    return render_mako_context(request,'home_application/home.html', countext)

def execute_task(request):

    ipaddr = request.GET.get('ipaddr')
    taskid = request.GET.get('taskid')

    kwargs = {'app_id': 3,'ipList': ipaddr , 'task_id': taskid}
    client = get_client_by_request(request)
    job = client.job.execute_task(kwargs)
    job_Id = job.get('data').get('taskInstanceId')
    job_Name = job.get('data').get('taskInstanceName')
    job_Status = job.get('result')


    return render_json({'job_Id': job_Id, 'job_Name': job_Name, 'job_Status': job_Status})
