from django import forms


class ContactForm(forms.Form):
    NECESIDAD_CHOICES = [
        ("", "Selecciona una opción"),
        ("desarrollo", "Desarrollo de aplicación"),
        ("automatizacion", "Automatización de procesos"),
        ("integracion", "Integración con servicios"),
        ("mantenimiento", "Mantenimiento de sistema"),
        ("infraestructura", "Infraestructura / hosting"),
        ("otro", "Otro"),
    ]

    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full", "placeholder": "Tu nombre"}),
    )
    empresa = forms.CharField(
        label="Empresa",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full", "placeholder": "Nombre de tu empresa (opcional)"}),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "input input-bordered w-full", "placeholder": "correo@ejemplo.com"}),
    )
    telefono = forms.CharField(
        label="Teléfono",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full", "placeholder": "Tu teléfono (opcional)"}),
    )
    necesidad = forms.ChoiceField(
        label="¿Qué necesitas?",
        choices=NECESIDAD_CHOICES,
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
    )
    mensaje = forms.CharField(
        label="Cuéntanos más",
        widget=forms.Textarea(attrs={"class": "textarea textarea-bordered w-full h-32", "placeholder": "Describe tu proyecto o necesidad..."}),
    )
