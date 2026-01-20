
{% if entry.note %}
- {{entry.note}}
{% elif entry.bullet %}
- {{entry.bullet}}
{% else %}
- **{{entry.date}}**{% if entry.name %}, **{{entry.name}}**{% endif %}{% if entry.institution %}, {{entry.institution}}{% endif %}{% if entry.topic %}, {{entry.topic}}{% endif %}
{% endif %}
