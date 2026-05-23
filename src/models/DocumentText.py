from dataclasses import dataclass, field

##@dataclass
class DocuementText:
    lines: list[str] = field(default_factory=lambda: [""])
    cursor_y: int = 0
    cursor_x: int = 0