# Chapter 10 원고·코드 정합성 검토 (2026-10-19)

## 판정
**본문 집필 완료 / 수집 가능한 코드 통합 실행 통과 / 출판용 원고 NOT FROZEN.**

현재 대화에서 집필한 10.1–10.7 본문을 기준으로 구조·용어를 점검했다. 10.1–10.7의 원문 전체가 독립적인 기계 판독 파일로 보관되어 있지는 않으므로 축자 대조, Word 수식 객체, 전체 원고 손실 여부는 검증하지 못했다. 따라서 이 보고서는 전체 Word 원고의 최종 교정본을 의미하지 않는다.

## 확정된 장 구조와 반영 상태
- 10.1 다중 패러다임 프로그래밍 — 본문 작성
- 10.2 함수와 객체의 협력 — 본문 작성
- 10.3 계산 구성 요소의 분리 — Canonical 주제로 재작성
- 10.4 Composition과 Dependency Injection — Canonical 주제로 재작성
- 10.5 실습: 반응속도 모델의 구조화 — 기준 구현 및 테스트 제공
- 10.6 좋은 설계와 지나친 추상화 — Canonical 주제로 재작성
- 10.7 Chapter Summary — 개정 장 구조 반영
- 3단계 세부 번호의 정확한 원본 대조는 미완료

## 코드 기준 및 역할
| 층위 | 파일 / 이름 | 목적 | 출판 관리 |
|---|---|---|---|
| 10.5 기준 실습 | `kinetics.py`: `RateLaw`, `FirstOrderRate`, `simulate_euler`, `Trajectory`, `exact_first_order` | 비음수 소모속도를 이용한 1차 반응 Euler 적분 | **CANONICAL SOURCE** |
| 10.3–10.4 교육용 독립 예시 | `ch10_composition_example.py`: `DerivativeModel`, `FirstOrderModel`, `EulerStep`, `MidpointStep`, `Simulation` | signed 변화율을 이용한 객체 합성 및 적분기 교체 | **EXPLANATORY / 별도 실행 가능, canonical kinetics 대체 아님** |
| 이전 장 연결 보충 | `ch10_pipeline.py`와 `c3_calibration.py`, `c3_validation.py` | C3 측정값·보정 모델 통합 사례 | **SUPPLEMENT / 10.5 중심 실습 아님** |

### 반드시 명시할 수학적 차이
- 10.3–10.4 `FirstOrderModel.derivative(c)`는 **부호가 포함된 변화율** `dc/dt = -k*c`를 반환한다.
- 10.5 `FirstOrderRate.rate(c)`는 **비음수 소모속도** `k*c`를 반환한다. `simulate_euler`가 `c_next = c - dt*rate(c)`를 계산한다.
- 둘은 1차 소모반응에서는 대수적으로 같지만, 메서드 이름과 계약은 다르다. **API를 서로 바꿔 끼울 수 없다.**
- `RateLaw`와 `DerivativeModel`을 유일한 공통 Protocol로 합치거나 이름만 바꾸지 않는다. 향후 통합하려면 부호·단위·유효영역을 설계하고 별도의 검증이 필요하다.

## 장별 원고 편집 조치
1. **10.1–10.2**: C3의 모델 교체 및 측정값 검증을 개념 도입 예시로 유지. 간소화 클래스는 canonical C3 구현이 아니라는 표시를 유지한다.
2. **10.3**: 일반 signed derivative `f(c)`와 일반 알고리즘을 설명하되, 입력 검증이 빠진 짧은 코드는 `개념 설명용/독립적 부분 코드`로 명시한다.
3. **10.4**: 위 독립 실행 예제 파일로 모델/solver/Simulation 협력을 재현한다. `FirstOrderModel`은 교육용 설명 API이며 10.5의 `FirstOrderRate`와 다르다고 명시한다.
4. **10.5**: 실습의 정규 단일 소스는 `kinetics.py`. 1차 비가역 반응, c>=0, k>=0, dt>0, 계산 중 음수 농도 거부, 단일 성분의 제한된 교육 모델임을 유지한다. `Trajectory`는 frozen이지만 객체 생성 자체에서 모든 시간·값·길이 계약을 검증하지는 않는다.
5. **10.6**: YAGNI·KISS/결합도·응집도·리팩터링 사례로 유지. 새로운 코드 조각을 실습 기준 소스로 혼동하지 않도록 서식과 설명을 구분한다.
6. **10.7**: 전체 장을 10.3–10.6 Canonical 제목에 맞춰 요약하며 C3가 아닌 반응속도 모델을 중심 사례로 둔다. C3는 선행 학습 연결 예시로만 보존한다.
7. **분량 관리**: 축약된 Word 파일로 대체하거나 이를 출판 마스터라고 주장하지 않는다. 원문 전체 확보 후 축자 대조·수식·표·코드가 원고에 보존되었는지 점검한다.

## 코드 실행 검증 (실행 환경: Python 3.13.5)
- 기존 C3 검증과 Chapter 9, C3 보충, 10.5 kinetics, 10.3–10.4 독립 교육용 사례의 총 **72개 pytest 사례 모두 통과**. 본 패키지의 `test_results.txt`에 기록.
- `kinetics.py`: 5초 Euler 0.327680 / 해석해 약 0.367879.
- `ch10_composition_example.py`: Euler 0.8 / Midpoint 0.82.
- `ch10_pipeline.py`: linear [0, 1, 4], quadratic [0, 1, 2].
- **Python 3.14.x에서 직접 실행하지 않았다.** `test` 통과는 과학적 모델의 실험 타당성 검증이 아니다.

## 수정 없이 유지할 제한사항
- `FirstOrderRate.rate()`는 비음수 소모속도로 정의되어 있으므로 생성항이나 일반적인 부호 변화율을 그대로 지원하지 않는다.
- `simulate_euler`는 일정 시간 간격의 명시적 Euler 및 단일 농도에 한정된다. 음수 농도가 나오면 ValueError를 발생시키며 결과를 임의로 0으로 보정하지 않는다.
- 10.3–10.4 독립 설명용 예제는 수치 모델·알고리즘 교체를 보여주지만 실험 데이터 검증 및 완전한 물리적 계약을 구현하는 production solver가 아니다.

## 다음 출판 게이트
- [ ] 10.1–10.7 전체의 원문을 손실 없이 편집 가능한 파일로 확보
- [ ] 3단계 Canonical 상세 목차 축자 대조
- [ ] 10.3, 10.4 중복 부분의 편집 정리 및 모든 코드의 실행/부분/의사코드 상태 표시
- [ ] Word OMML 수식 및 표·코드 서식 검수
- [x] 기준 코드와 교육용 예시의 역할 분리
- [x] 확보된 코드 통합 회귀 테스트 72개 통과

**최종 상태: Chapter 10 NOT FROZEN**
