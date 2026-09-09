# Center for Open Neuroscience site inputs

This directory is the declarative, site-owned layer of the Center for Open Neuroscience website and a presentation-independent store of reviewed CON metadata.
It is the repository root here and is integrated at `site-specific/` in the Orinoco Lite downstream through `git subtree`.
Paths in this document are relative to this directory.

## Content provenance

The full provenance for this content is not yet consolidated.
Its history is spread across:

- [CON research information](https://github.com/con/dump-research-info/);
- [the Orinoco Lite demo](https://github.com/leej3/orinoco-lite-demo); and
- [the existing CON website](https://centerforopenneuroscience.org).

Additional context for the earlier trimming of `orinoco-lite-demo` is preserved in [this shared conversation](https://claude.ai/share/a2aeb683-48a5-4f41-aff1-db2287ef3566).

## Structure

| Path | Purpose |
| --- | --- |
| `metadata/records/` | Reviewed Things YAML records; preserve stable PIDs. |
| `metadata/overlays/annotations/` | Machine-managed provenance companions. |
| `site.yaml` | CON identity, navigation, and presentation choices. |
| `content/` | Editorial pages, group order, and Hugo page resources. |
| `assets/`, `static/` | Site-owned presentation and static assets. |
| `sources/`, `curation-records/` | Source declarations and reviewed curation decisions. |

Together, `metadata/records/` and `metadata/overlays/annotations/` are the canonical metadata store for reviewed CON assertions and their machine provenance.
The Orinoco Lite website is one projection of those inputs.
Other consumers can derive different representations from the same metadata without depending on the website or treating generated output as canonical.

The homepage is `content/_index.md`.
Portraits live beside generated person pages as `portrait.*`, and project artwork lives beside generated project pages as `logo.*`.
These are ordinary Hugo page resources and do not require a downstream theme override.

Source declarations refer to executable adapters under `extensions/source-adapters/` from the downstream repository root.
Adapter code and the Orinoco Lite scaffold remain outside this subtree.

## Intentional presentation differences

These choices are specific to CON; shared behavior follows the [Orinoco Lite design charter](https://github.com/ORINOCO-Lite/orinoco-lite-dev/blob/main/docs/project-design.md) and its contracts.

- **Grouped people directory.** CON deliberately retains Centroids, Collaborators, Affiliated Faculty, and Emeritus instead of the upstream's single people listing.
  [The people page](content/persons/_index.md) owns the group membership and display order; preserve them during presentation and release updates.
  The “Other people” section keeps additional records visible when no group placement has been supplied, without asserting a role or involvement status.
  Do not change groups or membership merely to match upstream.
  Make proposed editorial changes explicit in a content pull request for maintainer review, using the existing `people-group` shortcode rather than a copied theme layout.

## Subtree integration

Import this history into a new downstream without squashing it:

```console
git subtree add \
  --prefix=site-specific \
  git@github.com:ORINOCO-Lite/con-site-specific.git \
  main
```

Pull a reviewed content update into an existing downstream with:

```console
git subtree pull \
  --prefix=site-specific \
  git@github.com:ORINOCO-Lite/con-site-specific.git \
  main
```

Do not add `--squash`; the focused history in this repository is part of the subtree's value.

## Edit, validate, and preview

Run these commands from the downstream repository root, not this directory:

```console
pixi run validate
pixi run build
pixi run serve
```

Review the source diff and rendered build.
Do not commit or hand-edit generated projection output.

## Documentation above this layer

- [Orinoco Lite template](https://github.com/ORINOCO-Lite/orinoco-lite-template): downstream scaffold creation and maintenance.
- [Project design charter](https://github.com/ORINOCO-Lite/orinoco-lite-dev/blob/main/docs/project-design.md): system responsibilities and data flows.
- [Orinoco Lite package](https://github.com/ORINOCO-Lite/orinoco-lite-dev/tree/main/packages/orinoco-lite): commands and package integrity.
- [Orinoco Lite releases](https://github.com/ORINOCO-Lite/orinoco-lite-dev/releases): immutable package and template selections.

Those shared layers do not own CON records, site-specific policy, or this site's provenance.
