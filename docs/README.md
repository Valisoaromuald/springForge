# SpringForge

SpringForge est un générateur de code Spring Boot développé en Python.

Son objectif est de réduire le temps de développement en générant automatiquement les différentes couches d'une application Spring Boot à partir d'une entité existante.

## Fonctionnalités

- Génération de Repository
- Génération de Service
- Génération de ServiceImpl
- Génération de Controller
- Support de JpaRepository
- Support de CrudRepository
- Support RestController
- Support Controller MVC
- Analyse automatique des entités Java
- Mise à jour automatique du pom.xml
- Compatible avec les architectures Microservices
- Compatible avec les architectures N-Tiers

## Fonctionnalités prévues

- DTO
- Mapper (MapStruct)
- Validation
- Exception Handler
- OpenAPI / Swagger
- Specifications JPA
- Tests unitaires
- Génération de documentation

## Structure du projet

```
SpringForge/
│
├── generate_microservice.py
├── generate_ntiers.py
├── config/
├── core/
├── generators/
├── parsers/
├── templates/
├── utils/
└── docs/
```

## Démarrage rapide

Installer les dépendances

```bash
pip install -r requirements.txt
```

Architecture Microservice

```bash
python generate_microservice.py
```

Architecture N-Tiers

```bash
python generate_ntiers.py
```

## Licence

Projet personnel développé à des fins d'apprentissage et de productivité.