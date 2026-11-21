from html.parser import HTMLParser
from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.h1=0;self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ['a','link'] and 'href' in a:self.links.append(a['href'])
  if tag in ['img','script'] and 'src' in a:self.links.append(a['src'])
  if tag=='img' and 'alt' not in a:self.errors.append('Missing image alt')
for name in ['index.html','privacy.html','404.html']:
 p=Page();s=(r/name).read_text(encoding='utf-8');p.feed(s)
 assert p.h1==1,(name,'h1 count',p.h1)
 assert len(set(p.ids))==len(p.ids),(name,'Duplicate IDs')
 for link in p.links:
  if link.startswith('#'):assert link[1:] in p.ids,(name,'Broken fragment',link)
  elif link.startswith('/') and link!='/':assert (r/link[1:].split('#')[0]).is_file(),(name,'Missing file',link)
 assert not p.errors,p.errors
 assert not any(t in s for t in ['TBC','Draft wording','data-pledge','data-countdown']),(name,'Placeholder')
 for block in __import__('re').findall(r'<script type="application/ld\+json">(.*?)</script>',s):json.loads(block)
 print(name+': headings, links, assets, alt text, JSON-LD and placeholder checks passed')
