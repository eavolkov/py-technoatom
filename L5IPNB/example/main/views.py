from django.shortcuts import render

from .forms import ExampleForm


def view_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        info = 'Форма заполнена, но некорректна'
        if form.is_valid():
            info = 'Форма заполнена и корректна'
    else:
        info = 'Форма не заполнена'
        form = ExampleForm(initial={'message': 'Привет, '})
    return render(
        request, 'example.html',
        {'form': form, 'info': info}
    )
