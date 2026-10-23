# Chapter 14 Code Candidate v52

검증된 대표 실행 예제입니다. 출판 원고의 모든 코드나 생물학적 예측 모델 전체가 아닙니다.

## 실행

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m pytest -q tests
```

Windows PowerShell에서는 `PYTHONPATH`를 설정하는 대신 프로젝트의 `src` 폴더를 IDE에서 소스 경로로 지정하거나 다음 명령으로 실행할 수 있습니다.

```powershell
$env:PYTHONPATH = 'src'
python -m pytest -q tests
```

프로젝트 코드는 CPU만으로 실행 가능합니다. 코드·본문 대응은 `Code_Companion_Guide.md`를 참고하세요.
