# ARCHITECTURE DIAGRAMS
## ASCII Technical Diagrams for Data Center Training
### xAI-Style Environment

---

# DIAGRAM 1: COMPLETE NETWORK HIERARCHY

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    xAI-STYLE DATA CENTER NETWORK HIERARCHY                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

TIER 3: SUPERCORE LAYER
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌────────┐          ┌────────┐          ┌────────┐          ┌────────┐  │
│  │  SCA   │          │  SCB   │          │  SCC   │          │  SCD   │  │
│  │SUPERCORE│          │SUPERCORE│         │SUPERCORE│         │SUPERCORE│ │
│  │  SW-A  │          │  SW-B  │          │  SW-C  │          │  SW-D  │  │
│  └───┬────┘          └───┬────┘          └───┬────┘          └───┬────┘  │
│      │                   │                   │                   │        │
│      └───────────────────┴───────────────────┴───────────────────┘        │
│                    Single Mode Fiber (Yellow)                              │
│                    400G / 800G uplinks                                     │
└──────────────────────────────────────────────────────────────────────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼

TIER 2: SU CABINET LAYER (Spine/Aggregation)
┌───────────┐        ┌───────────┐        ┌───────────┐        ┌───────────┐
│  NA01     │        │  NA02     │        │  NB01     │        │  NB02     │
│ SU Cabinet│        │ SU Cabinet│        │ SU Cabinet│        │ SU Cabinet│
│  Spine-A  │        │  Spine-B  │        │  Spine-C  │        │  Spine-D  │
│ [AGG-SW]  │        │ [AGG-SW]  │        │ [AGG-SW]  │        │ [AGG-SW]  │
└─────┬─────┘        └─────┬─────┘        └─────┬─────┘        └─────┬─────┘
      │                    │                    │                    │
      │ SMF Yellow         │ SMF Yellow         │ SMF Yellow         │
      │ Green LC           │ Green LC           │ Green LC           │
      │ 100G links         │ 100G links         │ 100G links         │
      ↓                    ↓                    ↓                    ↓

TIER 1: RACK CABINET LAYER (Leaf/Access)
┌──────┐ ┌──────┐  ┌──────┐ ┌──────┐  ┌──────┐ ┌──────┐  ┌──────┐ ┌──────┐
│ DH01 │ │ DH02 │  │ DH03 │ │ DH04 │  │ DH05 │ │ DH06 │  │ DH07 │ │ DH08 │
│Rack  │ │Rack  │  │Rack  │ │Rack  │  │Rack  │ │Rack  │  │Rack  │ │Rack  │
│[ToR] │ │[ToR] │  │[ToR] │ │[ToR] │  │[ToR] │ │[ToR] │  │[ToR] │ │[ToR] │
└──┬───┘ └──┬───┘  └──┬───┘ └──┬───┘  └──┬───┘ └──┬───┘  └──┬───┘ └──┬───┘
   │        │          │        │          │        │          │        │
   ▼        ▼          ▼        ▼          ▼        ▼          ▼        ▼
SERVERS  SERVERS    SERVERS  SERVERS    SERVERS  SERVERS    SERVERS  SERVERS
GPU nodes GPU nodes GPU nodes GPU nodes GPU nodes GPU nodes GPU nodes GPU nodes
```

---

# DIAGRAM 2: RACK CABINET INTERNAL STRUCTURE (FRONT VIEW)

```
╔══════════════════════════════════════════════════════════════════╗
║                    RACK CABINET — FRONT VIEW                     ║
║                    (Example: Rack DH20, 42U)                     ║
╚══════════════════════════════════════════════════════════════════╝

         OVERHEAD CABLE TRAY
    ═══════════════════════════════════
    │ Yellow│Blue│Blue│Blue│ Green │   │  (cables enter from tray)
    ─────────────────────────────────
         ↓ Brush Strip (top entry)
    ┌────────────────────────────────┐
42U │    ┌──────────────────┐   VCM │  ← Vertical Cable Manager
    │    │ HCM (top section)│    │  │     (right side)
41U │    ├──────────────────┤    │  │
    │    │                  │    │  │
40U │    │  SERVER AT U40   │    │  │
    │    │  ████████████████│    │  │
39U │    │  SERVER AT U39   │    │  │
    │    │  ████████████████│    │  │
38U │    ├──────────────────┤    │  │
    │    │ HCM              │    │  │
37U │    ├──────────────────┤    │  │
    │    │                  │    │  │
36U │    │  SERVER AT U36   │    │  │
    │    │  ████████████████│    │  │
 .  │    │       ...        │    │  │
 .  │    │                  │    │  │
 .  │    │                  │    │  │
14U │    ├──────────────────┤    │  │
    │    │ HCM              │    │  │
13U │    ├──────────────────┤    │  │
    │    │  SWITCH AT U13   │    │  │
    │    │  ████████████████│    │  │
12U │    │  [ToR SWITCH]    │    │  │
    │    ├──────────────────┤    │  │
11U │    │ HCM              │    │  │
    │    ├──────────────────┤    │  │
10U │    │                  │    │  │
    │    │       ...        │    │  │
    │    │                  │    │  │
 3U │    │  SERVER AT U3    │    │  │
    │    │  ████████████████│    │  │
 2U │    │  SERVER AT U2    │    │  │
    │    │  ████████████████│    │  │
 1U │    │  MGMT SWITCH U1  │    │  │
    │    └──────────────────┘    │  │
    │         [PDU-A] [PDU-B]    │  │  ← PDUs mounted vertically rear
    └────────────────────────────┘
    
KEY:
VCM  = Vertical Cable Manager (right side, runs full height)
HCM  = Horizontal Cable Manager (at specific rack unit levels)
PDU  = Power Distribution Unit (rear-mounted, vertical)
████ = Equipment face
```

---

# DIAGRAM 3: CABLE PATH DETAIL (SIDE VIEW)

```
╔══════════════════════════════════════════════════════════════════╗
║              CABLE PATH — SIDE/SECTION VIEW                      ║
╚══════════════════════════════════════════════════════════════════╝

                    ┌──────────────────────────────┐
OVERHEAD            │  CABLE TRAY                  │
CABLE TRAY          │  ══Yellow══Blue══Green══     │
                    └──────────┬───────────────────┘
                               │
                               │ (cables drop from tray)
                               ↓
                    ┌──────────────┐
BRUSH STRIP /       │//////////////│  ← Brush seal
TOP ENTRY           │//////////////│    allows cables
                    └──────────┬───┘    through, blocks
                               │        airflow/pests
                               │
                    ┌──────────────┐
VCM (right side)    │VCM           │  Yellow fiber runs here
                    ││             │  (secured with Velcro
                    ││  ∥∥∥∥∥∥∥   │   every 12-18 inches)
                    ││  Yellow     │
                    ││  Fiber      │
                    ││  Bundles    │
                    ││             │
                    │├─────────────┤  ← HCM level (cables branch
                    ││    HCM  ──────────────→  to equipment ports
                    │├─────────────┤
                    ││             │
                    ││  ∥∥∥∥∥∥∥   │
                    │└─────────────┘
                               │
                               │ (cables continue down VCM
                               │  to lower equipment levels)
                               ▼
                    ┌──────────────┐
                    │    HCM       │──────────→ Equipment at U5
                    └──────────────┘
```

---

# DIAGRAM 4: POWER ARCHITECTURE — DUAL FEED

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    DUAL POWER ARCHITECTURE                               ║
╚══════════════════════════════════════════════════════════════════════════╝

UTILITY                    A-SIDE PATH                    B-SIDE PATH
  │                              │                              │
  ├─── TRANSFORMER A ───────────►│                              │
  │    (High Voltage             │                              │
  │     Step-Down)               ▼                              │
  │                         ┌──────────┐                        │
  │                         │   UPS-A  │                        │
  │                         │(Battery  │                        │
  │                         │ Backup A)│                        │
  │                         └────┬─────┘                        │
  │                              │                              │
  │                         PANEL-A                             │
  │                         (Circuit Breaker Panel A)           │
  │                              │                              │
  │                              ▼                              │
  │                         ┌──────────┐                        │
  │                         │  PDU-A   │                        │
  │                         │ ┌──────┐ │                        │
  │                         │ │Outlet│ │                        │
  │                         │ │  1   ├─┼───────────→ PSU-1 (SERVER-01)
  │                         │ │  2   ├─┼───────────→ PSU-1 (SERVER-02)
  │                         │ │  3   ├─┼───────────→ PSU-1 (SERVER-03)
  │                         │ │ ...  │ │
  │                         │ │ 20   ├─┼───────────→ PSU-1 (SERVER-20)
  │                         │ └──────┘ │
  │                         └──────────┘
  │
  │                             (SERVER runs on BOTH simultaneously)
  │                              PSU-1 and PSU-2 share load
  │
  └─── TRANSFORMER B ────────────────────────────────────────────►
       (High Voltage                                               │
        Step-Down)                                           ┌─────┴────┐
                                                             │   UPS-B  │
                                                             │(Battery  │
                                                             │ Backup B)│
                                                             └────┬─────┘
                                                                  │
                                                             PANEL-B
                                                             (Circuit Breaker Panel B)
                                                                  │
                                                                  ▼
                                                             ┌──────────┐
                                                             │  PDU-B   │
                                                             │ ┌──────┐ │
                                                             │ │Outlet│ │
PSU-2 (SERVER-01) ←──────────────────────────────────────── │ │  1   │ │
PSU-2 (SERVER-02) ←──────────────────────────────────────── │ │  2   │ │
PSU-2 (SERVER-03) ←──────────────────────────────────────── │ │  3   │ │
                                                             │ │ ...  │ │
PSU-2 (SERVER-20) ←──────────────────────────────────────── │ │ 20   │ │
                                                             │ └──────┘ │
                                                             └──────────┘

FAULT TOLERANCE:
If A-SIDE fails → All servers continue running on PSU-2 (B-side)
If B-SIDE fails → All servers continue running on PSU-1 (A-side)
Both sides fail → Servers lose power (extremely rare with UPS)
```

---

# DIAGRAM 5: THREE BLUE CAT6 CABLES — RACK CONNECTIONS

```
╔══════════════════════════════════════════════════════════════════╗
║              BLUE CAT6 CABLE ASSIGNMENTS PER RACK                ║
╚══════════════════════════════════════════════════════════════════╝

                    OVERHEAD CABLE TRAY
    ─────────────────────────────────────────────────────────
              │              │              │
           Blue #1        Blue #2        Blue #3
          (PDU-A)        (PDU-B)        (RACK MGMT)
              │              │              │
              ▼              ▼              ▼
    ┌─────────────────────────────────────────────────────┐
    │                  RACK DH20                          │
    │                                                     │
    │  ┌───────────────────────────────────────────────┐  │
    │  │           VCM (cable routing)                 │  │
    │  │    Blue#1 │ Blue#2 │ Blue#3                   │  │
    │  │           │        │                           │  │
    │  │           │        └──────────► U1 Management │  │
    │  │           │                    Switch Port    │  │
    │  │           │                                   │  │
    │  │           └───────────────────► PDU-B         │  │
    │  │                                Management Port│  │
    │  │                                               │  │
    │  └──────────────────────────────────────────────┘  │
    │                                                     │
    │  [PDU-A]─────────────────────────────────────────── │
    │     │ Management Port ◄──────── Blue #1             │
    │     │                                               │
    │  [PDU-B]─────────────────────────────────────────── │
    │     │ Management Port ◄──────── Blue #2             │
    │                                                     │
    └─────────────────────────────────────────────────────┘

BLUE CABLE REFERENCE:
Blue #1 ──→ PDU-A Management   (power management, A-side)
Blue #2 ──→ PDU-B Management   (power management, B-side)
Blue #3 ──→ Rack Management    (OOB console/monitoring device)
```

---

# DIAGRAM 6: FIBER CONNECTOR TYPES

```
╔══════════════════════════════════════════════════════════════════╗
║                    FIBER CONNECTOR TYPES                         ║
╚══════════════════════════════════════════════════════════════════╝

LC CONNECTOR (Most common in data centers)
                    ┌─────────┐
                    │  GREEN  │  ← Green housing = Single Mode
                    │ housing │
                    │  ┌───┐  │
                    │  │ ● │  │  ← Ferrule (2.5mm diameter)
                    │  └─┬─┘  │
                    │    │    │
                    │  LATCH  │  ← Small tab latch (like RJ45)
                    └────┴────┘
                         │
                    LC DUPLEX (two fibers, TX+RX):
                    ┌────┐ ┌────┐
                    │  ● │ │  ● │  ← TX connector + RX connector
                    └────┘ └────┘
                    (joined together with plastic clip)

SC CONNECTOR (Older, larger format)
              ┌──────────────┐
              │   Square     │
              │   housing    │
              │   ┌──────┐   │
              │   │  ●   │   │  ← Ferrule (2.5mm)
              │   └──────┘   │
              │  push-pull   │
              └──────────────┘

MPO/MTP CONNECTOR (Multi-fiber, high density)
         ┌────────────────────────────┐
         │  ● ● ● ● ● ● ● ● ● ● ● ●  │  ← 12 fibers in a row
         │  (or 24 fibers in 2 rows)  │
         │        GUIDE PINS          │
         └────────────────────────────┘
         Used in trunk cables between patch panels
         One MPO = 12 or 24 individual fibers

COLOR CODE QUICK REFERENCE:
GREEN connector  = Single Mode Fiber (OS2)
BEIGE connector  = Multimode OM1/OM2
AQUA connector   = Multimode OM3/OM4
```

---

# DIAGRAM 7: FIBER END FACE INSPECTION ZONES

```
╔══════════════════════════════════════════════════════════════════╗
║              FIBER END FACE INSPECTION ZONES (IEC 61300-3-35)   ║
╚══════════════════════════════════════════════════════════════════╝

                    FIBER FERRULE END FACE
                    (as seen through FOSI scope)

                    ┌─────────────────────────────┐
                    │           FERRULE            │
                    │                              │
                    │    ┌───────────────────┐     │
                    │    │    Zone D         │     │
                    │    │  (Adhesive area)  │     │
                    │    │  ┌─────────────┐  │     │
                    │    │  │   Zone C    │  │     │
                    │    │  │ (Contact)   │  │     │
                    │    │  │  ┌───────┐  │  │     │
                    │    │  │  │Zone B │  │  │     │
                    │    │  │  │(Clad.)│  │  │     │
                    │    │  │  │ ┌───┐ │  │  │     │
                    │    │  │  │ │ A │ │  │  │     │
                    │    │  │  │ └───┘ │  │  │     │
                    │    │  │  └───────┘  │  │     │
                    │    │  └─────────────┘  │     │
                    │    └───────────────────┘     │
                    │                              │
                    └─────────────────────────────┘

ZONE DESCRIPTIONS:
Zone A (Core)     = 0-25µm radius from center  ★ MUST BE PERFECTLY CLEAN
Zone B (Cladding) = 25-120µm radius             ★ Should be clean
Zone C (Contact)  = 120-250µm radius              Minor contamination OK
Zone D (Adhesive) = 250-500µm radius              Contamination acceptable

CLEANLINESS CRITERIA:
Zone A: ZERO contamination or scratches allowed
Zone B: Maximum 3 particles, none > 3µm, no scratches across core edge
Zone C: Maximum 5 particles
Zone D: Contamination acceptable

IF Zone A has ANY contamination → CLEAN before connecting!
```

---

# DIAGRAM 8: NETWORK TRAFFIC FLOW — GPU TO GPU

```
╔══════════════════════════════════════════════════════════════════════════╗
║              GPU-to-GPU COMMUNICATION FLOW IN AI CLUSTER                ║
╚══════════════════════════════════════════════════════════════════════════╝

SCENARIO: GPU in Rack DH01 communicates with GPU in Rack DH50

GPU [DH01-SERVER1-GPU0]
    │
    │ AEC/Rocky cable (within server or adjacent rack)
    │ or 100G NIC connection
    ▼
[DH01 ToR Switch - Port 1]
    │
    │ Single Mode Fiber (Yellow)
    │ 100G or 400G uplink
    ▼
[NA01 SU Cabinet - Aggregation Switch]
    │
    │ Single Mode Fiber (Yellow)
    │ 400G or 800G uplink
    ▼
[SCA Supercore Switch]
    │
    │ (routing decision — traffic to DH50 goes through SC switches)
    │
[SCB Supercore Switch] (ECMP — may take different path)
    │
    │ Single Mode Fiber (Yellow)
    │ 400G or 800G downlink
    ▼
[NB05 SU Cabinet - Aggregation Switch]
    │
    │ Single Mode Fiber (Yellow)
    │ 100G or 400G downlink
    ▼
[DH50 ToR Switch - Port X]
    │
    │ AEC/Rocky cable or NIC connection
    ▼
GPU [DH50-SERVER5-GPU3]

TOTAL PATH: DH01 → NA01 → SCA/SCB → NB05 → DH50
LATENCY: Typically < 5 microseconds end-to-end
CABLE TYPES USED:
  Within rack:  AEC/Rocky (black)
  Rack to SU:   Single Mode Fiber (yellow, LC connectors)
  SU to Core:   Single Mode Fiber (yellow, MPO or LC)
  Management:   CAT6 copper (blue)
```

---

# DIAGRAM 9: IPMI MANAGEMENT NETWORK ARCHITECTURE

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    IPMI MANAGEMENT NETWORK                               ║
╚══════════════════════════════════════════════════════════════════════════╝

PRODUCTION NETWORK                    MANAGEMENT NETWORK (OOB)
(High bandwidth, latency sensitive)   (Low bandwidth, high reliability)

┌─────────────────────────┐          ┌─────────────────────────┐
│   Production Switch 1   │          │   Management Switch 1   │
│   (ToR in each rack)    │          │   (U1 in each rack)     │
└─────────────────────────┘          └────────────┬────────────┘
         │                                        │
         │ Yellow SMF                             │ SMF or CAT6
         │ to SU/Supercore                        │ to IPMI Infrastructure
         │                                        │
SERVER PRODUCTION NICs               SERVER BMC (IPMI) PORTS
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  SERVER-01                                                     │
│  ┌────────────────────────────────────────────────────────┐   │
│  │  NIC-0 (100G) ─────────────────►  Production Switch    │   │
│  │  NIC-1 (100G) ─────────────────►  Production Switch    │   │
│  │                                                        │   │
│  │  BMC (iDRAC/iLO) ─────────────►  MANAGEMENT SWITCH    │   │
│  │  Management port (1G)                                  │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  SERVER-02                                                     │
│  ┌────────────────────────────────────────────────────────┐   │
│  │  NIC-0 (100G) ─────────────────►  Production Switch    │   │
│  │  NIC-1 (100G) ─────────────────►  Production Switch    │   │
│  │                                                        │   │
│  │  BMC ──────────────────────────►  MANAGEMENT SWITCH    │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  (All servers in rack follow same pattern)                    │
│                                                                │
└────────────────────────────────────────────────────────────────┘

Management network path in our environment:
BMC Port → Management Switch (U1 in rack, via Blue CAT6 #3)
Management Switch → IPMI Infrastructure (via SMF or CAT6)
IPMI Infrastructure → NOC / Operators (via dedicated management network)

SEPARATION IS CRITICAL:
Production network: Carries AI computation data — must be fast
Management network: Carries control signals — must be reliable and secure
```

---

# DIAGRAM 10: AEC/ROCKY CABLE USAGE IN AI SERVER RACK

```
╔══════════════════════════════════════════════════════════════════════════╗
║              AEC/ROCKY CABLE DENSITY IN AI GPU RACK                      ║
╚══════════════════════════════════════════════════════════════════════════╝

TYPICAL AI TRAINING SERVER (8x GPU HGX Node):

SERVER REAR VIEW:
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌────┐┌────┐┌────┐┌────┐   ┌────┐┌────┐┌────┐┌────┐   Management     │
│  │GPU0││GPU1││GPU2││GPU3│   │GPU4││GPU5││GPU6││GPU7│   ├──── BMC Port  │
│  │NVL ││NVL ││NVL ││NVL │   │NVL ││NVL ││NVL ││NVL │   │               │
│  │P0  ││P0  ││P0  ││P0  │   │P0  ││P0  ││P0  ││P0  │   ├──── PSU-1    │
│  │P1  ││P1  ││P1  ││P1  │   │P1  ││P1  ││P1  ││P1  │   │    (to PDU-A)│
│  │P2  ││P2  ││P2  ││P2  │   │P2  ││P2  ││P2  ││P2  │   ├──── PSU-2    │
│  │P3  ││P3  ││P3  ││P3  │   │P3  ││P3  ││P3  ││P3  │   │    (to PDU-B)│
│  └────┘└────┘└────┘└────┘   └────┘└────┘└────┘└────┘   └──── NIC Ports│
│     │    │    │    │           │    │    │    │                          │
└─────┼────┼────┼────┼───────────┼────┼────┼────┼──────────────────────────┘
      │    │    │    │           │    │    │    │
      │    │    │    │AEC/Rocky  │    │    │    │
      │    │    │    │Cables     │    │    │    │
      ▼    ▼    ▼    ▼           ▼    ▼    ▼    ▼

[NVSwitch or InfiniBand Switch in same or adjacent rack]

ONE SERVER = 32 AEC ports (8 GPUs × 4 ports/GPU)
FOUR SERVERS IN RACK = 128 AEC ports
ALL AEC CABLES = SHORT LENGTH (1-3 meters)

WHY THIS MATTERS FOR TECHNICIANS:
- AI GPU racks have EXTREME cable density
- Each cable must be correctly labeled
- Service loops must be maintained
- Bend radius must be respected even in tight spaces
- Pulling one cable carelessly can disconnect 10 others
```

---

# DIAGRAM 11: CABLE DRESSING — CORRECT VS INCORRECT

```
╔══════════════════════════════════════════════════════════════════╗
║              CABLE DRESSING — CORRECT VS INCORRECT               ║
╚══════════════════════════════════════════════════════════════════╝

CORRECT DRESSING:                    INCORRECT DRESSING:
                                     
┌────────────────────┐               ┌────────────────────┐
│ ╔══════════════╗   │               │                    │
│ ║   Velcro     ║   │               │  ~~~~cables~~~~    │
│ ║   bundle     ║   │               │  ~~~scattered~~~   │
│ ║   in VCM     ║   │               │  ~~everywhere~~    │
│ ╚══════════════╝   │               │                    │
│ ╔══════════════╗   │               │  ○zip tie──────    │
│ ║              ║   │               │  (on fiber!)       │
│ ╚══════════════╝   │               │                    │
│ ╔══════════════╗   │               │  cables draped     │
│ ║   [HCM]      ║   │               │  across equipment  │
│ ╚══════════════╝   │               │  face: ≋≋≋≋≋≋     │
│    │  │  │  │      │               │                    │
│  equipment ports   │               │  no service loops  │
└────────────────────┘               └────────────────────┘
                                     
✓ Velcro straps                      ✗ No organization
✓ Service loops present              ✗ Zip ties on fiber  
✓ Cables in VCM/HCM                  ✗ Cables on equipment face
✓ Fiber on outside of bundles        ✗ No labels visible
✓ Labels facing outward              ✗ No service loops
✓ Minimum bend radius maintained     ✗ Cables on floor
```

---

*End of Architecture Diagrams*  
*All diagrams are ASCII art for use in text-based training materials.*  
*Supplement with photographs from the actual xAI facility when available.*
