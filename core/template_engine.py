from pathlib import Path
from string import Template


class TemplateEngine:
    """
    Moteur de rendu des templates.
    """

    def render(self, template: str, variables: dict[str, str]) -> str:
        """
        Remplace les variables d'un template.

        Parameters
        ----------
        template : str
            Contenu du template.

        variables : dict[str, str]
            Variables à remplacer.

        Returns
        -------
        str
            Template généré.
        """

        return Template(template).substitute(variables)

    def render_file(
        self,
        template_path: Path,
        variables: dict[str, str]
    ) -> str:
        """
        Génère un template à partir d'un fichier.

        Parameters
        ----------
        template_path : Path
            Chemin du template.

        variables : dict[str, str]
            Variables à remplacer.

        Returns
        -------
        str
            Contenu généré.
        """

        with open(template_path, "r", encoding="utf-8") as file:
            template = file.read()

        return self.render(template, variables)