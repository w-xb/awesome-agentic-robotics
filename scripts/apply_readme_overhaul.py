from pathlib import Path
import re

p = Path("README.md")
s = p.read_text(encoding="utf-8")

s = s.replace(
    "A living, selective reading list of influential work on autonomous physical agents, spanning planning, agentic VLA, memory, world models, verification, recovery, tool use, and safety.\n\n**Last updated:** 2026-09-07",
    "Agentic Robotics studies autonomous physical agents that reason, remember, plan, use tools, verify execution, recover from failure, and improve from embodied experience.\n\nA selective, living collection of influential papers, systems, benchmarks, and open-source resources spanning agent orchestration, VLA, memory, world models, verification, recovery, self-evolution, and physical safety.\n\n**Last updated:** 2026-09-11",
)

s = s.replace(
    "- [What Agentic Robotics Means Here](#what-agentic-robotics-means-here)\n",
    "- [What Agentic Robotics Means Here](#what-agentic-robotics-means-here)\n- [Taxonomy: Agent–Harness–VLA Stack](#taxonomy-agentharnessvla-stack)\n",
)
s = s.replace(
    "- [Verification, Recovery, and Safety Evaluation](#verification-recovery-and-safety-evaluation)",
    "- [Verification and Safety Evaluation](#verification-and-safety-evaluation)",
)
s = s.replace(
    "- [Open-Source Foundation Models](#open-source-foundation-models)\n- [Industrial Systems](#industrial-systems)",
    "- [Foundations and Industrial Systems](#foundations-and-industrial-systems)",
)
if "- [Related Awesome Lists](#related-awesome-lists)" not in s.split("## What Agentic Robotics Means Here", 1)[0]:
    s = s.replace(
        "- [Extended Reading](#extended-reading)\n- [Citation](#citation)",
        "- [Extended Reading](#extended-reading)\n- [Related Awesome Lists](#related-awesome-lists)\n- [Citation](#citation)",
    )

marker = "Agentic robotics is a continuum rather than a binary label. Not every work in this list presents a complete autonomous robot: some contribute a single capability, while others integrate several capabilities into a closed-loop system. This repository maps both the components of physical agency and the architectures that bring them together.\n\n"
taxonomy = """## Taxonomy: Agent–Harness–VLA Stack

The organizing view behind this repository is a closed-loop stack:

```text
Goal / Human Intent
        ↓
Agent / Planner
(reasoning · decomposition · task state)
        ↓
Harness / Runtime
(memory · tools · routing · verification · recovery · safety)
        ↓
VLA / Policy
(grounded perception-to-action execution)
        ↓
Robot + Physical World
        │
        └── observations · outcomes · failures ──↺

Persistent, validated updates across episodes → Self-Evolution
```

The **agent** decides *what* should happen; the **harness** coordinates components and governs execution; the **VLA/policy** performs grounded physical actions; the **physical world** supplies evidence about success, failure, and safety. **Self-evolution** begins when validated changes persist and influence future episodes.

This stack is a research lens rather than a claim that every system must use the same modular architecture. Papers are placed by their **primary agentic contribution**, while secondary capabilities are described in the entry. See **[TAXONOMY.md](TAXONOMY.md)** for layer boundaries, evolution targets, and open research questions.

"""
if "## Taxonomy: Agent–Harness–VLA Stack" not in s:
    s = s.replace(marker, marker + taxonomy)

s = s.replace(
    "**Links:** `[paper]` publication or preprint · `[project]` official project page · `[code]` official implementation · `[model]` official weights · `[dataset]` official data",
    "**Canonical placement.** A paper is categorized by the component or capability it changes most directly. Secondary capabilities are reflected in the description rather than by duplicating the paper across sections.\n\n**Links:** Each canonical title links to the official publication or preprint. Supplementary resources use `[Project]`, `[Code]`, `[Model]`, and `[Dataset]`.",
)

must_read = {
    "Harness VLA": "https://arxiv.org/abs/2607.08448",
    "VLAs-as-Tools": "https://arxiv.org/abs/2605.13119",
    "Agentic Robot": "https://arxiv.org/abs/2505.23450",
    "ART": "https://arxiv.org/abs/2608.14047",
    "Gemini Robotics 1.5": "https://arxiv.org/abs/2510.03342",
    "Zetta ζ": "https://arxiv.org/abs/2608.16590",
    "SHAPER": "https://arxiv.org/abs/2608.11350",
    "ASPIRE": "https://arxiv.org/abs/2607.00272",
    "VASO": "https://arxiv.org/abs/2606.05395",
    "ENPIRE": "https://arxiv.org/abs/2606.19980",
    "τ_0-VLA": "https://arxiv.org/abs/2608.16885",
    "G0.5": "https://arxiv.org/abs/2608.11739",
    "Qwen-VLA": "https://arxiv.org/abs/2605.30280",
    "π0.5": "https://arxiv.org/abs/2504.16054",
    "Hi Robot": "https://arxiv.org/html/2502.19417v1",
    "AtlasVLA": "https://arxiv.org/abs/2608.06729",
    "MEMORA": "https://arxiv.org/abs/2607.14252",
    "MemoryVLA": "https://arxiv.org/abs/2508.19236",
    "τ_0-WM": "https://arxiv.org/abs/2606.01027",
    "V-JEPA 2": "https://arxiv.org/abs/2506.09985",
    "SayCan": "https://arxiv.org/abs/2204.01691",
    "Inner Monologue": "https://arxiv.org/abs/2207.05608",
    "MANIGUARD": "https://arxiv.org/abs/2608.17386",
    "RoboCasa365": "https://arxiv.org/html/2603.04356v1",
    "Open X-Embodiment": "https://arxiv.org/abs/2310.08864",
}
for name, url in must_read.items():
    s = s.replace(f"**{name}** —", f"**[{name}]({url})** —")

s = s.replace(
    "## Verification, Recovery, and Safety Evaluation\n\n> Success detection, temporal and specification-grounded verification, runtime policy steering, execution checking, and process-level evaluation of physical safety.",
    "## Verification and Safety Evaluation\n\n> Success detection, temporal and specification-grounded verification, runtime policy steering, execution checking, and process-level evaluation of physical safety. Papers whose primary contribution is diagnosis or repair are listed separately under Failure Detection and Recovery.",
)

s = s.replace(
    "## Open-Source Foundation Models\n\n> Openly released generalist robot policies, model weights, training stacks, and reusable foundations that support adaptation across tasks, environments, and embodiments.",
    "## Foundations and Industrial Systems\n\n> Openly released robot foundations and industrial technical systems that materially shape reusable generalist control, embodied reasoning, cross-embodiment transfer, or deployment practice.",
)
s = s.replace(
    "\n## Industrial Systems\n\n> Technical reports and industrial systems that demonstrate deployable embodied reasoning, generalist robot control, cross-embodiment transfer, and real-world product direction.\n",
    "\n",
)

entry_re = re.compile(
    r"^- \\\[(?P<date>\d{4}\.\d{1,2})\] \*\*(?P<title>.+?)\*\* "
    r"\[paper\]\((?P<paper>https?://[^)]+)\)"
    r"(?P<resources>(?: \[(?:project|code|model|dataset)\]\(https?://[^)]+\))*)"
    r" — (?P<desc>.+)$"
)
resource_re = re.compile(r" \[(project|code|model|dataset)\]\((https?://[^)]+)\)")
label_map = {"project": "Project", "code": "Code", "model": "Model", "dataset": "Dataset"}
new_lines = []
for line in s.splitlines():
    m = entry_re.match(line)
    if not m:
        new_lines.append(line)
        continue
    paper = m.group("paper").rstrip("/")
    desc = m.group("desc").strip()
    grouped = {}
    for label, url in resource_re.findall(m.group("resources")):
        url = url.rstrip("/")
        grouped.setdefault(url, []).append(label_map[label])
    resources = []
    for url, labels in grouped.items():
        resources.append("[" + " / ".join(labels) + "](" + url + ")")
    out = f'- [{m.group("date")} · {m.group("title")}]({paper}) - {desc}'
    if resources:
        if out.endswith((".", "!", "?")):
            out = out[:-1]
        out += " Resources: " + " · ".join(resources) + "."
    new_lines.append(out)
s = "\n".join(new_lines) + "\n"

gemini = "- [2025.3 · \\\\[Google DeepMind] Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)"
octo = "- [2024.5 · Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)"
lines = s.splitlines()
gi = next((i for i, line in enumerate(lines) if line.startswith(gemini)), None)
oi = next((i for i, line in enumerate(lines) if line.startswith(octo)), None)
if gi is not None and oi is not None and gi > oi:
    line = lines.pop(gi)
    oi = next(i for i, item in enumerate(lines) if item.startswith(octo))
    lines.insert(oi, line)
    s = "\n".join(lines) + "\n"

s = s.replace(
    "Papers moved out of the main list during the 2026-08-27 curation pass remain available in [extended-reading.md](extended-reading.md). They remain useful background and adjacent work.",
    "Papers moved out of the main list during the 2026-08-27 curation pass remain available in [extended-reading.md](extended-reading.md). They are useful adjacent work, but scored lower on direct agentic relevance, influence, evidence, representativeness, or resource completeness.",
)
s = s.replace(
    "url = {https://github.com/Cat-blizzard/awesome-agentic-robotics},",
    "url = {https://github.com/w-xb/awesome-agentic-robotics},",
)
s = s.replace(
    "Contributions are welcome. Please read [contributing.md](contributing.md) before submitting a pull request.",
    "Contributions are welcome. Please read [contributing.md](contributing.md) before submitting a pull request or using the paper-suggestion issue template.",
)

p.write_text(s, encoding="utf-8")
