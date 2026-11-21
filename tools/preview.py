from pathlib import Path
r=Path(__file__).resolve().parent.parent
s=(r/'index.html').read_text(encoding='utf-8')
for directory in ['assets','img']:
 s=s.replace(f'"/{directory}/',f'"{r.as_uri()}/{directory}/')
s=s.replace('"/og.jpg"',f'"{r.as_uri()}/og.jpg"')
s=s.replace(f'{r.as_uri()}/assets/campaign.css',f'{r.as_uri()}/tools/preview.css')
css=(r/'assets/campaign.css').read_text(encoding='utf-8').replace("url('/assets/",f"url('{r.as_uri()}/assets/")
(r/'tools/preview.css').write_text(css,encoding='utf-8')
(r/'tools/preview.html').write_text(s,encoding='utf-8')
