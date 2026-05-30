#!/usr/bin/env python3
"""
setup_workspace.py

Automation script to bootstrap the 12-month Medical AI Engineer career transition workspace.
Scaffolds modular directories (m01 - m10) with subdirectories (theory, labs, notes),
populates local module-specific READMEs highlighting strategic goals and superpower bridges,
and generates the root files.
"""

import os
import sys
from pathlib import Path
from typing import Dict

MODULES: Dict[str, Dict[str, str]] = {
    "m01_python_foundations": {
        "title": "Module 1: AI Engineering Foundations & Python Ecosystem",
        "description": "Production-grade Python development, GIL, memory management, high-throughput web servers, and C-extension structures.",
        "bridge": "The Mobile Advantage: You already understand application memory constraints, CPU profiling, and event loops. We translate these to CPython's GIL, memory arenas (PyObject allocations), and asyncio loops to optimize high-performance AI services."
    },
    "m02_vector_databases": {
        "title": "Module 2: Data Engineering & Vector Databases",
        "description": "High-dimensional vector index structures, search algorithms, compression techniques, and metadata filtering.",
        "bridge": "The Physics Advantage: Multi-dimensional vector spaces and distance metrics (Cosine similarity, L2 Euclidean distance) share exact mathematical formulations with classical mechanics coordinate systems and spatial dot-product projection."
    },
    "m03_machine_learning": {
        "title": "Module 3: Core Machine Learning Intuition",
        "description": "Foundational linear algebra, matrix factorization, classical models, objective loss functions, and evaluation metrics.",
        "bridge": "The Physics Advantage: Singular Value Decomposition (SVD) and PCA are mathematically identical to finding Principal Axes of Inertia and diagonalizing symmetric tensors. Information entropy in decision trees is equivalent to thermodynamic entropy."
    },
    "m04_deep_learning_cv": {
        "title": "Module 4: Deep Learning Fundamentals & Computer Vision",
        "description": "Neural networks from scratch, multi-dimensional calculus, custom backpropagation, CNN architectures, and GPU computation.",
        "bridge": "The Physics & Mobile Advantage: Backpropagation is multivariate calculus and the chain rule (similar to Lagrangian field theory). Convolutional kernels are mathematical filters (similar to digital signal processing Fourier/convolution operations). On the mobile side, GPU compute and custom CUDA execution map to metal shaders and rendering pipeline shaders."
    },
    "m05_llm_transformers": {
        "title": "Module 5: LLMs & Prompt Engineering",
        "description": "Attention mechanism, KV caching, rotary embeddings (RoPE), positional encodings, and tokenization mechanics.",
        "bridge": "The Physics Advantage: Multi-head attention scores compute similarity between query and key vectors, analogous to quantum state overlaps or coupled harmonic oscillator systems. Positional encodings (sine/cosine waves) map to spatial wave phase representation."
    },
    "m06_advanced_rag": {
        "title": "Module 6: Advanced Retrieval-Augmented Generation (RAG)",
        "description": "Information retrieval, late interaction search (ColBERT), reranking architectures, and multimodal embeddings.",
        "bridge": "The Mobile Advantage: Building responsive, low-latency client applications translates to optimizing multi-stage retrieval pipelines where search quality must be balanced against inference response latency."
    },
    "m07_agentic_ai": {
        "title": "Module 7: Agentic AI & Multi-Agent Frameworks",
        "description": "Stateful agentic architectures, tool usage, cyclic execution graphs, and dynamic user interfaces.",
        "bridge": "The Mobile Advantage: Designing app architectures using state machines (e.g., Redux, MVI, or state restoration) directly prepares you to build reliable, cyclic multi-agent topologies (e.g., LangGraph state schemas) without race conditions."
    },
    "m08_model_optimization": {
        "title": "Module 8: Model Optimization & Edge Deployment",
        "description": "Post-training quantization (PTQ), quantization-aware training (QAT), ONNX runtimes, and mobile deployment pipelines.",
        "bridge": "The Mobile & Physics Advantage: Your premier mobile knowledge of NPUs, DSPs, Apple CoreML, and Android TFLite is a rare edge. We combine this with your physics intuition of precision quantization error (analog-to-digital signal conversion noise) to compile models for edge devices."
    },
    "m09_observability_llmops": {
        "title": "Module 9: AI Observability & Evaluation (LLMOps)",
        "description": "CI/CD for AI models, automated evaluation (G-Eval), telemetry data capture, cost-reduction, and inference caching.",
        "bridge": "The Mobile Advantage: Mobile application crash reporting (Crashlytics) and analytics instrumentation match the philosophy of AI telemetry (LangSmith/MLflow). You know how to log telemetry without impacting application execution thread pools."
    },
    "m10_medical_ai": {
        "title": "Module 10: Medical AI & Systems Integration",
        "description": "DICOM/NIfTI parsing, k-space reconstruction, 3D segmentation (U-Net/YOLO), ISO 13485 regulatory compliance, and HIPAA safety.",
        "bridge": "The Physics Advantage: Medical scanners (MRI, CT, Ultrasound) are sensor instruments. MRI reconstruction utilizes raw k-space data, which is mathematically related to image space via the Fourier Transform. Ultrasound beamforming is wave superposition. You understand the physical capture mechanism, which is an elite differentiator."
    }
}

MODULE_README_TEMPLATE: str = """# {title}

## 🎯 Strategic Focus
{description}

---

## ⚡ Superpower Bridge
{bridge}

---

## 📂 Subdirectories
*   `theory/`: Mathematical foundations, architecture reviews, and scientific literature.
*   `labs/`: Structured coding implementations, benchmark tests, and code projects.
*   `notes/`: Personal takeaways, cheatsheets, and concept mappings.

---

## 📅 Target Checklist
- [ ] Read module fundamentals and complete theory reviews
- [ ] Implement core math/algorithms from scratch
- [ ] Complete high-performance labs
- [ ] Synthesize notes and link with previous modules
"""

def setup_workspace(root_dir: Path) -> None:
    print(f"[*] Scaffolding Medical AI learning workspace under: {root_dir}")
    
    # Create modules directory
    modules_dir: Path = root_dir / "modules"
    modules_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate each module
    for mod_name, mod_info in MODULES.items():
        mod_path: Path = modules_dir / mod_name
        print(f"    - Setting up {mod_name}...")
        
        # Create subdirectories
        (mod_path / "theory").mkdir(parents=True, exist_ok=True)
        (mod_path / "labs").mkdir(parents=True, exist_ok=True)
        (mod_path / "notes").mkdir(parents=True, exist_ok=True)
        
        # Write module README.md
        readme_content: str = MODULE_README_TEMPLATE.format(
            title=mod_info["title"],
            description=mod_info["description"],
            bridge=mod_info["bridge"]
        )
        
        with open(mod_path / "README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
            
    print("[+] Workspace directories and READMEs scaffolded successfully.")

if __name__ == "__main__":
    workspace_root: Path = Path(__file__).resolve().parent.parent
    setup_workspace(workspace_root)
