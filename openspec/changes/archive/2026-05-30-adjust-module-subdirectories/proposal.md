## Why

To support granular learning tracking, each of the 10 modules must have dedicated subfolders for its respective submodules, containing independent `theory/`, `labs/`, and `notes/` directories. This prevents file clutter and aligns the physical workspace with the modular 12-month syllabus.

## What Changes

- Modify `scripts/setup_workspace.py` to support the nested submodule structure.
- Generate folders for each of the 38 submodules across the 10 core modules.
- Create local submodule `README.md` files describing the specific syllabus goals and the physics/mobile superpower bridges.
- Clean up legacy flat module folders (`theory/`, `labs/`, `notes/` at the module root level).

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `learning-workspace-structure`: Adjusts the directory tree from a module-flat configuration to a submodule-nested configuration.

## Impact

- Organizes the directory tree for better separation of concerns, enabling each lab to compile as its own package.
