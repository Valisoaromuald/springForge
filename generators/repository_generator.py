from models.entity_metadata import EntityMetadata
from core.template_engine import TemplateEngine
from models.repository_context import RepositoryContext
from utils.file_writer import FileWriter
from config.repository_config import repositories
from core.package_resolver import PackageResolver
from pathlib import Path
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
        template_path:Path
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
        
    def _validate(self, metadata: EntityMetadata) -> None:

        if not metadata.class_name:
            raise ValueError("Entity class name is missing.")

        if not metadata.package:
            raise ValueError("Entity package is missing.")

        if not metadata.id_type:
            raise ValueError("Entity id type is missing.")



    def _repository_import(self) -> str:
        if self.repository_type not in repositories:
            raise ValueError(
                f"Unsupported repository type: {self.repository_type}"
            )
        return repositories[self.repository_type]
    
    def generate_file(
    self,
    project_path: Path,
    entity_metadata: EntityMetadata,
    template_path: Path,
    writer: FileWriter
    ) -> None:

        content = self.generate(
            entity_metadata,
            template_path
        )
        output_path = self._build_output_path(
            project_path,
            entity_metadata
        )
        writer.write(
            output_path,
            content
        )

    def _build_output_path(
    self,
    source_root: Path,
    entity_metadata: EntityMetadata
    ) -> Path:

        repository_package = self.package_resolver.resolve(
            entity_metadata.package,
            "repository"
        )

        return (
            source_root
            / Path(*repository_package.split("."))
            / f"{entity_metadata.class_name}Repository.java"
        )
        