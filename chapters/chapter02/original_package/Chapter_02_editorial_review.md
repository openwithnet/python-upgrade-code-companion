# Chapter 2. Python과 프로그래밍 패러다임

## Introduction

Chapter 1에서는 Python의 기본 자료구조와 NumPy 배열을 이용하여 과학적 데이터를 표현하고 계산하는 방법을 살펴보았다. 하지만 데이터를 올바르게 표현한다는 것만으로 좋은 프로그램이 완성되는 것은 아니다. 실험 자료를 읽고, 검증하고, 계산하고, 결과를 남기는 일련의 과정을 어떤 단위로 나누고 연결할 것인지도 중요하다.

예를 들어 흡광도에서 농도를 계산하는 동일한 문제라도 명령문을 순서대로 실행하는 스크립트, 계산을 독립적인 함수로 분리한 프로그램, 검량선 모델을 객체로 나타낸 프로그램으로 작성할 수 있다. 수학적 결과가 같더라도 재사용성, 상태 관리, 입력 검증과 확장 방식이 달라진다. **프로그래밍 패러다임(Programming Paradigm)**은 이러한 구조적 선택을 이해하기 위한 사고방식이다.

Python은 하나의 패러다임에 묶여 있지 않은 **다중 패러다임(Multi-Paradigm)** 언어이다. 이 장에서는 주요 패러다임의 관계를 이해하고, 공통 과학 문제를 여러 방식으로 표현해 본다. Chapter 3의 절차적 프로그래밍, Chapter 4–5의 함수·함수형 접근, Chapter 6–8의 객체지향과 인터페이스, Chapter 10의 패러다임 조합으로 이어지는 개념 지도이다.

## 2.1 프로그래밍 패러다임의 의미

### 2.1.1 프로그래밍 패러다임이란?

프로그래밍 패러다임은 프로그램을 작성하고 구성하는 기본 사고방식이다. 특정한 문법이나 라이브러리의 이름이 아니라, 어떤 요소를 중심으로 문제를 표현하고 해결하는가에 관한 관점이다. 명령형 접근에서는 실행 순서와 상태 변화가, 함수 중심 접근에서는 입력과 출력이 분명한 계산 단위가, 객체지향 접근에서는 상태·책임·협력 관계가 핵심이 된다.

다음은 세 측정값의 평균이라는 동일한 문제를 표현하는 예이다.

```python
measurements = [10.0, 12.0, 14.0]
total = 0.0
for value in measurements:
    total += value
average = total / len(measurements)
print(average)
```

예상 출력:

```text
12.0
```

계산 과정을 함수로 분리할 수도 있다.

```python
def calculate_mean(values):
    return sum(values) / len(values)

print(calculate_mean([10.0, 12.0, 14.0]))
```

예상 출력:

```text
12.0
```

NumPy의 집계 함수를 이용하면 반복 계산의 세부 구현을 라이브러리에 위임할 수 있다.

```python
import numpy as np
print(np.mean(np.array([10.0, 12.0, 14.0])))
```

예상 출력:

```text
12.0
```

세 접근은 같은 계산 결과를 만든다. 그러나 NumPy의 사용 자체를 별개의 프로그래밍 패러다임이라고 부르는 것은 적절하지 않다. 배열 프로그래밍은 다양한 패러다임과 결합할 수 있는 계산 표현 방식이다.

### 2.1.2 문법과 프로그래밍 방식의 차이

`if`, `for`, `while`, `def`, `class`는 Python이 제공하는 문법이다. 반면 패러다임은 그 문법으로 어떤 구조를 구성할 것인가에 관한 판단이다. `def`를 사용했다고 해서 프로그램 전체가 함수형 프로그래밍이 되는 것은 아니며, `class`를 선언했다고 좋은 객체지향 설계가 이루어지는 것도 아니다.

```python
def process_data(values):
    result = []
    for value in values:
        result.append(value * 2)
    return result

print(process_data([1, 2, 3]))
```

예상 출력:

```text
[2, 4, 6]
```

위 코드는 함수를 사용하지만 내부에서는 명령형 반복문으로 결과를 만든다. 반면 함수를 다른 함수에 전달하는 다음 표현은 고차 함수의 사용을 보여준다.

```python
def double(value):
    return value * 2

print(list(map(double, [1, 2, 3])))
```

예상 출력:

```text
[2, 4, 6]
```

어느 쪽도 단일 문법으로 프로그램 전체의 성격을 판정할 수 없다. 함수형 설계에서는 순수 함수와 부작용 관리, 객체지향 설계에서는 책임과 객체 관계, 절차적 설계에서는 작업 분해와 순서 제어가 중요하다.

### 2.1.3 문제 표현과 프로그램 구조

시간에 따른 입자의 궤적 계산은 순서와 상태 변화가 두드러진다. 실험 측정값의 필터링과 변환은 독립적인 함수로 표현하기 쉽다. 서로 다른 장비나 계산 모델을 관리하는 프로그램은 상태와 책임을 가진 객체를 필요로 할 수 있다. 하지만 이것은 배타적인 대응 관계가 아니다.

어떤 구조가 적합한지 판단할 때는 계산 순서의 중요성, 재사용 여부, 상태 변경의 위치, 교체할 알고리즘의 수, 입력·출력의 명확성, 테스트 가능성, 변경 영향 범위를 살펴야 한다. 좋은 설계는 패러다임의 이름을 많이 적용한 설계가 아니라 **문제의 복잡성에 맞는 구조를 선택한 설계**이다.

## 2.2 주요 프로그래밍 패러다임

프로그래밍 패러다임은 모두 같은 수준의 분류가 아니다. 예를 들어 절차적 프로그래밍은 명령형 프로그래밍의 대표적 구성 방식이며, 이벤트 기반 접근은 객체지향 또는 함수형 설계와 함께 사용될 수 있다.

### 2.2.1 Imperative와 Procedural

**명령형 프로그래밍(Imperative Programming)**은 컴퓨터가 무엇을 어떤 순서로 실행해야 하는지를 명시한다. 반복문, 조건문과 변수 상태의 변화가 중요한 수단이다.

```python
measurements = [10.0, 12.0, 14.0]
total = 0.0
for value in measurements:
    total += value
print(total)
```

예상 출력:

```text
36.0
```

**절차적 프로그래밍(Procedural Programming)**은 관련 명령을 절차 또는 함수로 조직한다. 명령형 접근을 배제하지 않고 구조화한다.

```python
def calculate_total(values):
    total = 0.0
    for value in values:
        total += value
    return total

print(calculate_total([10.0, 12.0, 14.0]))
```

예상 출력:

```text
36.0
```

실험 데이터 읽기 → 입력 검사 → 변환 → 수치 계산 → 결과 저장의 순서가 명확한 작업에 적합하다. 다만 전체를 하나의 거대한 절차로 작성하면 반복과 공유 상태, 변경의 영향이 커질 수 있다. Chapter 3에서는 이러한 문제를 구체적으로 다룬다.

### 2.2.2 Functional과 Object-Oriented

**함수형 프로그래밍(Functional Programming)**은 계산을 함수의 적용과 조합으로 표현하며, 순수 함수, 불변성 및 부작용 관리에 주목한다. 순수 함수는 같은 입력에 대해 같은 결과를 반환하고 외부에서 관찰 가능한 상태를 변경하지 않는다.

```python
def double(value):
    return value * 2

measurements = [10.0, 12.0, 14.0]
print(list(map(double, measurements)))
```

예상 출력:

```text
[20.0, 24.0, 28.0]
```

`map`이나 `lambda` 사용만으로 함수형 설계가 완성되지는 않는다. 실험 파일 읽기나 장비 제어에는 외부 세계와의 상호작용이 필요하므로, 계산의 핵심과 입출력·부작용을 구분하는 것이 실용적이다.

**객체지향 프로그래밍(Object-Oriented Programming)**은 상태와 동작을 객체 단위로 표현한다. 상태를 가진 모델, 관련 연산, 객체 간 책임과 협력이 중요하다.

```python
class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def describe(self):
        return f"{self.value} {self.unit}"

print(Measurement(25.3, "C").describe())
```

예상 출력:

```text
25.3 C
```

실제 측정 모델이라면 단위의 유효성, 측정 범위, 불확실성 등을 더 고려해야 한다. `class` 문법이 있다는 사실만으로 이런 책임이 올바르게 설계된 것은 아니다.

함수형 접근과 객체지향 접근은 함께 사용할 수 있다. 객체는 매개변수를 관리하고 독립 함수는 수치 계산을 수행하도록 구성하면 역할을 분리할 수 있다.

```python
def concentration_from_signal(signal, slope):
    return signal / slope

class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def calculate(self, signal):
        return concentration_from_signal(signal, self.slope)

print(Calibration(2.0).calculate(6.0))
```

예상 출력:

```text
3.0
```

### 2.2.3 Declarative, Event-Driven, Reactive

패러다임의 분류에는 서로 다른 축이 존재한다. 명령형과 선언형은 계산의 *방법*과 *목표*를 어느 정도 명시하는지를 대비하는 관점이며, 이벤트 기반과 반응형은 계산이 *언제 시작되고 변화에 어떻게 대응하는지*를 강조한다. 따라서 선언형 코드도 이벤트가 발생한 후 실행될 수 있고, 객체지향 프로그램도 반응형 데이터 흐름을 포함할 수 있다.



**선언형 프로그래밍(Declarative Programming)**은 원하는 결과나 조건을 표현하고 실행 세부사항의 일부를 시스템에 맡긴다. SQL의 데이터 질의가 대표적이다. NumPy의 `np.mean(values)` 역시 반복 구현을 감추고 계산 의도를 높은 수준에서 표현하는 선언형 *스타일*로 볼 수 있지만, NumPy 사용만으로 별도의 패러다임이 확정되는 것은 아니다.

**이벤트 기반 프로그래밍(Event-Driven Programming)**은 장비의 데이터 도착, 버튼 클릭, 계산 완료 등 사건이 발생하면 등록된 처리 작업을 수행하는 방식이다.

```python
def on_measurement_received(value):
    print(f"Received: {value}")

# 이벤트 발생을 직접 호출로 모의한다.
on_measurement_received(25.3)
```

예상 출력:

```text
Received: 25.3
```

이 예제는 이벤트 처리 함수를 보여줄 뿐, 실제 이벤트 루프나 콜백 등록 시스템을 구현한 것은 아니다.

**반응형 프로그래밍(Reactive Programming)**은 시간에 따라 달라지는 값과 데이터 흐름, 그 변화가 다른 계산에 전파되는 구조를 강조한다. 단순한 주기적 반복문과 동일한 개념은 아니다. 새로운 온도 측정값에 따라 이동 평균과 경고 상태가 갱신되는 시스템을 떠올릴 수 있다. 이벤트 기반 접근과 반응형 접근은 관련되어 있지만 동일하지 않다.

### 2.2.4 Logic-Based와 Rule-Based

논리 기반 프로그램에서 사실과 관계를 기술하는 일은 일반적인 Python의 `if`문 작성과 다르다. Prolog와 같은 논리 프로그래밍 환경에서는 질의에 대한 답을 찾기 위해 추론을 활용한다. 한편 규칙 기반 시스템은 여러 조건 규칙의 충돌, 적용 순서와 우선순위를 별도로 관리할 수 있다. 조건문 한 개를 작성한 예제는 이러한 접근의 *출발 개념*이지 완전한 추론 엔진이나 규칙 엔진이 아니다.



**논리 기반 프로그래밍(Logic-Based Programming)**은 사실과 논리적 관계를 기술하고 질의를 통해 결론을 구한다. Prolog가 대표적인 예이다. **규칙 기반 프로그래밍(Rule-Based Programming)**은 특정 조건에 따라 결론이나 동작을 적용하는 규칙을 중심으로 한다.

```python
def classify_temperature(value):
    if value > 37.0:
        return "HIGH"
    return "NORMAL"

print(classify_temperature(38.2))
```

예상 출력:

```text
HIGH
```

37.0은 교육용 임계값이며 의학적 판단 기준이 아니다. 위 예는 일반적인 조건문의 규칙 표현으로, 별도 규칙 엔진이 있는 시스템을 의미하지는 않는다. 규칙 시스템을 확장할 때는 규칙의 충돌과 우선순위, 적용 범위를 다루어야 한다.

| 패러다임 | 중심 관점 |
|---|---|
| Imperative | 명령과 상태 변화 |
| Procedural | 절차와 작업 단위 |
| Functional | 함수 적용과 합성 |
| Object-Oriented | 객체의 상태, 책임, 협력 |
| Declarative | 원하는 결과와 조건 |
| Event-Driven | 사건 발생과 처리 |
| Reactive | 데이터 변화와 흐름 |
| Logic-Based | 사실과 논리적 관계 |
| Rule-Based | 조건과 규칙의 적용 |

## 2.3 Python의 Multi-Paradigm 특성

### 2.3.1 하나의 언어에서 여러 패러다임 사용하기

과학 프로그램에서는 입력과 출력의 흐름을 절차적으로 관리하고, 핵심 계산을 함수로 정의하며, 모델 매개변수를 객체로 관리할 수 있다. 여러 문법을 함께 사용했다는 사실보다 각 구성 요소의 책임이 분명한지가 중요하다.

원점을 지나는 선형 검량선에서 측정 신호 $A$와 농도 $c$의 관계를 다음과 같이 가정한다.

$$A=kc$$

따라서 기울기 $k$가 0이 아닐 때 농도는 다음과 같다.

$$c=\frac{A}{k}$$

```python
def calculate_concentration(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def concentration_from_signal(self, signal):
        return calculate_concentration(signal, self.slope)

calibration = Calibration(slope=2.0)
print(calibration.concentration_from_signal(6.0))
```

예상 출력:

```text
3.0
```

독립 함수는 계산을 담당하고 객체는 검량선 기울기를 관리하며, 호출 부분은 실행 순서를 맡는다. 그러나 기울기 하나만 다룰 때 반드시 클래스를 도입해야 하는 것은 아니다. 구조의 가치는 문제 요구사항과 변경 가능성에 따라 판단한다.

### 2.3.2 동일한 계산 문제의 서로 다른 표현

이 절의 네 표현은 **비교를 위한 간략한 미리보기**이다. 과학적 가정과 입출력 데이터는 고정한 채 코드의 조직 방식만 바꾼다. 데이터 단위, 오류 처리, 계산 모델의 경계 조건까지 포함한 하나의 연속 실습은 2.4에서 진행한다. 따라서 두 절에서 같은 농도 모델이 반복되는 것은 의도된 반복이다.



공통 조건은 측정 신호 `[2.0, 4.0, 6.0]`, 기울기 `2.0`, 기대 농도 `[1.0, 2.0, 3.0]`이다.

**절차적 표현**은 계산 순서를 직접 드러낸다.

```python
signals = [2.0, 4.0, 6.0]
slope = 2.0
concentrations = []
for signal in signals:
    concentrations.append(signal / slope)
print(concentrations)
```

예상 출력:

```text
[1.0, 2.0, 3.0]
```

**함수 중심 표현**은 계산 규칙을 재사용할 수 있도록 만든다.

```python
def concentration_from_signal(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

signals = [2.0, 4.0, 6.0]
concentrations = [concentration_from_signal(x, 2.0) for x in signals]
print(concentrations)
```

예상 출력:

```text
[1.0, 2.0, 3.0]
```

**객체 중심 표현**은 모델 매개변수와 계산 동작을 함께 관리한다.

```python
class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def calculate(self, signal):
        return signal / self.slope

calibration = Calibration(2.0)
print([calibration.calculate(x) for x in [2.0, 4.0, 6.0]])
```

예상 출력:

```text
[1.0, 2.0, 3.0]
```

**NumPy 배열 표현**은 원소별 연산을 사용한다.

```python
import numpy as np
signals = np.array([2.0, 4.0, 6.0], dtype=np.float64)
print(signals / 2.0)
```

예상 출력:

```text
[1. 2. 3.]
```

네 방법은 수학적으로 같은 계산이지만 프로그램의 구성 원리는 다르다. 배열 중심 계산은 함수 안에서도 객체 메서드 안에서도 활용할 수 있다.

### 2.3.3 패러다임 혼합의 장점과 한계

혼합의 이점은 문법의 다양성이 아니라 책임 분담에 있다. 함수는 수치 계산을 담당하고, 객체는 변경되거나 유지되어야 하는 설정을 담당하며, 실행 흐름은 입력·계산·출력의 순서를 담당할 수 있다. 반대로 동일한 검증을 여러 곳에서 중복하거나, 함수가 전달받은 배열을 예고 없이 변경하거나, 단순 계산을 수많은 클래스에 나누면 패러다임을 혼합해도 설계는 나빠진다.

객체가 가진 속성이 외부에서 수정 가능한 경우에는 계산 결과도 달라질 수 있다. 반면 입력만으로 결과가 정해지는 계산 함수는 개별적으로 시험하기 편리하다. 이러한 구분은 상태 변경과 재현성을 관리해야 하는 과학 프로그램에서 특히 중요하다.



장점은 문제에 맞는 역할 분담이다. 절차적 코드는 입출력과 실행 순서를 관리하고, 함수는 독립 계산과 테스트를, 객체는 모델의 상태와 책임을 관리할 수 있다. 각 단위를 잘 분리하면 계산 알고리즘이나 모델을 교체하기도 쉬워진다.

한계는 불필요한 복잡성과 상태 변경의 불투명성이다. 짧은 수식 하나에 여러 클래스와 추상화를 도입하면 오히려 코드를 이해하기 어려워진다. 또한 전달받은 배열을 직접 변경하는 함수는 다른 계산에 영향을 준다.

```python
import numpy as np

def scale_inplace(values, factor):
    values *= factor

data = np.array([1.0, 2.0, 3.0])
scale_inplace(data, 2.0)
print(data)
```

예상 출력:

```text
[2. 4. 6.]
```

원본 보존이 필요하면 새로운 배열을 반환하도록 작성할 수 있다.

```python
import numpy as np

def scaled(values, factor):
    return values * factor

data = np.array([1.0, 2.0, 3.0])
result = scaled(data, 2.0)
print(data)
print(result)
```

예상 출력:

```text
[1. 2. 3.]
[2. 4. 6.]
```

상태를 어느 구성 요소가 보관하는지, 입력값은 어디서 검증하는지, 계산을 어디서 수행하는지, 변경의 영향이 어디까지 미치는지 질문해야 한다. **하나의 패러다임에 문제를 맞추지 말고 문제에 적합한 구성을 선택한다.**

## 2.4 실습: 농도 계산 프로그램의 여러 표현

이번 절은 C1 Anchor Example의 첫 공식 실습이다. 동일한 수학 모델과 데이터를 절차적·함수 중심·객체 중심 프로그램으로 구현하여 구조의 차이를 확인한다. 예제는 모두 교육용 가상 데이터이며, 실험으로 확인된 검량선의 매개변수가 주어졌다고 가정한다.

일반적인 선형 검량선은 다음과 같다.

$$A=kc+b$$

여기서 $A$는 측정 신호, $c$는 농도, $k$는 기울기, $b$는 절편이다. $k\ne0$이면

$$c=\frac{A-b}{k}$$

이다. 이번 예제에서는 $b=0$, $k=2.0$을 가정한다. 농도 단위를 mmol/L, 흡광도를 무차원으로 놓으면 기울기의 단위는 L/mmol가 된다. 실제 데이터에는 검량 범위와 불확실성, 표준용액의 조건 등이 추가로 필요하다.

### 2.4.1 절차적 표현

이 실습에서 사용하는 기울기 `2.0`은 표준용액 데이터로부터 추정한 값이 아니라 **교육용으로 주어진 상수**이다. 또한 흡광도 측정 신호와 농도의 단위가 서로 일치하는 모델을 가정한다. 기울기가 양수라는 조건만 검사하므로, 입력 신호가 유효한 수치인지 또는 검량 범위 내부에 있는지까지 검사하지는 않는다.



```python
signals = [2.0, 4.0, 6.0]
slope = 2.0
if slope <= 0:
    raise ValueError("slope must be positive")

concentrations = []
for signal in signals:
    concentration = signal / slope
    concentrations.append(concentration)
print(concentrations)
```

예상 출력:

```text
[1.0, 2.0, 3.0]
```

실행 절차는 입력 준비 → 기울기 검증 → 측정값 반복 → 농도 계산 → 결과 저장 → 출력으로 이어진다. 계산의 흐름이 명확하므로 간단한 일회성 계산에는 충분하다. 반면 여러 위치에서 같은 계산을 수행하면 계산식과 검증을 중복 작성할 위험이 있다.

수학적으로 농도 계산에는 $k\ne0$이면 충분하다. 그러나 이 교육용 모델은 측정 신호가 농도에 따라 증가한다는 조건을 포함하므로 $k>0$을 요구한다. 과학 프로그램에서는 수학적 정의역과 모델의 과학적 허용 범위를 구분해야 한다.

### 2.4.2 함수 중심 표현

함수를 분리하면 입력조건을 한곳에서 관리할 수 있지만, *함수의 존재만으로 입력이 과학적으로 타당해지는 것은 아니다*. 예컨대 `float('nan')`이나 범위를 벗어난 신호를 다루는 계약은 현재 구현에 없다. 교육용 함수의 책임과 실제 분석 소프트웨어의 계약을 구분해야 한다.



```python
def concentration_from_signal(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

signals = [2.0, 4.0, 6.0]
concentrations = [concentration_from_signal(x, 2.0) for x in signals]
print(concentrations)
print([concentration_from_signal(x, 4.0) for x in signals])
```

예상 출력:

```text
[1.0, 2.0, 3.0]
[0.5, 1.0, 1.5]
```

함수는 계산의 책임을 분리한다. 이번 함수는 입력으로 신호와 기울기를 받고, 기울기가 양수임을 사전조건으로 요구하며, 농도 또는 `ValueError`를 반환한다. 반복되는 코드의 중복을 줄이고, 계산 하나를 독립적으로 테스트하기 쉬워진다.

```python
import math
assert math.isclose(concentration_from_signal(6.0, 2.0), 3.0)
```

일반적인 부동소수점 수치 비교에는 허용오차가 적절하다. 다만 단위, 신호의 수치적 유효성, 검량 범위, 실험적 불확실성까지 이 함수가 검증하는 것은 아니다. 함수 계약과 과학적 검증은 Chapter 4와 9에서 자세히 다룬다.

### 2.4.3 객체 중심 표현의 미리보기

객체가 관리하는 기울기는 같은 모델에 속하는 여러 관측값에서 반복해 이용된다. 이때 여러 객체가 각각 다른 기울기를 유지할 수 있으므로 모델별 설정을 관리하기 쉬워진다. 하지만 절편, 측정 범위, 불확실성을 고려하지 않은 이 객체는 아직 실제 검량선의 충분한 표현이 아니다.



```python
class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def concentration_from_signal(self, signal):
        return signal / self.slope

calibration = Calibration(slope=2.0)
signals = [2.0, 4.0, 6.0]
print([calibration.concentration_from_signal(x) for x in signals])

calibration_a = Calibration(2.0)
calibration_b = Calibration(4.0)
print(calibration_a.concentration_from_signal(8.0))
print(calibration_b.concentration_from_signal(8.0))
```

예상 출력:

```text
[1.0, 2.0, 3.0]
4.0
2.0
```

각 객체는 자신의 검량선 기울기를 관리한다. 여러 검량선 모델을 독립적으로 다뤄야 한다면 유용하지만, 계산 한 줄을 위해 객체를 무조건 만들 필요는 없다. 클래스는 책임과 상태를 조직하는 수단이지 더 고급스러워 보이기 위한 장치가 아니다.

**다중 패러다임 조합**에서는 객체가 기울기를 관리하고 독립 함수가 계산을 맡으며 절차적 코드가 여러 신호를 순차 처리할 수 있다.

```python
def calculate_concentration(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def calculate(self, signal):
        return calculate_concentration(signal, self.slope)

calibration = Calibration(2.0)
results = []
for signal in [2.0, 4.0, 6.0]:
    results.append(calibration.calculate(signal))
print(results)
```

예상 출력:

```text
[1.0, 2.0, 3.0]
```

같은 결과라는 사실은 다음과 같이 수치적으로 비교할 수 있다.

```python
import numpy as np
expected = np.array([1.0, 2.0, 3.0])
actual = np.array(results)
assert np.allclose(actual, expected)
```

그러나 이 테스트는 검량선 자체의 실험적 타당성이나 오차 전파를 검증하지 않는다. **코드 결과의 일치**와 **과학적 모델의 타당성**은 별개의 검증 대상이다.

| 기준 | 절차적 표현 | 함수 중심 표현 | 객체 중심 표현 |
|---|---|---|---|
| 계산식의 위치 | 실행 흐름 | 독립 함수 | 객체 메서드 |
| 매개변수 관리 | 일반 변수 | 함수 인수 | 객체 상태 |
| 강점 | 직접적이며 간결 | 재사용·단위 테스트 | 여러 모델의 상태 관리 |
| 주의점 | 반복 코드 증가 | 상태 관리 별도 고려 | 불필요한 추상화 |

C1은 Chapter 3의 처리 흐름, Chapter 4의 함수 계약, Chapter 6의 객체, Chapter 8의 인터페이스, Chapter 9의 검증, Chapter 11의 설계 패턴, Chapter 13의 SciPy 검량선 추정으로 발전한다. 완전한 화학 통합 예제는 향후 OpenWith의 온라인 동반 실습으로 제공할 계획이다. 책의 최종 Chapter 17은 물리학의 조화진동자(P2)를 중심 통합 사례로 사용한다.

## 2.5 Chapter Summary — 패러다임을 선택한다는 것

프로그래밍 방식의 선택은 한 번으로 끝나는 결정이 아니다. 짧은 계산을 절차적으로 시작했다가, 반복되는 부분이 드러나면 함수로 분리하고, 여러 매개변수와 교체 가능한 모델을 관리해야 할 때 객체 및 인터페이스를 도입할 수 있다. 이 책은 이처럼 **요구사항에 따라 구조를 점진적으로 발전시키는 과정**을 따른다.



Chapter 2에서는 문법과 설계 관점을 구분하고, Python에서 여러 패러다임을 선택·조합하는 방법을 살펴보았다. 절차적 접근은 실행 순서와 작업 단계, 함수 중심 접근은 계산 책임과 재사용, 객체지향 접근은 상태와 관련 동작을 조직하는 데 유용하다. 선언형·이벤트 기반·반응형·논리 기반·규칙 기반 접근은 다른 차원에서 문제를 바라보는 수단이며 서로 완전히 배타적이지 않다.

C1 실습에서 같은 선형 농도 계산을 세 방식으로 표현했다. 계산 결과는 일치하지만 데이터와 계산이 배치된 위치가 달랐다. 중요한 것은 방법의 이름이나 클래스의 수가 아니라, 현재 문제를 가장 명확하게 표현하고 변화와 검증을 지원하는가이다.

**구체적인 문제를 먼저 해결하고, 필요한 시점에 추상화한다(Concrete First, Abstraction Later).** 프로그램의 계산 순서, 재사용 여부, 상태의 소유자, 알고리즘 교체, 오류 검증, 변경의 영향 범위를 기준으로 선택해야 한다. 단순한 작업에는 간단한 스크립트가 적합할 수 있으며, 요구사항이 증가하면 함수와 객체, 인터페이스를 필요한 만큼 도입한다.

다음 Chapter 3에서는 물리학의 입자 궤적(P1) 사례를 중심으로 절차적 Python 프로그램을 구조화한다. 입력·계산·출력의 단계, 상태 변화와 반복 작업을 분리하면서 유지보수와 검증이 가능한 프로그램으로 발전시키는 것이 다음 학습의 목표이다.
