# Chapter 16 — AI 생성 코드 검토와 과학적 검증

## 실행할 코드
- `src/ch16_validated_decay.py`: **정상 구현**, `validated_decay` 사용.
- `src/ch16_review_workflow.py`: 원고 학습 목표를 확장한 **Code Companion 추가 구현**.

## 교육용 결함 재현 — 연구 계산에 사용 금지
- `src/ch16_initial_bug.py`: 원고 §16.5.1의 `initial_decay`를 재현하고, 별도의 `buggy_numeric_array` 예시도 제공한다. **의도적으로 금지된 입력을 받아들이는 코드**이므로 연구·생산용으로 사용하지 않는다.
- Word §16.4.2에서 `validate_times()`를 대상으로 한 검사가 주석 처리된 것은 중간 구현의 결함을 설명하기 위한 것이다. 합격 테스트로 간주하지 않는다.

## 재현 시험
`python -m pytest -q --import-mode=importlib chapters/chapter16/tests` (장별 `src`가 PYTHONPATH에 포함된 환경).

## 출처와 한계
Word v37 §16.5.1–16.5.3과의 집중 대조를 수행했다. 이는 Chapter 16 전체의 모든 코드·설명·출력을 전수 확인했다는 뜻은 아니다.
