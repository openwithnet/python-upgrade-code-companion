# CODE_COMPANION_ROLE: REFERENCE
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 16: executable contract, review and reproducibility teaching examples.

Educational demonstration; not a security sandbox or a scientific validation stamp.
"""
from __future__ import annotations

import hashlib
import json
import platform
from pathlib import Path
import numpy as np
from ch16_validated_decay import validated_decay


def inspect_python_source(source: str) -> dict:
    """Syntax and top-level definitions only: no execution or semantic assurance."""
    import ast
    if not isinstance(source, str):
        raise TypeError("source must be text")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return {"syntax_ok": False, "error_line": exc.lineno, "definitions": []}
    names = [node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    return {"syntax_ok": True, "error_line": None, "definitions": names}


def evaluate_decay_case(times, c0, k, *, rtol=1e-12, atol=1e-12):
    """Compare validated computation against an independent scalar reference."""
    observed = validated_decay(times, c0, k)
    values = np.asarray(times, dtype=float)
    reference = np.asarray([float(c0) * np.exp(-float(k) * float(t)) for t in values.reshape(-1)])
    reference = reference.reshape(values.shape)
    np.testing.assert_allclose(observed, reference, rtol=rtol, atol=atol)
    return {"shape": list(np.shape(observed)), "max_abs_error": float(np.max(np.abs(np.asarray(observed) - reference))) if reference.size else 0.0}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def save_reproducibility_record(output_path, source_path, *, parameter_notes=None):
    """Record input hash and runtime; never claim environment fully captured."""
    import sys
    path = Path(output_path)
    source = Path(source_path)
    record = {"source_file": source.name, "source_sha256": sha256_file(source),
              "python": sys.version.split()[0], "numpy": np.__version__,
              "platform": platform.system(), "parameter_notes": parameter_notes or {}}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return record
