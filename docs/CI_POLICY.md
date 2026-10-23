# CI 및 장별 실행 정책 (candidate, not frozen)

1. Chapter 1–17은 독립 작업으로 실행한다. 각 작업은 별도의 Python 프로세스에서 해당 Chapter 경로만 import하도록 한다.
2. 공유 의존성은 `requirements/base.txt`, Chapter 15 PyTorch/JAX 선택 의존성은 `requirements/ch15.txt`에 명시한다. **검증된 lockfile 아님**.
3. `check_all_chapters.py --chapters N --reset` 명령으로 CI에서 기존 결과를 강제로 초기화한다.
4. Chapter 10은 `--import-mode=importlib`로 테스트 파일의 동일 이름 충돌을 우회한다. 라이브러리 이름 충돌 자체가 해결됐다는 의미는 아니다.
5. `chapter17`은 원래 Word 원고의 검증된 원본 코드가 아니라 재구성 후보로서 provenance 경고 유지.
6. GitHub Actions YAML을 작성했지만 **실제 GitHub-hosted runner 실행은 아직 하지 않았다**. 현재 환경은 Linux Python의 기존 장별 검증만 확인했다.
7. Windows + Anaconda, Word 원고 전체 소스와 일대일 대응, 배포 환경 lock 및 GitHub 공개는 별도의 release gate로 남는다.

## 검증 명령

```bash
python -m pip install -r requirements/base.txt
python -m pip install -r requirements/ch15.txt # Chapter 15에만 필요
python scripts/check_all_chapters.py --chapters 10
```

## CI 게이트 구성
- push / pull_request / workflow_dispatch
- 17개 chapter 매트릭스 병렬 실행, `fail-fast: false`
- 장별 JSON 증거를 Actions artifact로 수집
- 후보의 보관/다운로드 요청은 별도 최종 릴리스에 한정
