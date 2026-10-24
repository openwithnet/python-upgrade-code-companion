# 과학자를 위한 Python 업그레이드 — 통합 Code Companion 후보 v75

**상태: 비공개 GitHub 저장소 업로드 및 Python 3.11 CI 통과 / 공개 Release 전 / NOT FROZEN**

- `chapters/chapter01`과 `chapters/chapter02`–`chapter17`에 현재 확보한 후보 소스를 보존했습니다.
- Chapter 02–10은 최초 `Downloads.zip`의 장별 검토 패키지에서 원래 상대경로/파일명으로 추출한 *원본 보존 사본*입니다. 테스트나 재구성 프로그램을 포함할 수 있으며 최종 canonical 코드 선정은 남았습니다.
- Chapter 11은 v72 회수 원본이며, Chapter 12–16은 대표 검증 코드 패키지, Chapter 17은 **원본이 아닌 재구성 후보**입니다.
- 테스트 통과는 문서 전체 코드와의 일대일 대응 또는 Windows 호환성 증명이 아닙니다.

## 독자용 장별 코드 안내

대표 파일과 사용 시 주의사항은 [`docs/READER_CODE_COMPANION_GUIDE.md`](docs/READER_CODE_COMPANION_GUIDE.md)에서 확인할 수 있습니다. 기계 판독 가능한 장별 대응표는 [`docs/READER_CODE_MAP_CH01_17.csv`](docs/READER_CODE_MAP_CH01_17.csv)입니다. **대표 파일 연결표는 Word 전체 코드의 1:1 검증을 의미하지 않습니다.**

## Chapter 02–10 테스트

```bash
python scripts/check_ch02_10.py
```

각 장을 별도 프로세스로 검사하며 원본 파일명을 수정하지 않습니다. Chapter 10은 중복 테스트 모듈명 해결을 위해 `--import-mode=importlib`를 사용합니다.

공개용 출처·검증 범위는 [`docs/PROVENANCE_AND_GATES.md`](docs/PROVENANCE_AND_GATES.md)와 [`docs/SOURCE_ROLE_AND_RELEASE_GATE.csv`](docs/SOURCE_ROLE_AND_RELEASE_GATE.csv)에서 확인할 수 있습니다. 상세한 원본 파일별 QA 기록은 내부 작업 저장소에 보존합니다.

## 전체 검증 및 GitHub CI (draft)

```bash
python -m pip install -r requirements/base.txt
python -m pip install -r requirements/ch15.txt
python scripts/check_all_chapters.py --reset
```

`--reset`은 이전 통과 기록을 무시해 재검증합니다. CI는 `.github/workflows/chapter-tests.yml`에서 장별 독립 작업으로 실행합니다. 자세한 주의사항은 `docs/CI_POLICY.md` 참조. GitHub 호스팅 검증: 2026-10-23 push Run #1 (ID `39938553273`), 커밋 `c9035fae9eed05a9cde49be12a4ccaecee725ab9`에서 preflight 1개 + Chapter 1–17 17개 작업 모두 `completed/success` 확인. [실행 기록](https://github.com/openwithnet/python-upgrade-code-companion/actions/runs/39938553273).

## Source roles and release boundaries

See [`docs/SOURCE_ROLE_AND_RELEASE_GATE.md`](docs/SOURCE_ROLE_AND_RELEASE_GATE.md) and [`docs/SOURCE_ROLE_AND_RELEASE_GATE.csv`](docs/SOURCE_ROLE_AND_RELEASE_GATE.csv). Tests passing **do not** imply every Word code block has a released source. Chapter 16 contains intentionally flawed teaching code; Chapter 17 is a documented reconstruction. The repository remains NOT FROZEN.


## Windows / Anaconda (CPU-first, draft)

Windows 사용자는 [`environments/windows-cpu.yml`](environments/windows-cpu.yml)로 독립 환경을 만들고 [`docs/WINDOWS_ANACONDA_REPRODUCIBILITY.md`](docs/WINDOWS_ANACONDA_REPRODUCIBILITY.md)의 절차를 따르십시오. Chapter 15의 PyTorch/JAX는 별도 선택 설치입니다. **Windows 설치·실행의 실측 검증은 아직 수행하지 않았습니다.**

## GitHub 공개 전 점검

내부 작업 저장소의 배포 준비 감사 기록을 참고하십시오. **Apache License 2.0의 최상위 LICENSE를 적용했으며**, GitHub Actions의 **최초 실행은 성공**했습니다. Windows 신규 환경 재현성·최종 Microsoft Word 표시 검증은 미완료입니다. 배포 승인 전까지 릴리스 후보로 유지합니다.

코드 출처·라이선스 1차 감사: 내부 작업 저장소의 출처 감사 기록. **Apache-2.0 선택은 확정했지만 파일별 제3자 권리 확인과 공개 승인은 미완료입니다.**

## 공개 파일 범위 게이트

파일별 공개 후보·교육용 결함·테스트·내부 QA 구분: 내부 작업 저장소의 공개 범위 결정·목록. 파일별 저작권·재배포 적합성 확인 및 릴리스 승인 전 **PUBLIC RELEASE HOLD**.

## 공개 라이선스 상태

- [라이선스 선택 판단 및 공개 게이트](docs/LICENSE_SELECTION_DECISION.md) — LICENSE 적용 이후에도 남은 권리·재현성 검증 사항.

**코드 저장소 라이선스: Apache-2.0 (사용자 승인: 2026-10-23).** LICENSE 파일을 추가했습니다. 다만 제3자 코드의 권리 확인 및 릴리스 검증 전까지 GitHub 공개는 보류합니다. Word 출판 원고는 코드 라이선스와 별도로 관리합니다.

## Python 3.11 verification status

Python 3.11 syntax-only audit passed (84 `.py` files). Hosted Ubuntu/Python 3.11 CI Run #1 passed all 18 jobs; independent Windows/Anaconda clean runtime remains unverified. See 내부 작업 저장소의 Python 3.11 재현성 검증 기록.

Offline CI configuration/target audit: `python scripts/ci_preflight.py` (does not require third-party packages).


## 릴리스 상태

이 저장소는 현재 **GitHub 비공개 저장소에 업로드된 검토용 후보**이며 최종 동결·공개하지 않았습니다. 2026-10-23 GitHub Actions Python 3.11 CI 최초 실행의 모든 18개 작업은 성공했습니다. Windows/Anaconda 독립 설치, 외부 자료 권리 확인, Word 원고 전체 코드의 1:1 대응 및 최종 Word 표시 검증은 완료되지 않았습니다. 내부 QA 원자료는 별도 작업 저장소에 보존합니다.
