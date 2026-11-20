from pathlib import Path
import re
r=Path(__file__).resolve().parent.parent
base=(r/'index.html').read_text(encoding='utf-8')
head=base.split('</head>')[0]
for filename,title,desc,body in [
('privacy.html','Privacy information | Antonio Edem Asinyo','How this static campaign website handles browsing, sharing and links to external services.','<h1>Privacy information</h1><p>This website provides information about Antonio Edem Asinyo. It has no active registration, newsletter, donation or contact forms.</p><h2>Browsing this website</h2><p>The website code does not set cookies, use browser storage, or load analytics, advertising trackers or embedded social feeds. Fonts and images are served locally. The hosting provider may process standard request information, such as IP address and browser details, to deliver and secure the website. Hosting retention and operator contact details must be confirmed before public launch.</p><h2>Sharing and external links</h2><p>The share button opens your device’s sharing options or copies the current page address. It does not send a message automatically. External news and social links take you to services with their own privacy practices.</p><h2>Changes</h2><p>Adding forms, analytics or third-party embeds requires an updated privacy notice and appropriate consent controls before those features go live.</p>'),
('404.html','Page not found | Antonio Edem Asinyo','This page could not be found. Return to the Antonio Edem Asinyo homepage.','<h1>Let’s get you<br>back on track.</h1><p>The page you’re looking for may have moved, or the address may be incorrect.</p>')]:
 h=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',head)
 h=re.sub(r'<meta name="description"[^>]*>',f'<meta name="description" content="{desc}">',h)
 h=re.sub(r'<meta (?:property="og:(?:title|description)"|name="twitter:(?:title|description)")[^>]*>','',h)
 h+=f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">'
 if filename=='404.html': h+='<meta name="robots" content="noindex">'
 (r/filename).write_text(h+'</head><body><main class="utility">'+body+'<p><a class="btn" href="/">Return to homepage</a></p></main></body></html>',encoding='utf-8')
(r/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /.impeccable/\n',encoding='utf-8')
(r/'assets/refinements.css').open('a',encoding='utf-8').write('\n.hdr{transition:none}.row-big{box-shadow:none}.hero-h{line-height:1}.hl{line-height:1.05}.hero-who,.hero-motion{opacity:1}.test-next{font-size:16px}.stamp{box-shadow:none}.hero-fig img{max-width:100%}button[hidden]{display:none!important}\n')
