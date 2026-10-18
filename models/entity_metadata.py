from dataclasses import dataclass, field


@dataclass
class EntityMetadata:
    package: str = ""
    class_name: str = ""
    imports: list[str] = field(default_factory=list)
    id_name: str = ""
    id_type: str = ""
    table_name: str = ""