# G3 Chapter 10 — Word XML declaration census and gate boundary (2026-10-26)

Directly parsed `word/document.xml` in the local Word QA master `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` and sliced the top-level paragraphs for each of the **59** currently registered Chapter 10 logical units. Used the **corrected** range p3243–3306 for `simulate_euler`.

## New measured evidence
- **59/59** registered ranges could be read from the Word XML.
- **50/59** registered logical units contain at least one statement starting with `def`, `class`, `from ... import` or `import`.
- **117** such declaration/import paragraph lines across the 59 ranges. These are **statement lines, not 117 standalone programs or tests**.
- **12** paragraph lines start with `assert` or `with pytest.raises`. Not necessarily a complete test count.
- **0** paragraphs among these 59 spans reported a code/source label via the simple `w:pStyle` ID substring rule. Thus style-only extraction is demonstrably unreliable for this Word build; code must be recovered from paragraph content and contextual grouping.
- Selected editorial corrections reconfirmed directly in Word: `simulate_euler` has complete return, abbreviated `derivative`, externally dependent `run_model`, `UniversalProcessor` / `DerivativeModel(Protocol)`, and two Chapter 10.7 reused function snippets.

CSV trace: `G3_CH10_59_Word_XML_Declaration_Census_20261026.csv`. Local reproduction script: `audit_ch10_word_units.py`.

## Gate decision

**Chapter 10 is not awarded unconditional G3 PASS on this census alone.** The census proves the registered ranges contain concrete Python-style declarations and that purely style-based detection is inappropriate. It does not prove those declarations are independently executable, covers all other possible Word layouts, or establish full word-to-source verbatim equivalence. This is a stronger direct-Word audit that supports the prior **scope-accepted, final-HOLD** determination.

Next useful action: turn the 50 declaration-bearing units into executable/dependent/illustrative *block-level* extraction with explicit dependencies and expected outputs, and compare only real executable blocks to source. Do not repeatedly rerun already-green 31 tests without changes.

Existing source evidence: local 31/31 and Linux run 40263298708 SUCCESS on relevant code commit; separate G4/G5/G6 gates remain HOLD. No Word or Python source was modified in this census.
