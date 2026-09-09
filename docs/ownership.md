# File ownership

The template owns the downstream scaffold, generic workflows and documentation, and every path under `.orinoco-lite/`.
That private namespace contains the small presentation adaptation, bounded licensed asset overlay, and tools that must remain aligned with the selected package and template.
The package resolves the complete upstream website, projection templates, and theme rather than copying them into this repository.

The downstream owns all declarative inputs under `site-specific/`, executable metadata adapters under `extensions/`, optional downstream-specific tests under `tests/`, release selection, repository policy, and generated deployment history.

Ordinary presentation belongs in `site-specific/site.yaml`, content, assets, and static inputs.
A custom layout is supported only as an explicit file under `site-specific/overrides/layouts/`.
Website code under `extensions/` is invalid, and extension source or generated outputs are never copied into a build.

Editorial files in `site-specific/content/` are applied after generated pages.
A site can supply `_index.md` for its homepage or a section and place ordinary Hugo page resources beside generated records, without copying their layouts.
Use `portrait.*` for people and `logo.*` for projects.

For a grouped people index, use `layout: editorial` and the `people-group` shortcode, with one `persons/<record-name>` page reference per line in its body.
The shortcode reuses the upstream cards and preserves the supplied order.
The `graph` shortcode embeds the upstream graph on an editorial page.
Set `params.hideGraph: true` on an editorial homepage to show its text alone.

## `site-specific` subtree

The website repository is the operational editing and review surface for changes submitted through the website.
The standalone [`ORINOCO-Lite/con-site-specific`](https://github.com/ORINOCO-Lite/con-site-specific) repository retains the focused history and distributes the same inputs to other projections.
The subtree is therefore integrated without squashing.

Synchronization uses a downstream-specific export workflow that splits `site-specific/` after an accepted change reaches `main` and pushes the focused history to the standalone repository.
The push must be a fast-forward from its current `main`; divergence must stop the workflow rather than overwrite either history.
Pull and review any intentional standalone change in this repository before accepting further website edits.

A commit must change either `site-specific/` or files owned by the parent repository, never both.
This boundary makes every subtree export independent of framework, adapter, workflow, and documentation changes.
Install the repository hook with `pixi run hooks-install` to enforce the boundary locally.
