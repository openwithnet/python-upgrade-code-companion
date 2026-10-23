# Chapter 15 Code Companion — v54 추가 검토

대상: 15.2 Tensor/계산 그래프, 15.3 JAX `grad`/`jit`, 15.4 미분법 비교, 15.6 세 라이브러리 비교.
기존 15.5의 `ch15_sensitivity.py`와 7개 테스트는 보존하였다.

| 원고 | 대응 코드 | 분류 | 검증 | 유의점 |
|---|---|---|---|---|
| 15.2.1 | `torch_tensor_numpy_copy()` | 대표 실행 코드 재구성 | 통과 | `torch.from_numpy`는 메모리 공유, `torch.tensor`는 복사 |
| 15.2.2–15.2.3 | `torch_backward_example()` | 대표 실행 코드 재구성 | 통과 | `.grad` 누적과 그래프 재사용은 다른 문제. 역전파 때 매번 새 계산 그래프 구성 |
| 15.3.1–15.3.3 | `jax_array_update()`, `jax_functional_grad()` | 대표 실행 코드 재구성 | 통과 | `.at[]`은 갱신된 새 배열을 반환; `jit` 수학 결과 비교 |
| 15.4.1–15.4.3 | `derivative_comparison()` | 대표 실행 코드 재구성 | 통과 | 유한차분은 근사이며 h의 크기에 따라 오차 변동; 절댓값 미분 불능 지점 별도 설명 필요 |
| 15.5 | `ch15_sensitivity.py` | 기존 v53 대표 실행 코드 | 통과 | Jacobian의 두 열 순서와 단위 |
| 15.6.1–15.6.3 | `three_library_decay()` | 대표 실행 코드 재구성 | 통과 | JAX float32와 NumPy/PyTorch float64 차이로 허용오차 필요 |

실행: `PYTHONPATH=src pytest -q tests`.
이 파일은 원고 전체 코드를 그대로 추출한 것이 아니며 원고의 대표 개념과 대조해 작성한 독립 검증 코드이다. Windows/Anaconda 및 사용자 환경은 아직 별도 검증하지 않았다. 원고의 본문 및 Word 구조는 변경하지 않았다.
