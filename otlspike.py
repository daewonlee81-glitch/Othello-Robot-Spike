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