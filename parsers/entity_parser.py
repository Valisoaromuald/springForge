from pathlib import Path

from utils.file_utils import FileUtils


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