"""Contrôle l'intégrité des fichiers du dossier extrait."""
from pathlib import Path
import hashlib
import json
import sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'SHA256.json').read_text(encoding='utf-8'))
errors=[]
for item in manifest['files']:
 p=root/item['path']
 if not p.is_file(): errors.append(item['path']+': absent');continue
 if p.stat().st_size!=item['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:
  errors.append(item['path']+': contenu différent')
for e in errors:print(e)
print(f"{len(manifest['files'])} fichiers contrôlés; {len(errors)} différence(s).")
sys.exit(bool(errors))
