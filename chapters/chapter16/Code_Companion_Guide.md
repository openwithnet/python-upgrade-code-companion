# Chapter 16 — Code Companion 검토본 v56

이 패키지는 『과학자를 위한 Python 업그레이드』 Chapter 16의 **대표 실행 코드**이며, 원고 내 모든 코드 문단의 전수 복원이 아니다.

## 원고와 코드의 대응

| 구간 | 교육적 역할 | 이번 파일 | 검증 상태 |
|---|---|---|---|
| 16.1 AI 보조 프로그래밍 | 책임과 검토 원칙 설명 | Guide | 개념 설명, 독립 코드 없음 |
| 16.2 문제 정의와 명세 | 입력/출력 계약 명확화 | `ch16_validated_decay.py` | 대표 계약에 대한 자동 테스트 |
| 16.3 구조 검토 | 함수·클래스 경계, 문법 점검 | `inspect_python_source()` | 구문과 최상위 정의만 검사; 의미/안전성 보증 불가 |
| 16.4 테스트와 검증 | 정상·경계·오류 입력과 기준 계산 비교 | `evaluate_decay_case()` | 수치 참고값·예외 테스트 |
| 16.5 결함 개선 | 불리언 입력이 잘못 허용되는 실패 사례 및 수정 | `ch16_initial_bug.py`, `ch16_validated_decay.py` | 결함 재현 및 회귀 검증 |
| 16.6 과학적 책임과 재현성 | 입력 기록, 해시, 실행 환경 메타데이터 | `sha256_file()`, `save_reproducibility_record()` | 파일 기록 테스트; 완전한 실험 재현성 보장은 아님 |
| 16.7 요약 | 학습 정리 | Guide | 별도 실행 대상 아님 |

## 실행

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m pytest -q tests
```

Windows PowerShell:

```powershell
$env:PYTHONPATH = 'src'
python -m pytest -q tests
```

## 독자가 확인할 핵심 사항

1. **문법 검사와 과학적 검증은 별개**: AST 파싱에 성공해도 식이 틀릴 수 있다.
2. **계약은 형변환 전에 검사**: `[True, 0]`을 숫자로 바꾼 뒤 검사하면 오류를 놓칠 수 있다.
3. **참고 계산은 독립적으로 구현**: 예제의 지수감쇠 해석식과 결과를 허용오차 내에서 비교한다.
4. **파일 해시는 무결성 힌트**: SHA-256만으로 출처, 연구 설계나 분석의 타당성이 증명되지는 않는다.
5. **테스트 수량의 범위**: 이번 43개는 기존 30개 및 새 13개이며 원고 전수 검증을 뜻하지 않는다.

## 남은 QA

- Word 원고 전체에 등장하는 예제별 독립 실행·부분 코드·의사코드 전수 분류
- Windows/Anaconda 환경에서의 실행 재현
- 원고와 실제 GitHub 배포판의 버전·환경 매니페스트 확정
