# Contributing

Thanks for helping improve Awesome Agentic Robotics.

This list is intentionally selective. Please add resources that contribute to at least one core capability of physical agency:

- embodied memory and state maintenance
- planning, reasoning, and skill composition
- world models and world-action models
- execution verification and self-evaluation
- failure detection, attribution, and recovery
- tool use, skill calling, and robot API invocation
- long-horizon manipulation and navigation
- human-robot interaction for agentic execution
- safety, governance, and physical-risk constraints

## Adding an Entry

Please follow the existing format:

```md
- \[YYYY.M] Title [paper](https://example.com) [project](https://example.com) [code](https://example.com)
```

Use the first public release month when possible, usually the arXiv month for papers.

## Selection Criteria

Good entries should be relevant to agentic robotics, not only general robotics or generic world modeling. A paper does not need to be a complete agentic robot system, but it should clearly contribute to a component of physical agency.

General VLA work belongs in this list only when it materially advances closed-loop autonomy, long-horizon execution, tool or skill use, verification and recovery, embodied memory, world-model-based decision making, continual adaptation, or deployment across embodiments. A more accurate or efficient VLA is not automatically an agentic VLA.

Please prefer:

- peer-reviewed papers, arXiv preprints, technical reports, or well-documented open-source systems
- works with real-robot evidence, a standard embodied benchmark, a reusable system or dataset, or a clearly defined new capability
- resources with working official paper, project, code, model, or dataset links
- systems that make the planning, memory, tool-use, verification, recovery, or adaptation mechanism explicit

Please avoid:

- weakly related robotics papers with no agentic component
- generic VLA training, compression, or inference papers without a clear effect on autonomous embodied behavior
- pure LLM-agent papers without a robotics or embodied AI connection
- abandoned repositories or undocumented projects
- duplicate entries across multiple sections unless the cross-listing is essential

## Pull Requests

Before opening a pull request:

- verify titles and first-public-release dates against the paper or project page
- check that links work and point to official sources
- search for duplicate titles and arXiv identifiers
- keep entries sorted by `[YYYY.M]` in descending order within each section
- keep descriptions concise and neutral
- run `npx awesome-lint README.md`
