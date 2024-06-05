import json
import os

import django
from django.template import Context, Template
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_django.settings")
django.setup()


template = {
    "title": "Информация по профилю: {{ name }}",
    "description": "Ваш опыт: {{ exp }}%\nКоличество персонажей: {{ count }} из {{ max_count }}\n",
    "color": 0x9932CC,
    "fields": '[{% if characters %}{% for char in characters %}{"name": "{{ char.name }}", "value": "{{ char.level }} ({{ char.experience }}%)", "inline": "{{ char.is_inline }}"}{% endfor %}{% endif %}]',
}

print("TEMPLATE----------")
print(json.dumps(template, ensure_ascii=False))

fields_template = {
    "name": "{{ name }}",
    "value": "{{ exp }}",
    "inline": "{{ is_inline }}",
}


template_str = json.dumps(template, ensure_ascii=False)
# fields_template_str = json.dumps(fields_template, ensure_ascii=False)


print(f"{type(template_str)}-тип, {template_str}")
# print(f"{type(fields_template_str)}-тип, {fields_template_str}")
print("----------------------------------------------")

template_instance = Template(template_str)

# fields_template_instance = Template(fields_template_str)

# print(template_instance)
# print(fields_template_instance)


fields = {
    "fields": [
        {
            "name": "bubr",
            "exp": 100,
            "is_inline": True,
        },
        {
            "name": "momba",
            "exp": 2,
            "is_inline": True,
        },
    ],
}


# fields_render = []
# if fields["fields"]:
#     for field in fields["fields"]:
#         field_context = Context(field)
#
#         result_render = fields_template_instance.render(field_context)
#         fields_render.append(json.loads(result_render))


context = Context(
    {
        "name": "Петр",
        "exp": 1,
        "count": 2,
        "max_count": 2,
        "fields": [
            {
                "name": "bubr",
                "exp": 100,
                "is_inline": True,
            },
            {
                "name": "momba",
                "exp": 2,
                "is_inline": True,
            },
        ],
    }
)

context_2 = Context(
    {
        "embed_name": "user_info",
        "name": "qwe",
        "discord_id": 123,
        "experience": 0,
        "characters_count": 2,
        "characters": [
            {"id": 1, "name": "Bumber", "user": 123, "level": 1, "experience": 0},
            {"id": 2, "name": "lamumber", "user": 123, "level": 1, "experience": 0},
        ],
    }
)

# print("Context")
# print(context)
# print(fields_render)
# context["fields"] = fields_render
# context["fields"] = json.dumps(fields_render, ensure_ascii=False)
# context.update({"fields": fields_render})


print(context)

render_str = template_instance.render(context_2)

print(type(render_str))
print(render_str)


result = json.loads(render_str)

print(type(result))
print(result)
