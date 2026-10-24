# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""B1 DNA sequence analysis: Chapter 4 canonical function-first example.

Python >= 3.13, standard library only. This is an educational, A/C/G/T-only model.
"""

from typing import TypedDict


class DNAResult(TypedDict):
    sequence_id: str
    length: int
    gc_fraction: float


def validate_dna(sequence: str) -> str:
    """Return normalized uppercase DNA; accept nonempty A/C/G/T strings only.

    Raises TypeError for a non-string, ValueError for an empty or invalid string.
    IUPAC ambiguity symbols, FASTA headers, and whitespace are unsupported.
    This checks character syntax, not biological provenance or quality.
    """
    if not isinstance(sequence, str):
        raise TypeError("sequence must be a string")
    normalized = sequence.upper()
    if not normalized:
        raise ValueError("sequence must not be empty")
    if any(base not in "ACGT" for base in normalized):
        raise ValueError("invalid DNA sequence")
    return normalized


def _gc_fraction_from_validated(sequence: str) -> float:
    """Compute GC fraction; PRECONDITION: nonempty uppercase A/C/G/T string."""
    return (sequence.count("G") + sequence.count("C")) / len(sequence)


def calculate_gc_fraction(sequence: str) -> float:
    """Compute a GC fraction in [0, 1] after validating the input."""
    normalized = validate_dna(sequence)
    return _gc_fraction_from_validated(normalized)


def summarize_dna(sequence_id: str, sequence: str) -> DNAResult:
    """Return identifier, length, and GC fraction for one DNA sequence."""
    if not isinstance(sequence_id, str):
        raise TypeError("sequence_id must be a string")
    if not sequence_id:
        raise ValueError("sequence_id must not be empty")
    normalized = validate_dna(sequence)
    return {"sequence_id": sequence_id,
            "length": len(normalized),
            "gc_fraction": _gc_fraction_from_validated(normalized)}


def analyze_sequences(sequences: dict[str, str]) -> list[DNAResult]:
    """Analyze all sequences in insertion order; fail fast on invalid input."""
    if not isinstance(sequences, dict):
        raise TypeError("sequences must be a dictionary")
    results: list[DNAResult] = []
    for sequence_id, sequence in sequences.items():
        results.append(summarize_dna(sequence_id, sequence))
    return results


def main() -> None:
    sequences = {"sample_A": "ATGCGC", "sample_B": "ATATAT",
                 "sample_C": "GGCC", "sample_D": "atgc"}
    results = analyze_sequences(sequences)
    print("ID         Length   GC fraction")
    for result in results:
        print(f"{result['sequence_id']:<10}"
              f"{result['length']:>6}"
              f"{result['gc_fraction']:>14.4f}")


if __name__ == "__main__":
    main()
