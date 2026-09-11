# Contributing

Thanks for helping improve Awesome Agentic Robotics. The main README is a selective, evolving map of high-signal work; broader, narrower, or less established work belongs in [extended-reading.md](extended-reading.md).

## Before You Submit

- Search both `README.md` and `extended-reading.md` for the title, arXiv identifier, and common short name.
- Prefer one paper or resource per pull request so placement and evidence can be reviewed independently.
- Use the paper-suggestion issue template if you want feedback on fit before preparing a pull request.
- Use official publication, project, code, model, and dataset links only.
- Keep descriptions neutral and contribution-focused rather than promotional.

## Scope

Submissions should materially advance at least one capability of physical agency:

- planning, reasoning, and skill composition
- VLA-as-tools, hierarchical VLA, or online VLA adaptation
- embodied memory and persistent state maintenance
- world models used for prediction, evaluation, or control
- execution verification, failure attribution, and recovery
- robot tool use, skill calling, or execution interfaces
- self-evolving skills, policies, objectives, data pipelines, verifiers, or runtime harnesses
- long-horizon manipulation or navigation
- governance, runtime safety, or process-level evaluation

General VLA work is not included solely because it improves accuracy, speed, or scale. It must clearly improve closed-loop autonomy, long-horizon execution, tool use, verification, recovery, memory, world-model-based decisions, continual adaptation, or cross-embodiment deployment.

## Placement Rule

Each work has one canonical entry in the main README. Place it according to the component or capability it changes most directly, not every mechanism it happens to use.

A paper may use memory, planning, and verification simultaneously; if its distinctive contribution is a recovery supervisor, its canonical home is **Failure Detection and Recovery**. Mention secondary capabilities in the description instead of duplicating the entry.

For self-evolving work, distinguish **persistent updates that affect future episodes** from transient replanning, retrying, test-time adaptation, or fixed-library retrieval. Use the closest primary target: `harness/runtime`, `skill/library`, `contract/verifier`, `policy/data`, `objective/reward`, or `memory/context`.

## Selection Rubric

Maintainers score candidates on a ten-point rubric:

| Criterion | Points | What earns a high score |
| --- | ---: | --- |
| Agentic relevance | 0–3 | The work directly changes how a physical agent plans, remembers, invokes capabilities, verifies, recovers, adapts, or remains safe. |
| Influence | 0–2 | The work is foundational, broadly adopted, peer reviewed, strongly cited for its age, or likely to shape the field. |
| Evidence quality | 0–2 | Claims are supported by real-robot results, strong embodied benchmarks, careful ablations, or unusually comprehensive evaluation. |
| Representativeness | 0–2 | The work is a clear reference for an important idea and is not redundant with a stronger paper already listed. |
| Resource completeness | 0–1 | Official code, models, datasets, or a well-maintained project page make the work easier to reproduce and use. |

Main-list candidates normally score at least **7/10** and at least **2/3** for agentic relevance. The list may grow as important work appears, but additions must clear the same quality bar and offer a distinct contribution beyond existing entries. Relevant, narrower, or less established candidates may be added to Extended Reading.

## Entry Format

Use the first public release month, normally the first arXiv submission or public project release, and add a neutral 18–35 word contribution summary:

```md
- [YYYY.M · Title](https://paper.example) - Concise, neutral description of the work's distinctive contribution to physical agency. Resources: [Project](https://project.example) · [Code](https://code.example).
```

The title should link to the official publication or preprint. Use supplementary link labels consistently:

- `[Project]` for the authors' project page
- `[Code]` for the official implementation
- `[Model]` for official model weights
- `[Dataset]` for official data

Only add links explicitly provided by the authors or publishing organization. Keep entries sorted newest first within their canonical section.

The **Start Here / Must Read** routes are intentionally maintainer-curated. A paper can be accepted to the main list without being added to Must Read. Changes to the taxonomy or top-level categories should be proposed separately from ordinary paper additions.

## Pull Request Checklist

Before opening a pull request:

- use a title such as `Add <paper or system name>`
- explain the work's agentic contribution and estimated rubric score
- explain why it merits main-list placement rather than Extended Reading
- identify the proposed canonical section and any secondary capabilities
- verify the exact title, first-public-release month, and paper identifier
- confirm every project, code, model, and dataset link is official
- search both Markdown files for duplicate titles and identifiers
- classify self-evolving entries by their primary persistent update target
- keep entries sorted newest first within their canonical section
- run `python3 scripts/validate_list.py` and `npx awesome-lint` from the repository root
- avoid unrelated formatting or taxonomy changes in the same pull request

Thank you for helping keep the list selective, useful, and easy to navigate.
