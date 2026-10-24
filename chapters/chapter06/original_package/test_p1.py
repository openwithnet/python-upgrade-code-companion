# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import math
import pytest
from dataclasses import FrozenInstanceError
from p1_particle_trajectory import ParticleState,euler_step,Particle,Trajectory,simulate_particle

def test_state():
 s=ParticleState(1,2);assert s.position==1.0 and s.velocity==2.0
 with pytest.raises(FrozenInstanceError):s.position=3
@pytest.mark.parametrize('bad',[True,'1',float('nan'),float('inf')])
def test_bad_state(bad):
 with pytest.raises((TypeError,ValueError)):ParticleState(bad,0)
def test_euler():
 s=ParticleState(0,1);assert euler_step(s,2,.5)==ParticleState(.5,2);assert s==ParticleState(0,1)
def test_predict_advance():
 p=Particle(ParticleState(0,1));next_s=p.predict(2,.5);assert p.state==ParticleState(0,1);p.advance(2,.5);assert p.state==next_s
@pytest.mark.parametrize('dt',[0,-1,float('nan')])
def test_bad_dt(dt):
 with pytest.raises(ValueError):euler_step(ParticleState(0,0),2,dt)
def test_atomic_failed_advance():
 p=Particle(ParticleState(1e308,1e308)); before=p.state
 with pytest.raises(ValueError):p.advance(1,2)
 assert p.state is before
@pytest.mark.parametrize('steps',[-1,1.5,True])
def test_bad_steps(steps):
 with pytest.raises((ValueError,TypeError)):simulate_particle(ParticleState(0,0),2,.5,steps)
def test_trajectory():
 t=Trajectory(); s=ParticleState(0,0);t.append(0,s)
 with pytest.raises(ValueError):t.append(0,s)
 with pytest.raises(ValueError):t.append(-1,s)
 assert len(t)==1 and len(t.records)==1

def test_result():
 s=ParticleState(0,0);t=simulate_particle(s,2,.5,4);assert len(t)==5
 assert [r.state.position for r in t.records]==[0,0,.5,1.5,3.]
 assert [r.state.velocity for r in t.records]==[0,1,2,3,4]
 assert math.isclose(t.records[-1].time,2.)
 assert s==ParticleState(0,0)
