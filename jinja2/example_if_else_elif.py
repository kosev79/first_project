from jinja2 import Template

# from markupsafe import escape

cities = [
    {"id": 1, "city": "Tver"},
    {"id": 5, "city": "Moscow"},
    {"id": 7, "city": "Minsk"},
    {"id": 8, "city": "Smolensk"},
    {"id": 11, "city": "Kaluga"},
]

link = """<select name ="cities'>
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == 'Moscow' -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
