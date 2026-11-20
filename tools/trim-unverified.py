from pathlib import Path
import re
p=Path(__file__).resolve().parent.parent/'index.html'
s=p.read_text(encoding='utf-8')
for date in ['2012–14','2017–20']:
 s=re.sub(r'<li class="row" data-row>\s*<span class="r-date mono">'+date+r'.*?</li>','',s,flags=re.S)
for domain in ['www.3news.com','starrfm.com.gh','thebftonline.com']:
 s=re.sub(r'<li><a href="https://'+re.escape(domain)+r'/.*?</li>','',s,flags=re.S)
p.write_text(s,encoding='utf-8')
