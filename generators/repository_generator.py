from models.entity_metadata import EntityMetadata
from core.template_engine import TemplateEngine
from models.repository_context import RepositoryContext
from utils.file_writer import FileWriter
from config.repository_config import repositories
from core.package_resolver import PackageResolver
class RepositoryGenerator:

    def __init__(
        self,
        template_engine: TemplateEngine,
        package_resolver: PackageResolver,
        repository_type: str = "JpaRepository"
    ):
        self.template_engine = template_engine
        self.repository_type = repository_type
        self.package_resolver = package_resolver


    def generate(
        self,
        entity_metadata: EntityMetadata,
        template_path
    ) -> str:
        context = RepositoryContext(
            package=self.package_resolver.resolve(
            entity_metadata.package,
            "repository"
        ),

            entity_package=entity_metadata.package,

            entity=entity_metadata.class_name,

            repository_type=self.repository_type,

            repository_import=self._repository_import(),

            id_type=entity_metadata.id_type
        )

        return self.template_engine.render_file(
            template_path,
            context.to_dict()
        )



    def _repository_import(self) -> str:
        return repositories[self.repository_type]
    
    def generate_file(self,entity_metadata,
    template_path,
    output_path,
    writer:FileWriter
    ):
        content = self.generate(
            entity_metadata,
            template_path
        )

        writer.write(
            output_path,
            content
        )