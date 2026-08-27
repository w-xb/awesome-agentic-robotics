# Contributing

Thanks for helping improve Awesome Agentic Robotics. The main README is intentionally limited to 100 high-signal papers; broader but relevant work belongs in [extended-reading.md](extended-reading.md).

## Scope

Submissions should materially advance at least one capability of physical agency:

- planning, reasoning, and skill composition
- VLA-as-tools, hierarchical VLA, or online VLA adaptation
- embodied memory and persistent state maintenance
- world models used for prediction, evaluation, or control
- execution verification, failure attribution, and recovery
- robot tool use, skill calling, or execution interfaces
- long-horizon manipulation or navigation
- governance, runtime safety, or process-level evaluation

General VLA work is not included solely because it improves accuracy, speed, or scale. It must clearly improve closed-loop autonomy, long-horizon execution, tool use, verification, recovery, memory, world-model-based decisions, continual adaptation, or cross-embodiment deployment.

## Selection Rubric

Maintainers score candidates on a ten-point rubric:

| Criterion | Points | What earns a high score |
| --- | ---: | --- |
| Agentic relevance | 0–3 | The work directly changes how a physical agent plans, remembers, invokes capabilities, verifies, recovers, adapts, or remains safe. |
| Influence | 0–2 | The work is foundational, broadly adopted, peer reviewed, strongly cited for its age, or likely to shape the field. |
| Evidence quality | 0–2 | Claims are supported by real-robot results, strong embodied benchmarks, careful ablations, or unusually comprehensive evaluation. |
| Representativeness | 0–2 | The work is a clear reference for an important idea and is not redundant with a stronger paper already listed. |
| Resource completeness | 0–1 | Official code, models, datasets, or a well-maintained project page make the work easier to reproduce and use. |

Main-list candidates normally score at least 7/10 and at least 2/3 for agentic relevance. Because the README remains capped at 100 papers, a new addition should replace a weaker or less representative canonical entry. Relevant candidates that do not clear the threshold may be added to Extended Reading.

## Entry Format

Use the first public release month, normally the first arXiv submission date, and add a neutral 18–35 word contribution summary:

```md
- \[YYYY.M] Title [paper](https://example.com) [project](https://example.com) [code](https://example.com) — Concise, neutral description of the work's distinctive contribution to physical agency.
```

Use link labels consistently:

- `[paper]` for the official publication or preprint
- `[project]` for the authors' project page
- `[code]` for the official implementation
- `[model]` for official model weights
- `[dataset]` for official data

Only add links explicitly provided by the authors or publishing organization. Each paper has one canonical entry and must not be duplicated across topic sections. Must Read descriptions are maintained by the repository curators and use 30–50 words.

## Pull Request Checklist

Before opening a pull request:

- explain the paper's agentic contribution and rubric score
- identify the existing entry it should replace, if proposing a main-list addition
- verify the exact title, first-public-release month, and arXiv identifier
- confirm every project, code, model, and dataset link is official
- search both README files for duplicate titles and identifiers
- keep entries sorted newest first within their canonical section
- run `npx awesome-lint README.md`
- confirm the main README still contains exactly 100 unique paper entries
