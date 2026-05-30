## Context

The user provided a detailed list of modules and submodules. We are updating the directory tree from a flat module setup to a nested submodule setup (Option B chosen by the user).

## Goals / Non-Goals

**Goals:**
- Implement nested submodule folders (e.g. `modules/m01_python_foundations/s11_advanced_production_python/labs/`).
- Update `scripts/setup_workspace.py` to maintain all 38 submodules, descriptions, and superpower bridges.
- Clean up legacy root-level module subdirectories.

**Non-Goals:**
- Moving any active user files (the repository was just initialized, so no custom user code is in `theory/`, `labs/`, or `notes/` yet).

## Decisions

### 1. Submodule folder naming format
*   **Decision:** Use `sXY_kebab_case` (where `X` is module index and `Y` is submodule index, e.g., `s11_advanced_production_python`).
*   **Rationale:** Avoids dots (`.`) in folder names so python interpreters can import files under them without syntax issues, and maintains alphabetical/chronological sorting.

### 2. Auto-cleanup of flat folders
*   **Decision:** Add directory pruning logic to `scripts/setup_workspace.py` to delete empty legacy flat directories (`theory/`, `labs/`, `notes/` directly under `modules/mXX_name/`).
*   **Rationale:** Keeps the workspace clean and prevents redundant paths.

## Risks / Trade-offs

*   **Risk:** Deep directory nest limits terminal traversal speed.
    *   **Mitigation:** Provide clear relative paths and reference them directly in portfolio logs.
