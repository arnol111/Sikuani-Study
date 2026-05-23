class DocumentServices:
    def load(self, file_path: str) -> list[str]:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines() or [""]

    def save(self, file_path: str, lines: list[str]) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)