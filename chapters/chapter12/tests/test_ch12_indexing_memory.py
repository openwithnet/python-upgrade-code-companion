import numpy as np
from ch12_indexing_memory_examples import *

def test_boolean():
 mask,sel,between,outside=boolean_indexing()
 assert mask.tolist()==[False,True,False,True,True]
 np.testing.assert_allclose(sel,[3.5,5.1,4.2]);np.testing.assert_allclose(between,[3.5,2.8,4.2]);np.testing.assert_allclose(outside,[1.2,5.1])

def test_advanced():
 x,share1,share2=advanced_indexing();assert x.tolist()==[20,50];assert share1 and not share2

def test_reshape():
 assert reshape_transpose()==((3,4),(3,4),(2,6),(3,2))

def test_view_copy():
 a,raw,work=view_copy();assert a.tolist()==[10,200,30,40,50];np.testing.assert_allclose(raw,[10,20,30,40]);np.testing.assert_allclose(work,[40,60])

def test_strides():
 assert strides()==((3,4),8,(32,8),6.)

def test_in_place():
 raw,bad_dtype=in_place_contract();np.testing.assert_allclose(raw,[10,40,60,40]);assert bad_dtype

def test_advanced_repeated_index():
 a=np.zeros(3,dtype=int); a[[0,0]]+=1; assert a[0]==1
 b=np.zeros(3,dtype=int);np.add.at(b,[0,0],1); assert b[0]==2

def test_reshape_not_axis_swap():
 a=np.arange(12).reshape(3,4)
 assert not np.array_equal(a.reshape(4,3),a.T)

def test_transpose_memory_view():
 a=np.arange(6).reshape(2,3); assert np.shares_memory(a,a.T)
