from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.src = Path(source)
        self.dst = Path(dest)

    def createDir(self, path):
        directory = self.dst / path.relative_to()
        directory.mkdir(parents=True, exist_ok=True)
