# Xbox 컨트롤러 RC카 — 로봇 배틀 오델로 (Robot Battle Othello)

본 RC카는 **World Robot League의 「로봇 배틀 오델로」** 경기를 위한 로봇입니다.
양면 색이 다른 미션블록(총 11개)을 자신의 색으로 뒤집어 득점하는 전략 제어 경기로,
**라이트웨이트(Pro)** 부문(프라이머리 U-12 / 세컨더리 U-18) 규격에 맞춰 설계되었습니다.

SPIKE Prime 허브와 Xbox 컨트롤러를 블루투스(BLE)로 연결하여 조종합니다.
D-pad로 방향을 조작하고, R-트리거로 출력을 조절하며, A 버튼으로 **미션블록 뒤집기 동작**(가운데 모터 0° → 90° → 0°)을 수행합니다.

---

## 경기 규정 요약 (라이트웨이트 Pro)

| 항목 | 규격 |
|------|------|
| 무게 | 500g 이하 (+3g 오차) |
| 크기 | 25 × 25 × 25 cm 이내 |
| 디펜스 구조 폭 | 25 cm 이하 (전·후·좌·우 중 한 면만 사용) |
| 배터리 | 11.7V 이하 (시판 안전 인증품) |
| 모터 | 제한 없음 (Unlimited) |
| 무선 통신 | IR · Bluetooth · RF · RC 사용 가능 |
| 경기 시간 | 2분 (11점 달성 시 Cold Game 즉시 승리) |
| 미션블록 | 원형 11개 (아군 5 + 적군 5 + 중앙 중립 1) |
| 공격 규정 | 블로킹만 허용 / 밀기·잡기·끌기·들기·뒤집기 **금지** |
| 회전 무기 | 회전식(rotary)·드럼형 무기 **사용 불가** |

> 본 로봇은 미션블록 위로 이동한 뒤 **가운데 모터(Port C)** 를 0°→90°→0°로 회전시켜
> 블록을 자신의 색으로 뒤집습니다. 상대 로봇을 직접 공격하는 구조가 아닌
> **블록 조작 + 블로킹** 중심의 전략형 로봇입니다.

---

## 모터 연결 포트

```
SPIKE Prime Hub
├── Port A → Large Motor (왼쪽 구동)   : 반시계 방향
├── Port E → Large Motor (오른쪽 구동) : 시계 방향
└── Port C → Medium Motor (가운데)     : A 버튼 동작용 (0° ↔ 90°)
```

| 포트 | 모터 | 역할 | 회전 방향 |
|------|------|------|----------|
| Port A | Large Motor | 왼쪽 구동 바퀴 | COUNTERCLOCKWISE |
| Port E | Large Motor | 오른쪽 구동 바퀴 | CLOCKWISE |
| Port C | Medium Motor | 가운데 동작 모터 | 기본 (0° → 90° → 0°) |

---

## Xbox 컨트롤러 연결 방법

Pybricks 펌웨어가 설치된 SPIKE Prime 허브에서 Xbox 컨트롤러를 블루투스로 연결합니다.

### 1단계: Pybricks 펌웨어 설치

1. [Pybricks Code](https://code.pybricks.com)에 접속합니다
2. 좌측 상단 **⚙️ 설정** 아이콘을 클릭합니다
3. **Install Pybricks Firmware**를 선택합니다
4. SPIKE Prime 허브를 USB 케이블로 PC에 연결합니다
5. 허브의 **블루투스 버튼을 누른 상태**에서 USB를 연결하면 DFU 모드로 진입합니다
6. 화면 안내에 따라 펌웨어를 설치합니다

### 2단계: Xbox 컨트롤러 페어링

1. SPIKE Prime 허브의 **센터 버튼**을 눌러 전원을 켭니다
2. 허브의 블루투스 표시등이 깜빡이며 페어링 대기 상태가 됩니다
3. Xbox 컨트롤러의 **Xbox 버튼**(가운데 큰 버튼)을 눌러 전원을 켭니다
4. 컨트롤러 상단의 **페어링 버튼**(작은 버튼)을 3초간 길게 누릅니다
5. 컨트롤러의 Xbox 버튼이 **빠르게 깜빡이면** 페어링 모드입니다
6. 잠시 기다리면 허브와 컨트롤러가 자동으로 연결됩니다
7. 허브 LED가 **초록색**으로 바뀌고 비프음이 울리면 연결 완료입니다

> **참고**: 허브 LED가 **빨간색**이면 연결 대기 중, **초록색**이면 연결 성공입니다.
> 연결에 실패하면 허브에서 길게 비프음이 울리고 프로그램이 종료됩니다.
> 이 경우 허브와 컨트롤러를 모두 껐다가 다시 시도해 주세요.

### 3단계: 코드 업로드 및 실행

1. [Pybricks Code](https://code.pybricks.com)에 접속합니다
2. 블루투스 아이콘을 클릭하여 허브에 연결합니다
3. `xbox_drive.py` 코드를 에디터에 붙여넣습니다
4. ▶️ **실행 버튼**을 클릭합니다
5. 허브 LED가 빨간색 → 초록색으로 바뀌면 조종 준비 완료입니다

---

## 조작 방법

| 입력 | 동작 |
|------|------|
| D-pad ↑ + R-트리거 | 전진 (트리거 깊이 = 속도) |
| D-pad ↓ + R-트리거 | 후진 |
| D-pad ← + R-트리거 | 좌회전 (제자리) |
| D-pad → + R-트리거 | 우회전 (제자리) |
| D-pad ↗↘↙↖ + R-트리거 | 대각선 이동 (전진/후진 + 좌/우 조향) |
| A 버튼 | 가운데 모터 동작 (0° → 90° → 0°) — **미션블록 뒤집기** |
| R-트리거 (놓음) | 정지 |

> **R-트리거**를 얼마나 깊이 누르느냐에 따라 속도가 0~100%로 조절됩니다.
> A 버튼을 누르면 구동 모터가 자동으로 정지한 뒤 가운데 모터가 동작하고, 완료 후 다시 조종할 수 있습니다.

---

## 코드 (`xbox_drive.py`)

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.tools import wait
from pybricks.iodevices import XboxController

# ─── 허브 & 모터 초기화 ───
hub = PrimeHub()

# 구동 모터
motor_right = Motor(Port.E, Direction.CLOCKWISE)
motor_left  = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# 가운데 모터
motor_c = Motor(Port.C)
motor_c.reset_angle(0)

# ─── Xbox 컨트롤러 연결 ───
hub.light.on(Color.RED)
try:
    xbox = XboxController()
except RuntimeError:
    hub.speaker.beep(500, 1000)
    raise SystemExit

hub.light.on(Color.GREEN)
hub.speaker.beep(1000, 100)

a_busy = False
prev_buttons = set()

# ─── 메인 루프 ───
while True:
    # ── D-pad + R-트리거 → 구동 ──
    dpad = xbox.dpad()
    lt, rt = xbox.triggers()
    power = rt

    if   dpad == 1:  drive, steer =  1,  0
    elif dpad == 2:  drive, steer =  1,  1
    elif dpad == 3:  drive, steer =  0,  1
    elif dpad == 4:  drive, steer = -1,  1
    elif dpad == 5:  drive, steer = -1,  0
    elif dpad == 6:  drive, steer = -1, -1
    elif dpad == 7:  drive, steer =  0, -1
    elif dpad == 8:  drive, steer =  1, -1
    else:            drive, steer =  0,  0

    left_power  = (drive + steer) * power
    right_power = (drive - steer) * power

    max_raw = max(abs(left_power), abs(right_power), 1)
    if max_raw > 100:
        left_power  = left_power  / max_raw * 100
        right_power = right_power / max_raw * 100

    motor_left.dc(left_power)
    motor_right.dc(right_power)

    # ── A 버튼 → C 모터: 0° → 90° → 0° ──
    buttons = xbox.buttons.pressed()

    if Button.A in buttons and not a_busy:
        a_busy = True
        motor_left.dc(0)
        motor_right.dc(0)
        motor_c.run_target(1500, 90)
        motor_c.run_target(1500, 0)
        motor_left.dc(0)
        motor_right.dc(0)
        a_busy = False

    prev_buttons = buttons

    wait(20)
```

---

## 조립 카드 및 3D 프린트 파일

| 폴더 | 설명 |
|------|------|
| `assembly/` | 조립 카드 (PDF/이미지) |
| `stl/` | 3D 프린트용 STL 파일 |

> 조립 카드와 STL 파일은 위 폴더에서 다운로드할 수 있습니다.

---

## 경기 문의처

**국제로봇교육협의회 (International Robotics Educational Association, IREA)**
- 이메일: robot-league@naver.com
- WhatsApp: +82-10-2604-3782 (협회 담당자 이대원 / Daewon LEE)

---

## 라이선스

MIT License
