# Agent instructions

## Scope and review

This repository publishes the Center for Open Neuroscience website from the released Orinoco Lite components selected in `orinoco.lock` and `pixi.lock`.
Read [ownership](docs/ownership.md), `site-specific/site.yaml`, and the current diff before editing.
Use the existing maintenance, content, or adapter skill for the applicable work; the site policy here governs how those workflows apply.

Agents may prepare ordinary, attributed metadata and content pull requests for maintainers to review and merge.
Prefer an existing source adapter when it fits, but do not require a new adapter or recorded accept/reject/defer decisions before proposing a bespoke correction.
An unresolved curatorial choice can be presented with evidence and alternatives in the pull request.
Do not invent facts, identities, roles, affiliations, rights, or human approval.
Never describe an AI proposal as human-authored or human-reviewed.
Do not approve, merge, or deploy a proposal on a maintainer's behalf.

## Website content

Keep declarative site content in `site-specific/` and executable metadata adapters in `extensions/source-adapters/`.
Reuse the selected upstream presentation and supported site configuration; propose reusable rendering fixes upstream instead of copying theme implementation into this site.
Show existing people without requiring a current/former classification or inventing involvement status.
The homepage retains useful contribution and support material; the former standalone engagement and support routes are intentionally retired.
Do not recreate legacy routes, aliases, or redirects merely to reproduce the previous website.

## Schema and assertion provenance

The installed, locked package supplies the schema.
Resolve `Path(orinoco_lite.__file__).parent / "_resources/schema/demo-research-information/unreleased.yaml"`, load it with `linkml_runtime.SchemaView`, and resolve the record's `schema_type` to its declared schema class before inspecting induced slots.
Check slot ranges, cardinality, prefixes, and qualified-object shapes.
Existing `xyzri:*` record classes and `dlthings:*` qualified types are intentional; do not substitute a newer upstream schema or invent YAML keys.

Read each record and its matching companion under `site-specific/metadata/overlays/annotations/`, when present, before editing.
Records hold semantic assertions; companions hold machine-import PAV.
Preserve unrelated assertions and unchanged provenance.
Companion selectors use `path`, `assertion_sha256`, `pav:importedBy`, and `pav:importedFrom`; a collection selector uses the collection path and assertion digest, not an array index.
Do not put imported PAV inline in records or invent a semantic field for AI attribution.

For a curator-directed correction, use `orinoco_lite.annotations.reconcile_annotation_companion(record, companion)` to remove selectors whose assertions no longer match.
Do not retarget an old import digest to newly authored content or drop unrelated selectors.
Use `orinoco_lite.canonical.canonical_yaml` for changed mappings and validate the complete joined graph.

For assertions actually imported or transcribed from an external source by software, use the real implementation identity and actual source record with the locked `orinoco_lite.enrichment` helpers: `update_schema_data_property`, `update_object_property`, or `update_multivalued_object_property` as appropriate.
These helpers preserve the upstream ownership rules and return the record, companion, and modification flag.
Do not borrow a Zotero or `dump-research-info` importer identity for a bespoke AI edit that did not run that importer, and do not mint an identity merely to fill provenance fields.
If the available provenance cannot accurately describe the proposed change, make that limitation explicit for review.

The companion terms `pav:importedBy` and `pav:importedFrom` describe import, not AI participation or approval.
Mechanical edits and literal implementation of a human-supplied correction are not automatically imports.
AI retrieval and transcription of external facts is import-like; an AI inference is not a claim of faithful import.
Identify sources, inferences, and limitations in the pull request, and attribute AI participation in Git and the pull request.
Absence of an import companion never proves human authorship.
Record adapter dispositions only from an explicit human decision, using the adapter's supported transaction.

## Validation and handoff

- Run `pixi run --frozen validate` and `pixi run --frozen verify-build`, then inspect affected pages and the final source diff.
- Run focused adapter tests when adapter code or policy changes.
- Use the Snapper pre-commit hook for prose.
- Keep caches, generated projections, browser output, and builds untracked.
- A commit must change either `site-specific/` or parent-repository files, never both; preserve the unsquashed subtree history.
- Use Conventional Commits and wrap prose near 80 columns.
  Resolve exact active Codex tool, model, and reasoning-effort provenance immediately before each Codex-authored commit; do not guess it.
- Use the configured SSH credential for GitHub Git pushes.
- Prefix posted agent-authored GitHub pull-request bodies and comments with `**AI-generated draft — not reviewed by John**`.
  Do not alter a posted comment after John edits it; post a new attributed correction instead.
