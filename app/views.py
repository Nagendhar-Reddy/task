from django.shortcuts import render,  get_object_or_404, redirect

from .models import *
from .forms import *

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib import messages
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login

import matplotlib.pyplot as plt
from io import BytesIO
import base64



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades': grades})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()

    return render(request, 'add_grade.html', {'form': form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    
    return render(request, 'delete_course_conform.html', {'course': course})

def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    
    return render(request, 'delete_grade_confirm.html', {'grade': grade})


def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()

    return render(request, 'add_class.html', {'form': form})

def delete_class(request, class_id):
    class_instance = Class.objects.get(id=class_id)
    if request.method == 'POST':
        class_instance.delete()
        return redirect('class_list')
    return render(request, 'delete_class_confirm.html', {'class_instance': class_instance})



def availability_list(request):
    availabilities = Availability.objects.all()
    return render(request, 'availability_list.html', {'availabilities': availabilities})

def add_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('availability_list')
    else:
        form = AvailabilityForm()

    return render(request, 'add_availability.html', {'form': form})

def delete_availability(request, availability_id):
    availability = get_object_or_404(Availability, pk=availability_id)
    
    if request.method == 'POST':
        availability.delete()
        return redirect('availability_list')

    return render(request, 'delete_availability_confirm.html', {'availability': availability})


def your_model_list(request):
    if request.method== "POST":
        images = request.FILES.getlist('images')
        for img in images:
           YourModel.objects.create(images=img)
    images = YourModel.objects.all()
    return render(request , 'your_model_list.html', {'images' : images})

def add_image(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('your_model_list')
    else:
        form = YourModelForm()

    return render(request, 'add_image.html', {'form': form})


@login_required
def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox') 
    else:
        form = MessageForm()
    return render(request, 'create_message.html', {'form': form})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user, read_at__isnull=True)
    read_messages = Message.objects.filter(recipient=request.user).exclude(read_at__isnull=True)
    return render(request, 'inbox.html', {'received_messages': received_messages, 'read_messages': read_messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id, recipient=request.user)
    return render(request, 'message_detail.html', {'message': message})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id, recipient=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('inbox')  
    return render(request, 'delete_message_confirm.html', {'message': message})

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
        
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']

         
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER, 
                recipient,
                fail_silently=True,  
            )

         
            form.save()

            return redirect('email_sent')

    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})

def email_sent(request):
    return render(request, 'email_sent.html')


def agenda_list(request):
    agendas = Agenda.objects.filter(user=request.user)
    return render(request, 'agenda_list.html', {'agendas': agendas})

def agenda_detail(request, agenda_id):
    agenda = Agenda.objects.get(id=agenda_id)
    return render(request, 'agenda_detail.html', {'agenda': agenda})

def create_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save(commit=False)
            agenda.user = request.user
            agenda.save()
            return redirect('agenda_list')
    else:
        form = AgendaForm()

    return render(request, 'create_agenda.html', {'form': form})


def delete_agenda(request, agenda_id):
    agenda = get_object_or_404(Agenda, id=agenda_id)
    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda_list')
    
    return render(request, 'delete_agends.html', {'agenda': agenda})


@login_required
def chat(request):
    messages = Chat.objects.all()
    form = ChatForm()

    return render(request, 'chat.html', {'messages': messages, 'form': form})

def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
         
            chat_instance = form.save(commit=False)
            chat_instance.user = request.user
            chat_instance.save()
            return redirect('chat')
    else:
        form = ChatForm()

    return render(request, 'chat.html', {'form': form})



def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    if request.method == 'POST' and request.user == message.user:
        message.delete()
        return redirect('chat')

    return render(request, 'delete_message.html', {'message': message})


def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            SupportQuestion.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                question=form.cleaned_data['question']
            )
            messages.success(request, 'Your question was submitted successfully.')
            return redirect('thank_you', submitted_question=form.cleaned_data['question'])
    else:
        form = SupportForm()

    return render(request, 'support_form.html', {'form': form})

def thank_you(request, submitted_question=None):
    return render(request, 'thank_you.html', {'submitted_question': submitted_question})