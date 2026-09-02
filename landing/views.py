from django.shortcuts import render

from .forms import ContactForm
from .context_data import (
    MAINTENANCE_PRICE,
    MAINTENANCE_CURRENCY,
    MAINTENANCE_NOTE,
    SERVICES,
    VALUE_PROPOSITIONS,
    HIRING_MODEL,
    PROJECT_EXAMPLE,
    PROCESS_STEPS,
    SOLUTION_TYPES,
    TECHNOLOGIES,
    FAQ_ITEMS,
    CTA,
    CONTACT_INFO,
)


def index(request):
    form = ContactForm()

    return render(request, "landing/index.html", {
        "form": form,
        "maintenance_price": MAINTENANCE_PRICE,
        "maintenance_currency": MAINTENANCE_CURRENCY,
        "maintenance_note": MAINTENANCE_NOTE,
        "services": SERVICES,
        "value_props": VALUE_PROPOSITIONS,
        "hiring_model": HIRING_MODEL,
        "project_example": PROJECT_EXAMPLE,
        "process_steps": PROCESS_STEPS,
        "solution_types": SOLUTION_TYPES,
        "technologies": TECHNOLOGIES,
        "faq_items": FAQ_ITEMS,
        "cta": CTA,
        "contact_info": CONTACT_INFO,
    })
