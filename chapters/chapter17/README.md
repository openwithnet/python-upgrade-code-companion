# Chapter 17.11 재구성 검증 후보

이 코드는 기존 최종 릴리스 원본이 아니라, 현재 확보된 17.7 기준 실행 코드와 17.11 Word 요구사항에서 새로 재구성한 **검토 후보**입니다.

```bash
python -m pip install -e '.[test]'
python -m oscillator_lab
python -m pytest -q
```

주요 계약: `solve(model, initial_state, dt, steps)` → `Trajectory(times, states)`; `steps=0`이면 초기 상태만 반환합니다. SciPy RK45는 내부적으로 적응형 시간 간격을 사용하나 반환은 `t_eval` 평가 시점입니다. `energy(model, state)`는 E=1/2*k*x²+1/2*m*v²를 사용합니다.
