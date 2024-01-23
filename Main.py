import re
import os

def convert_and_extend_html_files(input_directory, output_directory, base_template):
    # Statik dosyalara referans veren regex desenleri (raw string olarak)
    css_pattern = re.compile(r'href="([^"]+\.css)"')
    js_pattern = re.compile(r'src="([^"]+\.js)"')
    img_pattern = re.compile(r'src="([^"]+\.(png|jpg|jpeg|gif|svg))"')

    # Eğer çıktı dizini yoksa oluştur
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Belirtilen giriş dizinindeki tüm HTML dosyalarını dönüştür
    for filename in os.listdir(input_directory):
        if filename.endswith('.html'):
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, filename)

            with open(input_filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # {% load static %} ve {% extends '...' %} tag'larını ekleyin
            content = '{% load static %}\n{% extends "' + base_template + '" %}\n{% block content %}\n' + content + '\n{% endblock %}'

            # Statik dosya referanslarını güncelle
            content = css_pattern.sub(r'href="{% static \1 %}"', content)
            content = js_pattern.sub(r'src="{% static \1 %}"', content)
            content = img_pattern.sub(r'src="{% static \1 %}"', content)

            # Dönüştürülmüş içeriği yeni dosyaya yaz
            with open(output_filepath, 'w', encoding='utf-8') as file:
                file.write(content)

# Giriş ve çıktı dizinlerini belirtin
input_html_directory = 'path/to/your/original/html_files'
output_html_directory = 'path/to/your/extended/html_files'
base_template_name = 'base.html'
convert_and_extend_html_files(input_html_directory, output_html_directory, base_template_name)
