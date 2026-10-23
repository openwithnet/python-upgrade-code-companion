# Chapter 12 — NumPy 심화: Code Companion Guide (검토본 v48)

**성격:** v47 검증 소스의 사용·해석 안내서. 이 파일은 Word 원고 전체 코드의 완전한 전사본이 아니다. 기존 함수와 테스트를 변경하지 않은 문서화 단계이다.

## 1. 이 안내서와 교재의 관계

교재는 개념, 코드 조각, 출력, 수학식, 설명을 순서대로 학습하도록 작성되어 있다. `src/*.py`는 그중 **대표적인 계산을 독립 실행 가능하도록 재구성한 학습용 예제**이다. Word 코드와 글자 단위 동일성을 보장하지 않는다. `tests/*.py`는 재구성된 함수의 동작 계약을 검증한다. 코드에 없는 원고의 부분 예제는 누락이나 결함으로 바로 판단하지 말고 별도로 대조해야 한다.

코드 표시 기준: **[E] 실행용 기준 후보** = 현재 소스 파일에 정의되고 해당 테스트가 있는 함수, **[P] 부분 코드** = 원고에서 전후 문맥 없이 독립 실행할 수 없는 발췌, **[X] 의사코드/수식** = 학습 설명이며 실행 대상으로 취급하지 않는 표현, **[O] 출력** = 코드가 아니라 관찰/기대 결과이다. 이 분류는 원고 모든 문단의 개별 최종 판정이 아니라 배포용 파일의 상태를 설명한다.

## 2. 환경과 실행

`requirements.txt`: `numpy>=1.24,<3`, `pytest>=7,<10`. README의 Python 3.10 이상 권고는 광범위 호환성 **검증 증거가 아니다**. 패키지 루트에서 다음을 실행한다.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

결과는 실행 환경에 따라 달라질 수 있다. 부동소수점 값은 허용오차로 비교하고, 성능 측정 시간은 정답으로 고정하지 않는다.

## 3. 절별 기준 코드 및 학습 안내

| 절 | [E] 소스: 함수 | 먼저 확인할 개념 | 확인해야 할 실행 결과·검증 | 미완료 범위 |
|---|---|---|---|---|
| 12.1 | `ch12_canonical_examples.py`: `decay_vectorized`, `axis_means` | 해석적 지수감쇠의 배열 평가; `axis`와 축 제거 | 0~5 시간의 감쇠 배열, 시간별·실험별 평균 | 원고의 모든 배열 선언과 일대일 대응 아님 |
| 12.2 | `ch12_remaining_examples.py`: `shape_axis_reduction` | `ndim/shape/size`; `axis=0/1` | `(2,3)` 자료의 열·행 평균 | 전체 다차원 실습 미전수 |
| 12.3 | `ch12_canonical_examples.py`: `broadcasting`; `ch12_additional_manuscript_examples.py`: `apply_experiment_scales` | 오른쪽 정렬, 실험별 보정 계수의 축 확장 | `scales[:,None]`가 실험 수와 맞는지 검사 | Broadcasting 오류 사례 일부 미전수 |
| 12.4 | `ch12_indexing_memory_examples.py`: `boolean_indexing`, `advanced_indexing`, `reshape_transpose` | 마스크 추출과 원본 대입의 차이; 고급 인덱싱 복사; 형태변환 ≠ 축교환 | `np.shares_memory()` 및 배열 형태 검사 | 독립 코드/부분 코드 전체 구분 미완료 |
| 12.5 | 같은 파일: `view_copy`, `strides`, `in_place_contract` | View는 원본을 공유할 수 있음; Strides 단위는 바이트 | 수정 후 원본 배열, dtype 제약·오류 | 세부 사용 예제 미전수 |
| 12.6 | `ch12_6_10_verified_examples.py`: `concentration`; `ch12_additional_manuscript_examples.py`: `scale_in_chunks`; `ch12_remaining_examples.py`: `simulate_euler` | 벡터화 vs 구간별 처리 vs 시간 의존 순차 적분 | 구간 처리 결과 일치, Euler 단계 변화, 입력 경계 | 원고의 기타 코드 전체 미전수 |
| 12.7 | `ch12_remaining_examples.py`: `floating_point_examples` | 유한 정밀도, 소거, `float32/64` | `(1e16+1)-1e16`은 0으로 관찰될 수 있음 | 환경별 출력 표기 확인 필요 |
| 12.8 | `ch12_6_10_verified_examples.py`: `expression_analysis` | 행=시료, 열=유전자; 가상 데이터 그룹 분석 | 시료 합계, 유전자 평균, A/B 평균 | 통계적 차등발현 검증으로 해석하지 말 것 |
| 12.9 | `ch12_6_10_verified_examples.py`: `exact_positions`, `simulate_euler_motion`; `ch12_remaining_examples.py`: `positions_with_loop`, `positions_vectorized`, `compare_position_methods` | 해석해 평가와 수치적분은 별개; 공정한 성능 비교 | 결과 근접성·Euler 오차·실행시간의 실행환경 의존성 | 모든 성능 수치 재현 보장 없음 |
| 12.10 | 독립 실행 코드 없음 | 요약 및 개념 연결 | 실행 대상 아님 | 원고의 요약 코드 조각은 참고 표현 |

## 4. 핵심 예제 실행과 해석

### 4.1 배열 계산과 과학적 의미

`decay_vectorized()`는 `c(t)=c0 exp(-kt)` **해석식**을 시간 배열에 적용한다. 미분방정식을 Euler 등으로 적분하는 함수가 아니다. `axis_means()`에서 `axis=0`은 실험축을 제거하여 각 시간의 평균을 구하고, `axis=1`은 시간축을 제거하여 실험별 평균을 구한다. 실제 데이터의 행/열 정의가 바뀌면 해석도 바뀐다.

### 4.2 Broadcasting과 원본 데이터

`apply_experiment_scales(data, scales)`는 `data`의 첫 축 길이와 보정 계수 길이가 같을 때만 곱한다. `scales[:, None]`는 열 방향의 새 축을 만들어 실험별로 모든 측정값에 보정 계수를 적용한다. Boolean Indexing으로 선택한 복사본을 바꾸는 것과 `a[mask] = ...`로 원본을 바꾸는 것은 구별한다.

### 4.3 메모리와 수치 안정성

Slice는 View일 수 있지만 고급 인덱싱은 보통 복사본을 만든다. `reshape()`는 데이터 배치를 다시 표현하는 것으로 축의 과학적 의미를 자동 교환하지 않는다. `strides`는 원소 개수가 아닌 **바이트 단위 간격**이다. `floating_point_examples()`는 수치 소거가 존재함을 보여준다. 단순히 데이터형을 바꾼다고 모든 오차가 해결되지는 않는다.

### 4.4 계산 시간과 수치 정확도

`positions_with_loop()`와 `positions_vectorized()`는 같은 해석식을 비교한다. `compare_position_methods()`의 시간값은 플랫폼과 반복 횟수에 좌우된다. 한편 `simulate_euler()`와 `simulate_euler_motion()`은 앞 단계 결과를 다음 단계에 사용한다. 시간 간격을 변경한 수치 오차 개선과 벡터화에 의한 실행시간 개선을 혼동하지 않는다.

## 5. 실패 사례와 재검증 원칙

- `apply_experiment_scales()`에서 실험 수와 보정 계수 개수가 다르면 `ValueError`를 기대한다.
- `simulate_euler()`의 `steps`에는 불리언을 허용하지 않는다. `dt*k > 1` 조건은 이 **교육용 비음수 농도 모델**에서 제한한다.
- View 변경이 원본에 전파되는지 검사하고, 원본 보존이 목표라면 `.copy()`를 사용한다.
- 통계적 검정, 생물학적 해석, 외부 데이터의 유효성은 이 테스트 범위에 포함되지 않는다.

## 6. 증거 등급과 동결 조건

**확인 가능:** v48 시점에서 v47 코드를 재실행한 pytest 결과; `src/` 내 5개 모듈과 `tests/`의 대응 관계; 절별 대표 예제 커버리지. **확인하지 못함:** Word 원고의 모든 코드 문단을 1:1 추출·실행했는지, 원본 저장소와 같은 파일인지, Windows/Anaconda에서의 독립 테스트, GitHub 릴리스 검증. 따라서 상태는 **CODE COMPANION DRAFT / NOT FROZEN**이다.

최종 동결에는 각 원고 예제의 ID, 전체 원고 대응표, [E]/[P]/[X]/[O] 개별 판정, 환경 잠금 및 다중 OS 실행, 원고 출력 정합성, README와 실습 순서의 최종 교차검증이 필요하다.
