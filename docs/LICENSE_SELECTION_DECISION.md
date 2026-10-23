# Python Upgrade Code Companion — 라이선스 선택 판단 (2026-10-23)

**현재 결정: APACHE_2_0_SELECTED_AND_LICENSE_FILE_ADDED / PUBLIC_RELEASE_HOLD.** 사용자가 2026-10-23에 Apache-2.0을 선택했습니다. 이 결정은 코드 저장소의 라이선스 정책이며, 제3자 저작물 재배포 권한이나 GitHub 공개 승인을 의미하지 않습니다.

## 권장 선택

프로젝트가 독자적으로 작성한 소스·테스트·문서의 권리와 외부 코드의 재배포 조건이 확인되면 **Apache License 2.0**을 우선 후보로 권장합니다. 이는 이미 별도 OpenWith 교육·Scientific AI 저장소에서 Apache 2.0을 채택한 정책과의 관리 일관성을 위한 *권고*이지 확정이 아닙니다.

- Apache-2.0: 상업적 이용·수정·재배포 허용, 관련 기여자의 특허 사용 허락 규정 포함, 라이선스·저작권·관련 NOTICE 유지 및 변경 고지 의무.
- MIT: 간결하며 상업적 이용·수정·재배포 허용, 저작권·허락 고지 유지 의무. Apache-2.0과 특허 관련 조건 등 차이가 있음.
- 라이선스 미부여: GitHub에 공개한다고 재사용 권한이 자동으로 부여되는 것은 아님. 교육용 공개 배포의 장기 목적에는 부적합할 수 있음.

## 배포 범위 결정

1. **코드 저장소**: 사용자 소유·권리 확인된 Python 소스, 테스트, 실행문서에 한해 선택한 소스 라이선스 적용. Chapter 16 의도적 오류 예제 및 Chapter 17 재구성 표시 유지.
2. **Word 교재 본문**: 코드 저장소 라이선스와 자동 연동하지 않음. 출판용 원고·그림·인용물의 이용조건은 별도로 결정.
3. **제3자 코드/데이터**: 프로젝트 라이선스를 붙여 권리를 새로 부여할 수 없음. 재배포 요건을 파일별로 확인해 원 저작권·라이선스 표시를 유지하거나 제외.
4. **패키지 의존성**: numpy, scipy 등 pip/conda 설치 지시와 패키지 소스 재배포를 구별.

## 실제 공개 전 게이트 (최소)

- [ ] 사용자에게 코드 저작·인용 출처 및 재배포 가능한 범위 확인
- [x] 사용자가 Apache License 2.0을 명시적으로 선택 (2026-10-23)
- [ ] LICENSE 추가 완료. 제3자 권리 확인 및 필요한 NOTICE/원저작자 고지는 계속 점검
- [ ] 실제 GitHub CI 및 Windows 설치 재현성 검증
- [ ] 대표 원고–코드 계약 검증, Word 표시 QA

## 기준 출처

- Apache License 2.0 정본: https://apache.org/licenses/LICENSE-2.0.html
- Apache License 적용 FAQ: https://www.apache.org/foundation/license-faq
- MIT 라이선스(SPDX): https://spdx.org/licenses/MIT
- GitHub 라이선스 안내: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

**내부 파일. 지금 다운로드할 필요 없음.**
