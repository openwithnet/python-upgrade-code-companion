# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import json
import numpy as np
import pytest
from ch16_review_workflow import inspect_python_source, evaluate_decay_case, save_reproducibility_record, sha256_file


def test_syntax_good():
    assert inspect_python_source('def f(x):\n    return x+1\n')['definitions'] == ['f']

def test_syntax_failure_not_executed():
    result=inspect_python_source('def f(: pass')
    assert not result['syntax_ok'] and result['error_line']==1

def test_no_semantic_certification():
    assert inspect_python_source('def incorrect(t): return -123')['syntax_ok']

def test_wrong_type():
    with pytest.raises(TypeError): inspect_python_source(None)

@pytest.mark.parametrize('times', [[0., 1., 2.], np.array([0.5, 1.5]), np.array([]), 2.])
def test_scientific_reference(times):
    assert evaluate_decay_case(times, 2., .25)['max_abs_error'] < 1e-12

@pytest.mark.parametrize('times', [[True, 0.], ['0.0', 1.], [-1., 0.]])
def test_invalid_times(times):
    with pytest.raises(ValueError): evaluate_decay_case(times, 2., .25)

def test_hash_and_record(tmp_path):
    source=tmp_path/'input.csv'; source.write_text('x,y\n1,2\n', encoding='utf-8')
    record=save_reproducibility_record(tmp_path/'metadata.json',source,parameter_notes={'k': .25})
    assert record['source_sha256']==sha256_file(source)
    assert json.loads((tmp_path/'metadata.json').read_text())['parameter_notes']['k']==.25

def test_hash_detects_change(tmp_path):
    f=tmp_path/'x.txt';f.write_text('a');a=sha256_file(f);f.write_text('b');assert sha256_file(f)!=a
