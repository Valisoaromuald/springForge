# Architecture

SpringForge est organisé en plusieurs modules afin de respecter le principe de responsabilité unique (Single Responsibility Principle).

## Vue d'ensemble

```
Utilisateur
      │
      ▼
generate_microservice.py
      │
      ▼
Generator
      │
      ├───────────────┐
      ▼               ▼
Parsers         Generators
      │               │
      └──────┬────────┘
             ▼
      Template Engine
             │
             ▼
      Fichiers Java
```

---

## config/

Contient la configuration globale du projet.

Exemples :

- constantes
- paramètres
- options par défaut

---

## core/

Contient le moteur principal.

Responsabilités :

- détecter le projet
- lire les templates
- coordonner les générateurs
- mettre à jour le pom.xml

---

## generators/

Chaque générateur possède une seule responsabilité.

Exemples :

- RepositoryGenerator
- ServiceGenerator
- ControllerGenerator

---

## parsers/

Analyse les fichiers Java.

Exemples :

- lecture des annotations
- lecture des imports
- récupération de la clé primaire
- lecture des packages

---

## templates/

Contient tous les modèles Java.

Les générateurs remplacent simplement les variables présentes dans les templates.

Exemple :

```
${Entity}
${Repository}
${Package}
```

---

## utils/

Fonctions utilitaires.

Exemples :

- manipulation de fichiers
- affichage console
- pluralisation
- logger

---

## docs/

Documentation du projet.

Chaque nouvelle fonctionnalité devra être documentée dans ce dossier.