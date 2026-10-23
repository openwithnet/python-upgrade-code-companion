# Chapter 7. 객체의 관계: 상속, 합성과 다형성

> **검토용 재구성 원고 — NOT FROZEN.** 화면에서 집필한 7.1–7.7 원문을 문장 단위로 자동 추출하지 못했으므로 원문과의 1:1 보존은 검증되지 않았다. 아래 내용은 상세 목차·주요 개념·수식·사례를 다시 구성한 편집 검토본이다. 출판용 원본을 대체하지 않는다.

## Canonical Detailed TOC
- Introduction — 단일 객체에서 객체 간 관계로
- 7.1 객체 간 관계의 이해: 7.1.1 Is-a와 Has-a 관계 / 7.1.2 클래스 계층의 의미 / 7.1.3 객체 사이의 협력
- 7.2 상속과 다형성: 7.2.1 Inheritance / 7.2.2 Method Overriding과 `super()` / 7.2.3 Polymorphism
- 7.3 합성과 위임: 7.3.1 Composition / 7.3.2 Delegation / 7.3.3 상속과 합성의 비교
- 7.4 생물학 객체 모델: 7.4.1 Molecule과 SequenceMolecule / 7.4.2 DNA, RNA, Protein / 7.4.3 Nucleotide와 AminoAcid
- 7.5 실습: 서열 객체 계층 설계: 7.5.1 객체와 책임의 식별 / 7.5.2 공통 동작과 다형성 / 7.5.3 상속 구조와 합성 구조 비교
- 7.6 잘못된 객체 설계 개선: 7.6.1 과도한 상속 / 7.6.2 잘못된 책임 배분 / 7.6.3 객체 관계의 재설계
- 7.7 Chapter Summary

## Introduction 단일 객체에서 객체 간 관계로

Chapter 6에서는 객체의 상태와 책임을 중심으로 객체지향 프로그래밍의 기본을 다루었다. 이번 장은 서로 다른 객체들이 관계를 맺고 협력하는 방법을 이해하는 데 목적이 있다. DNA, RNA, Protein은 생물학적 서열이라는 공통점을 갖지만 구성 단위, 허용 기호, 분석 의미가 서로 다르다. 이를 하나의 상위 클래스에 무리하게 넣으면 추상화의 의미를 잃을 수 있다. 반대로 공통 기능을 모두 복사하면 유지보수 비용이 증가한다.

이번 장에서는 상속(Inheritance), 메서드 재정의(Method Overriding), 다형성(Polymorphism), 합성(Composition), 위임(Delegation)을 비교한다. B1 서열 분석 사례를 통해 객체의 관계가 단순한 생물학 분류표가 아니며, 데이터와 계산의 과학적 계약을 반영해야 한다는 점을 살펴본다. 단계별 예제는 개념 설명용이며 최종 정규 실행 코드는 별도 Python 파일에 유지한다.


## 7.1 객체 간 관계의 이해


### 7.1.1 Is-a와 Has-a 관계

Is-a는 한 개념이 다른 개념의 한 종류라는 의미이며 상속을 고려할 수 있는 출발점이다. DNASequence is a BiologicalSequence라고 말할 수 있지만, 이 문장만으로 반드시 상속이 필요한 것은 아니다. Has-a는 어떤 객체가 다른 객체를 참조하거나 구성 요소로 사용하는 관계이다. Experiment가 MeasurementRecord를 보유하는 경우가 이에 해당한다.

Has-a는 엄밀한 의미의 합성과 동일하지 않다. 구성 요소가 독점적으로 소유되는지, 외부에서 공유되는지, 객체의 수명이 종속되는지를 함께 살펴야 한다. Python에서 객체 참조를 속성에 저장한다는 것만으로 소유권의 의미가 자동 결정되지 않는다.


### 7.1.2 클래스 계층의 의미

상위 클래스는 공통 계약과 동작을 제공한다. DNA와 RNA는 length()를 재사용할 수 있지만 Protein에서 의미가 없는 gc_fraction()을 공통 최상위 클래스에 선언하는 것은 부적절하다. 하위 객체가 상위 객체를 기대하는 코드에서 계약을 유지해야 한다는 대체 가능성이 중요하다. BiologicalSequence→SequenceMolecule→NucleicAcid→DNASequence처럼 분류 단계만 무조건 늘리는 것은 소프트웨어가 복잡해지는 원인이 된다.


### 7.1.3 객체 사이의 협력

객체 간 협력에 반드시 상속이 필요하지는 않다. Chapter 6에서 Particle과 Trajectory는 상속 관계가 아니지만 실행 함수가 두 객체를 연결한다. DNA 분석에서도 객체는 유효한 서열을 제공하고 독립 함수는 특정 계산을 맡을 수 있다. 공개 인터페이스를 통해 협력할 때 객체의 내부 구현에 대한 결합을 줄일 수 있다. 그러나 단순한 기능마다 별도의 추상 계층을 두는 것은 권장되지 않는다.


## 7.2 상속과 다형성


### 7.2.1 Inheritance

상속은 기존 클래스의 구현과 계약을 활용하여 새 클래스를 정의하는 기능이다. class DNASequence(BiologicalSequence): 형태를 사용한다. 상위 클래스의 __init__()와 length() 등을 재사용할 수 있지만 DNA와 RNA의 허용 기호 규칙은 별도로 유지해야 한다. 공통 길이 계산을 한 번 정의하는 것과, 모든 하위 유형에 일관된 과학적 의미의 계약을 제공하는 것은 다른 문제이다.


### 7.2.2 Method Overriding과 super()

하위 클래스는 메서드를 재정의하여 동작을 구체화할 수 있다. super()는 메서드 탐색 순서(MRO)에서 다음에 해당하는 구현을 호출하며, 항상 이름상 직접 부모만을 의미하지는 않는다. 재정의하면서 length()의 반환값을 정수에서 설명 문자열로 바꾸면 상위 계약을 깨뜨린다. DNA와 RNA에서 특정 기호 빈도 계산을 공통화할 수 있지만 과학적 의미가 다른 계산을 이름만 같게 묶는 것은 피해야 한다.


### 7.2.3 Polymorphism

다형성은 서로 다른 객체가 같은 호출 규약을 제공할 때 외부 코드가 공통 방식으로 사용할 수 있다는 성질이다. report_length(obj)는 obj.length()만 요구할 수 있다. Python에서는 명시적인 상속 없이도 덕 타이핑(Duck Typing)으로 이를 달성할 수 있으며 typing.Protocol을 이용해 구조적인 인터페이스를 명시할 수도 있다. Protocol은 일반적으로 실행 중 수학적 의미를 검증하지 않는다. 객체의 구체적인 종류보다 메서드의 입력·출력 계약이 중요하다.


## 7.3 합성과 위임


### 7.3.1 Composition

합성은 다른 객체를 구성 요소로 활용하여 기능을 조직하는 방법이다. DNASequence가 SequenceData를 보유하고 AlphabetPolicy를 이용해 DNA 기호를 검증한다면 데이터 표현과 과학적 검증 정책을 구분할 수 있다. SequenceData는 비어 있지 않은 문자열을 대문자로 정규화하며, AlphabetPolicy는 유형별 허용 기호를 검증한다.


### 7.3.2 Delegation

위임은 객체가 자신의 작업 중 일부를 다른 객체가 수행하도록 요청하는 방식이다. DNASequence.length()는 내부 SequenceData의 __len__()을 호출할 수 있고, 검증은 AlphabetPolicy.validate()에 맡길 수 있다. 검증을 위임한다고 해서 외부 사용자가 기대하는 DNASequence의 유효성 책임이 사라지는 것은 아니다. 검증 정책을 바꿀 수 있도록 허용하는 경우 객체의 생물학적 의미가 일관되게 유지되는지도 검토해야 한다.


### 7.3.3 상속과 합성의 비교

상속은 종류의 관계와 공통 계약을 표현하는 데, 합성은 독립된 데이터·정책·기능을 조합하는 데 적합하다. 'Composition over Inheritance'는 무조건 상속을 금지한다는 뜻이 아니라 불필요한 계층을 만들기 전에 합성의 가능성을 검토하라는 권고이다. 작은 프로그램에서는 직접 함수 호출이 가장 단순할 수도 있다. 클래스의 개수는 설계 품질의 지표가 아니다.


## 7.4 생물학 객체 모델


### 7.4.1 Molecule과 SequenceMolecule

분자의 표현 수준에는 식별자, 서열, 분자 그래프, 3차원 구조, 동역학 등이 있다. Molecule을 식별자와 이름만 저장하는 객체로 정의할 수 있지만 그것이 화학적 분자 구조 전체를 나타내지는 않는다. SequenceMolecule은 Molecule과 SequenceData를 합성할 수 있지만 분석 대상이 항상 단일의 완전한 분자와 일치하는 것은 아니다. 이번 B1 사례에서는 불필요한 전체 화학 구조 모델을 도입하지 않는다.


### 7.4.2 DNA, RNA, Protein

교육용 DNA 알파벳은 {A,C,G,T}, RNA는 {A,C,G,U}, Protein은 표준 20개 아미노산 기호를 사용한다. 이들은 길이와 기호 빈도라는 공통 연산을 공유하지만 DNA/RNA에서 정의한 GC 비율을 Protein에 부여해서는 안 된다. 계산식 f_GC=(N_G+N_C)/L과 f_a=N_a/L은 서로 다른 과학적 계약을 가진다. FASTA 헤더, N 같은 모호 기호, 수정 잔기, 구조 정보는 현재 구현의 범위 밖이다.


### 7.4.3 Nucleotide와 AminoAcid

서열의 A, C, G, T, U는 잔기 종류를 나타내는 기호이지 완전한 독립 분자의 화학 구조가 아니다. NucleotideResidue나 AminoAcidResidue 클래스를 둘 수 있지만, 단순한 서열 길이와 빈도 계산에는 한 글자 문자열이 더 효율적일 수 있다. 실제 화학적 구조나 전하, 좌표 등이 필요해질 때 더 자세한 잔기 객체를 고려한다. 과학적 대상의 모든 속성을 모사하는 것보다 프로그램이 필요한 표현 수준을 정하는 것이 우선이다.


## 7.5 실습: 서열 객체 계층 설계


### 7.5.1 객체와 책임의 식별

기준 구현의 구성 요소는 SequenceData(문자열 정규화·보관), AlphabetPolicy(허용 기호 검증), _SequenceBase(공통 초기화와 길이/기호 계산), DNASequence·RNASequence·ProteinSequence(유형별 공개 기능), HasSequence(구조적 인터페이스)이다. _SequenceBase는 생물학적 분류 계층이 아니라 공통 구현 기반이다. Molecule, SequenceMolecule 및 잔기 객체들은 이 통합 코드에서 필요한 최소 요소가 아니므로 포함하지 않는다.


### 7.5.2 공통 동작과 다형성

DNASequence("atgcgc")는 ATGCGC로 정규화되고 GC 비율 4/6을 반환한다. RNASequence("augcgc") 역시 4/6을 반환하고, ProteinSequence("mkwvtf")에서 W의 비율은 1/6이다. Protein에는 gc_fraction()이 없다. describe_sequence(obj: HasSequence)는 객체의 실제 종류에 따른 조건 분기 없이 obj.sequence와 obj.length()를 사용한다. Protocol의 구조적 계약과 런타임의 입력 유효성 검사는 구분해야 한다.


### 7.5.3 상속 구조와 합성 구조 비교

순수 상속 방식은 공통 구현을 손쉽게 재사용하지만, 상위 클래스의 계약을 넓게 설계하기 쉽다. 순수 합성 방식은 책임을 분리하나 위임 코드의 중복이 생길 수 있다. 기준 구현은 제한적 상속으로 공통 구현을 재사용하고, 구성 객체에 저장·검증을 위임하며, Protocol로 외부 공통 인터페이스를 표현하는 절충 구조를 채택한다. 정상·오류 입력과 반환값의 의미는 별도 자동 테스트로 확인한다.


## 7.6 잘못된 객체 설계 개선


### 7.6.1 과도한 상속

BiologicalSequence에 gc_fraction()을 무조건 정의한 다음 Protein에서 NotImplementedError로 막는 구조는 상위 계약의 문제를 드러낸다. 계층을 깊게 만들지 말고 실제로 모든 하위 유형에 유효한 공통 동작만 상위에 둔다. DNA/RNA가 GC 계산식을 공유하더라도 이를 위해 NucleotideSequence라는 클래스를 반드시 추가할 필요는 없다.


### 7.6.2 잘못된 책임 배분

하나의 DNASequence 클래스가 파일 저장, 그림 작성, 외부 데이터베이스 검색, AI 예측까지 모두 담당한다면 변경 이유가 집중된다. 한편 단순한 len() 계산까지 여러 클래스로 분리하면 과도한 위임이 된다. SequenceData는 문자열과 빈 값, AlphabetPolicy는 허용 기호, 구체 서열 클래스는 생물학적 유형의 의미를 책임지도록 유지한다.


### 7.6.3 객체 관계의 재설계

DNA와 RNA에서 중복되던 GC 계산식을 calculate_gc_fraction(sequence) 독립 함수로 분리하였다. DNASequence.gc_fraction()과 RNASequence.gc_fraction()은 각각 해당 함수를 호출하여 공개 인터페이스를 유지한다. 이 함수는 이미 검증된 비어 있지 않은 대문자 DNA 또는 RNA 서열을 입력으로 받는 내부 계산 함수이다. ProteinSequence에는 GC 메서드를 추가하지 않는다. 결과와 예외 처리, 공통 인터페이스가 변하지 않는지는 회귀 테스트로 확인한다.


## 7.7 Chapter Summary

Chapter 6에서는 개별 객체의 상태와 캡슐화를 다루었다. 이번 Chapter 7에서는 상속·합성·위임·다형성을 통해 객체 사이의 책임을 설계하였다. 상속은 공통 계약과 종류의 관계를 표현할 때, 합성은 독립된 구성 요소를 조합할 때, 위임은 다른 객체의 기능을 활용할 때 사용한다. 다형성은 공통 인터페이스를 통해 서로 다른 객체를 처리할 수 있게 한다.

과학적 분류 체계를 클래스 계층에 그대로 복제해서는 안 된다. DNA와 Protein은 모두 서열이지만 GC 비율의 의미는 다르다. 공통 수학적 계산은 함수로 분리할 수 있으며, 객체는 해당 계산을 사용할 자격과 검증된 상태를 관리한다. B1 통합 프로그램은 정규화와 검증, 계산과 분석 인터페이스를 분리하여 이를 보여준다.

좋은 객체지향 설계는 많은 클래스나 추상화를 도입하는 것이 아니라, 과학적 의미를 보존하면서 프로그램의 변경 이유와 책임을 명확하게 하는 것이다. 마지막으로 구현의 정확성과 과학적 모델의 타당성은 서로 구분하여 검증해야 한다.


## B1 정규 Python 구현 및 검증

실행 가능한 예제와 테스트는 별도 `b1_sequences.py`, `test_b1_sequences.py`에 제공한다. 여러 절에서 반복 정의한 교육용 클래스를 최종 구현에 중복 포함하지 않는다.

```python
from b1_sequences import DNASequence, RNASequence, ProteinSequence

dna = DNASequence("atgcgc")
rna = RNASequence("augcgc")
protein = ProteinSequence("mkwvtf")
print(f"{dna.gc_fraction():.4f}")
print(f"{rna.gc_fraction():.4f}")
print(f"{protein.residue_fraction('W'):.4f}")
```

예상 출력: `0.6667`, `0.6667`, `0.1667`.

**수식:** `f_GC=(N_G+N_C)/L` 및 `f_a=N_a/L`.
