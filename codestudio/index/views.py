from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from product.models import Product

from .forms import FeedbackForm
from .models import Index, IndexSeo, Slider, Location, Feedback


def index_page(request):
    indexes = Index.objects.last()
    indexes_seo = IndexSeo.objects.last()
    sliders = Slider.objects.all()
    locations = Location.objects.last()
    products = Product.objects.all()

    context = {
        'indexes': indexes,
        'indexes_seo': indexes_seo,
        'sliders': sliders,
        'locations': locations,
        'products': products,
    }
    return render(request, 'index.html', context)


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():

            # валидируем данные для админки и сохраняем в БД
            feedback = Feedback(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            feedback.save()

            # валидируем данные в форме
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # логируем данные в консоли (только для отладки)
            print(f'Имя: {name}, Email: {email}, Сообщение: {message}')

            # отправляем email
            try:
                send_mail(
                    f'Новое сообщение от {name}',
                    f'От: {name} ({email})\n\n{message}',
                    'your_mail@yandex.ru',  # от кого письмо
                    ['your_mail@yandex.ru'],  # кому письмо
                    fail_silently=False
                )
            except Exception as e:
                # сообщение об ошибке при отправке email
                messages.error(request, f'Ошибка при отправке email: {str(e)}')
                return redirect('index:feedback_error')

            # сообщение об успешной отправке email
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('index:feedback_success')
    else:
        form = FeedbackForm()

    return render(request, 'error.html', {'form': form})


# редирект на страницу успеха
def feedback_success_view(request):
    return render(request, 'success.html')


# редирект на страницу ошибки
def feedback_error_view(request):
    return render(request, 'error.html')
