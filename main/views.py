from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Course, Statistic
from .forms import ContactForm, LoginForm, RegisterForm

def home(request):
    courses = Course.objects.filter(is_active=True)
    stats = Statistic.objects.all()
    
    faqs = [
        {"q": "SAT nima va nima uchun kerak?", "a": "SAT (Scholastic Assessment Test) — Amerika va dunyo universitetlariga kirish uchun zarur bo'lgan standartlashtirilgan imtihon. Ko'pchilik yetakchi universitetlar SAT ballini talab qiladi."},
        {"q": "SAT imtihoni qancha vaqt davom etadi?", "a": "SAT imtihoni 2 soat 14 daqiqadan 3 soatgacha davom etadi, test markazi politikasiga qarab."},
        {"q": "SAT yilga necha marta o'tiladi?", "a": "SAT yilga 7 marta o'tiladi. Siz har yili o'zingizga qulay kunni tanlashingiz mumkin."},
        {"q": "Kurs necha muddat davom etadi?", "a": "Bizning kurslar 4-8 hafta davom etadi. Offline kurslar 8 hafta, Online kurslar 4-6 hafta."},
        {"q": "Qaysi kursdan boshlashim kerak?", "a": "SAT bilan yangi tanishayotgan bo'lsangiz, Online kursdan boshlang. Allaqachon taniш bo'lsangiz, Offline yoki Shaxsiy darslarni tanlang."},
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada bog'lanamiz.")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'main/home.html', {
        'courses': courses,
        'stats': stats,
        'faqs': faqs,
        'form': form,
    })


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Xush kelibsiz, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri.")
    else:
        form = LoginForm()
    
    return render(request, 'main/login.html', {'form': form})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            messages.success(request, "Akkaunt muvaffaqiyatli yaratildi! Xush kelibsiz.")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    
    return render(request, 'main/register.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'main/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, "Siz muvaffaqiyatli chiqtingiz.")
        return redirect('home')
    return redirect('dashboard')
