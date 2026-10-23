# Chapter 13 — Code Companion v50 (검토 후보)

## 검증된 범위
- **13.3**: `least_squares`의 `success`, `status`, `nfev`, 허용오차, 함수평가 제한으로 종료하는 실패 사례. `ftol`은 실제 추정 오차의 상한이 아니다.
- **13.6**: pandas Series는 레이블을 기준으로 자동 정렬하며, 맞지 않는 레이블은 결측값을 생성한다. SciPy/NumPy로 변환하기 전에 `reindex`로 대응시켜야 한다. 결측·중복 식별자는 예제 함수에서 거부한다.
- **13.8**: 원고의 `fit_reaction` 및 `run_analysis` 흐름에 맞춰 입력 CSV → 정렬·검증 → `curve_fit` → 잔차·SSE·RMSE → 결과 CSV 및 SHA-256/환경 JSON 기록을 구현했다.

## 코드 성격
- `src/ch13_examples.py`: v49에서 이어받은 **재구성된 대표 실행 예제**.
- `src/ch13_extended.py`: 원고 13.3/13.6/13.8의 의도와 주요 필드를 대조해 새로 조립한 **검증 후보**, 원본 파일을 그대로 복원한 것이 아니다.
- `tests/`: 독립 실행을 보장하기 위한 자동 테스트. 전체 원고 코드의 전수 검증은 아니다.

## 실행
`python -m pip install -r requirements.txt` 후 `PYTHONPATH=src python -m pytest -q tests` (Windows PowerShell: `$env:PYTHONPATH="src"; python -m pytest -q tests`).

## 해석 및 제한
최적화 성공과 과학적 타당성은 다르며, 메타데이터의 작성 시각은 재실행 때 달라진다. 해시값은 파일 바이트의 동일성을 검증하지만 실험 자체의 과학적 재현성을 보장하지 않는다. Windows/Anaconda 및 교재의 모든 실행 블록에 대한 전수 검증은 아직 하지 않았다.
