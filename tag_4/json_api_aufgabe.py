"""
Die Todos-Api konsumieren und alle Todos eines spezifischen Users
in eine Json-Datei speichern (json.dump)

Dazu die Api auslesen und via Iteration alle Todos (dicts) in eine
Liste speichern. Diese Liste via json.dump in eine DAtei schreiben.


https://jsonplaceholder.typicode.com/todos
"""

from pathlib import Path
import requests

url = "https://jsonplaceholder.typicode.com/todos"
USER_ID = 1
