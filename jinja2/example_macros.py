from jinja2 import Template

# cars = [
#     {"model": "Audi", "price": 23000},
#     {"model": "Scoda", "price": 17300},
#     {"model": "Volvo", "price": 44300},
#     {"model": "Volkswagen", "price": 21300},
# ]


# digs = [1, 2, 3, 4, 5]

# tpl = "Суммарная цена автомобилей {{ cs | replace('o', 'O')  }}"
# tpl = "Суммарная цена автомобилей {{ cs | sum  }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)

persons = [
    {"name": "Aleksey", "old": 18, "weight": 78.5},
    {"name": "Nikolay", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.8},
]

html = """
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor%}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
"""

tm = Template(html)
msg = tm.render(users=persons)

print(msg)
