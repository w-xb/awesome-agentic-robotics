# Awesome Agentic Robotics [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A living, selective reading list of influential work on autonomous physical agents, spanning planning, agentic VLA, memory, world models, verification, recovery, tool use, and safety.

**Last updated:** 2026-08-27

## Contents

- [What Agentic Robotics Means Here](#what-agentic-robotics-means-here)
- [Scope and Curation](#scope-and-curation)
- [Start Here / Must Read](#start-here--must-read)
- [Surveys and Position Papers](#surveys-and-position-papers)
- [Agentic Robotics Architectures](#agentic-robotics-architectures)
- [Agentic VLA and Embodied Foundation Models](#agentic-vla-and-embodied-foundation-models)
- [Embodied Memory](#embodied-memory)
- [Planning and Reasoning](#planning-and-reasoning)
- [World Models and World-Action Models](#world-models-and-world-action-models)
- [Verification, Recovery, and Safety Evaluation](#verification-recovery-and-safety-evaluation)
- [Failure Detection and Recovery](#failure-detection-and-recovery)
- [Skill Learning and Tool Use](#skill-learning-and-tool-use)
- [Long-Horizon Manipulation](#long-horizon-manipulation)
- [Embodied Navigation](#embodied-navigation)
- [Human-Robot Interaction](#human-robot-interaction)
- [Governance and Physical Safety](#governance-and-physical-safety)
- [Benchmarks and Datasets](#benchmarks-and-datasets)
- [Open-Source Foundation Models](#open-source-foundation-models)
- [Industrial Systems](#industrial-systems)
- [Extended Reading](#extended-reading)
- [Related Awesome Lists](#related-awesome-lists)
- [Citation](#citation)

## What Agentic Robotics Means Here

Agentic Robotics is an emerging and not-yet-standardized research direction. In this repository, we use an ability-centered definition: a robotic system becomes more agentic as it can perceive and maintain task state, use memory, plan over future consequences, invoke skills or tools, verify execution, recover from failures, adapt from experience, and act under physical safety constraints.

Unlike many software agents, whose planning, memory, tool use, and reflection are mediated mainly through text and APIs, robotic agents must act in a dynamic, partially observable physical world. Their agency therefore depends not only on an external LLM-style loop, but also on embodied mechanisms such as spatial-temporal memory, action-conditioned world models, grounded skill interfaces, execution monitoring, failure attribution, recovery policies, and safety envelopes.

Agentic robotics is a continuum rather than a binary label. Not every work in this list presents a complete autonomous robot: some contribute a single capability, while others integrate several capabilities into a closed-loop system. This repository maps both the components of physical agency and the architectures that bring them together.

## Scope and Curation

**Core scope.** The list covers planning and grounded reasoning; VLA-as-tools and hierarchical VLA; embodied memory and persistent state; world models used for prediction, evaluation, or control; execution verification and recovery; skill learning and robot tool use; long-horizon manipulation and navigation; human-robot interaction; and governance, runtime safety, and embodied evaluation.

**Selection principles.** Entries are chosen for agentic relevance, influence, evidence quality, representativeness, and resource completeness. The list includes both modular LLM/VLM-agent architectures and tightly coupled robot-learning systems when they make a clear contribution to closed-loop physical agency. General-purpose VLA work is included only when it materially advances planning, long-horizon execution, tool use, verification, recovery, embodied memory, world-model-based decisions, continual adaptation, or cross-embodiment deployment.

**A living list.** New high-quality work may be added as the field develops; selectivity is maintained through a quality bar, not a fixed item count. Each paper has one canonical entry, items are ordered by first public release date within each section, and narrower or superseded work remains available in Extended Reading.

**Links:** `[paper]` publication or preprint · `[project]` official project page · `[code]` official implementation · `[model]` official weights · `[dataset]` official data

---

## Start Here / Must Read

> Twenty high-signal papers organized as four reading routes. Each also appears once in its canonical topic section.

### VLA as Tools and Agents

**Harness VLA** — Treats a frozen VLA as a retryable contact-rich primitive, while a memory-guided agent stages subtasks, models failures, verifies outcomes, and retries execution. It is a strong blueprint for composing existing policies into reliable long-horizon systems.

**VLAs-as-Tools** — Separates temporal reasoning from physical execution through a high-level VLM agent and specialized, progress-aware VLA tools. Event-triggered replanning and tool-aligned post-training make the architecture especially useful for understanding modular agentic manipulation.

**Agentic Robot** — Introduces a Plan-Execute-Verify loop that combines task planning, VLA execution, temporal verification, and structured recovery. The explicit closed loop makes it a representative system for studying how embodied agents detect and repair execution errors.

**ART** — Injects off-the-shelf multimodal tools into an end-to-end VLA without abandoning continuous action generation. Tool-use trajectories and long-horizon reasoning training demonstrate how modular capabilities can improve robustness, data efficiency, and extensibility in simulation and real robots.

**Gemini Robotics 1.5** — Couples a generalist robot policy with embodied reasoning, explicit thinking, and motion transfer across embodiments. It is an important industrial-scale example of moving beyond direct instruction following toward generalizable, reasoning-guided physical action.

### Hierarchical and Reasoning VLA

**τ_0-VLA** — Combines hierarchical control, execution memory, a learned world model, and test-time search to improve high-level subtask decisions. It shows how additional inference-time computation can be converted into more reliable long-horizon robot behavior.

**G0.5** — Generates reasoning and action tokens in one autoregressive stream, supported by visual memory and cross-embodiment action tokenization. The unified formulation is a useful reference for tightly integrating deliberation and control inside a foundation model.

**Qwen-VLA** — Unifies manipulation, navigation, trajectory supervision, multimodal understanding, and cross-embodiment training within one model family. Its broad task coverage makes it a valuable reference for studying generalist embodied foundations rather than isolated robot skills.

**π0.5** — Extends a generalist VLA with heterogeneous co-training and high-level semantic knowledge for open-world generalization. It is a key reference for understanding how web-scale knowledge and robot data can support deployment in unseen environments.

**Hi Robot** — Uses a hierarchical VLA to convert open-ended human instructions into semantic subgoals and low-level actions. It clearly illustrates why task-level reasoning and policy-level execution benefit from distinct but jointly coordinated representations.

### Memory and World Models

**AtlasVLA** — Maintains a persistent world-ego state that tracks spatial context and task progress across long executions. It directly addresses perceptual and progress forgetting, two central obstacles to reliable memory-aware VLA control.

**MEMORA** — Extracts editable, consolidated embodied action memories from egocentric experience and retrieves them for later reasoning and planning. It offers a concrete path from passive video experience to reusable procedural knowledge for physical agents.

**MemoryVLA** — Integrates perceptual and cognitive memory into VLA control so the policy can preserve scene evidence and task state over time. It is a representative memory architecture for long-horizon manipulation under partial observability.

**τ_0-WM** — Unifies action generation, future video prediction, candidate evaluation, and simulator-based rectification in one video-action world model. The design makes future imagination operational by using predictions to select and correct robot actions.

**V-JEPA 2** — Learns predictive video representations at scale and demonstrates understanding, anticipation, and planning on physical tasks. It is a foundational reference for how self-supervised world models can support downstream embodied decision making.

### Planning, Safety, and Evaluation

**SayCan** — Grounds language-model plans in learned robotic affordances, scoring candidate skills by both semantic usefulness and physical feasibility. This influential formulation established a practical pattern for connecting broad language knowledge to executable robot capabilities.

**Inner Monologue** — Adds environment feedback, success detection, and replanning to language-model-based control, converting open-loop plans into an embodied reasoning loop. It remains a foundational reference for feedback-aware planning and recovery in robotics.

**MANIGUARD** — Evaluates manipulation safety against explicit specifications and pairs the benchmark with safety-annotated trajectories for improvement. It is valuable because it measures process-level behavior rather than relying only on final task success.

**RoboCasa365** — Provides a large-scale, diverse simulation framework for training and evaluating generalist robot policies over everyday tasks. Its breadth makes it a central testbed for long-horizon generalization and agentic policy orchestration.

**Open X-Embodiment** — Aggregates large-scale robot datasets across institutions and embodiments and introduces RT-X models trained on the mixture. It established shared data and cross-robot transfer as core foundations for generalist embodied intelligence.

---

## Surveys and Position Papers

- \[2026.5] **World Action Models: The Next Frontier in Embodied AI** [paper](https://arxiv.org/abs/2605.12090) — Defines world-action modeling, organizes its major architectural choices, and identifies how predictive environment dynamics can improve planning and closed-loop robot control.
- \[2026.5] **World Model for Robot Learning: A Comprehensive Survey** [paper](https://arxiv.org/abs/2605.00080) — Reviews world-model objectives, representations, datasets, and downstream uses across robot learning, providing a broad foundation for prediction-guided embodied decision making.
- \[2026.4] **Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms** [paper](https://arxiv.org/abs/2604.23775) — Systematizes VLA safety threats, evaluation protocols, and mitigation mechanisms across training and deployment, connecting model risks to physical execution consequences.
- \[2025.8] **Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction** [paper](https://arxiv.org/abs/2508.05294) — Classifies language- and vision-driven robot agents by autonomy, interaction, architecture, and embodiment, clarifying the emerging design space of agentic robotics.
- \[2023.11] **Large Language Models for Robotics: A Survey** [paper](https://arxiv.org/html/2311.07226v2) — Surveys early uses of large language models for perception, planning, control, and human-robot interaction, establishing essential context for modern agentic systems.

## Agentic Robotics Architectures

- \[2026.8] **ETA: A New Agentic Paradigm for Embodied Tasks** [paper](https://arxiv.org/abs/2608.03924) — Presents an agentic embodied-task framework that coordinates reasoning and execution through a minimal interface, emphasizing transferable orchestration over monolithic policy scaling.
- \[2026.7] **Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation** [paper](https://arxiv.org/abs/2607.26148) — Shows that minimally interfaced foundation-model agents can compete with specialized navigation policies through zero-shot reasoning, feedback, and structured action selection.
- \[2026.6] **HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory** [paper](https://arxiv.org/abs/2606.23565) [project](https://horizonrobotics.github.io/robot_lab/holoagent/) [code](https://github.com/HorizonRobotics/HoloAgent) — Integrates 3D spatial memory, reasoning, and action in a unified embodied framework for persistent scene understanding and long-horizon task execution.
- \[2026.6] **What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents** [paper](https://arxiv.org/abs/2606.10267) [project](https://jiahenghu.github.io/hi-vla) — Systematically isolates orchestration choices in hierarchical VLA agents, revealing which planning, policy-selection, and feedback mechanisms most affect long-horizon performance.
- \[2026.6] **VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation** [paper](https://arxiv.org/abs/2606.07723) [project](https://chicychen.github.io/VoLo) — Coordinates perception, open-vocabulary reasoning, and reusable manipulation policies through a physical orchestrator designed for compositional long-horizon tasks in changing scenes.
- \[2026.4] **A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring** [paper](https://arxiv.org/abs/2604.07395) [project](https://wenzewwz123.github.io/Agentic-Loop/) [code](https://github.com/WenzeWWZ123/Agentic-Loop) — Closes the grasping loop with execution-state monitoring, allowing a language-guided agent to detect physical progress and adapt its next action.
- \[2023.9] **SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models** [paper](https://arxiv.org/abs/2309.10062) [project](https://sites.google.com/view/smart-llm/) [code](https://github.com/SMARTlab-Purdue/SMART-LLM) — Uses language models to decompose tasks, allocate roles, and coordinate heterogeneous robots, offering an influential architecture for multi-agent embodied planning.
- \[2022.4] **Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** [paper](https://arxiv.org/abs/2204.01691) [project](https://say-can.github.io/) — Grounds language-model planning in learned affordance values, ensuring selected skills are both semantically appropriate and physically executable by the robot.

## Agentic VLA and Embodied Foundation Models

- \[2026.8] **τ_0-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation** [paper](https://arxiv.org/abs/2608.16885) — Uses execution memory and world-model-guided test-time search to improve high-level subtask decisions in a hierarchical robot foundation model.
- \[2026.8] **Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use** [paper](https://arxiv.org/abs/2608.14047) — Introduces ART, which injects dynamic multimodal tool calls into VLA control and trains long-trajectory tool reasoning for robust physical execution.
- \[2026.8] **G0.5: One Autoregressive Stream for Robot Reasoning and Action** [paper](https://arxiv.org/abs/2608.11739) — Produces interleaved reasoning and actions with visual memory and cross-embodiment tokenization, unifying deliberation and robot control in one stream.
- \[2026.7] **Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents** [paper](https://arxiv.org/abs/2607.08448) [project](https://harnessvla.github.io/) [code](https://github.com/RLinf/RPent) — Wraps frozen VLAs as retryable manipulation primitives and adds task memory, failure modeling, verification, and agent-controlled recovery for long-horizon execution.
- \[2026.5] **Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments** [paper](https://arxiv.org/abs/2605.30280) — Unifies manipulation, navigation, multimodal understanding, and trajectory learning across environments and robot embodiments within a broadly trained foundation model.
- \[2026.5] **Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models** [paper](https://arxiv.org/abs/2605.22896) — Adds reward generation, language-guided exploration, and experience-weighted memory around a VLA, enabling efficient online adaptation to new manipulation tasks.
- \[2026.5] **Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models** [paper](https://arxiv.org/abs/2605.13119) — Frames specialized VLAs as tools for a high-level agent, with progress feedback, event-triggered replanning, and tool-aligned post-training for long horizons.
- \[2025.10] **Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer** [paper](https://arxiv.org/abs/2510.03342) — Combines generalist control, embodied reasoning, explicit thinking, and motion transfer to support complex tasks across multiple robot embodiments.
- \[2025.5] **Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents** [paper](https://arxiv.org/abs/2505.23450) [project](https://agentic-robot.github.io/) [code](https://github.com/Agentic-Robot/agentic-robot) — Coordinates planning, VLA execution, temporal verification, and error recovery through a structured Plan-Execute-Verify loop for embodied agents and autonomous recovery.
- \[2025.4] **π0.5: a Vision-Language-Action Model with Open-World Generalization** [paper](https://arxiv.org/abs/2504.16054) [project](https://www.pi.website/blog/pi05) [code](https://github.com/Physical-Intelligence/openpi) — Combines heterogeneous robot data and semantic knowledge to improve open-world generalization for manipulation in unseen environments and tasks.
- \[2025.2] **Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models** [paper](https://arxiv.org/html/2502.19417v1) [project](https://www.pi.website/research/hirobot) — Decomposes open-ended instructions into semantic subgoals and low-level VLA actions, demonstrating hierarchical reasoning for interactive robot control across diverse tasks.

## Embodied Memory

- \[2026.8] **AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models** [paper](https://arxiv.org/abs/2608.06729) — Maintains a persistent world-ego state that preserves spatial context and task progress, reducing forgetting during long-horizon VLA execution.
- \[2026.7] **MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning** [paper](https://arxiv.org/abs/2607.14252) [project](https://yuzihaowashu.github.io/MEMORA/) — Converts egocentric experience into editable, consolidated action memories that can be retrieved and recomposed for later embodied reasoning and planning.
- \[2026.3] **Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation** [paper](https://arxiv.org/abs/2603.24576) — Uses episodic experience retrieval to adapt manipulation behavior over long horizons, connecting remembered outcomes to current task decisions.
- \[2026.3] **MEM: Multi-Scale Embodied Memory for Vision Language Action Models** [paper](https://www.pi.website/download/Mem.pdf) [project](https://www.pi.website/research/memory) — Builds multi-scale memory over observations and actions so VLA policies can retain both short-term detail and long-term task context.
- \[2025.10] **MemER: Scaling Up Memory for Robot Control via Experience Retrieval** [paper](https://arxiv.org/abs/2510.20328) [project](https://jen-pan.github.io/memer/) [code](https://github.com/memer-policy/memer/tree/main) — Scales experience retrieval for robot control, selecting relevant prior trajectories to improve action decisions under new tasks and environments.
- \[2025.8] **MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation** [paper](https://arxiv.org/abs/2508.19236) [project](https://shihao1895.github.io/MemoryVLA/) [code](https://github.com/shihao1895/MemoryVLA) — Integrates perceptual and cognitive memory into VLA control, preserving scene evidence and task state for long-horizon manipulation under partial observability.
- \[2024.11] **\[CVPR 2025] 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning** [paper](https://arxiv.org/abs/2411.17735) [project](https://umass-embodied-agi.github.io/3D-Mem/) [code](https://github.com/UMass-Embodied-AGI/3D-Mem) — Constructs an explicit 3D scene memory that supports persistent exploration, spatial grounding, and reasoning across changing embodied viewpoints.
- \[2024.11] **DynaMem: Online Dynamic Spatio-Semantic Memory for Open World Mobile Manipulation** [paper](https://arxiv.org/abs/2411.04999) [project](https://dynamem.github.io/) [code](https://github.com/hello-robot/stretch_ai) — Updates spatio-semantic memory online as environments change, enabling open-world mobile manipulation with persistent object and scene knowledge during extended deployments.

## Planning and Reasoning

- \[2025.12] **Large Video Planner** [paper](https://arxiv.org/abs/2512.15840) [project](https://www.boyuan.space/large-video-planner/) [code](https://github.com/buoyancy99/large-video-planner/tree/main) — Plans long-horizon robot behavior through generated visual futures, using video-level predictions to represent intermediate physical states and actions.
- \[2025.9] **Reinforced Embodied Planning with Verifiable Reward for Real-World Robotic Manipulation** [paper](https://arxiv.org/abs/2509.25852) — Trains embodied planning with automatically verifiable rewards, improving structured reasoning and real-world manipulation without relying solely on imitation traces.
- \[2025.7] **ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning** [paper](https://arxiv.org/abs/2507.16815) [project](https://jasper0314-huang.github.io/thinkact-vla/) — Reinforces planning in a visual latent space before action generation, improving VLA reasoning while avoiding expensive natural-language chain-of-thought supervision.
- \[2025.3] **Embodied-Reasoner: Synergizing Visual Search, Reasoning, and Action for Embodied Interactive Tasks** [paper](https://arxiv.org/abs/2503.21696) [project](https://embodied-reasoner.github.io/) — Jointly trains visual search, reasoning, and action selection so embodied agents can gather missing evidence before committing to task decisions.
- \[2025.3] **Code-as-Symbolic-Planner: Foundation Model-Based Robot Planning via Symbolic Code Generation** [paper](https://arxiv.org/abs/2503.01700) [project](https://yongchao98.github.io/Code-Symbol-Planner/) — Generates executable symbolic planning code from multimodal task context, combining foundation-model understanding with structured constraints and reusable planning abstractions.
- \[2024.2] **Grounding LLMs For Robot Task Planning Using Closed-loop State Feedback** [paper](https://arxiv.org/abs/2402.08546) — Grounds language-model plans in observed state feedback, allowing task steps to be revised when physical execution changes the environment unexpectedly.
- \[2024.2] **Verifiably Following Complex Robot Instructions with Foundation Models** [paper](https://arxiv.org/abs/2402.11498) — Translates complex language instructions into formal task specifications and verifies execution, connecting foundation-model interpretation with reliable robot planning.
- \[2023.7] **VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models** [paper](https://arxiv.org/abs/2307.05973) [project](https://voxposer.github.io/) — Converts language and perception into composable 3D value maps, enabling zero-shot spatial reasoning and closed-loop manipulation planning from language instructions.
- \[2022.12] **LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models** [paper](https://arxiv.org/abs/2212.04088) — Uses few-shot language-model prompting and environmental grounding to generate executable plans for embodied tasks with limited demonstrations or domain-specific training.
- \[2022.9] **ProgPrompt: Generating Situated Robot Task Plans using Large Language Models** [paper](https://arxiv.org/abs/2209.11302) — Represents robot plans as situated programs with assertions and recovery steps, improving executability and robustness under changing environments.
- \[2022.7] **Inner Monologue: Embodied Reasoning through Planning with Language Models** [paper](https://arxiv.org/abs/2207.05608) — Feeds success signals, scene descriptions, and human feedback back into language-model planning, enabling closed-loop embodied reasoning and replanning.
- \[2022.1] **Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents** [paper](https://arxiv.org/abs/2201.07207) — Extracts actionable task sequences from pretrained language models and grounds them to available actions, establishing a foundational zero-shot planning baseline.

## World Models and World-Action Models

- \[2026.8] **World Tokens: Enhancing Embodied Policies with Training-Time World Modeling** [paper](https://arxiv.org/abs/2608.09730) — Adds predictive world tokens during training to improve embodied policies while avoiding the deployment cost of explicit future generation.
- \[2026.8] **Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models** [paper](https://arxiv.org/abs/2608.04404) — Retains future-conditioned action selection while reducing video-action interaction cost, making inference-time imagination more practical for robust control during online execution.
- \[2026.7] **ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts** [paper](https://arxiv.org/abs/2607.28993) [project](https://thu-wangmx.github.io/st-wam/) [code](https://github.com/Thu-WangMX/ST-WAM-Semantic-Temporal-World-Action-Model) — Combines DINOv3 semantic future prediction and history retrieval with VAE dynamics, improving zero-shot LIBERO-Plus by 21.3 points and real-world visual-shift success from 25.8% to 61.5%.
- \[2026.7] **ACID: Action Consistency via Inverse Dynamics for Planning with World Models** [paper](https://arxiv.org/abs/2607.02403) — Uses inverse dynamics to score whether imagined futures are consistent with candidate actions, improving world-model planning and trajectory selection.
- \[2026.6] **Learning Transferable Dynamics Priors from Action to World Modeling** [paper](https://arxiv.org/abs/2606.29501) — Introduces A2World, whose action-conditioned pretraining transfers dynamics priors to learned simulators and video-action policies in simulation and real robots.
- \[2026.6] **World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis** [paper](https://arxiv.org/abs/2606.05979) — Unifies predictive world modeling, language reasoning, and action synthesis so each capability can inform the others during robot decision making.
- \[2026.6] **τ_0-WM: A Unified Video-Action World Model for Robotic Manipulation** [paper](https://arxiv.org/abs/2606.01027) — Jointly predicts videos and actions, evaluates candidate futures, and rectifies control through simulator feedback within one manipulation world model.
- \[2026.3] **Fast-WAM: Do World Action Models Need Test-time Future Imagination?** [paper](https://arxiv.org/abs/2603.16666) [project](https://yuantianyuan01.github.io/FastWAM/) [code](https://github.com/yuantianyuan01/FastWAM) — Studies when explicit future imagination is necessary and distills world-action knowledge into faster policies for efficient robot deployment.
- \[2026.1] **PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation** [paper](https://arxiv.org/abs/2601.03782) [project](https://point-world.github.io/) [code](https://github.com/huangwl18/PointWorld) — Scales predictive modeling in 3D point space, improving geometry-aware future prediction and manipulation across diverse real-world scenes and object configurations.
- \[2025.6] **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** [paper](https://arxiv.org/abs/2506.09985) [project](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) [code](https://github.com/facebookresearch/vjepa2) — Learns predictive video representations at scale and transfers them to visual understanding, anticipation, and planning for physical tasks.

## Verification, Recovery, and Safety Evaluation

- \[2026.8] **MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation** [paper](https://arxiv.org/abs/2608.17386) — Evaluates manipulation trajectories against explicit safety specifications and provides annotated data for improving process-level physical safety during execution.
- \[2026.7] **SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents** [paper](https://arxiv.org/abs/2607.14543) — Measures safety violations caused by changing spatial relations during execution, revealing failures that final-state success metrics overlook during long-horizon tasks.
- \[2026.7] **EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards** [paper](https://arxiv.org/abs/2607.00218) — Tests embodied VLMs as streaming runtime guards using temporally annotated egocentric scenarios and diagnostic categories of physical risk.
- \[2026.6] **Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement** [paper](https://arxiv.org/abs/2606.18247) — Uses visual outcome verification to steer policy execution at inference time and generate signals for autonomous policy improvement.
- \[2026.5] **Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts** [paper](https://arxiv.org/abs/2605.22446) — Verifies proposed VLA and world-model rollouts before execution, preventing unsafe or inconsistent actions rather than reacting after failure.
- \[2026.4] **Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA** [paper](https://arxiv.org/abs/2604.02965) — Pairs efficient open-loop action planning with closed-loop speculative verification, preserving speed while catching execution drift and task errors.
- \[2024.10] **AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation** [paper](https://arxiv.org/abs/2410.00371) — Detects manipulation failures from visual observations and reasons about their causes, supporting interpretable diagnosis before recovery planning and replanning.
- \[2023.3] **Vision-Language Models as Success Detectors** [paper](https://arxiv.org/abs/2303.07280) — Evaluates general-purpose vision-language models as reusable task-success detectors, reducing the need for separately trained reward or verification models.

## Failure Detection and Recovery

- \[2026.1] **CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding** [paper](https://arxiv.org/abs/2601.02295) [project](https://dannymcy.github.io/cyclevla/) — Proactively detects uncertain subtasks, backtracks execution, and uses minimum Bayes risk decoding to select safer corrective VLA actions.
- \[2025.10] **FailSafe-VLM: Reasoning and Recovery from Failures in Vision-Language-Action Models** [paper](https://arxiv.org/html/2510.01642v1) — Uses vision-language reasoning to identify VLA execution failures, explain their causes, and produce context-sensitive recovery strategies during long-horizon execution.
- \[2025.9] **FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction** [paper](https://arxiv.org/abs/2509.04018) [project](https://fpcvla.github.io/) — Adds a supervisory model that predicts impending failures and corrects VLA actions before errors propagate through long-horizon tasks.
- \[2025.6] **SAFE: Multitask Failure Detection for Vision-Language-Action Models** [paper](https://arxiv.org/abs/2506.09937) [project](https://vla-safe.github.io/) — Trains a shared failure detector across manipulation tasks, improving recognition of execution errors without task-specific monitoring models or reward functions.
- \[2024.9] **Automating Robot Failure Recovery Using Vision-Language Models** [paper](https://arxiv.org/abs/2409.03966) — Uses vision-language models to interpret execution failures and automatically select recovery actions, establishing a practical general-purpose recovery pipeline.

## Skill Learning and Tool Use

- \[2026.6] **CLASP: Language-Driven Robot Skill Selection and Composition using Task-Parameterized Learning** [paper](https://arxiv.org/abs/2606.08169) — Uses language to select and compose task-parameterized robot skills, supporting adaptable execution beyond fixed primitive sequences and object configurations.
- \[2026.3] **CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation** [paper](https://arxiv.org/abs/2603.22435) — Benchmarks code-generating agents on robot manipulation and provides a framework for improving executable programs through environment feedback and iterative repair.
- \[2026.3] **Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation** [paper](https://arxiv.org/abs/2603.02623) — Builds a reusable skill repository that expands from experience, allowing manipulation agents to retrieve, adapt, and consolidate capabilities.
- \[2025.5] **Dynamic Robot Tool Use with Vision Language Models** [paper](https://arxiv.org/abs/2505.01399) — Uses vision-language reasoning to select, localize, and operate previously unseen physical tools under changing task requirements and scene conditions.
- \[2025.5] **DeCo: Task Decomposition and Skill Composition for Zero-Shot Generalization in Long-Horizon 3D Manipulation** [paper](https://arxiv.org/abs/2505.00527) [project](https://deco226.github.io/) — Decomposes language goals and composes learned 3D manipulation skills, enabling zero-shot generalization to new long-horizon task combinations and environments.
- \[2025.5] **RAI: Flexible Agent Framework for Embodied AI** [paper](https://arxiv.org/abs/2505.07532) [code](https://github.com/RobotecAI/rai) — Provides a modular agent framework that connects language reasoning with ROS tools, robot skills, logging, and execution feedback.
- \[2024.6] **ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning** [paper](https://arxiv.org/abs/2406.19741) — Integrates structured language-model reasoning with ROS execution and task feedback, exposing robot capabilities through a practical agent interface.
- \[2022.9] **Code as Policies: Language Model Programs for Embodied Control** [paper](https://arxiv.org/abs/2209.07753) — Generates executable policy code that composes perception and control APIs, establishing a foundational approach to language-driven robot tool use.

## Long-Horizon Manipulation

- \[2026.6] **SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation** [paper](https://arxiv.org/abs/2606.12956) — Maintains spatiotemporal environment and robot features to support persistent state tracking across long-horizon mobile manipulation tasks under partial observability.
- \[2026.4] **Long-Horizon Manipulation via Trace-Conditioned VLA Planning** [paper](https://arxiv.org/abs/2604.21924) — Conditions VLA planning on structured execution traces, preserving progress information and improving action selection over extended manipulation sequences.
- \[2026.4] **Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection** [paper](https://arxiv.org/abs/2604.13942) — Converts goals into reusable skills and adapts their composition through execution feedback and reflection during long-horizon manipulation and unexpected state changes.
- \[2026.3] **ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation** [paper](https://arxiv.org/abs/2603.27670) — Models task progress explicitly and uses it to guide diffusion-based action generation across multi-stage language-conditioned manipulation and recovery.
- \[2026.2] **LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies** [paper](https://arxiv.org/abs/2602.21531) — Links object-centric policies into compositional plans, enabling VLA execution to reuse local behaviors across longer manipulation tasks and environments.

## Embodied Navigation

- \[2026.8] **Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation** [paper](https://arxiv.org/abs/2608.17512) — Introduces TAMP-Nav, combining pixel-to-3D actions, selective reasoning, trajectory memory, and process-level alignment for efficient embodied navigation with lower overhead.
- \[2026.6] **SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning** [paper](https://arxiv.org/abs/2606.08992) — Maintains online spatial cognitive memory and reasons over it to perform zero-shot language-guided navigation in unseen environments without task-specific training.
- \[2026.3] **AgentVLN: Towards Agentic Vision-and-Language Navigation** [paper](https://arxiv.org/abs/2603.17670) — Reframes vision-language navigation as an agentic loop with explicit reasoning, state tracking, and adaptive decisions during execution and failures.
- \[2026.3] **SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation** [paper](https://arxiv.org/abs/2603.06914) — Coordinates reasoning and control at multiple levels to support real-world object navigation across different robot embodiments and environment types.
- \[2024.12] **\[RSS 2025] Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks** [paper](https://arxiv.org/abs/2412.06224) [project](https://pku-epic.github.io/Uni-NaVid/) — Uses video-conditioned action prediction to unify multiple embodied navigation settings within a single vision-language-action model and deployment environments.
- \[2022.7] **LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action** [paper](https://arxiv.org/abs/2207.04429) — Composes pretrained language, vision, and navigation models without task-specific fine-tuning, demonstrating modular zero-shot robot navigation across unseen environments.
- \[2018.6] **\[CVPR] Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments** [paper](https://openaccess.thecvf.com/content_cvpr_2018/papers/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.pdf) — Introduces the Room-to-Room task and benchmark, establishing the standard formulation for grounding natural-language instructions in embodied navigation and evaluation.

## Human-Robot Interaction

- \[2024.1] **Understanding LLM-powered Human-Robot Interaction** [paper](https://arxiv.org/abs/2401.03217) — Examines how large language models reshape human-robot communication, task interpretation, trust, and interaction design in embodied settings and deployments.
- \[2023.3] **Large Language Models as Zero-Shot Human Models for Human-Robot Interaction** [paper](https://arxiv.org/abs/2303.03548) — Uses language models to predict human preferences and behavior without task-specific training, supporting adaptive planning in human-robot interaction.

## Governance and Physical Safety

- \[2026.5] **Consent Chain Degradation in Embodied Multi-Agent Systems** [paper](https://arxiv.org/html/2605.16300v1) — Studies how consent constraints weaken across delegated multi-agent execution, exposing governance risks unique to embodied action chains and delegation structures.
- \[2026.4] **EmbodiedGovBench: A Benchmark for Governance-Constrained Embodied Agents** [paper](https://arxiv.org/html/2604.11174v1) — Evaluates whether embodied agents follow governance policies while pursuing tasks, separating rule compliance from conventional completion metrics or isolated benchmarks.
- \[2026.4] **Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution** [paper](https://arxiv.org/abs/2604.07833) — Introduces runtime governance mechanisms that monitor and constrain agent actions against explicit policies during physical execution with minimal latency.

## Benchmarks and Datasets

- \[2026.3] **RoboCasa365: A Large-Scale Simulation Framework for Generalist Robot Policies** [paper](https://arxiv.org/html/2603.04356v1) — Expands everyday manipulation simulation with broad tasks and environments for training and evaluating generalist, long-horizon robot policies across varied settings.
- \[2025.4] **RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins** [paper](https://arxiv.org/abs/2504.13059) — Uses generative digital twins to scale diverse dual-arm manipulation tasks, data collection, and reproducible policy evaluation across varied scenes.
- \[2023.10] **Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots** [paper](https://arxiv.org/abs/2310.13724) — Provides interactive human-avatar-robot simulation for studying navigation, collaboration, and socially situated embodied agents at scale across collaborative tasks.
- \[2023.10] **Open X-Embodiment: Robotic Learning Datasets and RT-X Models** [paper](https://arxiv.org/abs/2310.08864) [project](https://robotics-transformer-x.github.io/) [code](https://github.com/google-deepmind/open_x_embodiment) [dataset](https://robotics-transformer-x.github.io/) — Aggregates cross-institution robot datasets and RT-X models, establishing a shared foundation for cross-embodiment learning, transfer, and generalization at scale.
- \[2023.6] **LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning** [paper](https://arxiv.org/abs/2306.03310) — Evaluates lifelong robot learning across task suites designed to test knowledge transfer, retention, and efficient adaptation across sequential tasks.
- \[2021.12] **CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks** [paper](https://arxiv.org/abs/2112.03227) — Benchmarks language-conditioned policies on diverse, compositional manipulation chains, making long-horizon completion and generalization directly measurable across extended task sequences.

## Open-Source Foundation Models

- \[2024.5] **Octo: An Open-Source Generalist Robot Policy** [paper](https://arxiv.org/abs/2405.12213) [project](https://octo-models.github.io/) [code](https://github.com/octo-models/octo) — Provides an openly released generalist robot policy, training stack, and checkpoints built from heterogeneous manipulation datasets across embodiments.

## Industrial Systems

- \[2025.3] **\[Google DeepMind] Gemini Robotics: Bringing AI into the Physical World** [paper](https://arxiv.org/abs/2503.20020) — Presents an industrial-scale embodied reasoning model and generalist VLA system designed to transfer semantic understanding into dexterous physical action.

## Extended Reading

Papers moved out of the main list during the 2026-08-27 curation pass remain available in [extended-reading.md](extended-reading.md). They are useful adjacent work, but scored lower on direct agentic relevance, influence, evidence, representativeness, or resource completeness.

## Related Awesome Lists

- [Awesome Memory for Robotics](https://github.com/Everloom-129/Awesome-Memory-for-Robotics)
- [Awesome World Models](https://github.com/leofan90/Awesome-World-Models)
- [Awesome Embodied VLA / VA / VLN](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)

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

## Contributing

Contributions are welcome. Please read [contributing.md](contributing.md) before submitting a pull request.
