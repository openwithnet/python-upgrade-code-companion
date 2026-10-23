# Chapter 14 — Code Companion Guide (v52, 검토 후보)

이 패키지는 Chapter 14의 실제 Word 원고를 참고하여 재구성한 **대표 실행 예제**다. 원고의 전체 코드 추출본이 아니다.

| 원고 | 소스 | 역할과 검증 |
|---|---|---|
| 14.2 | `ch14_examples.py: dna_operations` | Seq의 전사·번역·역상보 검사 |
| 14.3.3 | `ch14_advanced.py: compare_estimators` | LinearRegression·Ridge를 동일한 fit/predict 방식으로 교체, 예상값 13과 12.621622 |
| 14.4 | `build_pipeline`, `pipeline_without_leakage` | StandardScaler + Ridge, 학습 데이터에 대해서만 scaler.fit 실행 |
| 14.5.2 | `MeanRegressor`, `fit_and_predict`, `FitPredictProtocol` | Duck Typing 실행 및 Protocol 정적 타입 표기. Protocol 타입 검사는 실행 시 자동 보장되지 않음 |
| 14.6 | `run_sequence_analysis` | 인공 DNA 12개 → SeqRecord → 길이·GC 비율 → GC 백분율 → 인공 목표값 → 앞 9개 학습·뒤 3개 평가 |

## 핵심 해석

- **교체 가능성**: fit/predict 호출 인터페이스가 동일해도 계산 결과와 모델 가정은 다르다.
- **데이터 누수**: StandardScaler는 훈련 데이터에 대해서만 통계량을 학습해야 한다. `Pipeline.fit(X_train, y_train)` 이후 `predict(X_test)`를 호출한다.
- **GC 단위 주의**: 기초 `sequence_features()`는 GC **비율 [0,1]**을 반환한다. 원고 14.6.2의 목표값 생성식은 GC **백분율 [0,100]**을 사용하므로, 14.6 통합 실행에서는 100을 곱한다. 이 단위 변환은 필수다.
- **합성 예제**: 목표값은 입력 특성으로 인공 생성했으므로, 좋은 오차 수치는 실제 생물학적 예측력을 입증하지 않는다.
- **평가 범위**: 12개의 인공 서열, 고정 9/3 분할은 인터페이스 설명용이며 통계적 일반화 검증이 아니다.

## 코드 분류

- **실행 코드**: `src/` 모듈과 `tests/`의 테스트 대상 함수.
- **부분 코드**: Word 원고 내 `SomeEstimator(...)`, `model.fit(X,y)` 등의 인터페이스 단편.
- **설명식·의사코드**: 알고리즘 계약 설명에 쓰이는 일반 표현.
- **예상 출력**: 실제 검증 결과와 별도로 적힌 수치 예시.

## 미해결 사항

1. Word 원고의 전체 코드 블록별 1:1 추적·전수 검사 미완료.
2. 실제 MS Word 내 코드 스타일 및 복사·붙여넣기 실험 미완료.
3. Windows/Anaconda 환경 재현 검증 미완료.
4. GitHub 공개/릴리스 전 환경 고정 및 전체 배포 테스트 미완료.
