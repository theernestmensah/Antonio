from pathlib import Path
r=Path(__file__).resolve().parent.parent
p=r/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('width="600" height="400"','width="460" height="478"')
s=s.replace('Antonio Edem Asinyo campaign branding','Antonio Edem Asinyo smiling against a green background')
p.write_text(s,encoding='utf-8')
