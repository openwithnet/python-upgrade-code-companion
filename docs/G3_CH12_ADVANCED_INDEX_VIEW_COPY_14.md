# Chapter 12 — 14 advanced-indexing and View/Copy checks

Date: 2026-10-26. Word v37 QA manuscript.

Fourteen reconstructed examples were executed with NumPy as required setup. All returned exit code zero, and all fourteen outputs matched the Word expected outputs after whitespace-only normalization.

Topics: Boolean selection versus assignment; integer selection; Basic vs Advanced Indexing memory sharing; paired indexing and np.ix_; repeated indices with += versus np.add.at; transpose memory sharing; View mutation versus Copy isolation; ndarray.base; in-place normalization.

Word paragraphs inspected span 5972–6449. Detailed individual paragraph mappings and outputs are stored in QA file G3_Ch12_AdvancedIndex_ViewCopy_14_Examples_20261026.csv.

Cumulative reviewed Chapter 12 examples: 63 scoped cases (61 successful ordinary runs, 59 with matching stated Word stdout and two with no stated output, plus two expected-error cases). This is not full-Chapter coverage. No Word or Python source edits; G3/G4/G5/G6 remain HOLD.