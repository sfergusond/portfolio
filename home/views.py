from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

from . import forms

@csrf_exempt
def landing(request):
    # General contact form
    if request.method == 'POST' and 'message' in request.POST:
        contact_form = forms.Contact(request.POST)
        if contact_form.is_valid():
            cleaned = contact_form.cleaned_data

            message = f"Name: {cleaned['first_name']} {cleaned['last_name']}\n\nMessage:\n{cleaned['message']}"

            email = EmailMessage(
                        subject='[Portfolio Visitor Message]',
                        body=message,
                        to=['sfergusond@gmail.com'],
                        reply_to=[cleaned['email']]
                    )
            email.send(fail_silently=True)
            return redirect(reverse('landing'))
    else:
        contact_form = forms.Contact()

    # Hire form
    if request.method == 'POST' and 'hire' in request.POST:
        hire_form = forms.Hire(request.POST)
        if hire_form.is_valid():
            cleaned = hire_form.cleaned_data

            payment_type = 'hourly' if cleaned['payment_type'] == 'hourly' else 'fixed'
            message = f"Name: {cleaned['first_name']} {cleaned['last_name']}\nProject: {cleaned['title']}\nBudget: ${cleaned['budget']} {payment_type}\nDeadline: {cleaned['deadline']}\n\nDescription:\n{cleaned['description']}"

            email = EmailMessage(
                        subject='[HIRE PROPOSAL] ' + cleaned['title'],
                        body=message,
                        to=['sfergusond@gmail.com'],
                        reply_to=[cleaned['email']]
                    )
            email.send(fail_silently=True)
            return redirect(reverse('landing'))
    else:
      hire_form = forms.Hire()

    context = {
            'contact': contact_form,
            'hire': hire_form
            }
    return render(request, 'landing.html', context)

def portfolio_item(request, portfolio_item):
    if portfolio_item != 'robots.txt':
        return render(request, f'{portfolio_item}.html', {})
    else:
        return render(request, 'robots.txt', {})
