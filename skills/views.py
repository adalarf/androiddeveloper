from django.shortcuts import render
import csv
# Create your views here.

def skills(request):

    with open('skills/static/skills/csv/vacancies_with_skills.csv', mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)

        def get_android_vacancies():
            android_vacancies = []
            for row in reader:
                if 'android' in row[0] or 'андроид' in row[0] or 'andorid' in row[0] or 'andoroid' in row[
                    0] or 'andoroid' in row[0] or 'andrind' in row[0] or 'xamarin' in row[0]:
                    android_vacancies.append(row)
            return android_vacancies


        value = get_android_vacancies()

        def get_skills(skills, year):
            skill_list = []
            for skill in skills:
                if skill[1] != '' and skill[6][:4] == year:
                    for property in skill[1].split('\n'):
                        skill_list.append(property)
            skills_with_numbers = dict((i, skill_list.count(i)) for i in skill_list)
            sorted_skills = dict(sorted(skills_with_numbers.items(), reverse=True, key=lambda item: item[1]))
            sorted_skills = list(sorted_skills.items())
            return dict(sorted_skills[:10])

        data = {
            '2015': get_skills(value, '2015'),
            '2016': get_skills(value, '2016'),
            '2017': get_skills(value, '2017'),
            '2018': get_skills(value, '2018'),
            '2019': get_skills(value, '2019'),
            '2020': get_skills(value, '2020'),
            '2021': get_skills(value, '2021'),
            '2022': get_skills(value, '2022')
        }
    return render(request, 'skills/skills.html', data)