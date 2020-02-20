from django.http import HttpResponse
from django.shortcuts import redirect, render
from management.models import ClassRoom



# Create your views here.
def student_list(request):
    return HttpResponse('List Student Page.')

def student_add(request):
    return HttpResponse('Add Student Page.')

def student_delete(request, student_id):
    return HttpResponse('Delete Student Page.')

def class_list(request):
    """
        แสดงข้อมูล classroom ทั้งหมดในระบบ
    """
    course = ClassRoom.objects.all()
    context = {'classroom': course}
    # context = dict()
    # context['classroom'] = course
    return render(request, 'management/class_list.html', context)

def class_add(request):
    """
        เพิ่มข้อมูล classroom ใหม่เข้าสู่ฐานข้อมูล
    """
    
    return render(request, 'management/class_add.html')

def class_delete(request, class_id):
    """
        ลบข้อมูล classroom โดยลบข้อมูลที่มี id = class_id
    """
    ClassRoom.objects.filter(id=class_id).delete()
    return redirect(to='class_list')
