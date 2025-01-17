from django.shortcuts import render, redirect
from .forms import ConversionForm
from django.contrib import messages
from .models import ConversionHistory
from .utils import get_exchange_rate


def convert_currency(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            source_currency = form.cleaned_data['source_currency']
            target_currency = form.cleaned_data['target_currency']
            amount = float(form.cleaned_data['amount'])

            try:
                rate = get_exchange_rate(source_currency, target_currency)
                converted_amount = amount * rate

                # Сохранение в историю
                ConversionHistory.objects.create(
                    source_currency=source_currency,
                    target_currency=target_currency,
                    amount=amount,
                    converted_amount=converted_amount
                )

                return render(request, 'converter/result.html', {'converted_amount': converted_amount})
            except ValueError as e:
                # Показ сообщения об ошибке
                messages.error(request, str(e))
                return redirect('convert_currency')
    else:
        form = ConversionForm()

    return render(request, 'converter/convert.html', {'form': form})


def history(request):
    conversions = ConversionHistory.objects.all().order_by('-timestamp')
    return render(request, 'converter/history.html', {'conversions': conversions})

