# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import datetime
import logging

logger = logging.getLogger('home')

def homepage(request):
    if request.method == "POST":
        # Get data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        subject_with_name = f"{name} ({subject})"
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Send email
        try:
            send_mail(
                subject_with_name,
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Show success message
            logger.info(f"[{current_time}] Email sent successfully to {settings.DEFAULT_FROM_EMAIL} from {email}")
            messages.success(request, "Thank you for your message! We will get back to you soon.")
            return redirect('homepage')

        except Exception as e:
            logger.error(f"[{current_time}] Error sending email: {e}")
            messages.error(request, f"Something went wrong. Please try again later. Error: {str(e)}")
            return redirect('homepage')

    return render(request, 'home/index.html')
