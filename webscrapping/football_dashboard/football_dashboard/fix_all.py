import glob, re

# Corriger les templates : supprimer le filtre custom
for path in glob.glob('templates/dashboard/*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('{% load static football_filters %}', '{% load static %}')
    content = re.sub(r'/media/\{\{ (\w+\.\w+)\|fix_media_path \}\}', r'/media/{{ \1 }}', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK:', path)

# Corriger data.py : nettoyer les chemins Windows directement en Python
with open('dashboard/data.py', 'r', encoding='utf-8') as f:
    content = f.read()

helper = '''
def _fix(p):
    if not p: return ''
    return p.replace(chr(92), '/').replace('images/', '')

'''

if '_fix' not in content:
    content = content.replace('LEAGUE_FLAGS = {', helper + 'LEAGUE_FLAGS = {')

old = 'return [dict(r) for r in rows]'
new = '''rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out'''

content = content.replace(old, new)

with open('dashboard/data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('data.py corrige OK')
