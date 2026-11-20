from pathlib import Path
import re,json
root=Path(__file__).resolve().parent.parent
p=root/'index.html'
s=p.read_text(encoding='utf-8')
s=re.sub(r'<script type="module" crossorigin src="[^"]+"></script>', '<script src="/assets/site.js" defer></script>', s)
s=s.replace('</head>','<link rel="stylesheet" href="/assets/refinements.css">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="Antonio Edem Asinyo | The record of service">\n<meta name="twitter:description" content="Explore Antonio’s background, youth leadership and published campaign coverage.">\n<meta name="twitter:image" content="/og.jpg">\n<meta property="og:type" content="website">\n<meta property="og:locale" content="en_GH">\n<meta property="og:image:alt" content="Antonio Edem Asinyo campaign branding">\n<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'Person','name':'Antonio Edem Asinyo','description':'Ghanaian communicator and former President of the World Universities Debating Council.'})+'</script>\n</head>')
s=re.sub(r'<title>.*?</title>','<title>Antonio Edem Asinyo | A record of youth leadership</title>',s)
s=re.sub(r'<nav class="nav".*?</nav>','<button class="menu-toggle" aria-expanded="false" aria-controls="section-nav" hidden>Menu</button><nav class="nav" id="section-nav" aria-label="Main navigation"><a href="#record">His record</a><a href="#case">His vision</a><a href="#floor">In the news</a><a href="#divide">Stay connected</a></nav>',s,flags=re.S)
s=re.sub(r'<a class="hdr-cta".*?</a>','<a class="hdr-cta" href="#record">Meet Antonio</a>',s,flags=re.S)
s=re.sub(r'<p class="hero-motion.*?</p>','<p class="hero-motion">Antonio Edem Asinyo<br>For NDC Deputy National Youth Organiser</p>',s,flags=re.S)
s=re.sub(r'<div class="hero-badge".*?</div>','',s,flags=re.S)
s=s.replace('Stand with Antonio <i aria-hidden="true">→</i>','Stay connected').replace('href="#divide">Stay connected','href="#divide">Stay connected')
s=re.sub(r'<p class="eyebrow.*?</p>','',s,flags=re.S)
s=re.sub(r'<section class="gap".*?</section>','',s,flags=re.S)
s=re.sub(r'<li class="row" data-row>\s*<span class="r-date mono">Public service.*?</li>','',s,flags=re.S)
s=s.replace('Audited by','References').replace('Press reports, linked per line','Published reporting, linked below')
s=re.sub(r'<div class="first-years.*?</div>','',s,flags=re.S)
s=s.replace('For 39 years no African had held the post. Delegates from debating nations elected a Legon coach to it, and he has spent the years since preparing young people to lead.','Elected in Cape Town on 1 January 2019, Antonio became the first Ghanaian and first Black African to lead the council. His work as a debate coach brought young Ghanaian voices to an international stage. <a href="https://www.citinewsroom.com/2019/01/ghanaian-named-first-black-african-chair-of-worlds-university-debate-council/" target="_blank" rel="noopener">Read the Citi News report</a>.')
start=s.index('  <div class="case-intro">'); end=s.index('</section>',start)
s=s[:start]+'''  <div class="case-intro"><h2 id="case-h" class="case-h">People before<br><em>politics.</em></h2><p class="case-lede">Antonio’s declaration places youth mobilisation, service and opportunity at the centre of his candidacy. Explore the published statement for his own account of that vision.</p></div>
  <div class="vision-body"><p>From the NDC Youth Forum at Kuku Hill to student organising through TEIN, his political background is rooted in youth participation.</p><p>His declaration connects that experience with a youth-centred vision and the NDC’s values of solidarity, probity and accountability.</p><a class="btn vision-link" href="https://onuaonline.com/antonio-edem-asinyo-declares-bid-for-ndc-deputy-national-youth-organiser/" target="_blank" rel="noopener">Read the published declaration</a></div>
''' + s[end:]
s=re.sub(r'<div class="next">.*?(?=\s*</div>\s*</div>\s*<div class="press">)','<p class="news-intro">Read the reporting behind the record. These articles cover Antonio’s candidacy and his work in youth leadership.</p>',s,flags=re.S)
s=s.replace('Making the case, <em>campus by campus.</em>','The story,<br><em>on the record.</em>')
s=s.replace('On air · GHOne TV, “NDC National Elections” · <span class="tbc">photo temporary</span>','Antonio in the GHOne TV studio · supplied press image')
start=s.index('<section class="divide"');end=s.index('</section>',start)+len('</section>')
s=s[:start]+'''<section class="divide" id="divide" aria-labelledby="divide-h"><div class="divide-copy"><h2 id="divide-h" class="divide-h">Keep the<br><em>conversation going.</em></h2><p class="divide-p">Explore Antonio’s public updates, read his background, or share this page with someone who wants to learn more.</p></div><div class="connect"><a class="connect-link" href="https://x.com/EclecticAntonio" target="_blank" rel="noopener">Follow Antonio on X <span>@EclecticAntonio</span></a><a class="connect-link" href="https://linkedin.com/in/antonioedem" target="_blank" rel="noopener">Explore his professional background <span>LinkedIn</span></a><button class="btn btn-light" id="share-page" hidden>Share this page</button><p id="share-status" role="status" aria-live="polite"></p></div></section>''' + s[end:]
s=re.sub(r'<li><span class="soc-tbc">.*?</li>','',s)
s=re.sub(r'<div>\s*<p class="foot-k mono">Campaign office</p>.*?</div>','<div><p class="foot-k mono">Explore</p><p class="foot-v"><a href="#record">His record</a><br><a href="#case">His vision</a><br><a href="/privacy.html">Privacy information</a></p></div>',s,flags=re.S)
s=s.replace('<p class="foot-k mono">The ballot</p>','<p class="foot-k mono">The candidacy</p>').replace('<br><strong>Number 3</strong>','')
s=re.sub(r'<p class="foot-legal.*?</p>','<p class="foot-legal">Campaign website concept by AYINKA Technologies. Campaign approval and image permissions remain pending. Biography references are linked within the page. No registration or donation forms are active.</p>',s,flags=re.S)
s=s.replace('“Before trusting a leader’s word, look at what they have&nbsp;done.”','A record of service.<br>A commitment to young people.')
s=s.replace('Antonio Edem Asinyo, declaring for Deputy National Youth Organiser, 1&nbsp;October&nbsp;2026','Youth organising · Debate leadership · Communication')
s=s.replace('“This time, I seek your support for a greater call.”','Youth leadership, documented.').replace('Closing line, 01·10·2026','Explore the sources')
p.write_text(s,encoding='utf-8')
