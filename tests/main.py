from pathlib import Path

from generators.repository_generator import RepositoryGenerator
from core.template_engine import TemplateEngine
from models.entity_metadata import EntityMetadata


metadata = EntityMetadata(
    package="com.example.demo.model",
    class_name="Client",
    id_type="Long"
)


generator = RepositoryGenerator(
    TemplateEngine(),"ListCrudRepository"
)


result = generator.generate(
    metadata,
    Path("templates/repository/repository.java.tpl")
)


print(result)