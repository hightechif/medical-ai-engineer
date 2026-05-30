## Context

The candidate is transitioning into a Medical AI engineering role. We need a standardized workspace structure to hold coding files, labs, notebook tutorials, and research notes. Currently, the repository has only the OpenSpec directories and configuration files.

## Goals / Non-Goals

**Goals:**
- Provide a clean, robust, and intuitive workspace directory structure.
- Scaffold folders for all 10 learning modules.
- Set up a python `pyproject.toml` and `.python-version` with high-prestige libraries for medical image processing, deep learning, vector databases, optimization, and evaluation.
- Document how physics and mobile engineering principles map to each module via structured subfolder READMEs.

**Non-Goals:**
- Writing actual machine learning models or pipelines in this setup phase.
- Populating full datasets (e.g., actual DICOM scan uploads) which must be done dynamically during the modules.

## Decisions

### 1. Programmatic Setup vs Manual Directory Creation
*   **Decision:** Build a python automation script `scripts/setup_workspace.py` to initialize the directory layout.
*   **Rationale:** Manual creation is prone to typos and inconsistency. Using a python script aligns with Module 1's goal of "Production Python" and provides a clean, repeatable bootstrap mechanism for future setups.

### 2. Module Folder Naming Convention
*   **Decision:** Use `modules/mXX_<kebab_case_name>` (e.g., `modules/m01_python_foundations`).
*   **Rationale:** Keeps directories sorted chronologically in IDE project trees, while keeping name components short and readable.

### 3. Dependencies Ecosystem Selection
*   **Decision:** Combine PyTorch, MONAI (medical DL), SimpleITK & Nibabel (DICOM/NIfTI parsing), Qdrant-Client (vector searches), ONNX/CoreML (edge compilation), and LangGraph (agentic loops).
*   **Rationale:** These libraries represent the absolute cutting edge of industry-grade medical AI engineering. We skip standard web-dev libraries in favor of high-performance ML libraries.

## Risks / Trade-offs

*   **Risk:** Pinned python packages may conflict on different hardware architectures (e.g., Apple Silicon vs Intel).
    *   **Mitigation:** We will group core packages without strict version pins first, letting pip resolve the most compatible versions for the user's current environment.
*   **Risk:** Directory bloat from 10 modules.
    *   **Mitigation:** Keep directories empty except for a template `README.md` inside each to serve as local syllabus checklists.
