from models.entity_metadata import EntityMetadata
from core.template_engine import TemplateEngine
from models.repository_context import RepositoryContext


class RepositoryGenerator:

    def __init__(
        self,
        template_engine: TemplateEngine,
        repository_type: str = "JpaRepository"
    ):
        self.template_engine = template_engine
        self.repository_type = repository_type


    def generate(
        self,
        entity_metadata: EntityMetadata,
        template_path
    ) -> str:

        context = RepositoryContext(
            package=self._repository_package(
                entity_metadata.package
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


    def _repository_package(
        self,
        entity_package: str
    ) -> str:

        return entity_package.replace(
            ".model",
            ".repository"
        )


    def _repository_import(self) -> str:

        repositories = {
            "JpaRepository":
                "org.springframework.data.jpa.repository.JpaRepository",

            "CrudRepository":
                "org.springframework.data.repository.CrudRepository",

            "PagingAndSortingRepository":
                "org.springframework.data.repository.PagingAndSortingRepository",

            "ListCrudRepository":
                "org.springframework.data.repository.ListCrudRepository"
        }

        return repositories[self.repository_type]