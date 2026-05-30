## MODIFIED Requirements

### Requirement: Inner Directory Structure
Each submodule folder SHALL contain subdirectories for `theory/`, `labs/`, and `notes/`. The submodule folders SHALL be nested under their parent module folder (e.g., `modules/mXX_name/sXX_submodule_name/`).

#### Scenario: Verify inner module subdirectories
- **WHEN** directory creation completes
- **THEN** every folder under `modules/m*/s*` contains exactly the folders `theory`, `labs`, and `notes`.
