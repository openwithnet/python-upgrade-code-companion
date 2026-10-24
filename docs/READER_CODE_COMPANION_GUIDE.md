# 독자용 Code Companion 안내 — Chapter 1–17

**상태: 배포 후보 / NOT FROZEN.** 이 문서는 Word 통합 원고 v37과 통합 저장소 v75를 잇는 **장별 대표 파일 안내**입니다. Word의 모든 코드 블록과 1:1 대조했다는 뜻이 아닙니다.

| 장 | 우선 읽을 Python 파일 | 역할 |
|---|---|---|
| 01 | `chapters/chapter01/sections/section_1_1_1.py` | 절별 실행 예제; 1.1–1.5 절 코드 15개는 sections/ 전체 참조 |
| 02 | `chapters/chapter02/original_package/ch02_examples.py` | 절차·함수·객체 예제의 순차 실행 |
| 03 | `chapters/chapter03/original_package/P1_particle_motion.py` | 입자 운동과 Euler 수치 적분 |
| 04 | `chapters/chapter04/original_package/b1_dna_analysis.py` | DNA 문자열 분석 |
| 05 | `chapters/chapter05/original_package/python_upgrade_ch05/c2_kinetics_pipeline.py` | 반응속도 계산 파이프라인 |
| 06 | `chapters/chapter06/original_package/p1_particle_trajectory.py` | 입자 궤적과 프로그램 구조화 |
| 07 | `chapters/chapter07/original_package/b1_sequences.py` | 서열 자료와 클래스 예제 |
| 08 | `chapters/chapter08/original_package/Chapter_08/c3_calibration.py` | 측정값의 보정(calibration) 모델 |
| 09 | `chapters/chapter09/original_package/c3_validation.py` | 보정 데이터의 검증 |
| 10 | `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/ch10_pipeline.py` | 여러 보정 모델의 분석 오케스트레이션; 10.1.3 단순 예제와 계약 다름 |
| 11 | `chapters/chapter11/ch11_lab.py` | Chapter 11 계산 실습 및 의존성 |
| 12 | `chapters/chapter12/src/ch12_canonical_examples.py` | 배열 계산 대표 예제; 추가 4개 src 파일 존재 |
| 13 | `chapters/chapter13/src/ch13_examples.py` | 과학 계산·재현성 실습; ch13_extended.py 별도 |
| 14 | `chapters/chapter14/src/ch14_examples.py` | 과학 데이터와 생물학 응용; ch14_advanced.py 별도 |
| 15 | `chapters/chapter15/src/ch15_core_concepts.py` | 자동미분·민감도 분석; ch15_sensitivity.py 별도 |
| 16 | `chapters/chapter16/src/ch16_validated_decay.py` | 입력 검증된 구현; ch16_initial_bug.py는 의도적 결함 시연 |
| 17 | `chapters/chapter17/src/oscillator_lab/core.py` | 조화진동자 모델·Euler/RK4/SciPy; 재구성 후보 |

## 실제 검증 실행

저장소 루트에서 `python scripts/check_all_chapters.py --reset`로 기존 캐시를 사용하지 않고 장별 테스트를 수행합니다. 일부 파일은 설명용 자료이므로 직접 실행보다 테스트·학습 순서에 따라 사용합니다. 테스트 통과 여부는 Word 전체 문장·출력의 정확성과 별도입니다.

## 읽을 때 반드시 구분할 점

- **Chapter 1:** 한 파일만 있는 것이 아니라 `sections/` 아래 절별 실행 파일 15개를 순서대로 학습합니다.
- **Chapter 10:** Word 10.1.3의 `run_analysis(measurements, model)`은 입문용 개념 예제입니다. 배포 후보 API는 여러 보정 모델을 받는 `ch10_pipeline.py`입니다. 동일 이름이더라도 억지로 병합하지 않습니다.
- **Chapter 16:** `ch16_initial_bug.py`는 **의도적인 결함 시연**입니다. 계산에 사용할 기준 구현은 `ch16_validated_decay.py`입니다.
- **Chapter 17:** `oscillator_lab`은 역사적 원본을 복원한 파일이 아닌 **재구성한 후보 코드**입니다. 실행 명령은 아래와 같습니다.

```bash
cd chapters/chapter17
PYTHONPATH=src python -m oscillator_lab
```

## 아직 확정하지 않은 내용

- Word v37의 모든 코드 블록과 저장소의 일대일 대응
- Windows/Anaconda 신규 환경 재현
- GitHub Actions의 첫 호스팅 실행은 **2026-10-23 Run #1 (`39938553273`)에서 18개 작업 모두 성공**했습니다(원본 기준 커밋 `c9035fae9eed05a9cde49be12a4ccaecee725ab9`). 이는 Ubuntu/Python 3.11 CI에만 해당합니다. [실행 기록](https://github.com/openwithnet/python-upgrade-code-companion/actions/runs/39938553273)
- 최종 원고의 Microsoft Word 수식·목차·페이지 표시 QA

배포 시 위의 미검증 범위를 검증 완료로 표시하지 않습니다.
