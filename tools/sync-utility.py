from pathlib import Path
import re
r=Path(__file__).resolve().parent.parent
for name in ['privacy.html','404.html']:
 p=r/name;s=p.read_text(encoding='utf-8')
 s=re.sub(r'<link rel="stylesheet" crossorigin[^>]+>\s*<link rel="stylesheet" href="/assets/refinements.css">','<link rel="stylesheet" href="/assets/campaign.css">',s)
 p.write_text(s,encoding='utf-8')
