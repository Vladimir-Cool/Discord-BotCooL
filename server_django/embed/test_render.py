import json
import os

import django
from django.template import Context, Template
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_django.settings")
django.setup()


example = {
    "title": "Информация по профилю: {{ name }}",
    "description": "Ваш опыт: {{ exp }}%\nКоличество персонажей: {{ count }} из {{ max_count }}\n",
    "color": 0x9932CC,
    "fields": [
        {"name": "{{ name_1 }}", "value": "{{ exp_1 }}"},
        {"name": "{{ name_2 }}", "value": "{{ exp_2 }}"},
    ],
}

template_str = json.dumps(example, ensure_ascii=False)

print(template_str)
print(type(template_str))

template = Template(template_str)

context = Context(
    {
        "name": "Петр",
        "exp": 1,
        "count": 2,
        "max_count": 2,
        "name_1": "bubr",
        "exp_1": 100,
        "name_2": "momba",
        "exp_2": 2,
    }
)

render_str = template.render(context)

result = json.loads(render_str)

print(result)
print(type(result))
