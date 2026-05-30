## 1. Setup Script Execution Updates

- [x] 1.1 Update metadata structure in `scripts/setup_workspace.py` to contain the detailed 38 submodules and their descriptions/bridges
- [x] 1.2 Implement nested folder generation and legacy flat directory cleanup in `scripts/setup_workspace.py`

## 2. Directory Scaffolding

- [x] 2.1 Execute the updated setup script using `uv run scripts/setup_workspace.py`

## 3. Verification

- [x] 3.1 Verify nested directory layout (e.g., theory/labs/notes inside submodule folders)
- [x] 3.2 Verify legacy empty flat folders at module roots have been removed
