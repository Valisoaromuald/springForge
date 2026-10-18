
from pathlib import Path

from parsers.entity_parser import EntityParser

# Le parser cherchera l'entité dans le dossier tests/resources
parser = EntityParser(Path("tests/resources"))

entity_path = parser.find_entity("Client")

metadata = parser.parse_entity  (entity_path)

print(metadata)