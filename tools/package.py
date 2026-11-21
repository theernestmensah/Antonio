"""Create a clean static release with only required public files."""
from pathlib import Path
from shutil import copy2
import zipfile
r=Path(__file__).resolve().parent.parent
files=['index.html','privacy.html','404.html','robots.txt','_headers','og.jpg',
 'assets/campaign.css','assets/site.js','assets/campaign-config.js',
 'assets/schibsted-grotesk-latin-wght-normal-Bb8VGrTG.woff2',
 'assets/dm-serif-display-latin-400-normal-C5_t9oOD.woff2',
 'assets/dm-serif-display-latin-400-italic-DpcbibHm.woff2',
 'img/mark.svg','img/antonio-cut.webp','img/ghone-studio.jpg','img/chevening-2020.jpg']
if (r/'sitemap.xml').exists():files.append('sitemap.xml')
out=r/'publish'
for f in files:
 destination=out/f;destination.parent.mkdir(parents=True,exist_ok=True);copy2(r/f,destination)
with zipfile.ZipFile(r/'campaign-site.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in files:z.write(out/f,f)
print(f'Packaged {len(files)} public files into publish/ and campaign-site.zip')
