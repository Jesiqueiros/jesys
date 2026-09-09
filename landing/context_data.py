# ============================================================
# Jesys Solutions — Contenido configurable
# Textos, precios y servicios de la página principal.
# ============================================================

from django.conf import settings


# --- Mantenimiento ---------------------------------------------------

MAINTENANCE_PRICE = "$500"
MAINTENANCE_CURRENCY = "MXN"
MAINTENANCE_NOTE = "El costo final depende de las características y necesidades de cada proyecto."


# --- Propuesta de valor ----------------------------------------------

VALUE_PROPOSITIONS = [
    {
        "title": "Hecho para ti",
        "description": "Cada negocio trabaja de manera diferente. Creamos una solución que se adapte a la forma en que haces las cosas, no al revés.",
        "icon": "tool",
    },
    {
        "title": "Ponemos orden",
        "description": "¿Tienes información en Excel, libretas, WhatsApp y mil lugares más? Te ayudamos a organizarla y tenerla disponible en un solo lugar.",
        "icon": "database",
    },
    {
        "title": "Menos trabajo repetitivo",
        "description": "Identificamos las tareas que te quitan tiempo y buscamos la forma de hacerlas más sencillas y automáticas.",
        "icon": "bolt",
    },
    {
        "title": "Todo en un solo lugar",
        "description": "Administra la información de tu negocio desde una misma aplicación, estés en la computadora, tablet o teléfono.",
        "icon": "globe",
    },
    {
        "title": "Crece contigo",
        "description": "La solución puede crecer conforme crece tu negocio. Si mañana necesitas algo nuevo, podemos agregarlo.",
        "icon": "chart",
    },
    {
        "title": "Seguimos contigo",
        "description": "Después de entregar el sistema seguimos disponibles para ayudarte con cambios, mejoras y mantenimiento.",
        "icon": "handshake",
    },
]


# --- Servicios -------------------------------------------------------

SERVICES = [
    {
        "title": "Organiza tu negocio",
        "description": "Te ayudamos a poner en orden la información y los procesos de tu negocio para que puedas tener todo más claro y bajo control.",
        "examples": [
            "Clientes",
            "Proyectos",
            "Citas",
            "Inventarios",
            "Cotizaciones",
            "Pagos",
            "Gastos",
            "Reportes",
            "Información interna",
            "Seguimiento de actividades",
        ],
    },
    {
        "title": "Administra todo en un solo lugar",
        "description": "Creamos un espacio donde puedas consultar, registrar y administrar lo que pasa en tu negocio sin tener que estar buscando información por todos lados.",
        "examples": [
            "Control de clientes",
            "Seguimiento de proyectos",
            "Agenda de citas",
            "Control de inventario",
            "Registro de ventas",
            "Cotizaciones",
            "Control de gastos",
            "Reportes",
            "Paneles de control",
        ],
    },
    {
        "title": "Hacemos tu trabajo más sencillo",
        "description": "Buscamos qué tareas puedes dejar de hacer manualmente para ahorrarte tiempo y reducir errores.",
        "examples": [
            "Avisos y recordatorios",
            "Envío de información",
            "Generación de reportes",
            "Registro de información",
            "Seguimiento de actividades",
            "Procesos repetitivos",
            "Comunicación con clientes",
        ],
    },
    {
        "title": "Conecta las herramientas que ya utilizas",
        "description": "Si utilizas diferentes servicios para trabajar, podemos buscar la manera de conectarlos para que la información fluya entre ellos.",
        "examples": [
            "WhatsApp",
            "Correo electrónico",
            "Almacenamiento de archivos",
            "Formularios",
            "Sistemas existentes",
            "Servicios que ya utilizas",
        ],
    },
    {
        "title": "Lo ponemos en marcha",
        "description": "Nos encargamos de dejar tu sistema listo para que puedas comenzar a utilizarlo. Tú preocúpate por tu negocio, nosotros por ponerlo a funcionar.",
        "examples": [
            "Puesta en marcha",
            "Configuración",
            "Migración de información",
            "Preparación del sistema",
            "Dominio",
            "Acompañamiento inicial",
        ],
    },
    {
        "title": "Seguimos después de entregarlo",
        "description": "Tu negocio va cambiando y el sistema también puede hacerlo. Podemos ayudarte a mantenerlo, corregir problemas y agregar nuevas funciones cuando las necesites.",
        "examples": [
            "Corrección de errores",
            "Mejoras",
            "Cambios",
            "Nuevas funciones",
            "Mantenimiento",
            "Soporte",
        ],
        "note": "Las nuevas funcionalidades y modificaciones importantes se cotizan por separado.",
    },
]

# -----------------------   PRICES AND PLANS TO CLIENTES ----------------------
DEVELOPMENT_PLANS = [
    {
        "name": "Base",
        "price": "$3,000",
        "subtitle": "Para poner orden.",
        "description": "Para organizar información y procesos sencillos en un solo lugar.",
        "features": [
            "Información organizada",
            "Clientes y registros",
            "Formularios",
            "Búsqueda de información",
            "Panel administrativo",
            "Procesos básicos",
        ],
        "featured": False,
    },
    {
        "name": "Plus",
        "price": "$6,000",
        "subtitle": "Para administrar y controlar.",
        "description": "Para manejar diferentes áreas de tu negocio desde un mismo lugar.",
        "features": [
            "Todo lo de Base",
            "Diferentes áreas",
            "Clientes, proveedores o proyectos",
            "Seguimiento de procesos",
            "Usuarios y permisos",
            "Reportes y paneles",
        ],
        "featured": True,
    },
    {
        "name": "Max",
        "price": "$9,000",
        "subtitle": "Para automatizar y hacer más.",
        "description": "Para soluciones más completas que además reduzcan trabajo manual.",
        "features": [
            "Todo lo de Plus",
            "Automatización de tareas",
            "Generación de documentos",
            "Cotizaciones personalizadas",
            "Notificaciones",
            "Integraciones y procesos personalizados",
        ],
        "featured": False,
    },
]

# --- Proceso de trabajo ----------------------------------------------

PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Nos cuentas qué pasa",
        "description": "Cuéntanos cómo trabajas, qué tienes actualmente y qué es lo que quieres mejorar. No necesitas saber de tecnología.",
    },
    {
        "number": "02",
        "title": "Entendemos el problema",
        "description": "Revisamos cómo manejas tu información y tus procesos para encontrar qué podemos organizar, simplificar o mejorar.",
    },
    {
        "number": "03",
        "title": "Proponemos una solución",
        "description": "Te explicamos qué podemos hacer y cómo funcionaría, de una forma clara y sin tecnicismos innecesarios.",
    },
    {
        "number": "04",
        "title": "Lo construimos contigo",
        "description": "Desarrollamos la solución y vamos revisando contigo que realmente resuelva lo que necesitas.",
    },
    {
        "number": "05",
        "title": "Lo ponemos a trabajar",
        "description": "Dejamos todo listo para que puedas comenzar a utilizarlo y seguimos disponibles para ayudarte después.",
    },
]


# --- Tipos de soluciones ---------------------------------------------

SOLUTION_TYPES = [
    "Gestión de clientes",
    "Control de proyectos",
    "Cotizaciones",
    "Sistemas de citas",
    "Inventarios",
    "Control de pagos",
    "Control de gastos",
    "Reportes",
    "Paneles de control",
    "Automatización de procesos",
    "Sistemas internos",
    "Soluciones personalizadas",
]


# --- FAQ -------------------------------------------------------------

FAQ_ITEMS = [
    {
        "question": "¿Cuánto cuesta hacer un sistema?",
        "answer": "Cada proyecto es diferente. Primero necesitamos conocer qué haces, qué necesitas y qué quieres resolver para poder darte un precio.",
    },
    {
        "question": "No sé nada de tecnología, ¿pueden ayudarme?",
        "answer": "Claro. Tú cuéntanos qué necesitas y cómo trabajas. Nosotros nos encargamos de la parte técnica y te explicamos las cosas de manera sencilla.",
    },
    {
        "question": "Tengo toda mi información en Excel, ¿pueden ayudarme?",
        "answer": "Sí. Podemos ayudarte a organizar esa información y llevarla a un sistema donde sea más fácil consultarla y administrarla.",
    },
    {
        "question": "Tengo información en diferentes lugares, ¿pueden juntarla?",
        "answer": "Sí. Podemos revisar cómo manejas actualmente tu información y buscar la mejor forma de tenerla organizada y disponible en un solo lugar.",
    },
    {
        "question": "¿Pueden automatizar algunas tareas de mi negocio?",
        "answer": "Sí. Revisamos qué tareas haces repetidamente y buscamos cuáles pueden simplificarse o hacerse automáticamente.",
    },
    {
        "question": "¿Tengo que pagar una mensualidad?",
        "answer": "No necesariamente. El desarrollo se cotiza como proyecto. Si quieres que nos encarguemos del mantenimiento y las mejoras después de entregarlo, puedes contratar ese servicio por separado.",
    },
    {
        "question": "¿Pueden seguir ayudándome después de entregar el sistema?",
        "answer": "Sí. Podemos encargarnos del mantenimiento, corregir problemas y agregar nuevas funciones conforme las necesites.",
    },
    {
        "question": "¿Trabajan solamente con empresas grandes?",
        "answer": "No. Trabajamos con negocios de diferentes tamaños. La solución se adapta a lo que realmente necesitas.",
    },
]


# --- CTA texts -------------------------------------------------------

CTA = {
    "hero_title": "Pon orden en tu negocio.",
    "hero_subtitle": "Te ayudamos a organizar tu información, simplificar tus procesos y tener el control de tu negocio en un solo lugar.",
    "hero_btn_primary": "Cuéntanos qué necesitas",
    "hero_btn_secondary": "Conoce lo que podemos hacer",
    "final_title": "¿Tienes un desmadre con tu información?",
    "final_subtitle": "Cuéntanos cómo trabajas actualmente y vemos juntos cómo podemos ayudarte a poner orden.",
    "final_btn": "Cuéntanos tu idea",
}


# --- Contacto --------------------------------------------------------

CONTACT_INFO = {
    "whatsapp": settings.PERSONAL_NUMBER,
    "email": "info@jesyssolutions.com",
    "social": {},
}