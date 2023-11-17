# yourappname/urls.py
from django.urls import path,include
from .views import *
from django_comments.urls import urlpatterns as comments_urls
urlpatterns = [
    
  
    
    path('', student_list, name='student_list'),
    path('add_student/', add_student, name='add_student'),

     path('grade_list/', grade_list, name='grade_list'),
    path('add_grade/', add_grade, name='add_grade'),
     path('delete_grade/<int:grade_id>/', delete_grade, name='delete_grade'),
    path('course_list/', course_list, name='course_list'),
    path('add_course/', add_course, name='add_course'),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'), 
    
    path('class_list/', class_list, name='class_list'),
    path('add_class/', add_class, name='add_class'),
    path('delete_class/<int:class_id>/', delete_class, name='delete_class'),
    
    path('availability_list/', availability_list, name='availability_list'),
    path('add_availability/', add_availability, name='add_availability'),
    path('delete_availability/<int:availability_id>/', delete_availability, name='delete_availability'),
     path('comments/', include('django_comments.urls')),
  
     path('your_model_list/', your_model_list, name='your_model_list'),
    path('add_image/', add_image, name='add_image'),
    
     path('create_message/', create_message, name='create_message'),
    path('inbox/', inbox, name='inbox'),
    path('message/<int:message_id>/', message_detail, name='message_detail'),
    path('message/<int:message_id>/delete/', delete_message, name='delete_message'),
   
   path('send_email/', send_email, name='send_email'),
    path('email_sent/', email_sent, name='email_sent'),
  
   path('agendas/', agenda_list, name='agenda_list'),
    path('agendas/<int:agenda_id>/', agenda_detail, name='agenda_detail'),
    path('create_agenda/', create_agenda, name='create_agenda'),
    path('agendas/<int:agenda_id>/delete/', delete_agenda, name='delete_agenda'),
    path('chat/', chat, name='chat'),
    path('create_chat/', create_chat, name='create_chat'),
     path('delete_message/<int:message_id>/', delete_message, name='delete_message'),
     

     path('support/', support, name='support'),
    path('thank-you/', thank_you, name='thank_you'),
    
 path('report/', reporting_view, name='reporting'),
]
