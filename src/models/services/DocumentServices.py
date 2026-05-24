from src.models import FileDocument


class DocumentServices:
    
    def load(self, file_path: str) -> FileDocument:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                doc = FileDocument()
                doc.lines = f.readlines() or [""]
                return doc
        except:
            return FileDocument()

    def save(self, file_path: str, lines: list[str]) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)