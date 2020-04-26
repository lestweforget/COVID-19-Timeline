
reversed order to show latest news

{% for block in site.data.news  reversed %}
### {{ block.date }}
{% for item in block.items %}
{% if item.item_name == "group" %}{{ item.content }}{% endif %}
{% if item.item_name == "news" %}* {{ item.content }} {% endif %}
{% endfor %}
{% endfor %}