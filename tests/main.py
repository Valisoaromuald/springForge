from models.entity_metadata import EntityMetadata
from generators.repository_generator import RepositoryGenerator
from pathlib import Path
from utils.file_writer import FileWriter
from core.template_engine import TemplateEngine
def main():
    generator = RepositoryGenerator(TemplateEngine())
    metadata = EntityMetadata(
        package="com.example.demo.model",
        class_name="Client",
        id_type="Long"
    )

    generator.generate_file(
        metadata,
        Path("templates/repository/repository.java.tpl"),
        Path("generated/ClientRepository.java"),
        FileWriter()
    )


if __name__ == "__main__":
    main()