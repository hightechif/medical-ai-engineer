#!/usr/bin/env python3
"""
setup_workspace.py

Automation script to bootstrap the 12-month Medical AI Engineer career transition workspace.
Scaffolds modular directories (m01 - m10) with submodule subdirectories (s11, s12, ...),
populates local submodule-specific READMEs highlighting strategic goals and superpower bridges,
and cleans up empty legacy folders.
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, TypedDict

class SubmoduleMetadata(TypedDict):
    folder: str
    title: str
    description: str
    bridge: str

class ModuleMetadata(TypedDict):
    title: str
    submodules: List[SubmoduleMetadata]

MODULES: Dict[str, ModuleMetadata] = {
    "m01_python_foundations": {
        "title": "Module 1: AI Engineering Foundations & Python Ecosystem",
        "submodules": [
            {
                "folder": "s11_advanced_production_python",
                "title": "Submodule 1.1: Advanced Production Python",
                "description": "Generators, Decorators, CPython GIL, Multiprocessing, and concurrent programming models.",
                "bridge": "The Mobile Advantage: You are already familiar with application loop structures, threading constraints, and background task dispatchers (like GCD or handlers). We translate these to CPython process architectures, GIL-bypass techniques, and asyncio co-routines."
            },
            {
                "folder": "s12_async_backend_api",
                "title": "Submodule 1.2: Asynchronous Backend API Development",
                "description": "FastAPI async endpoints, WebSockets for low-latency diagnostic feeds, and strict JSON schemas.",
                "bridge": "The Mobile Advantage: You understand client-side networking layer architectures, serialization/deserialization, and reactive state updates. This lets you build high-performance async backends with zero-copy networking principles."
            },
            {
                "folder": "s13_data_manipulation_libraries",
                "title": "Submodule 1.3: Data Manipulation Libraries",
                "description": "NumPy array vectorization and Polars/Pandas high-performance dataframe operations.",
                "bridge": "The Physics Advantage: Multi-dimensional array manipulations are matrices. Your physics training in tensor mathematics and linear transformations makes the indexing and broadcasting operations of NumPy feel like second nature."
            },
            {
                "folder": "s14_enterprise_containerization",
                "title": "Submodule 1.4: Enterprise Containerization & Dependency Tracking",
                "description": "Docker container virtualization and strict UV dependency trees.",
                "bridge": "The Mobile Advantage: App sandboxing and target builds (like Xcode scheme configurations or Gradle files) share conceptual logic with container isolation and multi-stage build pipelines."
            }
        ]
    },
    "m02_vector_databases": {
        "title": "Module 2: Data Engineering & Vector Databases",
        "submodules": [
            {
                "folder": "s21_sql_nosql_extraction",
                "title": "Submodule 2.1: SQL & NoSQL Data Extraction",
                "description": "Data pipelines, high-throughput extraction, database schema design, and SQLAlchemy ORM integrations.",
                "bridge": "The Mobile Advantage: Local database optimization techniques (like SQLite/Room indices, transaction batching, and schema migrations) directly prepare you for enterprise-grade database management."
            },
            {
                "folder": "s22_text_image_chunking",
                "title": "Submodule 2.2: Text/Image Chunking Strategies",
                "description": "Fixed-size, semantic chunking, and sliding window boundaries.",
                "bridge": "The Physics Advantage: Signal windowing (like Short-Time Fourier Transforms) uses overlapping sliding windows to preserve frequency-domain continuity. This is mathematically identical to token-overlapping sliding windows used in text chunking."
            },
            {
                "folder": "s23_data_embeddings",
                "title": "Submodule 2.3: Data Embeddings",
                "description": "High-dimensional vector representations using OpenAI and HuggingFace models.",
                "bridge": "The Physics Advantage: Wavefunctions in quantum mechanics are elements of an infinite-dimensional Hilbert space. Concept representation in embedding spaces behaves under the same linear algebra projection laws."
            },
            {
                "folder": "s24_vector_db_hnsw",
                "title": "Submodule 2.4: Vector Database Administration & Indexing",
                "description": "Qdrant configuration, index optimization, and Hierarchical Navigable Small World (HNSW) graphs.",
                "bridge": "The Mobile & Physics Advantage: HNSW indexes search high-dimensional spaces using proximity graphs, analogous to finding paths in statistical physical networks. We design these indices under the CPU cache constraints of edge runtimes."
            }
        ]
    },
    "m03_machine_learning": {
        "title": "Module 3: Core Machine Learning Intuition",
        "submodules": [
            {
                "folder": "s31_linear_algebra_stats",
                "title": "Submodule 3.1: Linear Algebra & Statistics Foundations",
                "description": "Matrix factorization, covariance matrices, eigenvalue/eigenvector decompositions, and probability distributions.",
                "bridge": "The Physics Advantage: Eigenvalue equations are the core of quantum wave mechanics (Schrödinger equation) and stress analysis. You already know how to diagonalize matrices and calculate probability densities."
            },
            {
                "folder": "s32_supervised_learning",
                "title": "Submodule 3.2: Supervised Learning Models",
                "description": "Regressions, Decision Trees, Random Forests, and Gradient Boosted Trees (XGBoost).",
                "bridge": "The Physics Advantage: Fitting equations of state to empirical observations matches supervised regressions. Decoupled tree ensembles map to statistical partition functions over path variations."
            },
            {
                "folder": "s33_unsupervised_learning",
                "title": "Submodule 3.3: Unsupervised Learning & Dimensionality Reduction",
                "description": "K-Means Clustering and Principal Component Analysis (PCA) dimensionality reduction.",
                "bridge": "The Physics Advantage: PCA is mathematically identical to finding the Principal Axes of Inertia in rigid-body dynamics. Clustering maps to phase separation boundaries in statistical physics."
            },
            {
                "folder": "s34_model_evaluation",
                "title": "Submodule 3.4: Model Evaluation Metrics",
                "description": "ROC-AUC curves, Precision, Recall, F1-Score, and overfitting/underfitting regularization mitigation.",
                "bridge": "The Physics Advantage: Signal Detection Theory (ROC analysis) originated in electrical and radar sensor engineering. You understand false-alarm-rate tradeoffs at the physical sensor level."
            }
        ]
    },
    "m04_deep_learning_cv": {
        "title": "Module 4: Deep Learning Fundamentals & Computer Vision",
        "submodules": [
            {
                "folder": "s41_neural_networks_backprop",
                "title": "Submodule 4.1: ANNs, Backpropagation & Loss Functions",
                "description": "Deep Neural Network architectures, backpropagation calculus, and customized gradient descent.",
                "bridge": "The Physics Advantage: Backpropagation is multivariate calculus and the chain rule of partial derivatives, similar to finding extremum trajectories in Classical Lagrangian Mechanics (Euler-Lagrange equations)."
            },
            {
                "folder": "s42_cnn_spatial_processing",
                "title": "Submodule 4.2: Convolutional Neural Networks (CNNs)",
                "description": "Spatial and structural image convolutions, stride layouts, and pooling.",
                "bridge": "The Physics Advantage: Convolution is a fundamental operator in wave propagation and signal response calculations. Your experience with green functions and Fourier convolution integrals makes deep CNN layers highly intuitive."
            },
            {
                "folder": "s43_transfer_learning_vision",
                "title": "Submodule 4.3: Transfer Learning & Vision Transformers",
                "description": "Fine-tuning pre-trained vision models (ResNet, ConvNeXt, ViT).",
                "bridge": "The Mobile Advantage: Utilizing pre-compiled platform libraries (like CoreGraphics or Metal shading libraries) maps conceptually to transfer learning—reusing complex pre-optimized feature extractors."
            },
            {
                "folder": "s44_gpu_acceleration_cuda",
                "title": "Submodule 4.4: GPU Acceleration & CUDA Optimization",
                "description": "VRAM constraint management, kernel profiling, and PyTorch CUDA tensors.",
                "bridge": "The Mobile Advantage: You understand rendering loops, frame rates, and mobile GPU constraints (e.g. Apple Metal API, OpenGL ES). You translate this directly to maximizing throughput and avoiding CPU-GPU memory copy bottlenecks."
            }
        ]
    },
    "m05_llm_transformers": {
        "title": "Module 5: LLMs & Prompt Engineering",
        "submodules": [
            {
                "folder": "s51_transformer_mechanics",
                "title": "Submodule 5.1: Transformer Architecture Mechanics",
                "description": "Self-attention mechanics, Byte-Pair Encoding (BPE), context windows, and Rotary Positional Embeddings (RoPE).",
                "bridge": "The Physics Advantage: Positional encodings (sinusoidal waves) and RoPE (complex rotations) share equations with spatial wave phase modulation and rotational mechanics in physics."
            },
            {
                "folder": "s52_advanced_prompt_techniques",
                "title": "Submodule 5.2: Advanced Prompt Techniques",
                "description": "Few-shot learning, Chain-of-Thought (CoT), and ReAct autonomous loops.",
                "bridge": "The Mobile Advantage: Prompt patterns function as runtime instructions. Your experience writing robust event-driven system scripts allows you to structure LLM inputs as clear state-machine transitions."
            },
            {
                "folder": "s53_hyperparameter_tuning",
                "title": "Submodule 5.3: Hyperparameter Tuning at Runtime",
                "description": "Temperature, Top-p, Top-k, frequency penalties, and token generation limit controls.",
                "bridge": "The Physics Advantage: Temperature in generative sampling is based on the thermodynamic Boltzmann distribution. Higher temperature increases entropy, causing particles (tokens) to occupy higher energy (less likely) states."
            },
            {
                "folder": "s54_api_integration",
                "title": "Submodule 5.4: Commercial & Open-Source API Integration",
                "description": "Integrating OpenAI, Anthropic, Gemini, and local Ollama runtimes.",
                "bridge": "The Mobile Advantage: Implementing robust API integration with failover handling, exponential backoff, rate limiting, and network retry state machines is a staple of senior mobile engineering."
            }
        ]
    },
    "m06_advanced_rag": {
        "title": "Module 6: Advanced Retrieval-Augmented Generation (RAG)",
        "submodules": [
            {
                "folder": "s61_semantic_search_reranking",
                "title": "Submodule 6.1: Semantic Search & Reranking Systems",
                "description": "Bi-encoders, cross-encoders, and ColBERT late interaction matching.",
                "bridge": "The Mobile Advantage: You understand performance budgets. Balancing fast coarse-stage retrieval (Bi-encoder) with slow precision ranking (Cross-encoder) maps to designing multi-tier mobile view rendering models."
            },
            {
                "folder": "s62_advanced_retrieval_patterns",
                "title": "Submodule 6.2: Advanced Retrieval Patterns",
                "description": "Parent-Child chunk retrieval, HyDE query generation, and self-query structures.",
                "bridge": "The Mobile Advantage: Database normalization, lazy-loading, and fetching hierarchical tree structures (like recursive JSON parses) align with parent-child chunk mapping mechanics."
            },
            {
                "folder": "s63_multimodal_rag",
                "title": "Submodule 6.3: Multi-modal RAG",
                "description": "Retrieving and embedding images, medical charts, and structured diagrams alongside text.",
                "bridge": "The Physics Advantage: Multimodal integration maps to multi-sensor fusion. Combining data from distinct modalities (text, visual data) follows vector projection methods used to unify telemetry sensors."
            },
            {
                "folder": "s64_rag_triage_hallucination",
                "title": "Submodule 6.4: RAG Triage & Hallucination Defense",
                "description": "Guardrails, context validation, hallucination checking, and secure data access.",
                "bridge": "The Mobile Advantage: Edge input verification and validation pipelines (to prevent UI failures and buffer overflows) translate directly to validating LLM context windows."
            }
        ]
    },
    "m07_agentic_ai": {
        "title": "Module 7: Agentic AI & Multi-Agent Frameworks",
        "submodules": [
            {
                "folder": "s71_function_calling_tool_use",
                "title": "Submodule 7.1: Function Calling / Tool Use Patterns",
                "description": "Dynamic function schemas, JSON validation, and safe API execution.",
                "bridge": "The Mobile Advantage: Interface boundary design, IPC serialization, and callbacks map directly to function calling protocols where the model executes tools dynamically."
            },
            {
                "folder": "s72_autonomous_loops_memory",
                "title": "Submodule 7.2: Autonomous Loops & Agent Memory Management",
                "description": "Stateful agentic feedback loops, short-term session storage, and long-term semantic memory databases.",
                "bridge": "The Mobile Advantage: Custom caching, cache invalidation, and state restoration (e.g. saving state during mobile application suspension) translate to managing persistent agent state maps."
            },
            {
                "folder": "s73_orchestration_frameworks",
                "title": "Submodule 7.3: Orchestration Frameworks",
                "description": "LangGraph, CrewAI, and LangChain orchestration pipelines.",
                "bridge": "The Mobile Advantage: Building cyclic UI graphs, screen navigators, and reactive state systems prepared you to construct resilient state topologies in LangGraph without deadlocks."
            },
            {
                "folder": "s74_generative_ui",
                "title": "Submodule 7.4: Generative UI Component Orchestration",
                "description": "Configuring agents to request interactive widgets (charts, graphs, forms) dynamically.",
                "bridge": "The Mobile Advantage: Dynamic view composition, server-driven UI layouts, and reactive components are premier skills in modern mobile development."
            }
        ]
    },
    "m08_model_optimization": {
        "title": "Module 8: Model Optimization & Edge Deployment",
        "submodules": [
            {
                "folder": "s81_model_quantization",
                "title": "Submodule 8.1: Model Quantization Mechanics",
                "description": "Quantization-Aware Training (QAT), Post-Training Quantization (PTQ), FP16, INT8, and INT4 precision conversions.",
                "bridge": "The Physics Advantage: ADC (Analog-to-Digital Conversion) quantization noise is a classic physical signal processing concept. The mathematics of quantization bins and noise bounds directly apply to weight scaling metrics."
            },
            {
                "folder": "s82_mobile_ai_runtimes",
                "title": "Submodule 8.2: Mobile AI Runtimes",
                "description": "CoreML compiler execution on iOS Neural Engine, TFLite runtimes, and cross-platform ONNX Runtime integration.",
                "bridge": "The Mobile Advantage: Deploying models on iOS/Android, linking NPU runtimes, profiling thread affinity, and optimizing application binary sizes represents your elite system domain advantage."
            },
            {
                "folder": "s83_local_compilation_hardware",
                "title": "Submodule 8.3: Local Compilation Pipelines",
                "description": "Hardware compilation, compiler backends, and local deployment loops on target device hardware.",
                "bridge": "The Mobile & Physics Advantage: Low-level compiler toolchains, binary linkers, and instruction set optimization map to both physics hardware modeling and senior mobile systems profiling."
            }
        ]
    },
    "m09_observability_llmops": {
        "title": "Module 9: AI Observability & Evaluation (LLMOps)",
        "submodules": [
            {
                "folder": "s91_prompt_versioning_cicd",
                "title": "Submodule 9.1: Prompt Versioning & CI/CD for AI",
                "description": "CI/CD automated testing for prompts and code layers, version tagging, and model releases.",
                "bridge": "The Mobile Advantage: Releasing mobile software requires rigorous store distribution pipelines, linting, and automated unit tests. Applying this to prompt deployment pipelines guarantees runtime reliability."
            },
            {
                "folder": "s92_logging_tracing_telemetry",
                "title": "Submodule 9.2: Continuous Logging & Tracing Telemetry",
                "description": "Logging and tracing calls using LangSmith, MLflow, and W&B.",
                "bridge": "The Mobile Advantage: Real-time telemetry, error tracking (Sentry/Crashlytics), and analytic capture systems mirror LLMOps monitoring. You know how to implement logging cleanly without causing UI delays."
            },
            {
                "folder": "s93_automated_evaluation",
                "title": "Submodule 9.3: Automated Evaluation Frameworks",
                "description": "Ragas, TruLens metrics, G-Eval, and LLM-as-a-judge methodologies.",
                "bridge": "The Physics Advantage: Standardizing metrics under experimental uncertainty requires variance calculation and confidence interval parsing—skills foundational to scientific data validation."
            },
            {
                "folder": "s94_cost_rate_limiting_cache",
                "title": "Submodule 9.4: Cost Management, Rate-Limiting & Caching",
                "description": "Semantic caching (GPTCache), rate-limiting middleware, and token expenditure monitoring.",
                "bridge": "The Mobile Advantage: Optimizing offline caching, payload data compression, and local rate limiting are core strategies for mobile network client libraries."
            }
        ]
    },
    "m10_medical_ai": {
        "title": "Module 10: Medical AI & Systems Integration",
        "submodules": [
            {
                "folder": "s101_medical_image_parsing",
                "title": "Submodule 10.1: Medical Image Formats & Parsing",
                "description": "DICOM metadata, NIfTI volumes, voxels, and raw k-space representations.",
                "bridge": "The Physics Advantage: Medical imaging technologies are physics instruments. MRI scanners acquire raw signals in k-space. The translation to anatomical images is done via 2D/3D Fourier Transforms. You understand the physics of acquisition."
            },
            {
                "folder": "s102_deep_learning_segmentation",
                "title": "Submodule 10.2: Deep Learning for Medical Segmentation",
                "description": "U-Net convolutional segmentation, YOLO object detection, and 3D segmentation architectures in healthcare.",
                "bridge": "The Physics Advantage: Segmenting boundaries and calculating physical volumes is similar to field boundary modeling and grid simulations in engineering physics."
            },
            {
                "folder": "s103_safety_compliance_protocols",
                "title": "Submodule 10.3: Medical Safety & Compliance Protocols",
                "description": "ISO 13485 (Medical Device Software Quality), HIPAA security rules, and FDA 510(k) pathway requirements.",
                "bridge": "The Mobile & Physics Advantage: Regulated devices demand strict software quality controls, audit trails, and data isolation. Your mobile knowledge of biometric encryption combined with engineering documentation standards supports safety compliance."
            }
        ]
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
- [ ] Read submodule fundamentals and complete theory reviews
- [ ] Implement core math/algorithms from scratch
- [ ] Complete high-performance labs
- [ ] Synthesize notes and link with previous modules
"""

def setup_workspace(root_dir: Path) -> None:
    print(f"[*] Re-scaffolding Medical AI learning workspace under: {root_dir}")
    
    modules_dir: Path = root_dir / "modules"
    modules_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate each module
    for mod_folder, mod_info in MODULES.items():
        mod_path: Path = modules_dir / mod_folder
        print(f"    - Setting up module: {mod_folder}...")
        mod_path.mkdir(parents=True, exist_ok=True)
        
        # Clean up legacy flat directories if they exist directly at module root
        for legacy_dir in ["theory", "labs", "notes"]:
            legacy_path: Path = mod_path / legacy_dir
            if legacy_path.exists():
                print(f"      [Pruning] Removing legacy directory: {legacy_path.relative_to(root_dir)}")
                shutil.rmtree(legacy_path)
                
        # Generate nested submodules
        for submod in mod_info["submodules"]:
            submod_folder: str = submod["folder"]
            submod_path: Path = mod_path / submod_folder
            print(f"      * Scaffolding submodule: {submod_folder}...")
            
            # Create submodule subdirectories
            (submod_path / "theory").mkdir(parents=True, exist_ok=True)
            (submod_path / "labs").mkdir(parents=True, exist_ok=True)
            (submod_path / "notes").mkdir(parents=True, exist_ok=True)
            
            # Write submodule README.md
            readme_content: str = MODULE_README_TEMPLATE.format(
                title=submod["title"],
                description=submod["description"],
                bridge=submod["bridge"]
            )
            
            with open(submod_path / "README.md", "w", encoding="utf-8") as f:
                f.write(readme_content)
                
    print("[+] Workspace reorganized and READMEs scaffolded successfully.")

if __name__ == "__main__":
    workspace_root: Path = Path(__file__).resolve().parent.parent
    setup_workspace(workspace_root)
