from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.
def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            roll = form.cleaned_data.get('roll')
            name = form.cleaned_data.get('name')
            marks = form.cleaned_data.get('marks')
            #print(roll, '--------', name, '---------', marks)
            obj = Student(roll = roll, name = name, marks = marks)
            obj.save()
            return HttpResponse('<h1>Data Saved...</h1>')
    template_name = 'app1/student_form.html'
    context = {'form': form}
    return render(request, template_name, context)
