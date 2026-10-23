# Windows + Anaconda 재현성 안내 (Candidate / NOT FROZEN)

## 검증 범위

이 문서는 **Windows에서 직접 실행해 검증한 결과가 아닙니다.** 기존 Linux/Python 3.13 작업 환경의 장별 테스트 성공과 설치 패키지 목록을 토대로 작성한 **Windows 설치 후보 절차**입니다. Windows + Python 3.11 + CPU 신규 환경에서 실제 설치·재실행하기 전에는 'Windows verified'로 표기하지 않습니다.

## 최소 설치 (Anaconda Prompt, Windows)

```bat
conda env create -f environments\windows-cpu.yml
conda activate python-upgrade
python -V
python -m pip check
python -m pytest --version
python scripts\check_all_chapters.py --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17 --reset
```

위 명령은 **저장소 최상위 폴더**에서 실행해야 합니다. `--reset`은 이전 실행 기록을 재사용하지 않고 선택 장을 재검증합니다. Chapter별 하위 작업 디렉터리에서 실행할 필요는 없습니다.

> Chapter 15는 별도로 설정하십시오. PyTorch/JAX는 대형 의존성이므로 기본 환경에 강제하지 않습니다. Windows/Python 3.11 CPU 플랫폼별 wheel 지원 여부는 설치 당시에 확인해야 합니다.

## Chapter 15 선택 설치 (CPU)

```bat
conda activate python-upgrade
python -m pip install -r requirements\ch15.txt
python -m pip check
python scripts\check_all_chapters.py --chapters 15 --reset
```

가능하면 가상환경에서 `python -m pip`를 사용하십시오. 설치에 문제가 있으면 무작정 CUDA 버전을 설치하지 말고 해당 패키지의 OS/Python/CPU 지원을 확인하십시오. Windows용 JAX 지원은 버전과 배포 채널에 따라 달라질 수 있습니다. 본 프로젝트의 Chapter 15 테스트 통과는 Windows에서 보장되지 않습니다.

## 재현성 확인과 증거

```bat
python -V
conda list --explicit > environment-explicit-windows.txt
python -m pip freeze > pip-freeze-windows.txt
python -m pip check
python scripts\check_all_chapters.py --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17 --reset
```

생성한 목록과 검사 결과는 환경 QA에 필요할 때에만 제출하고, 평상시 사용자에게 별도로 보관을 요구하지 않습니다. 배포 시에는 실제 지원되는 Python 버전과 패키지 조합을 확인한 후 별도 lockfile을 마련할 수 있습니다.

## 해석 원칙

- Chapter 1의 15개 절별 실행은 전체 Word 원고 코드의 완전한 검증과 같지 않습니다.
- 일부 장은 과학적 계산이 의도적으로 단순화되어 있으며, 교육용 오류 시연은 정상 구현과 구분해야 합니다.
- Chapter 10의 중복 테스트 모듈명은 pytest `--import-mode=importlib`로 수집하여 확인합니다.
- Chapter 17은 원본 소스의 완전 복원이 아니라 재구성된 검증 후보입니다.
- GitHub Actions의 Ubuntu 결과로 Windows 호환성을 확정하지 않습니다.

## 실패 시 진단

먼저 활성 환경(`conda info --envs`), Python 버전(`python -V`), 패키지 충돌(`python -m pip check`), 정확한 장별 실패 로그를 확인하십시오. 시험 환경과 배포 환경은 분리하십시오.
