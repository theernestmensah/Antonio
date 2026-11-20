"""Run with the approved HTTPS origin before deployment."""
from pathlib import Path
from urllib.parse import urlparse
import sys,re
r=Path(__file__).resolve().parent.parent
origin=sys.argv[1].rstrip('/') if len(sys.argv)>1 else ''
u=urlparse(origin)
if u.scheme!='https' or not u.netloc or u.path or u.query or u.fragment:
    raise SystemExit('Usage: python tools/configure-domain.py https://your-approved-domain')
for name in ['index.html','privacy.html','404.html']:
 p=r/name;s=p.read_text(encoding='utf-8')
 s=re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>','',s)
 s=re.sub(r'((?:property="og:image"|name="twitter:image") content=")[^"]*',lambda m:m[1]+origin+'/og.jpg',s)
 url=origin+('/' if name=='index.html' else '/'+name)
 if name!='404.html':s=s.replace('</head>',f'<link rel="canonical" href="{url}"><meta property="og:url" content="{url}"></head>')
 p.write_text(s,encoding='utf-8')
(r/'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /.impeccable/\nSitemap: {origin}/sitemap.xml\n',encoding='utf-8')
(r/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{origin}/</loc></url><url><loc>{origin}/privacy.html</loc></url></urlset>\n',encoding='utf-8')
print('Canonical URLs, social image URLs, robots.txt and sitemap.xml configured.')
