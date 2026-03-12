import os, sys, subprocess, shutil, webbrowser, threading, time
from pathlib import Path

BASE = Path(__file__).parent

def setup_media():
    for src, dst in [('images/players', 'media/players'), ('images/logos', 'media/logos')]:
        src_path = BASE / src
        dst_path = BASE / dst
        dst_path.mkdir(parents=True, exist_ok=True)
        if src_path.exists():
            for f in src_path.iterdir():
                dest = dst_path / f.name
                if not dest.exists():
                    shutil.copy2(f, dest)

def ouvrir_navigateur():
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:8000/')

print('Lancement Football Dashboard...')
setup_media()

# Ouvrir le navigateur automatiquement apres 2 secondes
threading.Thread(target=ouvrir_navigateur).start()

os.chdir(BASE)
subprocess.run([sys.executable, 'manage.py', 'runserver'])
