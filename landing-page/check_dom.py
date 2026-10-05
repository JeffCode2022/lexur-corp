import subprocess

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
from pathlib import Path
html_path = (Path(__file__).parent / 'index.html').resolve().as_uri()
cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--dump-dom',
    html_path
]
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
dom = res.stdout.decode('utf-8', errors='ignore')
idx = dom.find('giant-title')
while idx != -1:
    print('Found giant-title at', idx)
    print(dom[max(0, idx-50):idx+250])
    print('='*50)
    idx = dom.find('giant-title', idx+1)
