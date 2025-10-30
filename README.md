# a-maze-ing

## README Contents

1. Description
1. Authors
1. Installation
1. Requirements
1. Tests
1. Usage
1. File Structure
1. Domain Model

## External README Contents

1. [Team Agreement](team_agreement.md)
1. [Project Ideas](project_ideas.md)
1. [Project Design](project_design.md)
1. [Requirements](requirements.md)

## Description

This is a command-line interface to create and solve mazes. A client will be able to generate new mazes and save them as binary files. The client will also be able to generate a solution for a maze and save its image.

## Authors

[KP Gomez](https://github.com/kpgomez)

[Jacob Bassett](https://github.com/jdabassett)

## Installation

Run the following commands to clone and set up a local environment.

```bash
git clone https://github.com/amazing-maze-solver/a-maze-ing.git
cd a-maze-ing
python3 -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows (PowerShell): .venv\Scripts\Activate.ps1
```

## Requirements

This project uses a locked dependency set in `requirements.txt` (with hashes) compiled from `requirements.in`.

Fast start (no extra tooling):

```bash
pip install -r requirements.txt
```

Reproducible installs (recommended, requires pip-tools):

```bash
pip install "pip==24.0" "setuptools<72" wheel
pip install pip-tools
pip-sync requirements.txt
```

Updating dependencies (maintainers):

```bash
# Edit top-level deps in requirements.in
.venv/bin/pip-compile --generate-hashes -o requirements.txt requirements.in
.venv/bin/pip-sync requirements.txt
```

## Tests

Run the following command in the terminal to run all tests.

```bash
pytest --cov
```

## Usage

Run the following command in the terminal to start the application.

```bash
python3 -m scripts.main
```

## File Structure

```bash
.
├── README.md
├── requirements.in
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── location_classes.py
│   ├── location_functions.py
│   └── main.py
├── src
│   ├── generate
│   │   ├── __init__.py
│   │   ├── convert_api_maze.py
│   │   └── create_maze.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── border.py
│   │   ├── maze.py
│   │   ├── role.py
│   │   ├── solution.py
│   │   └── square.py
│   ├── persistence
│   │   ├── __init__.py
│   │   ├── file_format.py
│   │   └── serializer.py
│   ├── solve
│   │   ├── __init__.py
│   │   └── solver.py
│   └── view
│       ├── __init__.py
│       ├── decomposer.py
│       ├── primitives.py
│       └── renderer.py
└── tests
    ├── __init__.py
    ├── test_generate.py
    ├── test_menu.py
    ├── test_models.py
    ├── test_persistence.py
    ├── test_solve.py
    └── test_view.py
```

## Domain Model

This is the basic domain model from the tutorial.
We will be recreating a version of this and adding new features like generating new mazes and converting the solution into a movie.
![basic_domain_model](resources/images/domain-model.png)
