import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any link that contains 'Impressum' with 'impressum.html'
# This is a bit tricky because the structure might be <a href="#">Impressum</a>
# or <a ...>Impressum</a>.
# We will use regex to find <a ...>Impressum</a> and replace the href attribute.

def replacer(match):
    # match.group(0) is the entire <a ...>Impressum</a>
    # We want to replace href="#" or href="..." with href="impressum.html"
    tag = match.group(0)
    tag = re.sub(r'href="[^"]*"', 'href="impressum.html"', tag)
    return tag

# Find <a> tags containing Impressum (with possible inner tags)
html = re.sub(r'<a[^>]*>(?:<[^>]+>)*Impressum(?:</[^>]+>)*</a>', replacer, html, flags=re.IGNORECASE)

# Also there's an image for impressum
# <img id="top_impressum" name="top_impressum" class="mo" src="https://www.lernsax.de/pics/top_masthead.svg" alt="Impressum" title="Impressum">
# inside an <a> tag.
def img_replacer(match):
    tag = match.group(0)
    tag = re.sub(r'href="[^"]*"', 'href="impressum.html"', tag)
    return tag

html = re.sub(r'<a[^>]*>(?:<[^>]+>)*<img[^>]*alt="Impressum"[^>]*>(?:</[^>]+>)*</a>', img_replacer, html, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
