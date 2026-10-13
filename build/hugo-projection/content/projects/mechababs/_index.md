---


title: "mechababs"
params:
  graphRootNodePID: xyzrins:projects/mechababs
  conContribution: false
  parentProjects:

  - xyzrins:.

---

mechababs runs BIDS Apps over many studies on an HPC cluster, with BABS running the jobs. It works on a BIDS study, adding derivatives to it, and records how each one was made inside the study itself: the exact mechababs and BABS versions pinned in a lock, and every orchestration step as a DataLad run record. A superstudy groups many studies so one campaign sweeps them all, which is how mechababs feeds OpenNeuroStudies.

## Part of
- [Center for Open Neuroscience](/.)



