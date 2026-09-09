# -*- coding: utf-8 -*-
"""Markdown -> PDF via playwright + MathJax (supports LaTeX math & Chinese)."""
import re
import sys
import pathlib
import markdown
from playwright.sync_api import sync_playwright

CSS = """
body { font-family: 'Microsoft JhengHei', 'Segoe UI', 'Noto Sans CJK TC', sans-serif;
       font-size: 12pt; line-height: 1.6; margin: 40px; color: #111; }
h1 { font-size: 18pt; border-bottom: 2px solid #333; padding-bottom: 6px; }
h2 { font-size: 15pt; margin-top: 22px; }
h3 { font-size: 13pt; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #999; padding: 6px 10px; text-align: left; }
th { background: #eee; }
code { background: #f4f4f4; padding: 1px 4px; border-radius: 3px; }
pre { background: #f6f6f6; padding: 10px; border-radius: 4px; overflow-x: auto; }
blockquote { border-left: 4px solid #ccc; margin: 8px 0; padding: 4px 14px; color: #444; }
hr { border: none; border-top: 1px solid #ccc; margin: 18px 0; }
strong { font-weight: 700; }
"""

def protect_math(text):
    placeholders = {}
    def repl(m):
        idx = len(placeholders)
        key = f"\u0000MATH{idx}\u0000"
        placeholders[key] = m.group(0)
        return key
    text = re.sub(r'\$\$.*?\$\$', repl, text, flags=re.DOTALL)
    text = re.sub(r'\$[^$\n]+\$', repl, text)
    return text, placeholders

def restore(text, placeholders):
    for k, v in placeholders.items():
        text = text.replace(k, v)
    return text

def convert(src, out):
    src = pathlib.Path(src)
    out = pathlib.Path(out)
    md_text = src.read_text(encoding="utf-8")
    md_text, ph = protect_math(md_text)
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    body = restore(body, ph)
    html = f"""<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<script>window.MathJax = {{
  tex: {{ inlineMath: [['$','$'],['\\\\(','\\\\)']], displayMath: [['$$','$$'],['\\\\[','\\\\]']] }},
  svg: {{ fontCache: 'global' }}
}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<style>{CSS}</style></head><body>{body}</body></html>"""
    tmp_html = src.with_suffix(".tmp.html")
    tmp_html.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(tmp_html.as_uri())
        try:
            page.wait_for_function(
                "window.MathJax && MathJax.startup && MathJax.startup.promise && "
                "MathJax.startup.promise.then(() => true)", timeout=60000)
        except Exception:
            pass
        page.wait_for_timeout(1500)
        page.pdf(path=str(out), format="A4", print_background=True,
                 margin={"top": "40px", "bottom": "40px", "left": "40px", "right": "40px"})
        browser.close()
    tmp_html.unlink(missing_ok=True)
    print(f"OK: {out}")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])