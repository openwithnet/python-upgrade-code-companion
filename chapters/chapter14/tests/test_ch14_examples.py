# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import numpy as np
import pytest
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from ch14_examples import dna_operations, fit_linear_example, sequence_features, fit_sequence_pipeline

def test_dna_transcription():
    assert dna_operations()['rna']=='AUGAAAUUUUAA'

def test_dna_translation():
    assert dna_operations()['protein']=='MKF*'

def test_complements():
    d=dna_operations()
    assert d['reverse_complement']=='TTAAAATTTCAT'
    assert d['complement']=='TACTTTAAAATT'

def test_linear_fit():
    model,p=fit_linear_example()
    assert p==pytest.approx(13)
    assert model.coef_[0]==pytest.approx(2)

def test_sequence_features():
    r=SeqRecord(Seq('ATGC'),id='a')
    assert np.allclose(sequence_features(r),[4,.5])

def test_invalid_dna():
    with pytest.raises(ValueError):sequence_features(SeqRecord(Seq('ATN')))

def test_pipeline_prediction_shape():
    rs=[SeqRecord(Seq(s),id=str(i)) for i,s in enumerate(['ATAT','ATGC','GCGC','AAAC','GGGG'])]
    p,x=fit_sequence_pipeline(rs,np.array([1.,2.,3.,4.,5.]))
    assert p.predict(x).shape==(5,)

def test_pipeline_invalid_y():
    rs=[SeqRecord(Seq('ATGC'))]
    with pytest.raises(ValueError):fit_sequence_pipeline(rs,[1,2])
