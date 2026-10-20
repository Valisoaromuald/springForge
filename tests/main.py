from pathlib import Path

from core.template_engine import TemplateEngine
from models.repository_context import RepositoryContext

engine = TemplateEngine()

repositoryContext = RepositoryContext(
    "com.demo.repository",
    "com.demo.model",
    "Client",
    "Long",
    "JpaRepository",
    "org.springframework.data.jpa.repository.JpaRepository"
)


code = engine.render_file(
    Path("templates/repository/repository.java.tpl"),
    repositoryContext.to_dict()
)

print(code)