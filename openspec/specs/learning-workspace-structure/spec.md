# Specification: Learning Workspace Structure

## Purpose
This specification defines the architecture, directory structure, environment defaults, and documentation standards for the candidate's 12-month Medical AI transition workspace.

---

## Requirements

### Requirement: Modular Directory Scaffolding
The workspace SHALL contain a `modules/` directory containing ten subdirectory folders corresponding to the learning modules.

#### Scenario: Verify modules folder initialization
- **WHEN** the setup script runs
- **THEN** folders `modules/m01_python_foundations`, `modules/m02_vector_databases`, `modules/m03_machine_learning`, `modules/m04_deep_learning_cv`, `modules/m05_llm_transformers`, `modules/m06_advanced_rag`, `modules/m07_agentic_ai`, `modules/m08_model_optimization`, `modules/m09_observability_llmops`, and `modules/m10_medical_ai` are created.

### Requirement: Inner Directory Structure
Each module folder SHALL contain subdirectories for `theory/`, `labs/`, and `notes/`.

#### Scenario: Verify inner module subdirectories
- **WHEN** directory creation completes
- **THEN** every folder under `modules/m*` contains exactly the folders `theory`, `labs`, and `notes`.

### Requirement: Python Environment Configuration
The root directory SHALL contain a `pyproject.toml` and `.python-version` file defining the python version (>=3.11) and modern packaging dependencies.

#### Scenario: Verify environment configuration files exist
- **WHEN** checking the root of the workspace
- **THEN** the files `pyproject.toml` and `.python-version` exist, containing dependency list and `3.11` respectively.

### Requirement: Master Portfolio README
The root directory SHALL contain a comprehensive `README.md` summarizing the curriculum, modules, learning targets, and progress tracking.

#### Scenario: Verify README content
- **WHEN** reading the root `README.md`
- **THEN** it displays a dashboard detailing the candidate's strategic career transition, UGM Engineering Physics / Mobile Superpower bridges, and module roadmap.
