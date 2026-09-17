# CON website history rewrite plan

This is a proposed follow-up to the submodule conversion, not an executed rewrite.
The adoption pull request preserves the published history.
Its `site-specific` gitlink selects the same input tree that the website previously stored as a subtree.

## Intended result

Keep website code and configuration history in `con/dev-centerforopenneuroscience.org`.
Keep site-input history in `ORINOCO-Lite/con-site-specific`.
Remove historical embedded site-input trees and the imported subtree ancestry from the website's retained branches.
Preserve the current website tree, including its submodule gitlink, exactly.

Removing only the historical `site-specific/` paths is insufficient: unsquashed subtree imports also brought the metadata repository's earlier commits into website ancestry.
A disposable rewrite must remove those import-parent relationships as well, while preserving genuine website changes and merges.
Do not filter or rewrite the metadata repository.

## Rehearse after adoption

1. Resolve open website pull requests before the rewrite window.
   PR #6 has content changes that overlap metadata PR #3; preserve and review those changes in the metadata repository.
   Review whether this adoption supersedes scaffold PR #8 and subtree-export PR #4; do not discard their changes by assumption.
2. Fetch current website branches and tags into a disposable mirror and make an offline Git bundle backup.
   Verify the backup and record the exact remote ref values for rollback and lease checks.
   Keep the backup outside the published repository.
3. Identify the subtree import and synchronization commits from Git history.
   Rehearse a `git-filter-repo` rewrite that removes historical embedded site-input files, disconnects imported metadata-only ancestry, and prunes empty commits.
   Retain the new `site-specific` gitlink and legitimate website-only changes.
   Review the resulting graph rather than treating a path filter alone as sufficient.
4. Compare the rewritten tip's complete tree with the accepted pre-rewrite tip.
   They must be identical.
   Verify the selected metadata commit remains fetchable, then clone the rewritten repository with submodules and run the locked build and site verification.
5. Review the actual commit mapping and affected branches and tags before scheduling the remote change.
   Do not publish old-history backup branches to the same repository, since that would retain the ancestry being removed.

## Publish in a coordinated window

Pause repository writes and coordinate branch-protection changes only if required.
Recheck the remote refs against the recorded values, then update each approved ref with an explicit lease.
Reopen or recreate surviving pull requests against the rewritten history; existing commit links and approvals may no longer apply.
Restore protections and verify GitHub Actions, Pages, submodule cloning, and the website's final tree.
Ask collaborators to clone afresh instead of merging old branches back into the rewritten graph.

GitHub pull-request refs and caches can retain old objects after a branch rewrite.
Do not promise immediate storage reclamation or removal of old public commit URLs.
If that becomes a separate requirement, resolve it with GitHub after the branch migration.

If verification fails, restore the recorded refs from the verified offline backup with leases against the rewritten tips.
No force-push or protection change is authorized by this planning document alone.
