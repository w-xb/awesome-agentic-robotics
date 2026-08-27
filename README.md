# Awesome Agentic Robotics [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <a href="#agentic-vla-and-embodied-foundation-models"><img src="https://img.shields.io/badge/Focus-Agentic%20VLA-7c3aed" alt="Focus: Agentic VLA"></a>
  <a href="#start-here--must-read"><img src="https://img.shields.io/badge/Reading-Must%20Read-0891b2" alt="Must Read guide"></a>
  <a href="contributing.md"><img src="https://img.shields.io/badge/PRs-welcome-22c55e" alt="PRs welcome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC0--1.0-2563eb" alt="CC0 1.0 license"></a>
</p>

<p align="center">
  A curated survey of physical agents: embodied memory, planning, world/action models, verification, failure recovery, skill use, and safety for autonomous robots.
</p>

**Last updated:** 2026-08-27

## Contents

- [What Agentic Robotics Means Here](#what-agentic-robotics-means-here)
- [Scope](#scope)
- [Start Here / Must Read](#start-here--must-read)
- [Surveys and Position Papers](#surveys-and-position-papers)
- [Agentic Robotics Architectures](#agentic-robotics-architectures)
- [Agentic VLA and Embodied Foundation Models](#agentic-vla-and-embodied-foundation-models)
- [Embodied Memory](#embodied-memory)
- [Planning and Reasoning](#planning-and-reasoning)
- [World Models and World-Action Models](#world-models-and-world-action-models)
- [Verification and Self-Evaluation](#verification-and-self-evaluation)
- [Failure Detection and Recovery](#failure-detection-and-recovery)
- [Skill Calling, Tool Use, and Robot Execution Interfaces](#skill-calling-tool-use-and-robot-execution-interfaces)
- [Long-Horizon Manipulation](#long-horizon-manipulation)
- [Embodied Navigation Agents](#embodied-navigation-agents)
- [Human-Robot Interaction and Dialogue Agents](#human-robot-interaction-and-dialogue-agents)
- [Safety, Governance, and Physical Risk](#safety-governance-and-physical-risk)
- [Benchmarks, Simulators, and Datasets](#benchmarks-simulators-and-datasets)
- [Open-Source Systems and Frameworks](#open-source-systems-and-frameworks)
- [Industrial Signals and Technical Reports](#industrial-signals-and-technical-reports)
- [Related Awesome Lists](#related-awesome-lists)
- [Citation](#citation)
- [Contact](#contact)

## What Agentic Robotics Means Here

Agentic Robotics is still an emerging and not-yet-standardized research direction. In this repository, we adopt an ability-centered view: a robotic system becomes more agentic when it can maintain task state, use memory, plan over future consequences, invoke skills or tools, verify execution, recover from failures, and operate under physical safety constraints.

Unlike many LLM agents, which are often organized as text-mediated loops of planning, memory, tool use, and reflection, robotic agents must act in the physical world. Their agency is therefore not only expressed through an external LLM-style agent loop, but also through embodied mechanisms such as spatial-temporal memory, action-conditioned world models, execution verification, failure attribution, recovery policies, and safety envelopes.

Not every work listed here is a full agentic robot system. Some papers contribute only one component of physical agency, such as memory, world modeling, verification, or recovery. The goal of this repository is to map these components and track how they are converging toward agentic embodied systems.

## Scope

This list includes works that contribute to at least one of the following capabilities:

- embodied memory and state maintenance
- planning, reasoning, and skill composition
- world models and world-action models
- execution verification and self-evaluation
- failure detection, attribution, and recovery
- tool use, skill calling, and robot API invocation
- long-horizon manipulation and navigation
- human-robot interaction for agentic execution
- safety, governance, and physical-risk constraints

We intentionally include both explicit LLM/VLM-agent architectures and tightly coupled robot learning methods, because agentic behavior in robotics can emerge from either modular orchestration or internal embodied state dynamics.

This repository follows a compact Awesome-list style: entries are grouped by topic and sorted by month in descending order. Each item uses the format:

`\[YYYY.M] [Venue/Org] Title [paper] [project] [code]`

**Paper ordering:** within each topic, entries use `\[YYYY.M]` and are sorted newest first.

---

## Start Here / Must Read

> Four short reading routes through the list. Each paper has one canonical entry in the topic sections below.

### VLA-as-Tools

**Harness VLA** — Treats a frozen VLA as a retryable contact-rich primitive inside a memory-guided agent that stages, verifies, and retries execution.

**VLAs-as-Tools** — Separates temporal reasoning from physical execution through a high-level VLM agent and a family of progress-aware VLA tools.

**Agentic Robot** — Organizes planning, VLA execution, temporal verification, and recovery through a structured Plan-Execute-Verify loop.

**ART** — Injects on-the-fly multimodal tool use into an end-to-end VLA while preserving continuous action generation.

### Hierarchical and Reasoning VLA

**τ_0-VLA** — Uses execution memory and world-model-guided test-time search for difficult high-level subtask decisions.

**G0.5** — Generates reasoning and action tokens in one autoregressive stream with visual memory and cross-embodiment action tokenization.

**Qwen-VLA** — Unifies manipulation, navigation, trajectory supervision, and multimodal co-training across tasks and embodiments.

**Gemini Robotics 1.5** — Couples generalist robot control with embodied reasoning and motion transfer across embodiments.

### Memory and World Models

**AtlasVLA** — Maintains a persistent world-ego state to address perception and task-progress forgetting in long-horizon control.

**MEMORA** — Builds editable and consolidated embodied action memory from egocentric experience for later planning.

**τ_0-WM** — Unifies action generation, future prediction, candidate evaluation, and simulator-based rectification.

**Faster-WAM** — Preserves inference-time future conditioning while reducing the cost of video-action interaction.

### Safety and Evaluation

**MANIGUARD** — Evaluates manipulation safety against explicit specifications and pairs the benchmark with safety-annotated trajectories.

**EgoSafetyBench** — Tests embodied VLMs as streaming safety guards on temporally annotated egocentric robot-view scenarios.

**SafeRelBench** — Measures process-level safety violations caused by changing spatial relations during embodied execution.

---

## Surveys and Position Papers

> Field definitions, surveys, and position papers for Agentic Robotics.

### 2026

- \[2026.8] ComBodied Agents: a New Paradigm of Human-Centric Agentic AI [paper](https://arxiv.org/abs/2608.10915)
- \[2026.5] World Action Models: The Next Frontier in Embodied AI [paper](https://arxiv.org/abs/2605.12090)
- \[2026.5] World Model for Robot Learning: A Comprehensive Survey [paper](https://arxiv.org/abs/2605.00080)
- \[2026.4] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms [paper](https://arxiv.org/abs/2604.23775)
- \[2026.4] Vision-and-Language Navigation for UAVs: A Survey of Progress, Challenges and a Research Roadmap [paper](https://arxiv.org/abs/2604.13614)

### 2025

- \[2025.8] Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction [paper](https://arxiv.org/abs/2508.05294)
- \[2025.8] Agentic LLM-based robotic systems for real-world applications [paper](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1605405/full)

### 2023

- \[2023.11] Large Language Models for Robotics: A Survey [paper](https://arxiv.org/html/2311.07226v2)

---

## Agentic Robotics Architectures

> End-to-end or multi-module robot-agent systems that organize planning, execution, memory, verification, recovery, skill selection, tool interfaces, or multi-agent coordination.

### 2026

- \[2026.8] ETA: A New Agentic Paradigm for Embodied Tasks [paper](https://arxiv.org/abs/2608.03924)
- \[2026.7] Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation [paper](https://arxiv.org/abs/2607.26148)
- \[2026.6] HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory [paper](https://arxiv.org/abs/2606.23565) [project](https://horizonrobotics.github.io/robot_lab/holoagent/) [code](https://github.com/HorizonRobotics/HoloAgent)
- \[2026.6] What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents [paper](https://arxiv.org/abs/2606.10267) [project](https://jiahenghu.github.io/hi-vla)
- \[2026.6] Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins [paper](https://arxiv.org/abs/2606.08214)
- \[2026.6] VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation [paper](https://arxiv.org/abs/2606.07723) [project](https://chicychen.github.io/VoLo)
- \[2026.4] Long-Term Memory for VLA-based Agents in Open-World Task Execution [paper](https://arxiv.org/abs/2604.15671)
- \[2026.4] A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring [paper](https://arxiv.org/abs/2604.07395) [project](https://wenzewwz123.github.io/Agentic-Loop/) [code](https://github.com/WenzeWWZ123/Agentic-Loop)
- \[2026.4] ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration [paper](https://arxiv.org/abs/2604.04664) [project](https://www.rosclaw.io/) [code](https://github.com/ros-claw/rosclaw)
- \[2026.3] RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks [paper](https://arxiv.org/abs/2603.11558) [code](https://github.com/RoboClaw-Robotics/RoboClaw)
- \[2026.2] Agentic AI for Robot Control: Flexible but still Fragile [paper](https://arxiv.org/abs/2602.13081) [project](https://dfki-ni.github.io/AGENTS-MAKE-2026/) [code](https://github.com/DFKI-NI/mobipick_labs)
- \[2026.2] PLanAR: Planning-Language-Grounded Agentic Reasoning for Robot Manipulation [paper](https://arxiv.org/abs/2602.01662) [project](https://planar-robot.github.io/)

### 2025

- \[2025.5] RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation [paper](https://arxiv.org/abs/2505.01709) [project](https://abliao.github.io/RoBridge/) [code](https://github.com/abliao/RoBridge)
- \[2025.3] CLEA: Closed-Loop Embodied Agent for Enhancing Task Execution in Dynamic Environments [paper](https://arxiv.org/abs/2503.00729) [project](https://sp4595.github.io/CLEA/) [code](https://github.com/SP4595/CLEA-Closed-Loop-Embodied-Agent)

### 2023

- \[2023.9] SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models [paper](https://arxiv.org/abs/2309.10062) [project](https://sites.google.com/view/smart-llm/) [code](https://github.com/SMARTlab-Purdue/SMART-LLM)

### 2022

- \[2022.4] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances [paper](https://arxiv.org/abs/2204.01691) [project](https://say-can.github.io/)

---

## Agentic VLA and Embodied Foundation Models

> VLA-centric systems that expose robot policies as skills or tools, add planning, verification, recovery, memory, dynamic tool use, or online adaptation, or provide hierarchical and cross-embodiment foundations for agentic control.

### 2026

- \[2026.8] τ_0-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation [paper](https://arxiv.org/abs/2608.16885)
- \[2026.8] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use [paper](https://arxiv.org/abs/2608.14047)
- \[2026.8] G0.5: One Autoregressive Stream for Robot Reasoning and Action [paper](https://arxiv.org/abs/2608.11739)
- \[2026.7] TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM [paper](https://arxiv.org/abs/2607.27205)
- \[2026.7] RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model [paper](https://arxiv.org/abs/2607.17977) [code](https://github.com/alibaba-damo-academy/RynnBrain)
- \[2026.7] Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents [paper](https://arxiv.org/abs/2607.08448) [project](https://harnessvla.github.io/) [code](https://github.com/RLinf/RPent)
- \[2026.5] Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments [paper](https://arxiv.org/abs/2605.30280)
- \[2026.5] Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models [paper](https://arxiv.org/abs/2605.22896)
- \[2026.5] Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models [paper](https://arxiv.org/abs/2605.13119)

### 2025

- \[2025.10] Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer [paper](https://arxiv.org/abs/2510.03342)
- \[2025.5] Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents [paper](https://arxiv.org/abs/2505.23450) [project](https://agentic-robot.github.io/) [code](https://github.com/Agentic-Robot/agentic-robot)
- \[2025.4] π0.5: a Vision-Language-Action Model with Open-World Generalization [paper](https://arxiv.org/abs/2504.16054) [project](https://www.pi.website/blog/pi05) [code](https://github.com/Physical-Intelligence/openpi)
- \[2025.2] Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models [paper](https://arxiv.org/html/2502.19417v1) [project](https://www.pi.website/research/hirobot)

---

## Embodied Memory

> Memory systems for physical agents: working memory, memory banks, semantic-spatial memory, scene memory, and embodied retrieval.

### 2026

- \[2026.8] AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models [paper](https://arxiv.org/abs/2608.06729)
- \[2026.7] MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning [paper](https://arxiv.org/abs/2607.14252) [project](https://yuzihaowashu.github.io/MEMORA/)
- \[2026.7] Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation [paper](https://arxiv.org/abs/2607.07608)
- \[2026.6] eMEM: A Hybrid Spatio-Temporal Memory System For Embodied Agents [paper](https://arxiv.org/abs/2606.03374)
- \[2026.3] Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation [paper](https://arxiv.org/abs/2603.24576)
- \[2026.3] ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries [paper](https://arxiv.org/abs/2603.12942)
- \[2026.3] MEM: Multi-Scale Embodied Memory for Vision Language Action Models [paper](https://www.pi.website/download/Mem.pdf) [project](https://www.pi.website/research/memory)

### 2025

- \[2025.11] EchoVLA: Robotic Vision-Language-Action Model with Synergistic Declarative Memory for Mobile Manipulation [paper](https://arxiv.org/abs/2511.18112)
- \[2025.11] Searching in Space and Time: Unified Memory-Action Loops for Open-World Object Retrieval [paper](https://arxiv.org/abs/2511.14004) [project](https://amrl.cs.utexas.edu/STAR/) [code](https://github.com/ut-amrl/STAR)
- \[2025.10] MemER: Scaling Up Memory for Robot Control via Experience Retrieval [paper](https://arxiv.org/abs/2510.20328) [project](https://jen-pan.github.io/memer/) [code](https://github.com/memer-policy/memer/tree/main)
- \[2025.9] Meta-Memory: Retrieving and Integrating Semantic-Spatial Memories for Robot Spatial Reasoning [paper](https://arxiv.org/abs/2509.20754) [project](https://itsbaymax.github.io/meta-memory.github.io/) [code](https://github.com/ItsBaymax/Meta-Memory)
- \[2025.8] MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation [paper](https://arxiv.org/abs/2508.19236) [project](https://shihao1895.github.io/MemoryVLA/) [code](https://github.com/shihao1895/MemoryVLA)
- \[2025.8] RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Lifelong Learning in Physical Embodied Systems [paper](https://arxiv.org/abs/2508.01415) [project](https://sp4595.github.io/robomemory/)

### 2024

- \[2024.11] \[CVPR 25] 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning [paper](https://arxiv.org/abs/2411.17735) [project](https://umass-embodied-agi.github.io/3D-Mem/) [code](https://github.com/UMass-Embodied-AGI/3D-Mem)
- \[2024.11] DynaMem: Online Dynamic Spatio-Semantic Memory for Open World Mobile Manipulation [paper](https://arxiv.org/abs/2411.04999) [project](https://dynamem.github.io/) [code](https://github.com/hello-robot/stretch_ai)
- \[2024.9] Embodied-RAG: General Non-parametric Embodied Memory for Retrieval and Generation [paper](https://arxiv.org/html/2409.18313v2)

---

## Planning and Reasoning

> LLM/VLM-based planning, grounded reasoning, task decomposition, value maps, and closed-loop feedback.

### 2026

- \[2026.4] RoboAgent: Chaining Basic Capabilities for Embodied Task Planning [paper](https://arxiv.org/abs/2604.07774)

### 2025

- \[2025.12] Large Video Planner [paper](https://arxiv.org/abs/2512.15840) [project](https://www.boyuan.space/large-video-planner/) [code](https://github.com/buoyancy99/large-video-planner/tree/main)
- \[2025.11] LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models [paper](https://arxiv.org/abs/2511.07727)
- \[2025.9] Robix: A Unified Model for Robot Interaction, Reasoning and Planning [paper](https://arxiv.org/abs/2509.01106)
- \[2025.9] OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning [paper](https://arxiv.org/abs/2509.09332)
- \[2025.9] Reinforced Embodied Planning with Verifiable Reward for Real-World Robotic Manipulation [paper](https://arxiv.org/abs/2509.25852)
- \[2025.7] ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning [paper](https://arxiv.org/abs/2507.16815) [project](https://jasper0314-huang.github.io/thinkact-vla/)
- \[2025.6] Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning [paper](https://arxiv.org/abs/2506.23127)
- \[2025.3] Embodied-Reasoner: Synergizing Visual Search, Reasoning, and Action for Embodied Interactive Tasks [paper](https://arxiv.org/abs/2503.21696) [project](https://embodied-reasoner.github.io/)
- \[2025.3] LLM+MAP: Bimanual Robot Task Planning using Large Language Models and Planning Domain Definition Language [paper](https://arxiv.org/abs/2503.17309) [code](https://github.com/Kchu/LLM-MAP)
- \[2025.3] GraspCoT: Integrating Physical Property Reasoning for 6-DoF Grasping under Flexible Language Instructions [paper](https://arxiv.org/abs/2503.16013) [code](https://github.com/cxmomo/GraspCoT)
- \[2025.3] Safety Aware Task Planning via Large Language Models in Robotics [paper](https://arxiv.org/abs/2503.15707)
- \[2025.3] Code-as-Symbolic-Planner: Foundation Model-Based Robot Planning via Symbolic Code Generation [paper](https://arxiv.org/abs/2503.01700) [project](https://yongchao98.github.io/Code-Symbol-Planner/)

### 2024

- \[2024.12] Multi-Modal Grounded Planning and Efficient Replanning For Learning Embodied Agents with A Few Examples [paper](https://arxiv.org/abs/2412.17288)
- \[2024.8] Autonomous Behavior Planning For Humanoid Loco-manipulation Through Grounded Language Model [paper](https://arxiv.org/abs/2408.08282)
- \[2024.7] LLaMAR: Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments [paper](https://arxiv.org/abs/2407.10031)
- \[2024.4] Long-horizon Locomotion and Manipulation on a Quadrupedal Robot with Large Language Models [paper](https://arxiv.org/abs/2404.05291)
- \[2024.3] CoPa: General Robotic Manipulation through Spatial Constraints of Parts with Foundation Models [paper](https://arxiv.org/abs/2403.08248)
- \[2024.2] Grounding LLMs For Robot Task Planning Using Closed-loop State Feedback [paper](https://arxiv.org/abs/2402.08546)
- \[2024.2] Verifiably Following Complex Robot Instructions with Foundation Models [paper](https://arxiv.org/abs/2402.11498)

### 2023

- \[2023.7] VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models [paper](https://arxiv.org/abs/2307.05973) [project](https://voxposer.github.io/)

### 2022

- \[2022.12] LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models [paper](https://arxiv.org/abs/2212.04088)
- \[2022.9] ProgPrompt: Generating Situated Robot Task Plans using Large Language Models [paper](https://arxiv.org/abs/2209.11302)
- \[2022.7] Inner Monologue: Embodied Reasoning through Planning with Language Models [paper](https://arxiv.org/abs/2207.05608)
- \[2022.1] Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents [paper](https://arxiv.org/abs/2201.07207)

---

## World Models and World-Action Models

> Predictive models that support future imagination, control, action synthesis, and internal planning.

### 2026

- \[2026.8] World Tokens: Enhancing Embodied Policies with Training-Time World Modeling [paper](https://arxiv.org/abs/2608.09730)
- \[2026.8] Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models [paper](https://arxiv.org/abs/2608.04404)
- \[2026.7] ACID: Action Consistency via Inverse Dynamics for Planning with World Models [paper](https://arxiv.org/abs/2607.02403)
- \[2026.7] ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts [paper](https://arxiv.org/abs/2607.28993) [project](https://thu-wangmx.github.io/st-wam/) [code](https://github.com/Thu-WangMX/ST-WAM-Semantic-Temporal-World-Action-Model)
- \[2026.6] Learning Transferable Dynamics Priors from Action to World Modeling [paper](https://arxiv.org/abs/2606.29501)
- \[2026.6] MemoryWAM: Efficient World Action Modeling with Persistent Memory [paper](https://arxiv.org/abs/2606.20562)
- \[2026.6] NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation [paper](https://arxiv.org/abs/2606.13494)
- \[2026.6] World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis [paper](https://arxiv.org/abs/2606.05979)
- \[2026.6] WALL-WM: Carving World Action Modeling at the Event Joints [paper](https://arxiv.org/abs/2606.01955) [project](https://github.com/X-Square-Robot/wall-x)
- \[2026.6] τ_0-WM: A Unified Video-Action World Model for Robotic Manipulation [paper](https://arxiv.org/abs/2606.01027)
- \[2026.5] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation [paper](https://arxiv.org/abs/2605.22882)
- \[2026.5] Being-H0.7: A Latent World-Action Model from Egocentric Videos [paper](https://arxiv.org/abs/2605.00078)
- \[2026.4] MotuBrain: An Advanced World Action Model for Robot Control [paper](https://arxiv.org/abs/2604.27792)
- \[2026.3] ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment [paper](https://arxiv.org/abs/2603.23376)
- \[2026.3] GigaWorld-Policy: An Efficient Action-Centered World--Action Model [paper](https://arxiv.org/abs/2603.17240)
- \[2026.3] MosaicMem: Hybrid Spatial Memory for Controllable Video World Models [paper](https://arxiv.org/abs/2603.17117) [project](https://mosaicmem.github.io/mosaicmem/)
- \[2026.3] Fast-WAM: Do World Action Models Need Test-time Future Imagination? [paper](https://arxiv.org/abs/2603.16666) [project](https://yuantianyuan01.github.io/FastWAM/) [code](https://github.com/yuantianyuan01/FastWAM)
- \[2026.3] ImagiNav: Scalable Embodied Navigation via Generative Visual Prediction and Inverse Dynamics [paper](https://arxiv.org/abs/2603.13833)
- \[2026.3] DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control [paper](https://arxiv.org/abs/2603.10448) [project](https://dit4dit.github.io/)
- \[2026.2] World Action Models are Zero-shot Policies [paper](https://arxiv.org/html/2602.15922v1)
- \[2026.1] Causal World Modeling for Robot Control [paper](https://arxiv.org/abs/2601.21998) [project](https://technology.robbyant.com/lingbot-va) [code](https://github.com/Robbyant/lingbot-va)
- \[2026.1] PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation [paper](https://arxiv.org/abs/2601.03782) [project](https://point-world.github.io/) [code](https://github.com/huangwl18/PointWorld)

### 2025

- \[2025.6] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning [paper](https://arxiv.org/abs/2506.09985) [project](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) [code](https://github.com/facebookresearch/vjepa2)
- \[2025.3] Object-Centric World Model for Language-Guided Manipulation [paper](https://arxiv.org/abs/2503.06170)

---

## Verification and Self-Evaluation

> Success detection, temporal verification, execution checking, and safety-aware evaluation.

### 2026

- \[2026.8] MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation [paper](https://arxiv.org/abs/2608.17386)
- \[2026.7] SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents [paper](https://arxiv.org/abs/2607.14543)
- \[2026.7] EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards [paper](https://arxiv.org/abs/2607.00218)
- \[2026.6] Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement [paper](https://arxiv.org/abs/2606.18247)
- \[2026.6] VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents [paper](https://arxiv.org/abs/2606.05395)
- \[2026.5] Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts [paper](https://arxiv.org/abs/2605.22446)
- \[2026.5] SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation [paper](https://arxiv.org/abs/2605.12386)
- \[2026.4] Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA [paper](https://arxiv.org/abs/2604.02965)
- \[2026.3] Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model [paper](https://arxiv.org/abs/2603.18091)
- \[2026.2] Metamorphic Testing of Vision-Language Action-Enabled Robots [paper](https://arxiv.org/abs/2602.22579)
- \[2026.2] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models [paper](https://arxiv.org/abs/2602.01811)

### 2025

- \[2025.12] Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models [paper](https://arxiv.org/abs/2512.01946)
- \[2025.11] ROVER: Regulator-Driven Robust Temporal Verification of Black-Box Robot Policies [paper](https://arxiv.org/abs/2511.17781)
- \[2025.5] Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition [paper](https://arxiv.org/abs/2505.11175)
- \[2025.3] RoboGuard: Safety Guardrails for LLM-Enabled Robots [paper](https://arxiv.org/abs/2503.07885) [code](https://github.com/KumarRobotics/RoboGuard)

### 2024

- \[2024.10] AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation [paper](https://arxiv.org/abs/2410.00371)
- \[2024.3] \[AAAI] Vision-Language Models for Robot Success Detection [paper](https://ojs.aaai.org/index.php/AAAI/article/view/30552/32714)

### 2023

- \[2023.3] Vision-Language Models as Success Detectors [paper](https://arxiv.org/abs/2303.07280)

---

## Failure Detection and Recovery

> Failure detection, natural-language failure reasoning, motion correction, task-level recovery, and safe takeover.

### 2026

- \[2026.2] ARMOR: Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning [paper](https://arxiv.org/html/2602.12405v1)
- \[2026.1] CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding [paper](https://arxiv.org/abs/2601.02295) [project](https://dannymcy.github.io/cyclevla/)

### 2025

- \[2025.10] FailSafe-VLM: Reasoning and Recovery from Failures in Vision-Language-Action Models [paper](https://arxiv.org/html/2510.01642v1)
- \[2025.9] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction [paper](https://arxiv.org/abs/2509.04018) [project](https://fpcvla.github.io/)
- \[2025.6] SAFE: Multitask Failure Detection for Vision-Language-Action Models [paper](https://arxiv.org/abs/2506.09937) [project](https://vla-safe.github.io/)
- \[2025.3] STAR: A Foundation Model-driven Framework for Robust Task Planning and Failure Recovery in Robotic Systems [paper](https://arxiv.org/abs/2503.06060)
- \[2025.3] A Unified Framework for Real-Time Failure Handling in Autonomous Robots [paper](https://arxiv.org/html/2503.15202v2)

### 2024

- \[2024.9] Automating Robot Failure Recovery Using Vision-Language Models [paper](https://arxiv.org/abs/2409.03966)

---

## Skill Calling, Tool Use, and Robot Execution Interfaces

> Robotic skill libraries, tool/API invocation, Code-as-Policy, Tool-as-Policy, ROS/MCP execution interfaces, capability discovery, skill composition, and self-evolving skill repositories for physical agents.

### 2026

- \[2026.6] CLASP: Language-Driven Robot Skill Selection and Composition using Task-Parameterized Learning [paper](https://arxiv.org/abs/2606.08169)
- \[2026.3] ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction [paper](https://arxiv.org/abs/2603.26997)
- \[2026.3] CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation [paper](https://arxiv.org/abs/2603.22435)
- \[2026.3] Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation [paper](https://arxiv.org/abs/2603.02623)
- \[2026.1] ALRM: Agentic LLM for Robotic Manipulation [paper](https://arxiv.org/abs/2601.19510)

### 2025

- \[2025.5] Dynamic Robot Tool Use with Vision Language Models [paper](https://arxiv.org/abs/2505.01399)
- \[2025.5] DeCo: Task Decomposition and Skill Composition for Zero-Shot Generalization in Long-Horizon 3D Manipulation [paper](https://arxiv.org/abs/2505.00527) [project](https://deco226.github.io/)
- \[2025.5] RAI: Flexible Agent Framework for Embodied AI [paper](https://arxiv.org/abs/2505.07532) [code](https://github.com/RobotecAI/rai)
- \[2025.4] SPECI: Skill Prompts based Hierarchical Continual Imitation Learning for Robot Manipulation [paper](https://arxiv.org/abs/2504.15561)
- \[2025.1] An Atomic Skill Library Construction Method for Data-Efficient Embodied Manipulation [paper](https://arxiv.org/abs/2501.15068)

### 2024

- \[2024.6] ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning [paper](https://arxiv.org/abs/2406.19741)

### 2022

- \[2022.9] Code as Policies: Language Model Programs for Embodied Control [paper](https://arxiv.org/abs/2209.07753)

---

## Long-Horizon Manipulation

> Long-horizon robotic manipulation, including hierarchical VLA systems, memory-augmented policies, progress-aware control, skill chaining, mobile manipulation, recovery-aware execution, and multi-stage task completion.

### 2026

- \[2026.6] SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation [paper](https://arxiv.org/abs/2606.12956)
- \[2026.4] Long-Horizon Manipulation via Trace-Conditioned VLA Planning [paper](https://arxiv.org/abs/2604.21924)
- \[2026.4] HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation [paper](https://arxiv.org/abs/2604.18791)
- \[2026.4] Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection [paper](https://arxiv.org/abs/2604.13942)
- \[2026.3] ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation [paper](https://arxiv.org/abs/2603.27670)
- \[2026.3] Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks [paper](https://arxiv.org/abs/2603.09513)
- \[2026.3] Non-Markovian Long-Horizon Robot Manipulation via Keyframe Chaining [paper](https://arxiv.org/abs/2603.01465)
- \[2026.2] LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies [paper](https://arxiv.org/abs/2602.21531)

---

## Embodied Navigation Agents

> Embodied navigation agents, including vision-language navigation, object-goal navigation, spatial memory, map/scene-graph reasoning, active exploration, self-correction, cross-embodiment navigation, aerial/ground navigation, and navigation world models.

### 2026

- \[2026.8] Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation [paper](https://arxiv.org/abs/2608.17512)
- \[2026.6] SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning [paper](https://arxiv.org/abs/2606.08992)
- \[2026.6] EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation [paper](https://arxiv.org/abs/2606.03509)
- \[2026.5] Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation [paper](https://arxiv.org/abs/2605.27582)
- \[2026.4] A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration [paper](https://arxiv.org/abs/2604.21363)
- \[2026.3] ReMemNav: A Rethinking and Memory-Augmented Framework for Zero-Shot Object Navigation [paper](https://arxiv.org/abs/2603.26788)
- \[2026.3] AgentVLN: Towards Agentic Vision-and-Language Navigation [paper](https://arxiv.org/abs/2603.17670)
- \[2026.3] OmniVLN: Omnidirectional 3D Perception and Token-Efficient LLM Reasoning for Visual-Language Navigation in Air-Ground Robots [paper](https://arxiv.org/abs/2603.17351)
- \[2026.3] EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments [paper](https://arxiv.org/abs/2603.16947)
- \[2026.3] AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38878)
- \[2026.3] NaVLA^2: A Vision-Language-Audio-Action Model for Multimodal Instruction Navigation [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38886)
- \[2026.3] SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation [paper](https://arxiv.org/abs/2603.06914)
- \[2026.1] VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory [paper](https://arxiv.org/abs/2601.08665)

### 2024

- \[2024.12] \[RSS 25] Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks [paper](https://arxiv.org/abs/2412.06224) [project](https://pku-epic.github.io/Uni-NaVid/)
- \[2024.4] GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation [paper](https://arxiv.org/abs/2404.06609)
- \[2024.4] VLM-Social-Nav: Socially Aware Robot Navigation through Scoring Using Vision-Language Models [paper](https://arxiv.org/html/2404.00210v1)

### 2023

- \[2023.10] Co-NavGPT: Multi-Robot Cooperative Visual Semantic Navigation using Large Language Models [paper](https://arxiv.org/abs/2310.07937)

### 2022

- \[2022.7] LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action [paper](https://arxiv.org/abs/2207.04429)

### 2018

- \[2018.6] \[CVPR] Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments [paper](https://openaccess.thecvf.com/content_cvpr_2018/papers/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.pdf)

---

## Human-Robot Interaction and Dialogue Agents

> Human feedback, dialogue management, mixed initiative, social robot planning, and human-in-the-loop coordination.

### 2025

- \[2025.8] MICoBot: Mixed-Initiative Dialog for Human-Robot Collaborative Manipulation [paper](https://arxiv.org/html/2508.05535v1)

### 2024

- \[2024.2] Conversational Language Models for Human-in-the-Loop Multi-Robot Coordination [paper](https://arxiv.org/abs/2402.19166)
- \[2024.1] Understanding LLM-powered Human-Robot Interaction [paper](https://arxiv.org/abs/2401.03217)

### 2023

- \[2023.3] Large Language Models as Zero-Shot Human Models for Human-Robot Interaction [paper](https://arxiv.org/abs/2303.03548)

---

## Safety, Governance, and Physical Risk

> Safety guardrails, policy-constrained execution, governance benchmarks, consent, delegation, and physical irreversibility.

### 2026

- \[2026.5] Consent Chain Degradation in Embodied Multi-Agent Systems [paper](https://arxiv.org/html/2605.16300v1)
- \[2026.4] EmbodiedGovBench: A Benchmark for Governance-Constrained Embodied Agents [paper](https://arxiv.org/html/2604.11174v1)
- \[2026.4] Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution [paper](https://arxiv.org/abs/2604.07833)

---

## Benchmarks, Simulators, and Datasets

> Benchmarks and datasets for long-horizon tasks, memory, recovery, navigation, multi-robot systems, and safety.

### 2026

- \[2026.3] RoboCasa365: A Large-Scale Simulation Framework for Generalist Robot Policies [paper](https://arxiv.org/html/2603.04356v1)

### 2025

- \[2025.10] NaviTrace: Evaluating Embodied Navigation of Vision-Language Models [paper](https://arxiv.org/abs/2510.06757)
- \[2025.4] RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins [paper](https://arxiv.org/abs/2504.13059)

### 2024

- \[2024.6] RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots [paper](https://arxiv.org/abs/2406.02523)

### 2023

- \[2023.10] Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots [paper](https://arxiv.org/abs/2310.13724)
- \[2023.10] Open X-Embodiment: Robotic Learning Datasets and RT-X Models [paper](https://arxiv.org/abs/2310.08864) [project](https://robotics-transformer-x.github.io/) [code](https://github.com/google-deepmind/open_x_embodiment)
- \[2023.8] BridgeData V2: A Dataset for Robot Learning at Scale [paper](https://arxiv.org/abs/2308.12952)
- \[2023.6] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning [paper](https://arxiv.org/abs/2306.03310)

### 2021

- \[2021.12] CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks [paper](https://arxiv.org/abs/2112.03227)

---

## Open-Source Systems and Frameworks

> Open models, robot agent frameworks, simulation systems, benchmark codebases, and data infrastructure.

### 2024

- \[2024.10] Dimensional OS: Agentic Operating System for Physical Space [project](https://dimensionalos.com/) [code](https://github.com/dimensionalOS/dimos)
- \[2024.5] Octo: An Open-Source Generalist Robot Policy [paper](https://arxiv.org/abs/2405.12213) [project](https://octo-models.github.io/)

### 2023

- \[2023.11] RoboFlamingo: Vision-Language Foundation Models as Effective Robot Imitators [paper](https://arxiv.org/abs/2311.01378)

---

## Industrial Signals and Technical Reports

> Technical reports, model releases, product signals, and industrial systems that point toward deployable physical agents.

### 2025

- \[2025.3] \[Google DeepMind] Gemini Robotics: Bringing AI into the Physical World [paper](https://arxiv.org/abs/2503.20020)
- \[2025.3] \[NVIDIA] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots [paper](https://arxiv.org/abs/2503.14734) [code](https://github.com/Nvidia/Isaac-GR00T)
- \[2025.2] \[Figure] Helix [project](https://www.figure.ai/news/helix)

---

## Related Awesome Lists

- [Awesome Memory for Robotics](https://github.com/Everloom-129/Awesome-Memory-for-Robotics)
- [Awesome World Models](https://github.com/leofan90/Awesome-World-Models)
- [Awesome Embodied VLA / VA / VLN](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)

---

## Citation

If you find this repository useful, please consider citing this list:

```bibtex
@misc{liu2026awesomeagenticrobotics,
  title = {Awesome Agentic Robotics},
  author = {Duo Liu and Xinbai Wang},
  journal = {GitHub repository},
  url = {https://github.com/Cat-blizzard/awesome-agentic-robotics},
  year = {2026},
}
```

---

## Contributing

Contributions are welcome. Please read [contributing.md](contributing.md) before submitting a pull request.

## Contact

Questions, suggestions, and collaborations are welcome. Contact [Duo Liu](mailto:duoliu@stu.hit.edu.cn) or connect with [Xinbai Wang](https://github.com/w-xb) on GitHub.
