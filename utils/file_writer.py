from pathlib import Path


class FileWriter:
    """
    Responsable de l'écriture des fichiers générés.
    """

    def write(
        self,
        file_path: Path,
        content: str
    ) -> None:

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)