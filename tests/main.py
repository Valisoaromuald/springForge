from models.entity_metadata import EntityMetadata
from generators.repository_generator import RepositoryGenerator
from pathlib import Path
from utils.file_writer import FileWriter
from core.template_engine import TemplateEngine
from core.package_resolver import PackageResolver
from parsers.entity_parser import EntityParser
def main():
    generator = RepositoryGenerator(TemplateEngine(),PackageResolver())
    project_path = Path(r"C:\Users\WINDOWS 10\Documents\Projets\springForge")
    entity_parser = EntityParser(project_path)
    entity_path = entity_parser.find_entity("Client")
    metadata = entity_parser.parse_entity(entity_path)
    generator.generate_file(
        project_path,
        metadata,
        Path("templates/repository/repository.java.tpl"),
        FileWriter()
    )


if __name__ == "__main__":
    main()
