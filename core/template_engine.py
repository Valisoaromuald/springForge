from pathlib import Path

class TemplateEngine:

    def load(self, template_path):
        return Path(template_path).read_text(encoding="utf-8")