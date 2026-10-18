from pathlib import Path
import javalang
from utils.file_utils import FileUtils
from models.entity_metadata import EntityMetadata


class EntityParser:

    def __init__(self, project_path: Path):
        self.project_path = project_path

    def find_entity(self, entity_name: str) -> Path:
        """
        Recherche une entité Java dans le projet.

        Parameters
        ----------
        entity_name : str

        Returns
        -------
        Path
        """

        filename = f"{entity_name}.java"

        entity = FileUtils.find_file(
            self.project_path,
            filename
        )

        if entity is None:
            raise FileNotFoundError(
                f"L'entité '{entity_name}' est introuvable."
            )

        return entity

    def parse_entity(self, entity_path: Path) -> EntityMetadata:
        metadata = EntityMetadata()
        with open(entity_path, "r", encoding="utf-8") as file:
            source = file.read()
        try:
            tree = javalang.parse.parse(source)
        except javalang.parser.JavaSyntaxError as e:
            raise ValueError(
                f"Syntaxe Java invalide : {e}"
            )
        metadata.package = (
        tree.package.name
        if tree.package
        else "")
        if not tree.types:
            raise ValueError(
                "Aucune classe trouvée."
            )
        clazz = tree.types[0]
        metadata.class_name = tree.types[0].name
        metadata.imports = [
            imp.path
            for imp in tree.imports
        ]
        
        self._extract_primary_key(clazz, metadata)
        return metadata
    def _extract_primary_key(self, clazz, metadata):
        # -----------------------------
        # Recherche de la clé primaire
        # -----------------------------
        for field in clazz.fields:
            for annotation in field.annotations:
                if annotation.name == "Id":
                    metadata.id_name = field.declarators[0].name
                    metadata.id_type = field.type.name
                    return
            raise ValueError(
            f"Aucune clé primaire (@Id) trouvée dans {metadata.class_name}."
            )