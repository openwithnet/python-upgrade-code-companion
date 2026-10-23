# Chapter 4. 함수로 프로그램을 구조화하기

> 과학자를 위한 Python 업그레이드 · Canonical TOC v1.2 · 교육적 설명 보강본(원문 문장별 완전 보존본 아님)

## Introduction

Chapter 3에서는 입자 운동의 초기조건 설정, 계산, 결과 기록과 검증을 하나의 절차적 스크립트 안에서 분명히 구분했다. 그러나 여러 초기조건을 반복하거나 동일한 입력 검증을 여러 분석에 적용해야 할 때 긴 스크립트는 재사용과 검증이 어려워질 수 있다.

함수(Function)는 계산에 이름과 경계를 부여한다. 중요한 것은 단순히 `def` 문을 사용하는 것이 아니라 **함수의 책임, 입력·출력, 사용 계약, 상태 변경과 부작용을 예측 가능하게 설계하는 것**이다. 여기에서는 절차적 P1 입자 운동 계산을 함수로 표현한 다음, B1 DNA 서열의 검증과 GC 함량 계산을 하나의 함수 중심 프로그램으로 발전시킨다. Chapter 5의 고차 함수와 함수 합성, Chapter 9의 고급 계약 및 자동화 검증은 각각 후속 장에서 본격적으로 다룬다.

명시적 오일러 방법의 한 단계를 예로 들자. 현재 위치와 속도를 사용하여 다음 시점의 값을 계산한다.

$$x_{n+1}=x_n+v_n\Delta t$$

$$v_{n+1}=v_n+a\Delta t$$

```python
# P1에서 가져온 한 단계 계산

def euler_step(position, velocity, acceleration, time_step):
    next_position = position + velocity * time_step
    next_velocity = velocity + acceleration * time_step
    return next_position, next_velocity

print(euler_step(0.0, 0.0, 2.0, 0.5))
# (0.0, 1.0)
```

코드의 경계가 분명해졌지만, 시간 간격의 허용 범위나 반환 상태의 시점 등은 여전히 설명과 검증이 필요하다. 이것이 이번 장의 출발점이다.

## 4.1 함수의 역할과 설계

### 4.1.1 함수는 계산의 독립적인 단위이다

다음 평균 계산은 짧고 명확하다. 그러나 같은 계산을 여러 곳에서 사용한다면 함수 이름으로 계산 목적을 표현할 수 있다.

```python
measurements = [10.0, 12.0, 14.0]
print(sum(measurements) / len(measurements))  # 12.0

def calculate_mean(values):
    if len(values) == 0:
        raise ValueError('values must not be empty')
    return sum(values) / len(values)

print(calculate_mean(measurements))  # 12.0
```

함수 정의는 오히려 코드 줄 수를 늘릴 수 있다. 이익은 줄 수가 아니라 **의미 있는 이름과 검증 가능한 책임 단위**를 확보하는 데 있다. 함수가 독립적이라는 것은 다른 라이브러리를 전혀 쓰지 않는다는 뜻이 아니라, 호출자가 필요한 입력과 반환값 및 사용 조건을 알 수 있다는 뜻이다. 빈 입력을 명시적으로 거부하는 것도 계산의 책임을 밝히는 작업이다.

### 4.1.2 매개변수와 반환값으로 계산을 표현하기

**• 계산과 출력의 차이**

함수의 결과를 화면에 표시하는 것과 반환하는 것은 다르다. `print()`는 사용자에게 내용을 표시하지만, 그 함수가 별도로 반환하지 않으면 호출 결과는 `None`이다. 반대로 반환값은 다른 수치 계산, 표 작성 또는 저장 절차에 직접 연결할 수 있다. 입자 운동의 `euler_step()`처럼 둘 이상의 값을 반환하는 경우에는 Tuple의 위치가 무엇을 뜻하는지 명시해야 한다. 복잡한 결과에 대해서는 Chapter 후반부에서 Dictionary나 `TypedDict`를 검토한다.

**• 외부 의존성을 입력에 표시한다**

계산에 필요한 기울기나 시간 간격이 함수 외부의 전역 변수에 숨어 있으면 재현하기 어려워질 수 있다. 같은 측정 신호라도 전역 검량선 기울기가 바뀌면 다른 농도가 산출된다. 반면 `calculate_concentration(signal, slope)`처럼 필요한 인수를 직접 전달하면 호출 자체가 계산 조건의 기록이 된다. 다만 함수 인수가 많아질 때에는 아무 값이나 길게 나열하기보다 의미를 갖는 구조로 묶는 방안을 검토해야 한다.



계산에 필요한 데이터는 가급적 매개변수로 표현한다. 일정 속도에서 이동 거리는 다음과 같다.

$$d=vt$$

```python
def calculate_distance(velocity, time):
    return velocity * time

print(calculate_distance(2.0, 5.0))  # 10.0
```

외부 전역 변수 `velocity`, `time`을 암묵적으로 참조하는 함수는 해당 변수가 변경되면 같은 호출에서도 다른 결과를 낼 수 있다. 또한 `print()`와 `return`은 다르다. 화면에 출력만 하는 함수는 계산 결과를 반환하지 않으면 `None`을 반환하므로 다음 계산에서 결과를 재사용하기 어렵다. 여러 결과는 Tuple로 반환할 수 있으며, `euler_step()`의 반환값도 두 원소의 Tuple이다. 반환 필드가 많으면 순서보다 의미 있는 이름을 가진 결과 구조를 고려한다.

### 4.1.3 함수의 책임과 응집도

좋은 함수는 한 가지 명확한 목적을 갖는다. DNA 서열의 문자 변환, GC 계산, 결과 출력과 파일 저장을 무조건 하나의 함수에 섞으면 개별 계산의 재사용이 어려워질 수 있다. 반대로 `count_g()`, `count_c()`, `add_counts()`와 같은 아주 작은 함수를 아무 필요 없이 만드는 것도 흐름을 복잡하게 할 수 있다.

```python
def calculate_gc_fraction(sequence):
    sequence = sequence.upper()
    if not sequence:
        raise ValueError('sequence must not be empty')
    if any(base not in 'ACGT' for base in sequence):
        raise ValueError('invalid DNA sequence')
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

print(f'{calculate_gc_fraction("ATGCGC") * 100:.2f}%')  # 66.67%
```

함수의 길이보다 **목적·입력·반환·변경 이유의 일관성(응집도)**을 우선한다. 검증을 여러 분석에서 공유하게 되면 그때 공통 검증 함수로 나누는 것이 유리하다.

## 4.2 함수 인터페이스

### 4.2.1 위치 인수와 키워드 인수

같은 실수형 인수 두 개를 받는 농도 계산에서 순서가 뒤바뀌어도 Python은 의미 오류를 알아채지 못한다. 키워드 인수로 측정 신호와 기울기의 의미를 드러낼 수 있다.

```python
def calculate_concentration(signal, *, slope):
    if slope <= 0:
        raise ValueError('slope must be positive')
    return signal / slope

print(calculate_concentration(6.0, slope=2.0))  # 3.0
```

`*` 뒤의 `slope`는 키워드 전용이다. 반대로 매개변수 선언에 `/`를 사용하면 위치 전용으로 지정할 수 있다. 이런 문법은 외워야 할 형식 이상으로, **사용자에게 어떤 값을 이름과 함께 명시하도록 요구할지** 결정하는 설계 수단이다. 속도·가속도·시간 간격처럼 혼동하기 쉬운 과학 매개변수에서는 의미가 뚜렷한 호출이 유리하다.

### 4.2.2 기본 인수와 가변 인수

**• 과학적 기본값의 의미**

기본 인수는 단지 호출을 짧게 만드는 기능이 아니다. 예를 들어 `time_step=0.1`은 수치 적분의 분해능을, `intercept=0.0`은 검량선이 원점을 지난다는 가정을 뜻한다. 사용자가 의식적으로 선택해야 하는 조건이라면 기본값을 없애고 키워드 전용 인수로 지정하는 편이 안전할 수도 있다.

**• 변경 가능한 기본값의 함정**

다음 예는 호출 사이에 같은 List가 공유되므로 피해야 한다.

```python
def collect_bad(value, results=[]):
    results.append(value)
    return results

print(collect_bad(10))
print(collect_bad(20))
# [10]
# [10, 20]
```

통상적으로 `results=None`을 기본값으로 두고 함수 안에서 새 List를 생성한다. 다만 명시적으로 List를 전달받아 `append()`하면 그 원본은 여전히 수정된다는 사실을 따로 설명해야 한다. **기본값 공유를 피하는 것과 부작용을 없애는 것은 서로 다른 설계 문제**이다.



기본값은 편의 기능이면서 과학적 가정일 수 있다. `time_step=0.1`을 기본값으로 채택하면 수치 오차와 계산 비용에 영향을 미친다. 따라서 사용자가 반드시 의식해야 할 매개변수에는 기본값을 제공하지 않는 선택도 타당하다.

```python
def gc_content(sequence, *, percent=False):
    fraction = calculate_gc_fraction(sequence)
    return fraction * 100 if percent else fraction

print(gc_content('ATGCGC', percent=True))  # 66.66666666666666
```

변경 가능한 List를 기본값으로 쓰는 것은 주의해야 한다. 기본 인수는 정의 시 평가되므로 여러 호출이 같은 List를 공유한다.

```python
# 피해야 할 예: 호출 간 results가 공유된다.
def append_bad(value, results=[]):
    results.append(value)
    return results

# 기본 호출마다 새 List를 만드는 방식
def append_measurement(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results
```

`*args`는 여러 위치 인수를 Tuple로, `**kwargs`는 여러 키워드 인수를 Dictionary로 받는다. 선택적 메타데이터나 전달형 인터페이스에 유용하나, 필수 계산 매개변수를 모두 감추면 함수 사용 조건이 모호해진다. 이미 하나의 List·배열로 존재하는 과학 데이터라면 컬렉션 인수 하나가 더 명확할 수 있다.

### 4.2.3 입력과 출력의 구조 설계

하나의 서열에 대한 함수와 여러 서열을 다루는 반복 작업을 분리할 수 있다. 반환값이 적으면 Tuple을 사용하고, 이름으로 접근해야 하는 결과라면 Dictionary를 선택할 수 있다. 예컨대 `{'length': 6, 'gc_fraction': 2/3}`는 각 결과의 의미를 보여주지만 키와 값의 타입은 추가로 문서화해야 한다.

일반 선형 검량선은 원점 통과를 가정하지 않으면 다음과 같다.

$$A=kc+b,\qquad c=\frac{A-b}{k}$$

```python
def linear_concentration(signal, *, slope, intercept=0.0):
    if slope == 0:
        raise ValueError('slope must not be zero')
    return (signal - intercept) / slope

print(linear_concentration(6.0, slope=2.0, intercept=1.0))  # 2.5
```

여기서 `slope != 0`은 수학적 계산 가능 조건이다. 과학적 모델이 증가하는 검량선만 허용한다면 `slope > 0`을 계약으로 요구해야 한다. 정상적인 GC 비율 `0.0`과 오류를 같은 반환값으로 표현하지 말아야 한다. 반환값의 단위, 결측·모호 염기의 처리, 입력 서열과 결과의 대응 순서는 모두 인터페이스의 일부이다.

## 4.3 함수의 계약

### 4.3.1 사전조건과 사후조건

함수 계약(Function Contract)은 호출자의 사전조건(Precondition)과 정상적으로 종료했을 때 구현이 보장하는 사후조건(Postcondition)을 함께 정의한다. 비어 있지 않은 유한 실수의 산술평균은 다음 범위에 놓인다.

$$\min_i x_i\leq\bar{x}\leq\max_i x_i$$

검량선에서 양의 기울기를 요구하는 것은 과학적 모델의 추가 조건이다. 농도 계산의 수학적 사후조건은 `slope × concentration ≈ signal`이며 부동소수점 계산에서는 허용오차를 고려한다. 그러나 검량식의 대수 관계가 성립한다고 해서 실험의 참농도를 검증한 것은 아니다. **코드 계약의 충족과 과학적 모델의 타당성은 별개**이다.

### 4.3.2 함수의 입력 검증

**• 자료형 검증과 과학적 유효성 검증**

숫자 자료형만 확인해도 유한성이 보장되지는 않는다. `nan`이나 `inf`는 실수형 연산에 등장할 수 있다. 그러나 `math.isfinite()`가 참이라는 사실만으로 측정값이 실험적으로 적절하다고 볼 수도 없다. 예를 들어 농도 계산의 음수 신호는 배경 보정 과정에서 나타날 수 있으므로, 거부할지 처리할지는 분석 정책으로 명시해야 한다.

DNA의 `N`도 마찬가지이다. `N`은 실제 데이터에서 불명확한 염기를 나타내는 유효한 기호일 수 있지만, 이 장의 B1 함수에서는 A/C/G/T만 허용한다. **입력 거부는 보편적 생물학 판정이 아니라 이 함수의 계산 정의**이다. 모호 염기를 허용하는 버전은 분모를 전체 길이로 할지 확정 염기의 수로 할지 먼저 결정해야 한다.



스칼라 수치 입력에서는 `math.isfinite()`로 `nan`, `inf`를 검사할 수 있다. 자료형, 배열 형태, 단위, 허용 범위는 별도의 정책이다.

```python
import math

def safe_concentration(signal, slope):
    if not math.isfinite(signal) or not math.isfinite(slope):
        raise ValueError('signal and slope must be finite')
    if slope <= 0:
        raise ValueError('slope must be positive')
    return signal / slope

print(safe_concentration(6.0, 2.0))  # 3.0
```

이 함수는 음수 신호를 거부하지 않는다. 배경 보정 뒤 음수 신호가 나올 수 있기 때문이다. 이를 농도로 해석할 것인지는 별도 과학 정책이다. DNA 서열의 경우도 `N`은 무조건 잘못된 생물학적 데이터가 아니다. 이번 B1 교육용 분석이 **A/C/G/T만 허용한다는 입력 범위**를 채택한 것이다. 검증 위치는 외부 입력의 경계와 계산 함수의 재사용 범위를 함께 고려해 결정한다.

### 4.3.3 예외와 오류 처리

잘못된 자료형에는 `TypeError`, 허용 범위의 위반에는 `ValueError`를 이용할 수 있다. 검증 함수는 예외를 발생시키고 호출자는 오류를 보고하거나 적절히 복구하도록 책임을 나눌 수 있다. `try/except`로 모든 예외를 잡아 오류를 숨기는 것은 과학적 결과의 신뢰성을 떨어뜨릴 수 있다.

```python
try:
    calculate_gc_fraction('ATNG')
except ValueError as error:
    print(f'Invalid sequence: {error}')
# Invalid sequence: invalid DNA sequence
```

잘못된 서열에 대해 `0.0`을 반환하면 진짜 GC 비율이 0인 `ATATAT`와 구분할 수 없다. 임의로 다른 서열을 대신 계산하는 것도 과학적 정책 없이는 올바른 복구가 아니다. 예외를 잡는 것과 데이터 오류를 해결하는 것은 다르다.

## 4.4 함수와 상태

### 4.4.1 지역 변수와 이름의 범위

지역 이름은 함수 안에서 정의되며, 반환하지 않은 지역 결과에 호출자가 직접 접근할 수는 없다. Python의 이름 탐색은 통상 Local → Enclosing → Global → Built-in(LEGB)으로 설명한다. 중첩 함수는 바깥 함수의 이름을 참조할 수 있으며 `global`, `nonlocal`은 외부 이름의 재할당과 관련한다.

```python
calibration_slope = 2.0

def dependent_calculation(signal):
    return signal / calibration_slope

print(dependent_calculation(6.0))  # 3.0
calibration_slope = 3.0
print(dependent_calculation(6.0))  # 2.0
```

같은 명시적 인수로 함수 호출을 반복해도 결과가 달라졌다. 재사용할 수치 계산에서는 기울기를 매개변수로 드러내는 방식이 더 예측하기 쉽다. 외부 상수나 관리되는 설정의 사용이 항상 틀린 것은 아니지만, 계산 결과에 영향을 미치는 가변 의존성은 명확하게 해야 한다.

### 4.4.2 상태 변경과 가변 객체

**• 재할당과 내부 수정은 다르다**

Python 함수에 숫자를 전달하고 매개변수 이름에 다른 숫자를 다시 할당하더라도 호출자의 변수 이름은 바뀌지 않는다. 그러나 List나 NumPy 배열은 함수 인수로 전달한 객체의 내부를 수정할 수 있다. 따라서 `return` 여부만 확인해서는 원본 데이터 보존을 판단할 수 없다.

```python
import numpy as np

def scale_inplace(values, factor):
    values *= factor

def scaled(values, factor):
    return values * factor

source = np.array([1.0, 2.0, 3.0])
result = scaled(source, 2.0)
print(source)  # [1. 2. 3.]
print(result)  # [2. 4. 6.]
scale_inplace(source, 2.0)
print(source)  # [2. 4. 6.]
```

또한 기본 슬라이싱이 생성하는 NumPy View는 원본 데이터를 공유할 수 있다. 원본 측정 데이터를 보존해야 할 때에는 `.copy()`가 필요한지 판단한다. 모든 배열을 무조건 복사하면 메모리 비용이 커질 수 있으므로, 성능 최적화보다 먼저 함수의 수정 계약을 분명히 해야 한다.



Python에서 이름을 다시 할당하는 것과 List·NumPy 배열의 내부 요소를 수정하는 것은 다르다. 가변 객체를 인수로 받는 함수가 `append()`를 호출하거나 배열에 제자리 연산을 하면 호출자가 보유한 원본도 바뀐다.

```python
import numpy as np

def normalize_inplace(values, maximum):
    values /= maximum

def normalized(values, maximum):
    return values / maximum

values = np.array([2., 4., 6.])
copy_result = normalized(values, 6.)
print(values)       # [2. 4. 6.]
print(copy_result)  # [0.33333333 0.66666667 1.        ]
normalize_inplace(values, 6.)
print(values)       # [0.33333333 0.66666667 1.        ]
```

NumPy 기본 슬라이싱이 원본의 메모리를 공유하는 View를 반환할 수 있다는 점도 주의한다. `array[1:3].copy()`와 같이 명시적으로 복사하면 독립된 데이터를 얻는다. 모든 원본을 무조건 복사하는 것은 대규모 배열의 메모리 비용을 높일 수 있으므로 의도된 상태 변경과 데이터 보존을 균형 있게 선택한다. View·Copy의 깊은 규칙은 Chapter 12의 소관이다.

### 4.4.3 재사용 가능한 함수와 부작용

부작용(Side Effect)은 반환값 외에 외부에서 관찰할 수 있는 변화이다. 화면 출력, 파일 기록, 외부 장비 제어, 입력 배열 수정 등이 포함된다. 순수 함수(Pure Function)는 같은 입력에 대해 같은 값을 반환하고 관찰 가능한 부작용을 만들지 않는 계산이다.

```python
def square(value):
    return value * value

print(square(3.0))  # 9.0
```

실제 과학 프로그램은 입출력이 반드시 필요하다. 따라서 모든 함수를 순수하게 만들기보다 **계산의 핵심을 가능한 한 독립적으로 유지하고 외부 상호작용을 명확한 경계에서 관리**하는 것이 실용적이다. 데이터의 원본 보존, 성능, 동시 접근 등은 각각 요구사항에 따라 결정한다.

## 4.5 함수의 표현과 문서화

### 4.5.1 Type Hints

Type Hints는 매개변수와 반환값의 자료형 의도를 표현한다. 자동 실행 검증은 아니다. `str`, `float`, `list[float]`, `Sequence[float]`, `str | None` 등을 사용할 수 있으며 Python 3.12+의 `type` 문과 `TypedDict`로 별칭과 구조를 표현할 수 있다.

```python
from collections.abc import Sequence

def mean_of_sequence(values: Sequence[float]) -> float:
    if not values:
        raise ValueError('values must not be empty')
    return sum(values) / len(values)

print(mean_of_sequence((10., 12., 14.)))  # 12.0
```

`Sequence`는 순서가 있는 읽기 중심의 컬렉션을 나타내지만, 유한한 실수만 허용하거나 과학적 단위가 올바르다는 것을 보장하지 않는다. `TypedDict` 역시 키·값의 의도된 정적 구조를 기술할 뿐 실행 시 강제하지 않는다.

### 4.5.2 Docstring과 함수 사용 조건

**• 문서가 반드시 설명해야 할 한계**

검량선 함수의 단순한 수식 `(signal - intercept) / slope`만으로는 기울기·절편을 어떻게 추정했는지, 검량 범위 밖의 외삽을 허용하는지, 농도 단위가 무엇인지 알 수 없다. Docstring에는 적어도 계산 가정과 보장하지 않는 사항을 적는다. 이러한 정보는 과학적 결과의 해석을 제한하는 조건이지 장식용 설명이 아니다.

```python
def square(value: float) -> float:
    """Return the square of a value; does not validate units."""
    return value * value

print(square.__doc__)
```

Docstring은 `help()`나 `__doc__`로 확인할 수 있지만, 선언된 조건을 실행 시 자동으로 강제하지는 않는다. Type Hints도 동일하게 기본적으로 자동 검증을 제공하지 않는다. 문서·타입·실제 검증 코드가 일치하도록 함께 관리해야 한다.



Docstring은 함수의 목적·입력·출력·예외·제한을 설명한다. 과학 함수에서는 **단위, 적용 가능한 검량 범위, 입력 표준, 수치 알고리즘과 측정 불확실성의 처리 여부**를 기록할 필요가 있다. 특정 스타일(NumPy, Google 등)보다 설명의 정확성과 실제 구현과의 일관성이 중요하다.

```python
def calculate_distance(velocity: float, time: float) -> float:
    """Return distance in metres.

    Parameters are velocity (m/s) and elapsed time (s).
    Assumes constant velocity; does not check input units.
    """
    return velocity * time
```

Docstring에 입력 조건을 적는 것만으로 실행 중 검사되는 것은 아니다. 함수의 검증 코드와 문서가 다르면 문서 자체가 오류 원인이 된다.

### 4.5.3 읽기 쉽고 검증 가능한 함수 인터페이스

B1 GC 함수는 `calculate_gc_fraction(sequence: str) -> float`라는 이름과 타입을 사용한다. 허용 입력은 비어 있지 않은 A/C/G/T 서열이며 소문자를 대문자로 정규화한다. 비율은 0에서 1 사이, 원본 입력은 보존한다. `N`과 공백 및 FASTA 헤더는 이번 버전에서 지원하지 않는다.

$$f_{\mathrm{GC}}=\frac{N_G+N_C}{N},\qquad 0\leq f_{\mathrm{GC}}\leq1$$

정상값 검증은 양 끝(0과 1), 중간값, 대소문자 처리의 예제를 포함하고, 오류 검증은 빈 문자열·모호 염기·자료형 오류를 포함한다. 테스트에서 수치 비교는 상황에 맞는 허용오차를 사용할 수 있다. 인터페이스의 모든 문장과 코드, 테스트가 서로 일치하는지가 핵심이다.

## 4.6 실습: DNA 서열 처리 함수

### 4.6.1 GC Content 계산

실습의 출발점은 DNA 서열 `ATGCGC`에서 G 두 개, C 두 개, 전체 여섯 개를 확인하여 GC 비율을 `4/6`으로 계산하는 것이다. 초기 절차적 구현은 간단하지만 소문자를 `0.0`으로 잘못 계산하고 빈 서열에서 0으로 나누는 문제가 있다. 계산을 함수로 분리하고 정규화 및 검증을 명시적으로 추가한다.

```python
sequence = 'ATGCGC'
gc_count = sequence.count('G') + sequence.count('C')
print(gc_count / len(sequence))  # 0.6666666666666666
```

백분율이 필요하다면 비율에 100을 곱하지만, 외부 함수 이름은 `fraction`이라는 결과 의미를 유지한다.

### 4.6.2 DNA 서열 검증

B1 함수의 정책은 다음과 같다. 문자열만 허용하고, 빈 입력과 공백·`N`·기타 문자를 거부하며, 소문자를 대문자로 변환한다. 유효하지 않은 문자열이면 `ValueError`, 자료형이 맞지 않으면 `TypeError`를 발생시킨다. 이 함수는 서열이 실험적으로 정확한지 판정하지 않는다.

```python
from b1_dna_analysis import validate_dna, calculate_gc_fraction

print(validate_dna('atgcgc'))            # ATGCGC
print(calculate_gc_fraction('atgcgc'))   # 0.6666666666666666
```

검증과 GC 계산은 분리하되 공개 계산 함수가 검증을 직접 호출하여 사용자가 누락하지 않도록 만든다.

### 4.6.3 기능별 함수 분리와 프로그램 재구성

**• 학습 단계의 코드와 최종 실행 파일 구별**

앞선 소절에 등장한 함수는 기능을 단계적으로 발전시키기 위한 교육용 중간 버전이다. 최종 사용 코드는 별도 제공하는 `b1_dna_analysis.py`를 기준으로 한다. 여러 버전의 `validate_dna()`나 `calculate_gc_fraction()`을 하나의 파일에 무심코 차례로 복사하면 나중 정의가 앞선 정의를 덮어쓸 수 있다. 따라서 학습용 예제와 표준 실행 파일을 구별하는 편이 안전하다.

**• 이중 검증을 줄이는 이유와 비용**

외부 공개 함수는 언제나 서열을 검증하도록 유지한다. 여러 분석 함수에서 이미 검증한 값을 재사용하는 경우에는 `_gc_fraction_from_validated()`처럼 제한된 내부 함수를 사용할 수 있다. 이 설계는 한 서열에서의 성능 향상을 과장하려는 목적이 아니라, **공개 경계의 안전성과 내부 책임 구분**을 보여준다. 내부 함수는 비어 있지 않은 대문자 A/C/G/T 서열이라는 사전조건에 의존하므로 외부에서 직접 호출하는 용도로 설명하지 않는다.

**• 오류로 중단하는 정책**

일괄 분석 중 한 시료가 잘못되었을 때 현재 구현은 즉시 예외를 발생시킨다. 유효한 다른 시료의 결과를 조용히 반환하면 전체 시료 집합과 분석 시료 집합이 달라질 수 있기 때문이다. 실제 연구에서는 실패 시료를 별도 기록하고 나머지를 처리하는 정책을 선택할 수 있지만, 그 경우 실패 목록과 이유를 함께 반환하도록 요구사항을 다시 정의해야 한다.



B1 완전 구현은 별도 실행 파일 **`b1_dna_analysis.py`**를 기준으로 한다. 다음 구성 요소를 사용한다.

| 구성 요소 | 책임 |
|---|---|
| `DNAResult` | 결과 Dictionary의 정적 타입 구조 설명 |
| `validate_dna()` | 서열 타입 검사, 정규화 및 허용 문자 검사 |
| `_gc_fraction_from_validated()` | 검증된 서열만 받아 GC 비율 계산 |
| `calculate_gc_fraction()` | 공개적으로 검증을 포함하는 GC 계산 |
| `summarize_dna()` | 식별자·길이·GC 결과 작성 |
| `analyze_sequences()` | 시료 순서대로 일괄 분석; 오류 시 중단 |
| `main()` | 입력 준비와 화면 출력 |

`analyze_sequences()`는 하나의 부적합한 서열을 만나면 분석을 중단하는 **Fail-Fast** 정책을 따른다. 잘못된 시료를 조용히 생략하면 원래 시료 집합과 분석 대상이 달라져 과학적 해석이 어려워진다. 상황에 따라 결측 시료를 별도로 기록하고 처리할 수 있지만 이는 별도의 명시적 요구사항이다.

파일을 저장한 뒤 다음과 같이 실행할 수 있다.

```bash
python b1_dna_analysis.py
python -m unittest -v test_b1_dna_analysis.py
```

예상 출력:

```text
ID         Length   GC fraction
sample_A       6        0.6667
sample_B       6        0.0000
sample_C       4        1.0000
sample_D       4        0.5000
```

`test_b1_dna_analysis.py`에는 정상값, 양 끝값, 소문자, 원본 보존, 빈 입력, 공백, `N`, 잘못된 자료형, 시료 순서, 실패 전파 등 **15개 테스트**가 들어 있다. 테스트의 통과는 지정된 조건에서의 기능 확인이지 모든 생물학적 입력에 대한 정확성의 증명은 아니다.

함수 중심 구조는 절차적 코드보다 책임과 검증 경계를 명확히 할 수 있지만 단순한 일회성 계산에는 과한 구조가 될 수도 있다. 추후 Chapter 6에서는 관련 상태와 동작을 객체로 표현하고, Chapter 8에서는 교체 가능한 인터페이스를 검토한다.

## 4.7 Chapter Summary — 계산을 독립적인 책임으로 분리하기

이 장에서는 다음 일곱 가지 원칙을 확인했다.

1. **책임:** 계산의 목적을 분명히 하는 함수 단위를 선택한다.
2. **인터페이스:** 위치·키워드 인수, 기본값, 반환 구조에서 과학적 의미를 드러낸다.
3. **계약:** 사전조건·사후조건과 계산 적용 범위를 구분한다.
4. **상태:** 전역 의존성, 입력 객체 변경, NumPy View 등의 부작용을 확인한다.
5. **문서화:** Type Hints와 Docstring에 타입, 단위, 모델 가정과 한계를 기록한다.
6. **검증:** 정상값·경계값·오류 입력과 계산 결과를 독립적으로 확인한다.
7. **점진적 추상화:** 단순한 계산을 무조건 여러 함수로 분리하지 않는다.

B1에서는 절차적 GC 계산을 재사용 가능한 공개 함수와 내부 계산 함수, 일괄 처리 및 출력 단계로 분리했다. 반면 오류 입력을 정상적인 `0.0`으로 반환하지 않고, 과학적 정책에 따라 예외를 명시하였다. **함수 중심 구조화는 코드를 여러 파일로 분산하는 것이 아니라 계산의 책임과 계약을 분명히 하는 설계 과정**이다.

Chapter 5에서는 한 단계 더 나아가 함수를 값으로 다루고, 고차 함수와 함수 합성, 상태 변경을 줄이는 데이터 처리 파이프라인을 살펴본다. 계산 핵심은 독립적으로 유지하되 파일·장비·출력과 같은 실제 부작용을 명확한 경계에서 관리하는 실용적인 함수형 프로그래밍으로 연결한다.
