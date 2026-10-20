from models.entity_metadata import EntityMetadata
from generators.repository_generator import RepositoryGenerator
from pathlib import Path
from utils.file_writer import FileWriter
from core.template_engine import TemplateEngine
from core.package_resolver import PackageResolver
from parsers.entity_parser import EntityParser
def main():
    generator = RepositoryGenerator(TemplateEngine(),PackageResolver())
    entity_parser = EntityParser(Path("tests/resources"))
    entity_path = entity_parser.find_entity("Client")
    metadata = entity_parser.parse_entity(entity_path)
    print(f"{metadata}")
    generator.generate_file(
        metadata,
        Path("templates/repository/repository.java.tpl"),
        Path("tests/resources/repository/ClientRepository.java"),
        FileWriter()
    )


if __name__ == "__main__":
    main()
