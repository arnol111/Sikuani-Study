from dataclasses import dataclass


@dataclass
class FileDocument:
    filepath: str
    content: str
    encoding: str = "utf-8"