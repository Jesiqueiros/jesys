# ============================================================
# Jesys Solutions — Contenido configurable
# Modificar este archivo para actualizar textos, precios y
# servicios sin tocar templates ni vistas.
# ============================================================

from django.conf import settings

# --- Mantenimiento ---------------------------------------------------
MAINTENANCE_PRICE = "$25"
MAINTENANCE_CURRENCY = "USD"
MAINTENANCE_NOTE = "El costo final depende de las características y necesidades de cada proyecto."

# --- Propuesta de valor ----------------------------------------------
VALUE_PROPOSITIONS = [
    {
        "title": "A tu medida",
        "description": "No necesitas adaptar tu negocio a un software genérico. Desarrollamos la solución alrededor de tus procesos.",
        "icon": "tool",
    },
    {
        "title": "Automatización",
        "description": "Reducimos tareas repetitivas mediante automatizaciones e integraciones.",
        "icon": "bolt",
    },
    {
        "title": "Información centralizada",
        "description": "Toda la información importante de tu negocio puede estar disponible desde un solo sistema.",
        "icon": "database",
    },
    {
        "title": "Accesible desde cualquier lugar",
        "description": "Aplicaciones web disponibles desde computadora, tablet o teléfono.",
        "icon": "globe",
    },
    {
        "title": "Escalable",
        "description": "La aplicación puede evolucionar conforme crece tu negocio.",
        "icon": "chart",
    },
    {
        "title": "Acompañamiento",
        "description": "No desaparecemos después de entregar el sistema. Podemos encargarnos del mantenimiento y evolución de la aplicación.",
        "icon": "handshake",
    },
]

# --- Servicios -------------------------------------------------------
SERVICES = [
    {
        "title": "Desarrollo de software",
        "description": "Desarrollo de aplicaciones web personalizadas según las necesidades y procesos de cada negocio.",
        "examples": [
            "Sistemas administrativos",
            "Gestión de clientes",
            "Control de proyectos",
            "Sistemas de citas",
            "Inventarios",
            "Cotizaciones",
            "Reportes",
            "Dashboards",
            "Gestión financiera",
            "Sistemas internos",
        ],
    },
    {
        "title": "Implementación y despliegue",
        "description": "Nos encargamos de llevar la aplicación desde desarrollo hasta producción.",
        "examples": [
            "Configuración del servidor",
            "Despliegue de la aplicación",
            "Configuración de base de datos",
            "Dominio",
            "SSL",
            "Variables de entorno",
            "Configuración de servicios",
        ],
    },
    {
        "title": "Integraciones y automatización",
        "description": "Integración con servicios externos para automatizar procesos.",
        "examples": [
            "WhatsApp",
            "Correo electrónico",
            "APIs",
            "Almacenamiento de archivos",
            "Servicios de terceros",
            "Automatizaciones",
        ],
    },
    {
        "title": "Mantenimiento",
        "description": "Servicio recurrente para mantener la aplicación funcionando correctamente.",
        "examples": [
            "Corrección de errores",
            "Actualizaciones",
            "Revisiones",
            "Mantenimiento técnico",
            "Soporte básico",
            "Actualizaciones de seguridad",
        ],
        "note": "Las nuevas funcionalidades y modificaciones importantes se cotizan por separado.",
    },
    {
        "title": "Infraestructura",
        "description": "Configuración y administración de los servicios necesarios para ejecutar la aplicación.",
        "examples": [
            "Hosting",
            "Bases de datos",
            "Almacenamiento",
            "Servicios de automatización",
            "Dominios",
            "Otros servicios necesarios",
        ],
    },
]

# --- Modelo de contratación ------------------------------------------
HIRING_MODEL = [
    {
        "number": "01",
        "title": "Desarrollo",
        "description": "Analizamos la necesidad y desarrollamos la aplicación.",
        "price_note": "Precio único según complejidad.",
    },
    {
        "number": "02",
        "title": "Implementación",
        "description": "Configuramos y desplegamos la aplicación para dejarla lista para utilizarse.",
        "price_note": "Se cotiza según los servicios necesarios.",
    },
    {
        "number": "03",
        "title": "Servicios adicionales",
        "description": "Si el proyecto necesita servicios externos como hosting, almacenamiento, WhatsApp, dominios, etc., se configuran según las necesidades del proyecto.",
        "price_note": "",
    },
    {
        "number": "04",
        "title": "Mantenimiento",
        "description": "Una vez puesta en producción, el cliente puede contratar mantenimiento mensual.",
        "price_note": f"Desde {MAINTENANCE_PRICE} {MAINTENANCE_CURRENCY}/mes",
    },
]

# --- Ejemplo de proyecto ---------------------------------------------
PROJECT_EXAMPLE = [
    "Desarrollo de aplicación",
    "Implementación",
    "Base de datos",
    "Almacenamiento",
    "Automatizaciones",
    "Mantenimiento",
]

# --- Proceso de trabajo ----------------------------------------------
PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Conocemos tu necesidad",
        "description": "Entendemos tu negocio, tus procesos y el problema que quieres resolver.",
    },
    {
        "number": "02",
        "title": "Definimos la solución",
        "description": "Determinamos qué debe hacer la aplicación y qué tecnología o servicios necesita.",
    },
    {
        "number": "03",
        "title": "Desarrollamos",
        "description": "Construimos la aplicación de forma iterativa.",
    },
    {
        "number": "04",
        "title": "Implementamos",
        "description": "Configuramos la infraestructura y ponemos el sistema en producción.",
    },
    {
        "number": "05",
        "title": "Mantenemos y evolucionamos",
        "description": "Seguimos disponibles para mantenimiento y nuevas funcionalidades.",
    },
]

# --- Tipos de soluciones ---------------------------------------------
SOLUTION_TYPES = [
    "Sistemas administrativos",
    "Gestión de clientes",
    "Sistemas de citas",
    "Control de proyectos",
    "Cotizaciones",
    "Inventarios",
    "Dashboards",
    "Reportes",
    "Automatización de procesos",
    "Sistemas internos",
    "Integraciones con APIs",
    "Soluciones personalizadas",
]

# --- Tecnologías -----------------------------------------------------
TECHNOLOGIES = [
    "Python",
    "Django",
    "PostgreSQL",
    "Docker",
    "APIs",
    "Cloud / hosting",
    "Automatización",
]

# --- FAQ -------------------------------------------------------------
FAQ_ITEMS = [
    {
        "question": "¿Cuánto cuesta desarrollar una aplicación?",
        "answer": "Cada aplicación es diferente. El precio depende de la complejidad, funcionalidades, integraciones e infraestructura requerida.",
    },
    {
        "question": "¿Tengo que pagar una mensualidad?",
        "answer": "No necesariamente. El desarrollo se cotiza como proyecto. El mantenimiento mensual es un servicio adicional.",
    },
    {
        "question": "¿El hosting está incluido?",
        "answer": "Depende del proyecto. Podemos encargarnos de configurar y administrar la infraestructura necesaria.",
    },
    {
        "question": "¿Pueden integrar WhatsApp?",
        "answer": "Sí. Podemos integrar servicios de comunicación y automatización según las necesidades del proyecto.",
    },
    {
        "question": "¿Pueden mantener mi aplicación después de entregarla?",
        "answer": "Sí. Ofrecemos mantenimiento mensual.",
    },
    {
        "question": "¿Puedo solicitar nuevas funcionalidades?",
        "answer": "Sí. Las nuevas funcionalidades se analizan y cotizan de forma independiente.",
    },
    {
        "question": "¿Trabajan solamente con empresas grandes?",
        "answer": "No. Las soluciones pueden adaptarse al tamaño y presupuesto de cada negocio.",
    },
]

# --- CTA texts -------------------------------------------------------
CTA = {
    "hero_title": "Software hecho para tu negocio.",
    "hero_subtitle": "Desarrollamos aplicaciones web a medida para digitalizar procesos, automatizar tareas y ayudarte a administrar tu negocio de forma más eficiente.",
    "hero_btn_primary": "Solicitar cotización",
    "hero_btn_secondary": "Conocer nuestros servicios",
    "final_title": "¿Tienes una idea para mejorar tu negocio?",
    "final_subtitle": "Cuéntanos qué necesitas y encontremos una solución.",
    "final_btn": "Solicitar cotización",
}

# --- Contacto --------------------------------------------------------
CONTACT_INFO = {
    "whatsapp": settings.PERSONAL_NUMBER,
    "email": "jesiqueiros@hotmail.com",
    "social": {},
}
