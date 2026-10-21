from dataclasses import dataclass
from models.template_context import TemplateContext
@dataclass
class RepositoryContext(TemplateContext):
    package: str
    entity_package: str
    entity: str
    repository_type: str
    repository_import: str
    id_type: str