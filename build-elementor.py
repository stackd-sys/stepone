#!/usr/bin/env python3
"""Gera elementor.html a partir de index.html.

- Imagens e fontes com endereço absoluto (CDN jsDelivr a partir deste repositório).
- Todo o CSS fica dentro de #so, com prioridade sobre os estilos do tema e do Elementor.

Uso: python3 build-elementor.py
"""
import re

BASE = 'https://cdn.jsdelivr.net/gh/stackd-sys/stepone@main/'
SCOPE = '#so'

# Anula TODOS os estilos do tema/Elementor dentro de #so (volta aos valores base do browser);
# as regras da página, mais específicas, são aplicadas a seguir. SVG fica de fora para manter stroke/fill.
RESET = f"""
{SCOPE},{SCOPE} :where(*:not(svg,svg *)),{SCOPE} :where(*:not(svg,svg *))::before,{SCOPE} :where(*:not(svg,svg *))::after{{all:revert}}
"""


def scope_selector(sel):
    sel = sel.strip()
    if sel in (':root', 'html', 'body'):
        return SCOPE
    for tag in ('html', 'body'):
        if sel.startswith(tag + '{') or sel.startswith(tag + ' ') or sel.startswith(tag + ':') or sel == tag:
            return SCOPE + sel[len(tag):]
    if sel.startswith(':root'):
        return SCOPE + sel[len(':root'):]
    return f'{SCOPE} {sel}'


def scope_css(css):
    out, i, n = [], 0, len(css)
    while i < n:
        if css[i].isspace():
            out.append(css[i]); i += 1; continue
        if css.startswith('/*', i):
            j = css.index('*/', i) + 2; out.append(css[i:j]); i = j; continue
        brace = css.index('{', i)
        head = css[i:brace].strip()
        # encontrar o fim do bloco
        depth, j = 0, brace
        while True:
            if css[j] == '{': depth += 1
            elif css[j] == '}':
                depth -= 1
                if depth == 0: break
            j += 1
        body = css[brace + 1:j]
        if head.startswith('@media') or head.startswith('@supports'):
            out.append(head + '{' + scope_css(body) + '}')
        elif head.startswith('@'):
            out.append(head + '{' + body + '}')  # @font-face, @keyframes
        else:
            sels = ','.join(scope_selector(s) for s in head.split(','))
            out.append(sels + '{' + body + '}')
        i = j + 1
    return ''.join(out)


src = open('index.html', encoding='utf-8').read()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1).strip()
body = body.replace('href="#main"', 'href="#so-main"').replace('id="main"', 'id="so-main"')

out = (
    '<!-- Step One: colar num widget HTML do Elementor (modelo "Elementor Canvas"). '
    'Gerado a partir de index.html por build-elementor.py. -->\n'
    '<style>' + RESET + scope_css(css) + '</style>\n'
    f'<div id="{SCOPE[1:]}">\n' + body + '\n</div>\n'
).replace('assets/', BASE + 'assets/')

open('elementor.html', 'w', encoding='utf-8').write(out)
print('elementor.html:', len(out), 'caracteres')
