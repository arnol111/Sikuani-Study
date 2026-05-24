from dataclasses import dataclass, field


@dataclass
class FileDocument:
    lines: list[str] = field(default_factory=lambda: [""])
    pos_y: int = 0
    pos_x: int = 0