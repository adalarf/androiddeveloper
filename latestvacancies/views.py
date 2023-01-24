from django.shortcuts import render
import requests
import json
import re

def latest_vacancies(request):
    def get_page():
        params = {
            'date_from': f'2022-12-25T00:00:01+0300',
            'date_to': f'2022-12-25T23:59:59+0300',
            'specialization': 1,
            'only_with_salary': True,
        }

        req = requests.get('https://api.hh.ru/vacancies?per_page=10', params)
        data = req.content.decode()
        req.close()
        return data

    js_objs = []
    js_obj = json.loads(get_page())
    js_objs.extend(js_obj["items"])

    def get_vacancy():
        data1 = []
        for v in js_obj['items']:
            req1 = requests.get(v['url'])
            data1.append(req1.content.decode())
            req1.close()
        return data1

    vacancy = get_vacancy()

    vacancy_properties = []
    for property in vacancy:
        value = json.loads(property)
        vacancy_properties.append(
            [value['name'], value['description'], value['key_skills'], value['employer']['name'], value['salary']['from'],
             value['salary']['to'], value['salary']['currency'], value['area']['name'], value['published_at']])
    list_vacancy = []
    for i in vacancy_properties:
        for j in i:
            if type(j) == str and '<' in j:
                j = re.sub(r'<.*?>', '', ', '.join(j.split('\n')))
            if type(j) == list:
                j = ((str(j).replace("{'name': '", '')).replace("'}", '')).replace(']', '')[1:]
            list_vacancy.append(j)

    return render(request, 'latestvacancies/latestvacancies.html', {'data': list_vacancy})