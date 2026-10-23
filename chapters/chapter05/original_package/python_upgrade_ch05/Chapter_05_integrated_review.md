# Chapter 5. 함수형 프로그래밍과 데이터 처리 파이프라인

**Python 3.14.x 기준 · Canonical Detailed TOC v1.2 · C2 화학 반응속도**  
**원고 상태: RECONSTRUCTED INTEGRATED REVIEW / NOT FROZEN**

> 편집 고지: 이 통합 검토본은 채팅에서 작성한 Chapter 5의 5.1–5.8 구성과 핵심 논증, 주요 수식 및 실습을 토대로 새로 정리한 원고이다. 채팅 본문 모든 문장을 기계적으로 일대일 추출한 무손실 원문 복제본은 아니다. 해당 차이를 최종 동결 전 원고 대조 항목으로 남긴다.

## Canonical Detailed TOC

- **5.1 함수형 프로그래밍의 사고방식**: 5.1.1 계산을 함수의 조합으로 표현하기 · 5.1.2 Pure Function · 5.1.3 Side Effect와 Immutability
- **5.2 함수를 값으로 다루기**: 5.2.1 First-Class Function · 5.2.2 Higher-Order Function · 5.2.3 lambda와 익명 함수
- **5.3 데이터 변환 함수**: 5.3.1 `map` · 5.3.2 `filter` · 5.3.3 `reduce`
- **5.4 함수 합성과 Closure**: 5.4.1 Function Composition · 5.4.2 Closure와 자유 변수 · 5.4.3 함수형 파이프라인 구성
- **5.5 반복 가능한 데이터와 지연 계산**: 5.5.1 Iterable과 Iterator · 5.5.2 Generator와 `yield` · 5.5.3 Lazy Evaluation
- **5.6 과학 데이터의 함수형 처리**: 5.6.1 NumPy와 순수 함수 · 5.6.2 데이터 변환 단계의 분리 · 5.6.3 함수형 접근의 장점과 한계
- **5.7 실습: 화학 반응속도 데이터 처리**: 5.7.1 반응속도 계산 함수 · 5.7.2 데이터 변환 파이프라인 · 5.7.3 결과 검증과 함수 합성
- **5.8 Chapter Summary**

## Introduction

과학적 데이터 분석은 입력값을 읽고, 유효성을 검증하고, 필요한 변환을 수행한 뒤 결과를 해석하는 과정이다. 절차적 프로그래밍에서는 명령문의 순서가 중심이며, 함수 중심 설계에서는 계산을 독립적인 책임으로 나눈다. 함수형 프로그래밍은 더 나아가 **값의 변환과 함수의 조합**을 중심으로 계산 흐름을 표현한다. 여기서 중요한 점은 Python을 순수 함수형 언어처럼 사용하는 것이 아니라, Scientific Python의 요구에 맞춰 프로그램을 설계하는 것이다.

하나의 함수에 모든 일을 담으면 재사용과 검증이 어려워진다. 반대로 단순한 계산을 의미 없이 수십 개의 작은 함수로 나눠도 수학적 관계가 감춰진다. 좋은 설계는 독립적으로 검증할 단위와 함께 관찰해야 할 중간 결과를 식별하는 데서 출발한다. 화학 분석의 배경 신호 보정, 검량선 적용, 반응속도 계산은 각각 다른 계약을 갖고 있으며 그 순서도 결과의 일부이다.

이 장에서는 순수 함수, 일급 함수, 고차 함수, 함수 합성, 클로저, 반복자와 생성기, NumPy 배열 처리의 결합을 학습하고, 마지막에 C2 화학 반응속도 프로그램으로 정리한다. 모든 코드가 함수형으로 표현되어야 한다는 규칙은 채택하지 않는다. 복잡한 상태 갱신, 다중 배열 정렬, 파일·장비 입출력에서는 일반적인 반복과 명시적 제어가 더 적합할 수 있다.

## 5.1 함수형 프로그래밍의 사고방식

### 5.1.1 계산을 함수의 조합으로 표현하기

측정 신호 $A$에서 배경 신호 $b$를 제거하고 검량선 기울기 $k$로 나누면 농도를 추정할 수 있다. 이번 단순 모델은 다음과 같다.

$$A_{\mathrm{corrected}}=A-b$$

$$c=\frac{A_{\mathrm{corrected}}}{k}$$

변환 단계를 수학적으로 표현하면 $f(A)=A-b$, $g(A)=A/k$이므로 $(g\circ f)(A)=g(f(A))=(A-b)/k$이다. 다음 코드는 두 단계의 의미를 이름으로 표현한다.

```python
def subtract_background(signal, background):
    return signal - background

def signal_to_concentration(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

corrected = subtract_background(7.0, 1.0)
concentration = signal_to_concentration(corrected, 2.0)
print(concentration)  # 3.0
```

반드시 중첩 호출을 사용할 필요는 없다. 중간 변수를 남기면 각 변환 결과와 단위를 확인하기 쉽다. 순서를 바꾸면 일반적으로 계산이 달라진다. 실제 검량선이 $A=kc+b_0$라면 기기 배경 $b$와 회귀 절편 $b_0$를 동일한 값처럼 취급하지 않아야 한다. 함수 합성은 계산식뿐 아니라 과학적 가정의 연결이다.

### 5.1.2 Pure Function

순수 함수(Pure Function)는 같은 입력에서 같은 결과를 내고 외부에 관찰 가능한 부작용을 일으키지 않는다. `square(x)`나 `celsius_to_kelvin(x)`는 기본적인 예이다. 계산에 필요한 기울기를 전역 변수에서 읽으면 동일한 명시 인수라도 다른 결과가 생길 수 있다. 기울기를 매개변수로 전달하면 의존성이 드러난다.

```python
def scale_value(value: float, factor: float) -> float:
    return value * factor

assert scale_value(3.0, 2.0) == 6.0
```

순수 함수의 장점은 치환 가능성, 독립적인 테스트, 원본 보존이다. 그러나 순수성은 과학적 타당성이나 모든 환경에서의 비트 단위 동일성을 보장하지 않는다. 부동소수점 연산 순서와 병렬 집계, 난수 생성기 상태는 별도로 관리해야 한다.

### 5.1.3 Side Effect와 Immutability

`append()`나 NumPy의 `/=`는 원본 데이터를 변경할 수 있다. 파일 출력, 로깅, 장비 제어 역시 부작용이다. 상태 변경이 무조건 나쁜 것은 아니지만 외부에서 보이는 영향을 명시해야 한다. 원본 데이터가 연구의 기준 자료라면 변환 결과를 별도 객체로 반환하는 방법이 안전하다.

```python
def with_added_measurement(values, new_value):
    return values + [new_value]

original = [10.0, 12.0]
new_values = with_added_measurement(original, 14.0)
assert original == [10.0, 12.0]
assert new_values == [10.0, 12.0, 14.0]
```

그러나 수백만 원소의 배열을 매 단계에서 복사하면 메모리 부담이 커진다. 따라서 함수형 설계는 무조건적 복사 정책이 아니라, 어떤 단계에서 공유 데이터가 수정되는지 알 수 있는 명확한 경계를 마련하는 일이다.

## 5.2 함수를 값으로 다루기

### 5.2.1 First-Class Function

Python 함수는 변수에 할당하거나 자료구조에 저장할 수 있는 일급 객체이다. `operation = square`는 함수 객체를 연결하지만 `result = square(3)`은 함수를 실행한다. 과학 프로그램에서는 여러 모델을 동일한 인터페이스로 호출할 때 이 성질을 사용할 수 있다.

```python
import math

def zero_order_concentration(c0, rate_constant, time):
    return c0 - rate_constant * time

def first_order_concentration(c0, rate_constant, time):
    return c0 * math.exp(-rate_constant * time)

models = {"zero_order": zero_order_concentration,
          "first_order": first_order_concentration}
result = models["first_order"](10.0, 0.2, 5.0)
print(f"{result:.4f}")  # 3.6788
```

0차 반응에서 $k$의 단위는 농도/시간이고, 1차 반응에서는 시간의 역수이다. 두 함수의 매개변수 개수가 같더라도 동일한 수치 파라미터가 동일한 물리적 의미를 가지는 것은 아니다. 또한 0차 모델을 농도가 0 이하로 내려가는 시점까지 무제한 외삽해서는 안 된다.

### 5.2.2 Higher-Order Function

고차 함수는 함수를 입력받거나 함수를 반환한다. 데이터 순회 방식과 계산 규칙을 분리할 수 있고, 적분 알고리즘에 임의의 적분 대상 함수를 전달할 수도 있다.

```python
def transform_measurements(values, operation):
    return [operation(value) for value in values]

def square(value):
    return value * value

assert transform_measurements([1, 2, 3], square) == [1, 4, 9]
```

`functools.partial`로 기울기 같은 매개변수를 고정하면 인수 하나를 받는 변환 함수를 생성할 수 있다. 예를 들어 `partial(signal_to_concentration, slope=2.0)`이다. 수치 적분 역시 `integral(func, a, b, steps)`와 같은 함수 인터페이스가 계산 알고리즘과 수학 모델을 분리하는 대표적 예이다. 교육용 사다리꼴 방법의 $\int_0^1 x^2 dx$ 근삿값은 100구간에서 0.333350이다. 실무에서는 직접 구현의 검증 수준을 고려해 SciPy 같은 수치 라이브러리를 사용하는 편이 일반적이다.

### 5.2.3 lambda와 익명 함수

`lambda`는 짧은 함수를 이름 없이 표현한다. 정렬의 `key=lambda item: item[1]`처럼 일회성 규칙에 적합하다. 그러나 검량선 적용 범위, 입력 검증, 예외 정책, 단위 등을 문서화해야 하는 과학 함수는 일반적인 `def` 함수가 더 명확하다.

```python
observations = [("A", 3.2), ("B", 1.5), ("C", 2.8)]
ordered = sorted(observations, key=lambda item: item[1])
assert ordered[0][0] == "B"
```

## 5.3 데이터 변환 함수

### 5.3.1 `map`

`map(function, iterable)`은 반복 가능한 데이터의 각 원소에 함수를 적용한다. Python 3에서 `map()`의 결과는 즉시 생성된 List가 아니라 반복자다. `list(map(...))`은 소비 시점에 결과를 생성한다.

```python
def celsius_to_kelvin(value):
    return value + 273.15

converted = list(map(celsius_to_kelvin, [0., 25., 100.]))
assert converted == [273.15, 298.15, 373.15]
```

다수의 반복 가능한 객체를 함께 `map`에 전달할 때에는 가장 짧은 입력에서 종료된다. 시료별 신호와 배경값을 일대일 대응시킨다면 길이와 시료 식별자를 검증해야 한다. 큰 NumPy 수치 배열의 단순 변환에서는 `array + 273.15` 같은 배열 연산이 일반적으로 더 적합하다.

### 5.3.2 `filter`

`filter(predicate, iterable)`는 조건을 만족하는 원소를 고른다. `None`과 유효한 `0.0`을 같은 결측값으로 취급하지 않아야 한다. 또한 음수 배경 보정 결과가 항상 오류인 것은 아니다. 어떤 관측치를 제외할지는 측정 모델과 분석 정책에 달려 있다.

```python
import math

def is_finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)

observations = [3.0, None, 0.0, float("nan"), 7.0]
valid = list(filter(is_finite_number, observations))
assert valid == [3.0, 0.0, 7.0]
```

필터링을 통해 표본이 줄어들면 통계적 해석도 달라질 수 있다. 실제 분석에서는 제외된 데이터의 식별자와 원인을 기록하고 분석에 사용된 모집단을 분명히 해야 한다.

### 5.3.3 `reduce`

`functools.reduce()`는 누적 상태 $a_i$와 다음 데이터 $x_i$를 이용해 $a_{i+1}=f(a_i,x_i)$를 구성한다. 합계처럼 목적이 분명한 작업에는 `sum()`이 간결하지만 복합 상태를 누적할 때에는 교육적으로 유용하다.

```python
from functools import reduce

def add_to_summary(state, value):
    total, count = state
    return total + value, count + 1

total, count = reduce(add_to_summary, [10., 12., 14.], (0., 0))
assert (total, count) == (36., 3)
```

비어 있는 데이터에서 평균을 계산할 때의 정책, 부동소수점 누적 오차, 누적 상태의 변경 가능성을 별도로 고려해야 한다. `reduce()`는 상태를 없애는 것이 아니라 **상태 전이를 함수의 입력과 반환값으로 드러내는 기법**이다.

## 5.4 함수 합성과 Closure

### 5.4.1 Function Composition

합성 관계는 $(g\circ f)(x)=g(f(x))$이다. 배경 보정 뒤 검량선을 적용하는 계산과 그 반대는 대개 같지 않다. 앞 단계의 출력과 뒤 단계의 입력이 자료형뿐 아니라 단위·차원·과학적 의미까지 일치해야 한다.

```python
def compose(outer, inner):
    def composed(value):
        return outer(inner(value))
    return composed

correct = lambda value: value - 1.0
convert = lambda value: value / 2.0
analysis = compose(convert, correct)
assert analysis(7.0) == 3.0
```

수학적으로 동일한 경우가 아니면 계산 단계를 임의로 재배열하지 않는다. 또한 중간 결과를 검증해야 할 때에는 억지로 중첩 함수를 만들기보다 단계별 이름을 유지한다.

### 5.4.2 Closure와 자유 변수

클로저는 중첩 함수가 둘러싸는 범위에 있는 자유 변수와의 연결을 유지하는 구조이다. 검량선 기울기·절편이나 반응속도 상수를 적용한 함수를 생성하는 데 유용하다.

```python
def make_scaler(factor):
    def scale(value):
        return value * factor
    return scale

assert make_scaler(2.0)(5.0) == 10.0
```

자유 변수가 가변 상태를 참조하면 클로저 결과도 그 변경에 영향을 받을 수 있다. 반복문 안에서 `lambda x: x * factor`를 여러 개 만들면 마지막 `factor`를 함께 참조하는 늦은 바인딩 문제가 생길 수 있다. 함수 생성기를 따로 작성하거나 `lambda x, factor=factor: ...`처럼 생성 시점 값을 고정한다.

### 5.4.3 함수형 파이프라인 구성

값 하나를 받아 값 하나를 내놓는 단계들이라면 순서대로 적용하는 파이프라인을 작성할 수 있다.

```python
def make_pipeline(*steps):
    def run(value):
        for step in steps:
            value = step(value)
        return value
    return run

pipeline = make_pipeline(lambda x: x - 1., lambda x: x / 2.)
assert pipeline(7.) == 3.
```

그러나 시간 배열과 농도 배열을 함께 사용하는 반응속도 분석에는 이처럼 단일 수치 인터페이스만으로 충분하지 않다. 그 경우에는 `analyze_kinetics(times, concentrations)`처럼 여러 입력을 명시적으로 받는 조정 함수가 더 자연스럽다. 또한 파이프라인을 구현했다고 데이터 출처(Provenance), 오류 단계, 사용한 매개변수가 자동 기록되지는 않는다.

## 5.5 반복 가능한 데이터와 지연 계산

### 5.5.1 Iterable과 Iterator

Iterable은 순회 가능한 객체이며 Iterator는 `next()` 호출에 따른 진행 상태를 관리한다. List는 새 반복자를 얻어 다시 순회할 수 있지만 일반적인 반복자·생성기는 소비한 값을 다시 제공하지 않는다.

```python
values = [10., 12., 14.]
it = iter(values)
assert next(it) == 10.
assert next(it) == 12.
```

`map()`과 `filter()`도 반복자를 반환한다. 첫 번째 `list(iterator)`가 모든 값을 소비하면 두 번째 결과는 빈 List일 수 있다. 같은 데이터를 여러 차례 분석하려면 새로운 반복자를 만들거나 저장 전략을 결정해야 한다.

### 5.5.2 Generator와 `yield`

생성기 함수는 `yield`로 값을 내보내고 실행 위치와 지역 상태를 유지한다. 호출만으로 함수 본문 전체가 실행되지는 않으며 첫 `next()` 때까지 검증도 지연될 수 있다.

```python
def generate_times(time_step, steps):
    if time_step <= 0 or steps < 0:
        raise ValueError("invalid generation settings")
    for index in range(steps + 1):
        yield index * time_step

assert list(generate_times(.5, 4)) == [0., .5, 1., 1.5, 2.]
```

위 검증은 생성기를 처음 순회할 때 실행된다. 호출 시점을 기준으로 오류가 즉시 발생해야 한다면 외부 일반 함수에서 검증하고 내부 생성기를 반환하도록 설계할 수 있다. 파일을 열어 둔 생성기는 중간에 사용을 중단할 때 자원 해제 시점도 고려한다.

### 5.5.3 Lazy Evaluation

지연 계산은 필요한 시점에 데이터 처리 일부를 실행함으로써 중간 List를 줄인다. 긴 실험 로그, 대규모 CSV 파일, 순차적으로 도착하는 측정값의 처리에 유용하다. 그러나 속도를 반드시 높이지는 않는다. NumPy 벡터화는 원소별 Python 생성기보다 빠를 수 있다.

B2 유전자 발현 행을 순차 처리할 때는 0과 결측값의 구분, 카운트·정규화·로그변환 데이터별 허용 범위, 파일의 수명과 종료 처리를 함께 고려한다. 한 번의 순회만으로 계산 가능한 분석과 반복 접근이 필요한 분석에 동일한 방식을 강제하지 않는다.

## 5.6 과학 데이터의 함수형 처리

### 5.6.1 NumPy와 순수 함수

NumPy의 배열 연산은 함수형 구조와 조합할 수 있지만 두 개념은 동일하지 않다. 벡터화는 실행 방식, 순수성은 관찰 가능한 상태 변경에 관한 것이다.

```python
import numpy as np

def subtract_background(signals: np.ndarray, background: float) -> np.ndarray:
    return signals - background

original = np.array([3., 5., 7.])
corrected = subtract_background(original, 1.)
np.testing.assert_array_equal(original, [3., 5., 7.])
np.testing.assert_array_equal(corrected, [2., 4., 6.])
```

반면 `signals -= background`는 원본을 변경한다. `numpy.typing.NDArray[np.float64]`는 원소 자료형의 의도를 표현할 수 있지만 차원, 유한성, 단위, 검량선 적용 범위를 실행 시 자동 검사하지 않는다.

### 5.6.2 데이터 변환 단계의 분리

일반적인 과학 분석은 입력 검증, 배경 보정, 농도 변환, 출력 검증을 단계별로 나누어 표현한다. 각 단계의 반환값은 다음 단계의 계약을 만족해야 한다. C2의 구간별 속도는 다음과 같다.

$$r_i=-\frac{C_{i+1}-C_i}{t_{i+1}-t_i}$$

`np.diff()`로 시간과 농도의 인접 차이를 얻고 나눗셈을 수행한다. 이때 길이가 같고 적어도 두 시점이 있으며 시간이 엄격하게 증가해야 한다. 인접한 관측값의 대응을 확인해야 하므로 단순히 원소별 `map()`만 적용할 수는 없다.

### 5.6.3 함수형 접근의 장점과 한계

계산의 독립적 테스트, 다른 모델과의 교체, 원본 보존은 함수형 설계의 장점이다. 그러나 큰 배열을 매 단계 복사하면 메모리가 증가하고 복잡한 시뮬레이션의 상태 갱신은 명시적 반복문이 더 명확할 수 있다. 일반적인 과학계산에서는 핵심 수치 계산을 순수 함수로 구성하되, 입출력과 반복 제어를 필요에 따라 결합하는 혼합 구조가 실용적이다.

## 5.7 실습: 화학 반응속도 데이터 처리

### 5.7.1 반응속도 계산 함수

이번 C2 교육용 데이터는 다음과 같다.

| 시간 (min) | 농도 (mmol/L) |
|---:|---:|
| 0 | 10.0 |
| 1 | 8.2 |
| 2 | 6.7 |
| 3 | 5.5 |
| 4 | 4.6 |

순간 소모 속도는 $r(t)=-dC/dt$이고, 관측값으로부터의 구간 평균 속도는 $r_i=-\Delta C_i/\Delta t_i$이다. 결과는 `[1.8, 1.5, 1.2, 0.9]` mmol/(L·min)이다. 구간 중간 시점은 `[0.5, 1.5, 2.5, 3.5]` min으로 표시한다. 중간 시점에서 실제 순간 속도가 구간 평균 속도와 반드시 같지는 않다.

### 5.7.2 데이터 변환 파이프라인

전체 실행 코드는 별도 파일 `c2_kinetics_pipeline.py`에 보존하였다. 공개 호출 함수 `calculate_interval_rates()`는 자체 검증을 수행하고 `analyze_kinetics()`는 검증·계산·결과 구조화를 조정한다. 이중 검증 호출을 피하기 위해 조정 함수에서 직접 배열 차분을 계산하지만, 공개 API의 안전성과 수학적 계약은 유지한다.

```python
# c2_kinetics_pipeline.py에서 발췌한 호출 예
import numpy as np
from c2_kinetics_pipeline import analyze_kinetics

times = np.array([0., 1., 2., 3., 4.])
concentrations = np.array([10., 8.2, 6.7, 5.5, 4.6])
result = analyze_kinetics(times, concentrations)
print(result['interval_rate'])
# [1.8 1.5 1.2 0.9]
```

입력 계약은 일차원 실수형 수치 배열, 같은 길이, 두 관측 이상, 유한성, 0 이상의 시간과 농도, 엄격히 증가하는 시간이다. 이 계약은 교육용 비음수 농도 모형을 위한 것이며 모든 보정 농도에 적용되는 일반 규칙은 아니다. 파일은 사용된 시료의 동일성이나 단위를 자동 판정하지 않는다.

### 5.7.3 결과 검증과 함수 합성

1차 반응 모델은 다음과 같다.

$$\frac{dC}{dt}=-kC, \qquad C(t)=C_0e^{-kt}, \qquad r(t)=kC(t)$$

$C_0=10$ mmol/L와 $k=0.2$ min$^{-1}$의 모델 예측은 $t=0,1,2,3,4$ min에 각각 약 10.0000, 8.1873, 6.7032, 5.4881, 4.4933 mmol/L이다. 반면 관측 농도는 마지막 시점 4.6이다. 두 자료의 차이는 데이터와 모델의 불일치를 보여주지만, 관측 오차·매개변수 추정·적합도 평가 없이 모델의 과학적 적합성을 단정하지 않는다.

코드 검증에서는 구간 평균 소모 속도, 중간 시점, 출력 배열의 독립성, 원본 배열 보존, 중복 시간·길이 불일치·비유한 값·음수 농도·음수 반응속도 상수 등 오류를 검사한다. 실제 실행 출력과 테스트 내역은 `execution_output.txt`, `test_results.txt`에 기록되어 있다.

## 5.8 Chapter Summary

함수형 프로그래밍은 계산을 입력과 출력이 명확한 변환으로 구성하고, 함수를 값으로 전달하거나 합성하여 처리 흐름을 표현한다. 순수 함수는 독립적 검증에 유리하지만 과학적 정확성까지 보장하지 않는다. `map`, `filter`, `reduce`는 변환·선택·집계의 패턴을 보여주지만, 단순 수치 연산에서는 List Comprehension이나 NumPy가 더 적합할 수 있다.

클로저는 모델 매개변수를 가진 계산 함수를 만드는 데 도움이 된다. 생성기와 지연 계산은 자료를 조금씩 처리할 수 있게 하지만 일회성 소비, 늦은 예외 발생, 자원 해제를 고려해야 한다. NumPy 계산과 함수형 설계는 상호 보완적이다. 프로그램을 고도로 추상화하기보다 데이터의 과학적 의미, 단위, 연결 관계와 검증 가능성을 우선한다.

C2 사례에서는 구간 평균 소모 속도와 1차 반응 모델의 순간 속도·농도 예측을 구별했다. 기능별 책임을 분리하면서 NumPy 배열을 명시적 제어 함수에서 결합하는 구조를 택했다. **핵심은 함수형 문법을 많이 사용하는 것이 아니라, 계산을 이해하고 검증하며 재사용할 수 있도록 설계하는 것이다.** 이후 객체지향 프로그래밍은 이러한 함수들을 대체하기보다 데이터와 연관된 책임을 다른 방식으로 조직하는 도구가 된다.

---

**통합 검토 상태**: 이 원고는 교정·실행 검증용 재구성본이며, 원 대화 본문 전체와의 문장 단위 대조를 완료하지 않았다. 최종 원고의 완전한 본문 보존 확인 전에는 `FROZEN`으로 표시하지 않는다.
