
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher, StudentTeacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.all().order_by(ordering)
    context = {'students': students}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)
