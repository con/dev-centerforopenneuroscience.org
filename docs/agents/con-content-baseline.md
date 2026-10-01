# CON content baseline and comparison scope

This active review supports selection of CON inputs before adapting package PRs 171–173.
Retire it after that comparison work is resolved; Git and the existing curation records retain the history.

## Selected content

Use `ORINOCO-Lite/con-site-specific` and preserve its existing history.
John selected this baseline after the comparison of the four repositories' default branches.
All observations below concern those branches on September 30, 2026, not unpublished proposals or a fresh source acquisition.

| Source | Metadata and curation | Other differences from CON inputs |
| --- | --- | --- |
| `ORINOCO-Lite/con-site-specific` | Baseline: 224 records, 202 companions | Authoritative retained content history |
| `con/dev-centerforopenneuroscience.org` | Identical | Entire `site-specific/` tree identical |
| `leej3/orinoco-lite-demo` | Identical after the companion-directory rename | Current root configuration; demo identity and marker |
| `ORINOCO-Lite/test-orinoco-downstream-website` | Identical | Omits two posters and their previews; changes homepage, contact route settings, and test identity |

The source configurations, retained captures, and decision caches are byte-identical across the four sources.
The caches retain 82 accepted dump-research-info decisions and 126 accepted Zotero decisions.
Their linked submissions remain available in [demo PR 19](https://github.com/leej3/orinoco-lite-demo/pull/19#issuecomment-5420263058) and [demo PR 27](https://github.com/leej3/orinoco-lite-demo/pull/27#issuecomment-5451910959).
The 225 files in `metadata/records/` include `.dumpthings.yaml`; there are 224 records.

Preserve every record, companion's contents, editorial page, source input, decision, portrait, logo, and poster.
Only rename the companion directory to `metadata/overlays/machine-provenance-annotations/` and move the former `site.yaml` settings into the downstream's `pyproject.toml`.
The removed settings remain available in the unsquashed content history.

[Content PR 3](https://github.com/ORINOCO-Lite/con-site-specific/pull/3) and [dev-site PR 6](https://github.com/con/dev-centerforopenneuroscience.org/pull/6) contain additional presentation proposals.
Their navigation and people-directory changes were not adopted by this migration.
Existing production decisions concerning identities, portraits, rights, hosting, and approval remain open.
Schema validation does not resolve those decisions.

## Recorded preparation

The existing dev-site branch records the actual Copier update, conversion of retained site settings, and unsquashed content pull with DataLad.
Both previous default-branch histories remain ancestors of the result.
Package and template selections are retained by the existing answers, manifest, and lock.

A separate fresh dataset exercises the corresponding instantiation pattern:

1. Create a plain-Git DataLad dataset.
2. Record Copier creation from the selected template commit with starter content disabled.
3. Record `git subtree add` from the exact published CON content commit, without squashing.
4. Record conversion of the existing CON settings from their retained Git revision.
5. Activate the generated site's locked Pixi environment and validate separately.

The fresh and updated instances have identical site configuration and content trees.
The fresh instance captures website preparation, not a fresh metadata acquisition or a reconstruction of earlier content provenance.
It does not contain the existing dev site's source-adapter extensions.
German API capture, JSONL import from that API, authored German site import, and Annex media retrieval do not participate.
The package still resolves its selected upstream software normally.

## Validation and limits

- Current-package validation passes for all 224 records, with 499 graph edges and no dropped edges.
- The dev candidate builds 193 metadata pages and 876 output files; local preview verification passes.
- The retained Zotero adapter suite passes 47 tests and 14 subtests after updating its fixture paths.
- Joining the CON YAML and companions to JSONL and converting back yields zero differing records.
- Browser inspection confirms the CON homepage and grouped people directory render, without the duplicated Congo demo introduction seen on the reference deployment.
- The existing website comparator reports one missing fragment: `/review/` links to `#main-content`, but its generated page has no matching ID.
  This remains a package presentation defect, not a content repair or a passing link check.

Hosted authenticated editing and deployment have not been exercised in this review.

## Reuse of PRs 171–173

The content is compatible with the retained Things model and existing record comparison.
There is no evidence here that a separate CON diff engine is needed.

| Boundary | Reuse and next work |
| --- | --- |
| Records and companions | Existing export, roundtrip, and typed comparison run successfully on CON. |
| RDF and temporary service | Existing operations accept retained record streams. Their preservation behavior on CON has not yet been measured. |
| Authored inputs | Current `dev inputs import` requires `sourcedata/www-from-model` and imports German site inputs. CON needs an explicitly selected retained CON tree and its root site configuration. |
| Projection and assembly | Reuse the operations, but distinguish identical-input comparisons from complete paths. Current orchestration assumes upstream/Lite roles and particular preceding outputs. |
| Rendered files and links | Existing primitives work on CON; the link checker found the review-page defect above. |
| Browser review | Report and bundle machinery appears reusable by inspection. A CON report bundle has not yet been exercised in the review application. |

First compare two declared software selections using the same CON inputs.
Then test upstream and Lite operations on that same valid CON stream if the question is specifically upstream preservation.
Comparing a German site with a CON site would combine intentional data and presentation differences with software effects.
Before extending the stack, define those two operands and expose the smallest authored-input selection the existing operations need.
No diff-stack implementation was changed for this preparation.
