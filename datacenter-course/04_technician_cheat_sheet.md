# DATA CENTER TECHNICIAN CHEAT SHEET
## Quick Reference Card — xAI Style Environment
### Шпаргалка технического специалиста / Quick Reference

---

## ⚡ SAFETY FIRST / БЕЗОПАСНОСТЬ ПРЕЖДЕ ВСЕГО

```
NEVER:                              ALWAYS:
❌ Look into active fiber            ✅ Wear ESD strap when touching hardware
❌ Open live electrical panels       ✅ Get change ticket before modifying anything
❌ Use zip ties on fiber             ✅ Cap fiber ends immediately when disconnected
❌ Step on cables                    ✅ Use Velcro on fiber cables
❌ Skip change tickets               ✅ Verify before touching: is this the right port?
❌ Work without ESD strap            ✅ Two-person lift for servers over 35 lbs
```

---

## 🎨 CABLE COLOR CODES / ЦВЕТОВЫЕ КОДЫ КАБЕЛЕЙ

```
YELLOW  (жёлтый)   = Single Mode Fiber (SMF)
                     → Rack→SU, Rack→Supercore, IPMI paths

GREEN CONNECTOR     = LC connector for Single Mode Fiber
(зелёный разъём)

GREEN CABLE         = CAT6 Data (between racks / management)
(зелёный кабель)

BLUE #1  (синий)   = CAT6 → PDU-A  (A-side power management)
BLUE #2  (синий)   = CAT6 → PDU-B  (B-side power management)
BLUE #3  (синий)   = CAT6 → Rack Management

BLACK  (чёрный)    = AEC / Rocky cables (server interconnects)
```

---

## 📍 LABEL DECODER / ДЕКОДЕР МАРКИРОВОК

```
DH20  = Data Hall D, Column H, Position 20
        Зал данных D, Колонна H, Позиция 20

NA05  = Network Cabinet A, Position 05
        Сетевой шкаф A, Позиция 05

NB13  = Network Cabinet B, Position 13
        Сетевой шкаф B, Позиция 13

SCA   = Supercore Cabinet A
        Шкаф Supercore A

SCB   = Supercore Cabinet B
        Шкаф Supercore B

T     = Top port (верхний порт)
D     = Down/Bottom port (нижний порт)
RU    = Rack Unit number (номер юнита)
```

**Cable label format:**
```
[SOURCE RACK]-[DEVICE]-[PORT][T/D] → [DEST RACK]-[DEVICE]-[PORT][T/D]
Example: DH20-SW1-P14T → SCA-P44D
```

---

## 🗼 RACK STRUCTURE / СТРУКТУРА СТОЙКИ

```
                    OVERHEAD CABLE TRAY
                    ┌───────────────────┐
                    │  Yellow  │Blue│Grn│
                    └──────┬───┴────┴───┘
                           ↓ TOP ENTRY (brush strip)
          ┌────────────────┼────────────────┐
          │ VCM            ↓            VCM │
          │  │    ┌────────────────┐    │   │
          │  │    │   42U          │    │   │
          │  │    │   EQUIPMENT    │    │   │
          │  ├────┤   HCM (27U)    │    │   │
          │  │    │                │    │   │
          │  ├────┤   HCM (24U)    │    │   │
          │  │    │                │    │   │
          │  │    │      ...       │    │   │
          │  │    │                │    │   │
          │  │    │    1U          │    │   │
          │  │    └────────────────┘    │   │
          │  │   [PDU-A]    [PDU-B]     │   │
          └──┴──────────────────────────┴───┘

Count RU from BOTTOM (1) to TOP (42)
Считать RU снизу (1) до верха (42)
```

---

## 🔌 POWER ARCHITECTURE / АРХИТЕКТУРА ПИТАНИЯ

```
GRID-A → TRANSFORMER → UPS-A → PANEL-A → PDU-A → SERVER PSU-1
                                                         ║
                                                   SERVER RUNS
                                                         ║
GRID-B → TRANSFORMER → UPS-B → PANEL-B → PDU-B → SERVER PSU-2

RULE: Each PDU ≤ 50% load capacity
      PSU-1 always on PDU-A (A-side)
      PSU-2 always on PDU-B (B-side)
```

---

## 🌐 NETWORK HIERARCHY / СЕТЕВАЯ ИЕРАРХИЯ

```
           SUPERCORE (SCA, SCB)
               ↕          ↕
          SU CABINETS  (NA05, NB13...)
               ↕          ↕
          RACK ToR SWITCHES  (DH20, DH21...)
               ↕          ↕
          SERVERS / GPUs

Fiber type: Single Mode (Yellow) at all levels in this environment
AEC/Rocky: Within rack and adjacent racks only
```

---

## 🔍 FIBER INSPECTION CHECKLIST / КОНТРОЛЬНЫЙ СПИСОК ОСМОТРА ВОЛОКНА

```
BEFORE EVERY FIBER CONNECTION:

□ Step 1: Pick up FOSI scope
□ Step 2: Insert adapter for LC connector
□ Step 3: View end face
□ Step 4: CHECK Zone A (core) — MUST be clean
□ Step 5: If dirty → Use one-click cleaner
□ Step 6: Re-inspect after cleaning
□ Step 7: PASS? → Connect. FAIL? → Clean again.
□ Step 8: Remove dust caps from destination ports
□ Step 9: Insert connector — listen for CLICK
□ Step 10: Verify link light on both ends
```

---

## 📏 KEY MEASUREMENTS / КЛЮЧЕВЫЕ ИЗМЕРЕНИЯ

```
1U (Rack Unit)         = 1.75 inches = 44.45 mm
42U rack height        ≈ 73.5 inches ≈ 186.7 cm
19-inch rack width     = 19 inches between rails

SMF minimum bend radius = 30mm (1.2 inches)
CAT6 minimum bend radius = 4× cable diameter ≈ 25mm

CAT6 max distance @ 1GbE   = 100 meters
CAT6 max distance @ 10GbE  = 55 meters
AEC max distance           = 1 to 7 meters (speed dependent)
SMF typical reach          = 10 to 500+ meters

Velcro spacing in VCM      = Every 12-18 inches (30-45cm)
```

---

## 🔧 FIBER TROUBLESHOOTING QUICK GUIDE / БЫСТРОЕ УСТРАНЕНИЕ НЕИСПРАВНОСТЕЙ ВОЛОКНА

```
SYMPTOM             FIRST CHECK           SECOND CHECK
─────────────────────────────────────────────────────
No link light       Clean connectors      Re-seat transceiver
Intermittent drops  Dirty connector       Check bend radius
High error rate     Loss budget exceeded  Check connector polish type
"Port not present"  Re-seat cable firmly  Check cable compatibility
Link down one side  Check polarity        Check wavelength match
```

---

## ⚙️ IPMI QUICK COMMANDS / БЫСТРЫЕ КОМАНДЫ IPMI

```bash
# Check power status | Проверить статус питания
ipmitool -H <BMC_IP> -U admin -P <password> power status

# Power on | Включить питание
ipmitool -H <BMC_IP> -U admin -P <password> power on

# Power off (graceful) | Выключить (мягко)
ipmitool -H <BMC_IP> -U admin -P <password> power soft

# Force reset | Принудительный сброс
ipmitool -H <BMC_IP> -U admin -P <password> power reset

# Get temperatures | Получить температуры
ipmitool -H <BMC_IP> -U admin -P <password> sdr type Temperature

# Get System Event Log | Получить журнал событий
ipmitool -H <BMC_IP> -U admin -P <password> sel list

# Get fan speeds | Получить скорости вентиляторов
ipmitool -H <BMC_IP> -U admin -P <password> sdr type Fan
```

---

## 📦 NEW SERVER INSTALL CHECKLIST / УСТАНОВКА НОВОГО СЕРВЕРА

```
PRE-INSTALL:
□ Approved change ticket open
□ Correct rack and U position confirmed
□ Server matches work order specs
□ All cables prepared and labeled

PHYSICAL INSTALL:
□ ESD strap on
□ Rails installed at correct U position
□ Server slides onto rails smoothly
□ Server secured with screws

CABLING:
□ PSU-1 → PDU-A outlet (documented)
□ PSU-2 → PDU-B outlet (documented)
□ Data NICs → switches (fiber inspected first)
□ BMC/IPMI port → management switch
□ All cables labeled at both ends
□ Cables dressed per standards

VERIFICATION:
□ PDU-A load still under 50%?
□ PDU-B load still under 50%?
□ Server powered on via IPMI
□ BMC accessible via management network
□ Server visible on production network
□ DCIM updated with all connections
□ Work order completed with notes
□ Photos taken if required
```

---

## 🚨 ESCALATION TRIGGERS / КОГДА НУЖНА ЭСКАЛАЦИЯ

```
IMMEDIATELY escalate when:
├── PDU load exceeds 80% of capacity
├── Temperature sensor > threshold alert
├── Multiple fans fail on same server
├── Fiber damage found in production path
├── Unknown cables discovered with no labels
├── Discrepancy found between physical and DCIM
├── Any planned change cannot be completed as documented
└── Anything you are unsure about — ASK, don't guess!
```

---

## 📋 QC SIGN-OFF CHECKLIST / КОНТРОЛЬНЫЙ СПИСОК КК

```
Before closing any work ticket:

LABELS:    □ Both ends labeled □ Labels match DCIM
PORTS:     □ Correct port □ Link light present
FIBER:     □ Inspected □ Cleaned □ Dust caps on unused ports
PHYSICAL:  □ Dressed □ Bend radius ok □ Service loop present
POWER:     □ PDU-A < 50% □ PDU-B < 50% □ Both PSUs connected
DOCS:      □ DCIM updated □ Work order notes complete
```

---

## 🏷️ COMMON RACK LABEL EXAMPLES / ПРИМЕРЫ МАРКИРОВОК СТОЕК

```
Rack IDs (sample):
DH01, DH02 ... DH30  — Data Hall D, Row H
DG01, DG02 ... DG30  — Data Hall D, Row G

Network/SU Cabinets:
NA01, NA02 ... NA10  — Network Tier A
NB01, NB02 ... NB10  — Network Tier B

Supercore:
SCA, SCB, SCC        — Supercore Cabinets A, B, C

Port indicators on labels:
P1T  = Port 1, Top
P1D  = Port 1, Down (bottom)
P2T  = Port 2, Top
P2D  = Port 2, Down
```

---

*Keep this cheat sheet with you on the data center floor.*  
*Держите эту шпаргалку при себе на полу дата-центра.*
