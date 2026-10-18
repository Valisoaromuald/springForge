from pathlib import Path


class FileUtils:

    @staticmethod
    def find_file(root: Path, filename: str) -> Path | None:
        """
        Recherche récursivement un fichier à partir d'un dossier.

        Parameters
        ----------
        root : Path
            Dossier de départ.

        filename : str
            Nom du fichier recherché.

        Returns
        -------
        Path | None
            Chemin du fichier si trouvé, sinon None.
        """
        for file in root.rglob(filename):
            return file

        return None