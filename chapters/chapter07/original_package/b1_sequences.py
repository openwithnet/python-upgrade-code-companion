from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class SequenceData:
    value: str
    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError('sequence must be a string')
        val = self.value.upper()
        if not val:
            raise ValueError('sequence must not be empty')
        object.__setattr__(self, 'value', val)
    def __len__(self) -> int:
        return len(self.value)

@dataclass(frozen=True)
class AlphabetPolicy:
    name: str
    symbols: frozenset[str]
    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError('policy name must not be empty')
        if not isinstance(self.symbols, frozenset) or not self.symbols:
            raise ValueError('symbols must be a nonempty frozenset')
        if any(not isinstance(x,str) or len(x) != 1 or x != x.upper() for x in self.symbols):
            raise ValueError('symbols must be uppercase single characters')
    def validate(self, data: SequenceData) -> None:
        if not isinstance(data, SequenceData):
            raise TypeError('data must be SequenceData')
        invalid = set(data.value) - self.symbols
        if invalid:
            raise ValueError(f'invalid {self.name} symbols: {sorted(invalid)}')

DNA_POLICY = AlphabetPolicy('DNA', frozenset('ACGT'))
RNA_POLICY = AlphabetPolicy('RNA', frozenset('ACGU'))
PROTEIN_POLICY = AlphabetPolicy('Protein', frozenset('ACDEFGHIKLMNPQRSTVWY'))

class HasSequence(Protocol):
    @property
    def sequence(self) -> str: ...
    def length(self) -> int: ...

class _SequenceBase:
    _POLICY: AlphabetPolicy
    def __init__(self, sequence: str):
        data = SequenceData(sequence)
        self._POLICY.validate(data)
        self._data = data
    @property
    def sequence(self) -> str:
        return self._data.value
    def length(self) -> int:
        return len(self._data)
    def count_symbol(self, symbol: str) -> int:
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError('symbol must be a single character')
        s = symbol.upper()
        if s not in self._POLICY.symbols:
            raise ValueError('symbol is not in alphabet')
        return self.sequence.count(s)

def calculate_gc_fraction(sequence: str) -> float:
    """Compute GC fraction of a prevalidated uppercase DNA/RNA sequence."""
    if not isinstance(sequence, str):
        raise TypeError("sequence must be a string")
    if not sequence:
        raise ValueError("sequence must not be empty")
    return (sequence.count("G") + sequence.count("C")) / len(sequence)

class DNASequence(_SequenceBase):
    _POLICY = DNA_POLICY
    def gc_fraction(self) -> float:
        return calculate_gc_fraction(self.sequence)

class RNASequence(_SequenceBase):
    _POLICY = RNA_POLICY
    def gc_fraction(self) -> float:
        return calculate_gc_fraction(self.sequence)

class ProteinSequence(_SequenceBase):
    _POLICY = PROTEIN_POLICY
    def residue_fraction(self, symbol: str) -> float:
        return self.count_symbol(symbol) / self.length()

def describe_sequence(obj: HasSequence) -> str:
    return f'{type(obj).__name__}: length={obj.length()}, sequence={obj.sequence}'

# This educational base class shares implementation; it is not a biological taxonomy.
# Sequence classes compose SequenceData and delegate validation to AlphabetPolicy.

if __name__ == '__main__':
    items = [DNASequence('atgcgc'), RNASequence('augcgc'), ProteinSequence('mkwvtf')]
    for item in items:
        print(describe_sequence(item))
    print('DNA GC:', f'{items[0].gc_fraction():.4f}')
    print('RNA GC:', f'{items[1].gc_fraction():.4f}')
    print('Protein W:', f'{items[2].residue_fraction("W"):.4f}')
