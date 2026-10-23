# Part III. 객체와 객체지향 프로그래밍

## Part III Introduction

과학 프로그램은 계산식만으로 이루어지지 않는다. 측정 대상을 식별하고, 각 대상의 상태를 보관하며, 변화 규칙을 실행하고, 관측 이력을 추적해야 한다. 앞의 Part II에서 독립적인 함수와 데이터 처리 파이프라인을 학습한 이유도 계산의 책임을 명확하게 하기 위해서였다. 객체지향 프로그래밍(Object-Oriented Programming, OOP)은 여기에 **데이터의 소유와 상태 변경의 책임**이라는 관점을 추가한다.

입자의 위치·속도를 하나의 객체에 담을 수도 있고, DNA 서열의 식별자·염기서열·주석을 함께 관리할 수도 있다. 그러나 모든 계산을 메서드로 옮기는 것이 목적은 아니다. 수학적 모델은 순수 함수로 유지하고, 현재 상태와 기록의 수명은 객체에 맡기는 혼합 구조도 효과적이다. 이번 Part에서는 문제에 근거한 책임 분배를 출발점으로 삼는다.

# Chapter 6. 객체와 클래스: 상태와 책임

## Canonical Detailed TOC

- 6.1 객체지향 프로그래밍의 기본 개념
  - 6.1.1 객체와 클래스
  - 6.1.2 속성과 메서드
  - 6.1.3 `self`와 객체의 정체성
- 6.2 객체의 생성과 상태
  - 6.2.1 생성자와 초기화
  - 6.2.2 객체의 상태
  - 6.2.3 상태 변화와 객체의 동작
- 6.3 캡슐화와 책임
  - 6.3.1 Encapsulation
  - 6.3.2 상태 검증과 Property
  - 6.3.3 객체의 책임 분배
- 6.4 실용적인 클래스 설계
  - 6.4.1 dataclass
  - 6.4.2 함수와 클래스의 선택 기준
  - 6.4.3 상태 없는 계산과 상태 있는 객체
- 6.5 실습: Particle과 Trajectory
  - 6.5.1 입자 운동 모델과 객체 구조 설계
  - 6.5.2 Particle과 Trajectory의 통합 구현
  - 6.5.3 시뮬레이션 실행과 결과 검증
- 6.6 Chapter Summary — 상태와 책임의 관점에서 함수와 객체의 역할 정리

## Introduction

Chapter 3에서는 입자 운동의 계산 순서를 절차적으로 표현하였다. Chapter 4에서는 위치·속도·가속도·시간 간격을 입력받아 다음 상태를 반환하는 `euler_step()`을 독립 함수로 분리하였다. Chapter 5에서는 계산 함수의 합성과 불변성, 부작용 경계를 살펴보았다. 이제 같은 P1 모델에서 여러 입자의 **개별 상태**, 상태 변경 규칙, 시간에 따른 궤적을 조직한다.

명시적 Euler 방법의 핵심은 다음과 같다.

$$x_{n+1}=x_n+v_n\Delta t$$

$$v_{n+1}=v_n+a_n\Delta t$$

수학적 규칙은 객체를 도입한다고 바뀌지 않는다. 바뀌는 것은 위치와 속도를 어느 구성 요소가 관리하고, 계산 중 오류가 발생하면 현재 상태를 어떻게 보호하며, 시간에 따른 과거 상태를 누가 기록하는가라는 프로그램 구조이다.

## 6.1 객체지향 프로그래밍의 기본 개념

### 6.1.1 객체와 클래스

Python의 정수, 문자열, List 모두 객체이다. 객체는 정체성(Identity), 자료형(Type), 값(Value)을 가진다. 클래스는 객체가 가질 구조와 동작을 정의하며, `Particle()`은 클래스로부터 인스턴스를 생성하는 표현식이다. 같은 클래스에서 만들어졌다는 사실은 같은 객체라는 뜻이 아니다.

```python
class Particle:
    pass

particle_a = Particle()
particle_b = Particle()
assert particle_a is not particle_b
```

객체의 **정체성**은 값의 동등성과 구별된다. 같은 위치·속도를 갖는 두 입자 객체가 서로 다른 개별 시뮬레이션 대상일 수 있다. 반대로 두 변수 이름이 동일한 객체를 가리키면, 한 이름을 통한 상태 변경이 다른 이름에도 보인다. Python의 `id()`는 실행 중 객체 식별에 사용되는 값이지 영구적인 실험 시료 식별자가 아니다. 시료 ID나 입자 ID는 별도로 관리해야 한다.

객체지향 설계는 현실의 물체를 그대로 복제하는 작업도 아니다. 분자, 실험, 시간 기록, 반응 모델처럼 데이터와 책임을 일관된 단위로 표현할 필요가 있을 때 클래스를 선택한다. 한 줄짜리 수치 변환에는 클래스가 불필요할 수 있다.

### 6.1.2 속성과 메서드

속성(Attribute)은 객체에 연결된 데이터이며 메서드(Method)는 객체와 관련된 동작이다. 다음 교육용 예시는 위치와 속도를 보관하고 일정 속도 운동에서 미래 위치를 예측한다.

```python
class SimpleParticle:
    def __init__(self, position: float, velocity: float) -> None:
        self.position = position
        self.velocity = velocity

    def position_after(self, time: float) -> float:
        return self.position + self.velocity * time

    def advance(self, time_step: float) -> None:
        self.position = self.position_after(time_step)

p = SimpleParticle(1.0, 2.0)
assert p.position_after(3.0) == 7.0
assert p.position == 1.0
p.advance(3.0)
assert p.position == 7.0
```

`position_after()`는 상태를 읽고 계산하지만, `advance()`는 상태를 변경한다. 둘은 외부에서 관찰되는 부작용이 다르므로 인터페이스와 이름으로 구분한다. 이 예시는 검증과 가속도를 생략했으며, 최종 P1 구현은 이후 절에서 별도로 정의한다.

### 6.1.3 `self`와 객체의 정체성

인스턴스 메서드의 첫 매개변수 `self`는 현재 인스턴스를 참조하는 관례적 이름이다. `particle.position_after(3)`은 일반적인 인스턴스 메서드에서 개념적으로 `SimpleParticle.position_after(particle, 3)`에 대응한다. 다른 인스턴스를 통해 호출하면 같은 메서드 구현이 그 인스턴스의 상태를 읽는다.

```python
p1 = SimpleParticle(0.0, 1.0)
p2 = SimpleParticle(10.0, 3.0)
assert p1.position_after(2.0) == 2.0
assert p2.position_after(2.0) == 16.0
```

`is`는 동일 객체인지, `==`는 동등성 규칙에 따라 같은 값인지 비교한다. 일반 클래스는 별도 `__eq__()` 정의가 없으면 정체성에 근거하여 비교하는 반면, 기본 `dataclass`는 필드값 동등성을 제공한다. NumPy 배열이나 부동소수점 결과의 검증에는 자동 `==`보다 허용오차 비교가 적절할 수 있다.

## 6.2 객체의 생성과 상태

### 6.2.1 생성자와 초기화

객체 생성에는 일반적으로 `__new__()`와 `__init__()`이 관여한다. `__new__()`는 새 객체 생성, `__init__()`은 생성된 객체 초기화를 담당한다. 보통 사용자가 직접 구현하는 것은 `__init__()`이다. 이 메서드는 정상 완료 시 `None`을 반환해야 한다.

초기화는 단순한 대입이 아니라 **유효한 초기 상태를 보장하는 단계**이다. 위치와 속도는 방향에 따라 음수가 가능하지만, 이번 실습에서는 `nan`, 양·음의 무한대를 거부한다. `bool`은 Python의 정수 하위형이므로 수치 입력 정책에 맞지 않아 별도로 배제한다.

```python
import math

def require_finite_real(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return float(value)
```

Python 기본 정수와 실수만을 허용하는 교육용 계약이다. NumPy 스칼라나 임의의 실수 프로토콜까지 지원하려면 설계를 확장해야 한다. 초기화 시 기본값 `velocity=0`을 선택하면 이는 단순 편의가 아니라 정지 초기조건이라는 과학적 가정이다. 의미가 불분명하면 필수 인수로 유지해야 한다.

### 6.2.2 객체의 상태

일차원 입자 상태는 위치와 속도로 이루어진다.

$$\mathbf{s}(t)=\begin{bmatrix}x(t)\\v(t)\end{bmatrix}$$

클래스 수준의 속성과 개별 인스턴스 속성을 혼동하지 않아야 한다. 특히 `history=[]`를 클래스 속성으로 두면 다수의 입자가 동일한 List를 공유할 수 있다. 인스턴스별로 서로 다른 기록이 필요하면 `self.history=[]`와 같이 객체가 생성될 때마다 할당한다. 또한 현재 상태와 전체 이력은 다른 책임이다. 입자의 현재 상태는 `Particle`, 시간별 상태의 이력은 `Trajectory`에 맡기는 설계를 고려할 수 있다.

같은 인스턴스를 두 변수에 할당하는 것은 복제가 아니라 참조 공유다. 독립 상태를 유지하려면 새 객체 또는 불변 상태 객체를 만들어야 한다. 특히 중첩 List와 배열이 있으면 얕은 복사의 공유 여부를 검토해야 한다.

객체의 불변조건(Invariant)은 유효 상태에서 지속적으로 만족해야 하는 규칙이다. 여기서는 위치·속도의 유한성을 기본 조건으로 둔다. 질량을 도입한다면 양수 조건을 별도 정의할 수 있다. 모든 과학적 변수가 동일한 조건을 갖는 것은 아니다.

### 6.2.3 상태 변화와 객체의 동작

명시적 Euler 갱신은 현재 상태를 읽어 다음 상태를 계산한다. 속도를 먼저 바꾸고 그 새로운 속도로 위치를 갱신하면 앞서 정의한 명시적 Euler와 다른 알고리즘이 된다. 따라서 `next_position`과 `next_velocity`를 먼저 계산한 뒤 상태에 반영해야 한다.

상태를 변경하지 않는 `predict()`와 실제 변경을 수행하는 `advance()`는 구분한다. 예측 실패 시 이전 상태가 유지되도록 다음 상태 전체를 계산·검증한 뒤 교체한다. 다만 이를 다중 스레드의 트랜잭션 보장으로 해석해서는 안 된다. 수치 오차 또한 클래스와 별개의 문제이다. 일정 가속도에서 정확한 해는 다음과 같다.

$$x(t)=x_0+v_0t+\frac12at^2,\qquad v(t)=v_0+at$$

명시적 Euler는 위치에 근사 오차가 발생할 수 있으며 객체의 구조 변경만으로 그 오차가 해결되지는 않는다.

## 6.3 캡슐화와 책임

### 6.3.1 Encapsulation

캡슐화는 내부 구현과 공개 인터페이스를 구분하고 객체가 어떤 상태 변경을 허용하는지 정의하는 설계 원칙이다. Python의 `_position`은 내부 사용 관례를 나타내며 외부 접근을 기술적으로 막지 않는다. `__position`은 이름 변경(Name Mangling)의 대상이지만 보안 경계는 아니다. `__init__`과 같은 특수 메서드는 별도의 Python 프로토콜이다.

캡슐화의 목표를 모든 속성에 Getter·Setter를 기계적으로 만드는 것으로 이해하면 안 된다. 외부 조회가 필요하되 임의 변경은 부적절할 때 `@property`가 적합하다. 내부 수치 알고리즘을 바꿀 때에도 공개 계약에 포함된 수치 방법과 결과의 의미가 달라지는지 검토해야 한다.

### 6.3.2 상태 검증과 Property

다음과 같은 읽기 전용 Property는 값 조회를 허용하면서 공개 대입을 제한한다.

```python
class ReadOnlyParticle:
    def __init__(self, position: float) -> None:
        self._position = require_finite_real(position, "position")

    @property
    def position(self) -> float:
        return self._position
```

Setter를 추가하면 외부 변경 시 유효성 검사를 수행할 수 있지만, 과학적 갱신 절차의 준수까지 보장하는 것은 아니다. 이번 입자 모델에서는 `advance()`라는 명시적인 상태 변경 동작이 더 적절하다. 복수의 수치 필드를 별도로 변경하면 부분 상태가 노출될 수 있으므로, 불변 상태 객체 하나를 교체하는 접근을 사용할 수 있다.

읽기 전용 Property가 List나 NumPy 배열을 반환한다면 그 내용 자체는 여전히 수정 가능할 수 있다. 복사본, Tuple, 읽기 전용 View 등의 방식을 선택할 때 성능과 실제 불변성의 범위를 함께 검토해야 한다.

### 6.3.3 객체의 책임 분배

`Particle`이 현재 상태, 이력, CSV 저장, 그래프 작성, 수치 적분기, 전체 실행을 모두 담당하면 하나의 구성 요소에 변경 이유가 지나치게 집중된다. 단일 책임 원칙은 메서드 하나마다 클래스를 따로 만들라는 뜻이 아니라, 한 구성 요소에 일관된 변경 이유를 갖도록 하자는 취지이다.

이번 P1에서 책임은 `ParticleState`(한 시점의 상태), `euler_step()`(계산), `Particle`(현재 상태), `TrajectoryRecord`(시간과 상태의 쌍), `Trajectory`(기록 순서), `simulate_particle()`(실행 조정)으로 나눈다. 불필요한 Manager·Factory 계층은 추가하지 않는다. 간단한 실행은 함수로 충분하며 더 복잡한 실행 수명과 자원 관리가 요구될 때 별도의 시뮬레이션 객체를 검토할 수 있다.

## 6.4 실용적인 클래스 설계

### 6.4.1 dataclass

`@dataclass`는 선언된 필드에서 초기화·표현·동등성 메서드 등을 생성한다. 데이터 구조의 표현에 유리하지만 Type Hints를 실행 중 검사하지는 않는다. 유효성 검증은 `__post_init__()`에서 수행할 수 있다. `frozen=True`는 정상적인 필드 변경을 제한하여 값 객체를 표현하는 데 도움이 되지만, 참조된 가변 객체 내부까지 깊게 동결하지 않는다.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point1D:
    position: float
    def __post_init__(self) -> None:
        object.__setattr__(self, "position", require_finite_real(self.position, "position"))
```

값의 동등성 `==`가 자동 생성되어도 실수 계산의 비교에는 `math.isclose()` 등이 필요한 경우가 있다. NumPy 배열 필드에 대해 자동 `__eq__()`는 의도대로 작동하지 않을 수 있다. List 같은 가변 기본 필드에는 `field(default_factory=list)`를 사용하여 인스턴스별 별도 값을 생성한다.

### 6.4.2 함수와 클래스의 선택 기준

독립적인 식 `r=kC`, 단위 변환, 수치 적분의 한 단계는 순수 함수가 자연스럽다. 반면 상태값과 동작의 수명을 함께 관리하거나 불변조건을 지킬 책임이 있는 구성 요소는 클래스를 고려한다. B1 DNA 서열에서도 GC 계산은 함수로, 식별자와 검증된 염기서열을 함께 표현할 때에는 `DNASequence` 같은 값 객체로 나눌 수 있다. 모호 염기 `N`을 허용할지는 과학 데이터 정책으로 정해야 한다.

객체를 사용할 이유가 단지 함수를 묶는 이름 공간이라면 모듈과 함수만으로 충분한지 먼저 검토한다. 데이터가 `float`라는 이유로 단위가 맞거나 과학적으로 올바른 입력이라는 뜻은 아니다.

### 6.4.3 상태 없는 계산과 상태 있는 객체

불변 `ParticleState`는 시간 단계의 위치와 속도를 함께 표현한다. `euler_step()`은 기존 상태를 변경하지 않고 다음 상태를 반환한다. `Particle`은 현재 상태를 가리키는 참조를 보유하고 `advance()`에서 검증된 새 상태를 교체한다. 이로써 **불변 데이터 객체 + 독립 계산 함수 + 상태 관리 객체**를 결합한다.

대량의 입자를 개별 Python 객체로 생성하는 것은 메모리·실행 오버헤드가 발생할 수 있다. 대규모 문제에서는 NumPy 배열이나 다른 수치 자료구조가 효율적일 수 있다. 설계의 명료함과 실행 성능은 함께 검토한다.

## 6.5 실습: Particle과 Trajectory

### 6.5.1 입자 운동 모델과 객체 구조 설계

일차원 입자 운동에서 $dx/dt=v$, $dv/dt=a$이고 이번에는 일정한 가속도 $a$를 가정한다. 초기 위치 0 m, 초기 속도 0 m/s, 가속도 2 m/s², 시간 간격 0.5 s, 네 번의 갱신을 사용한다. 각 수치 기록은 시간과 상태의 하나의 쌍으로 보관한다.

$$\mathcal{T}=((t_0,\mathbf{s}_0),(t_1,\mathbf{s}_1),\ldots,(t_N,\mathbf{s}_N))$$

검증 계약은 유한한 위치·속도·시간·가속도, 양수 시간 간격, 음수가 아닌 기록 시간, 엄격하게 증가하는 기록 시간, 상태 객체의 불변성, 오류 시 기존 현재 상태 보존이다. 위치·속도·가속도·시간 단위는 각각 m·m/s·m/s²·s로 해석하되 일반 `float`로 자동 단위 검사되지는 않는다.

### 6.5.2 Particle과 Trajectory의 통합 구현

최종 프로그램은 다음의 함수와 클래스를 단일 기준 파일에 정의한다.

- `finite_real`: 기본 정수·실수 입력의 타입과 유한성 검사
- `ParticleState`: 위치와 속도에 대한 불변 `dataclass`
- `euler_step`: 명시적 Euler 한 단계, 새로운 상태 반환
- `Particle`: `state` 조회, `predict`와 `advance` 구분
- `TrajectoryRecord`: 시간과 `ParticleState`의 불변 결합
- `Trajectory`: 시간 순서에 따른 기록 추가, `records`는 Tuple 제공
- `simulate_particle`: 실행 설정 검사, 초기 기록을 포함한 반복 실행

다음은 위 구성 요소 전체가 들어간 **실제 실행 검증된 기준 프로그램**이다. 앞 절의 단편 예제와 충돌하지 않도록 배포용 원본을 하나로 유지한다.

```python
"""Chapter 6, P1: particle trajectory with explicit Euler integration."""
from __future__ import annotations

from dataclasses import dataclass
import math


def finite_real(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return float(value)


@dataclass(frozen=True)
class ParticleState:
    position: float
    velocity: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "position", finite_real(self.position, "position"))
        object.__setattr__(self, "velocity", finite_real(self.velocity, "velocity"))


def euler_step(state: ParticleState, acceleration: float, time_step: float) -> ParticleState:
    if not isinstance(state, ParticleState):
        raise TypeError("state must be a ParticleState")
    a = finite_real(acceleration, "acceleration")
    dt = finite_real(time_step, "time_step")
    if dt <= 0:
        raise ValueError("time_step must be positive")
    return ParticleState(
        position=state.position + state.velocity * dt,
        velocity=state.velocity + a * dt,
    )


class Particle:
    def __init__(self, initial_state: ParticleState) -> None:
        if not isinstance(initial_state, ParticleState):
            raise TypeError("initial_state must be a ParticleState")
        self._state = initial_state

    @property
    def state(self) -> ParticleState:
        return self._state

    def predict(self, acceleration: float, time_step: float) -> ParticleState:
        return euler_step(self._state, acceleration, time_step)

    def advance(self, acceleration: float, time_step: float) -> None:
        next_state = self.predict(acceleration, time_step)
        self._state = next_state


@dataclass(frozen=True)
class TrajectoryRecord:
    time: float
    state: ParticleState

    def __post_init__(self) -> None:
        object.__setattr__(self, "time", finite_real(self.time, "time"))
        if not isinstance(self.state, ParticleState):
            raise TypeError("state must be a ParticleState")


class Trajectory:
    def __init__(self) -> None:
        self._records: list[TrajectoryRecord] = []

    @property
    def records(self) -> tuple[TrajectoryRecord, ...]:
        return tuple(self._records)

    def append(self, time: float, state: ParticleState) -> None:
        record = TrajectoryRecord(time, state)
        if record.time < 0:
            raise ValueError("time must be nonnegative")
        if self._records and record.time <= self._records[-1].time:
            raise ValueError("time must be strictly increasing")
        self._records.append(record)

    def __len__(self) -> int:
        return len(self._records)


def simulate_particle(initial_state: ParticleState, acceleration: float, time_step: float, steps: int) -> Trajectory:
    if not isinstance(steps, int) or isinstance(steps, bool):
        raise TypeError("steps must be an integer")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    # Validate even when steps=0; avoid partial execution for invalid settings.
    a = finite_real(acceleration, "acceleration")
    dt = finite_real(time_step, "time_step")
    if dt <= 0:
        raise ValueError("time_step must be positive")
    particle = Particle(initial_state)
    trajectory = Trajectory()
    trajectory.append(0.0, particle.state)
    for index in range(1, steps + 1):
        particle.advance(a, dt)
        trajectory.append(index * dt, particle.state)
    return trajectory


def main() -> None:
    initial = ParticleState(0.0, 0.0)
    trajectory = simulate_particle(initial, acceleration=2.0, time_step=0.5, steps=4)
    print("time   position   velocity")
    for record in trajectory.records:
        print(f"{record.time:4.1f}   {record.state.position:8.3f}   {record.state.velocity:8.3f}")
    final = trajectory.records[-1]
    exact_position = initial.position + initial.velocity * final.time + 0.5 * 2.0 * final.time**2
    print(f"Euler final position: {final.state.position:.3f}")
    print(f"Exact final position: {exact_position:.3f}")
    print(f"Absolute position error: {abs(final.state.position-exact_position):.3f}")

if __name__ == "__main__":
    main()

```

### 6.5.3 시뮬레이션 실행과 결과 검증

위 파일을 `python p1_particle_trajectory.py`로 실행하면 다음 결과를 얻는다.

```text
time   position   velocity
 0.0      0.000      0.000
 0.5      0.000      1.000
 1.0      0.500      2.000
 1.5      1.500      3.000
 2.0      3.000      4.000
Euler final position: 3.000
Exact final position: 4.000
Absolute position error: 1.000
```

이 결과는 네 번의 갱신과 다섯 개 기록을 나타낸다. 첫 시간 단계에서는 초기 속도가 0이므로 위치가 변하지 않지만 가속도로 속도가 1.0으로 증가한다. 마지막 시간 2초의 정확한 위치는 4.0 m이며 Euler의 위치는 3.0 m이다. 객체지향 구현과 무관하게 사용한 수치 방법의 오차가 발생한다.

$$E_x=\lvert x_{\mathrm{Euler}}-x_{\mathrm{exact}}\rvert=1.0\,\mathrm{m}$$

일정 가속도에서 최종 시간 $T$를 고정하고 일정한 간격 $\Delta t$로 명시적 Euler 방법을 적용하면 위치의 전역 오차 크기는 다음과 같다.

$$E_x=\frac12\lvert a\rvert T\Delta t$$

이 관계는 해당 문제의 특정 조건 아래에서 성립한다. 일반 비선형 미분방정식이나 다른 적분기에 그대로 적용해서는 안 된다.

검증 코드는 정상 상태, 불변 필드의 변경 거부, `nan`·무한대·문자열·불리언 입력 거부, 잘못된 시간 간격, 예측과 실제 갱신의 분리, 실패 시 상태 유지, 기록의 중복·역순 시간 거부, 최종 궤적 결과를 포함한다. `python -m pytest -q test_p1.py` 실행으로 확인한다. 실제 실행 결과는 **16 passed**이다. 검증된 범위 밖인 동시성·외부 자원·Python 3.14 전용 환경 호환성까지 자동 보증하는 것은 아니다.

## 6.6 Chapter Summary — 상태와 책임의 관점에서 함수와 객체의 역할 정리

Chapter 6에서는 같은 과학적 모델을 객체지향 구조로 재조직하였다. 객체는 정체성과 상태를 가지며 클래스는 공통 구조·동작을 정의한다. `self`는 메서드가 어느 인스턴스에 접근하는지 알려준다. 객체를 생성할 때에는 필드의 개수보다 유효한 초기 상태가 중요한데, 과학 데이터의 유효성은 타입만으로 판단할 수 없다.

캡슐화는 내부 상태를 무조건 은폐하는 것이 아니라 외부와 맺는 계약을 관리하는 원칙이다. 읽기 전용 Property, 별도의 상태 변경 메서드, 불변 상태 객체 등의 조합으로 상태 갱신의 경로를 명확히 할 수 있다. `dataclass`는 값의 표현을 간결하게 하지만 런타임 과학 검증을 대체하지 않는다.

P1 실습의 구조는 다음과 같이 요약된다.

| 구성 요소 | 역할 | 선택 근거 |
|---|---|---|
| `ParticleState` | 한 시점의 값 | 불변 데이터 표현 |
| `euler_step()` | 수학적 계산 | 명시적 입력과 새로운 출력 |
| `Particle` | 현재 상태 | 상태 갱신의 책임 |
| `TrajectoryRecord` | 시간과 상태의 결합 | 데이터 대응 관계 보호 |
| `Trajectory` | 상태의 이력 | 시간 순서 계약 유지 |
| `simulate_particle()` | 실행 절차 | 단순 조정은 함수로 충분 |

절차적 프로그래밍은 실행의 순서를, 함수 중심 설계는 계산의 독립성을, 객체지향 설계는 데이터와 동작의 책임을 강조한다. 이 세 가지는 서로 배타적이지 않다. 하나의 과학 프로그램 안에서 명시적인 반복문이 흐름을 관리하고, 순수 함수가 수치 계산을 수행하며, 객체가 상태와 기록을 보유할 수 있다.

객체를 사용했다고 수치 계산이 정확해지거나 빠르게 실행되는 것은 아니다. Euler 방법의 오차는 여전히 Euler 방법의 오차다. 검증된 모델의 적용 범위·데이터 단위·입력 계약·실행 환경을 함께 관리해야 한다. **객체지향 프로그래밍의 핵심은 계산식을 클래스 안으로 옮기는 것이 아니라 상태와 책임의 경계를 명확하게 만드는 데 있다.** 다음 Chapter에서는 여러 객체의 관계와 공통 동작의 재사용을 학습한다.
