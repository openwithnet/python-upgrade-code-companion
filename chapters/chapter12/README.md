# Chapter 12 — NumPy 심화: 기준 코드 후보 (v47)

이 패키지는 12.1–12.9절의 **대표적인 학습용 실행 코드**를 이전 검토(v42–v44)에서 모은 것이다. 원고의 모든 코드 조각을 일대일 추출한 전체 재현본이 아니며, 과거 배포 소스의 원본 복원도 아니다. 12.10절은 장 요약으로 별도 실행 대상이 없다.

## 실행

Python 3.10 이상 권장. 가상환경에서:

```bash
python -m pip install -r requirements.txt
python -m pytest
```

## 구성 및 본문 연결

| 원고 절 | 소스 | 함수 | 검증 |
|---|---|---|---|
| 12.1.1 | ch12_canonical_examples.py | decay_vectorized | test_decay |
| 12.1.2 | ch12_canonical_examples.py | axis_means | test_axis_means |
| 12.3.1 | ch12_canonical_examples.py | broadcasting | test_broadcasting |
| 12.4 | ch12_indexing_memory_examples.py | boolean_indexing, advanced_indexing, reshape_transpose | tests 12.4–12.5 |
| 12.5 | ch12_indexing_memory_examples.py | view_copy, strides, in_place_contract | tests 12.4–12.5 |
| 12.6–12.7 | ch12_6_10_verified_examples.py | concentration 및 수치 정밀도 테스트 | tests 12.6–12.9 |
| 12.8 | ch12_6_10_verified_examples.py | expression_analysis | tests 12.6–12.9 |
| 12.9 | ch12_6_10_verified_examples.py | exact_positions, simulate_euler_motion | tests 12.6–12.9 |

## 분류
- **실행 가능한 기준 예제 후보:** `src/*.py`의 함수들; 해당 테스트가 포함됨.
- **부분 코드/설명용 표현:** Word 원고 내 함수 일부, ndarray 인터페이스 설명, 개념 예제; 이 패키지에 포함하지 않은 것들이 있음.
- **의사코드·수학식·출력:** 실행 소스로 취급하지 않음.

## 주의
- 수치 출력은 배열 자료형과 부동소수점 환경에 따라 마지막 자리가 달라질 수 있다.
- 유전자 발현 행렬은 교육용 가상 자료이다.
- `reshape()`와 축 교환, View와 Copy, 벡터화와 수치 적분 정확도는 서로 다른 개념이다.
- 최종 GitHub 릴리스/원고 코드 전수 정합성 검증은 아직 완료되지 않았다.


## v46 원고 대조 추가
- `ch12_additional_manuscript_examples.py`: 12.3.3 `apply_experiment_scales`, 12.6.2 `scale_in_chunks`를 Word 코드 문단에서 재조립; 연결 검증 포함.
- `MANUSCRIPT_COVERAGE.csv`: 12.1–12.10 절별 기준 코드와 누락·추가 확인 범위.
- 모든 Word 코드 전수 검증을 의미하지 않음.

## v47 추가: 미완료 영역의 실행 예제
- §12.2: `shape_axis_reduction` — ndim/shape/size와 axis 집계 (원고 직접 대응).
- §12.6.3: `simulate_euler` — 원고 코드의 시간 순차 의존성과 입력 계약을 보존한 실행본.
- §12.7: `floating_point_examples` — 큰 수의 덧셈과 뺄셈의 소거 현상 예제.
- §12.9.3: `positions_with_loop`, `positions_vectorized`, `compare_position_methods` — 같은 해석식을 이용한 비교. 시간 측정값은 PC·환경·실행 횟수에 의존하며 속도비를 보장하지 않음.
- 모듈 `src/ch12_remaining_examples.py`에 구현. `tests/test_ch12_remaining_examples.py`에서 검증.
- 이 패키지는 Chapter 12의 모든 부분 코드와 출력까지 전수 추출한 Code Companion이 아님.
