from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, AttendanceForm, FeedbackForm
from .models import Attendance, Feedback, CustomUser
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'landing.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    context = {}
    if user.role == 'admin':
        # admin sees all attendance and feedback
        context['attendances'] = Attendance.objects.all().order_by('-date')[:50]
        context['feedbacks'] = Feedback.objects.all().order_by('-created_at')[:50]
        template = 'dashboard_admin.html'
    elif user.role == 'teacher':
        # teacher sees all students' attendance and feedback, and can add attendance
        context['attendances'] = Attendance.objects.all().order_by('-date')[:50]
        context['feedbacks'] = Feedback.objects.all().order_by('-created_at')[:50]
        context['attendance_form'] = AttendanceForm()
        template = 'dashboard_teacher.html'
    else:
        # student sees only their own attendance and feedback, and can submit feedback
        context['attendances'] = Attendance.objects.filter(student=user).order_by('-date')[:50]
        context['feedbacks'] = Feedback.objects.filter(student=user).order_by('-created_at')[:50]
        context['feedback_form'] = FeedbackForm()
        template = 'dashboard_student.html'

    return render(request, template, context)

@login_required
def add_attendance(request):
    if request.method == 'POST' and request.user.role == 'teacher':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            att = form.save(commit=False)
            att.recorded_by = request.user
            att.save()
    return redirect('dashboard')

@login_required
def add_feedback(request):
    if request.method == 'POST' and request.user.role == 'student':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.student = request.user
            fb.save()
    return redirect('dashboard')

