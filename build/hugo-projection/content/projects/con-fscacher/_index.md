---


title: "con/fscacher"
params:
  graphRootNodePID: xyzrins:projects/con-fscacher
  conContribution: false
  parentProjects:

  - xyzrins:.

---

con/fscacher is a Python library providing a persistent, file-content-aware memoization cache. Functions decorated with @cache.memoize_path are re-executed only when the fingerprint (timestamps + size) of their file arguments changes — making it easy to cache expensive operations on large file trees without stale results. It is used internally by the DANDI client and other CON tools.

## Part of
- [Center for Open Neuroscience](/.)



