# Medical AI Engineer Career Transition Portfolio

This repository contains the learning resources, codebase, mathematical proofs, and labs compiled during my 12-month career transition from a Senior Mobile Systems Engineer to an **Elite Medical AI Engineer**.

My ultimate target is to secure high-prestige roles in international MedTech firms (e.g., Philips, Siemens Healthineers, Roche) and admission to elite European Master's programs (e.g., ETH Zurich, TU Munich).

---

## 🚀 The 12-Month Timeline & Roadmap

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              12-MONTH STRATEGIC MILESTONES                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Month 01: [M1 & M2] Python AI Foundations & Vector DB / RAG Data Engineering           │
│ Month 02: [M3] Core Machine Learning Intuition (Stats, Regressions, Tree Architectures) │
│ Month 03: [M4] Deep Learning & Computer Vision (Backpropagation, CNNs, GPU/CUDA)        │
│ Month 04: [M10 (Part 1)] Medical Imaging Basics (DICOM, NIfTI, 2D/3D U-Net Segment)    │
│ Month 05: [M10 (Part 2)] Regulated Medical AI (ISO 13485, HIPAA, FDA 510(k) Paths)     │
│ Month 06: [M5] LLMs & Prompt Engineering (Transformers, Tokenizers, API Architecture)   │
│ Month 07: [M6] Advanced RAG (Bi/Cross-Encoders, Multimodal RAG, Hallucination Triage)  │
│ Month 08: [M7] Agentic AI & Clinical Decision Support Systems (LangGraph, StateMachines)│
│ Month 09: [M8] Edge Deployment & Hardware compilation (Quantization, CoreML/ONNX)      │
│ Month 10: [M9] LLMOps & Observability (LangSmith, CI/CD, Automated Evaluation)          │
│ Month 11: [Capstone] Production Medical AI System on Edge (Mobile-embedded Diagnosis)  │
│ Month 12: [Prestige] Portfolio Packaging, Academic Proposals, & Headhunting Pipeline   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ The Double-Threat Superpower Bridges

### 1. The Physics Advantage (UGM B.Eng. Engineering Physics)
*   **Medical Scanning Physics:** Direct mathematical mappings of electromagnetic and acoustic wave mechanics to MRI (k-space frequency representation), Ultrasound (beamforming physics), and CT (Radon transforms).
*   **Signal Processing & Transforms:** Deep understanding of filtering, Fourier transforms, and wave convolution directly translates to low-level CNN layer dynamics and raw scan preprocessing.
*   **Statistical Mechanics:** Core statistical metrics (entropy, diffusion paths, thermodynamic state equations) map to information gain algorithms and generative diffusion models.

### 2. The Mobile Advantage (Senior Mobile Engineer)
*   **System Constraints:** Expert in memory footprint reduction, cache optimizations, threading models, and low-latency response loops.
*   **Edge Compute Runtimes:** Unfair advantage compiling models using CoreML (Apple Neural Engine), TensorFlow Lite, and ONNX Runtime to target hardware-accelerated clinical environments.

---

## 📚 Curriculum Structure

The repository is organized into 10 modules under the `/modules/` directory:

| Folder | Module Title | Submodules & Focus Areas |
| :--- | :--- | :--- |
| [`m01_python_foundations`](./modules/m01_python_foundations) | AI Foundations & Python | PyObject layout, GIL concurrency, async event loops, zero-copy arrays |
| [`m02_vector_databases`](./modules/m02_vector_databases) | Data Eng & Vector DBs | HNSW graph generation, Product Quantization (PQ), IVF indexes |
| [`m03_machine_learning`](./modules/m03_machine_learning) | Core ML Intuition | SVD, PCA, Gini/Entropy tree splits, Gradient Boosting |
| [`m04_deep_learning_cv`](./modules/m04_deep_learning_cv) | DL & Computer Vision | Backpropagation calculus, custom CUDA kernels, ResNet skip connections |
| [`m05_llm_transformers`](./modules/m05_llm_transformers) | LLMs & Transformers | Attention math, BPE tokenizer, RoPE, KV Caching optimizations |
| [`m06_advanced_rag`](./modules/m06_advanced_rag) | Advanced RAG | Cross-encoders, ColBERT late interaction, CLIP projections |
| [`m07_agentic_ai`](./modules/m07_agentic_ai) | Agentic AI | Directed Acyclic Graphs (DAGs), cyclic state machines, ReAct loops |
| [`m08_model_optimization`](./modules/m08_model_optimization) | Model Optimization | PTQ vs QAT, Int8/FP4 quantization, ONNX graph optimization |
| [`m09_observability_llmops`](./modules/m09_observability_llmops) | Observability & LLMOps | G-Eval mathematical scoring, Semantic caching, MLflow telemetry |
| [`m10_medical_ai`](./modules/m10_medical_ai) | Medical AI Systems | DICOM parsing, 3D U-Net segmentation, ISO 13485 compliance |

---

## 🛠️ Repository Setup

### Prerequisites
- Python 3.11+ (managed automatically if using `uv`)
- [uv](https://github.com/astral-sh/uv) (fast Python package installer and resolver)

### Installation
1. Synchronize dependencies and automatically create/activate the virtual environment:
   ```bash
   uv sync
   ```
2. Run the automated workspace setup script to scaffold (or re-scaffold) the directory structure:
   ```bash
   uv run scripts/setup_workspace.py
   ```

