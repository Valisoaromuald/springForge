from dataclasses import dataclass, asdict

@dataclass
class TemplateContext:
    def to_dict(self) -> dict[str, Any]:
       return asdict(self)
        
        