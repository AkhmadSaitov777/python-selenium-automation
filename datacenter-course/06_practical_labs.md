# PRACTICAL LAB EXERCISES
## Data Center Technician Training Program
### Hands-On Skill Development

---

# LAB 1: RACK NAVIGATION AND UNIT IDENTIFICATION

## Objective
Master rack cabinet navigation, rack unit counting, and label interpretation.

## Prerequisites
- Completion of Module 3 (Rack Cabinets)
- Access to: Any physical rack or rack diagram

## Materials Needed
- Tape measure
- Flashlight
- This worksheet

---

### Exercise 1.1 — Rack Unit Counting (10 minutes)

**Task:** Count rack units on a physical or diagram rack.

1. Locate a 42U rack cabinet (physical or diagram)
2. Starting from the bottom (U1), place a colored sticker or mark at:
   - U1, U5, U10, U14, U20, U24, U30, U35, U40, U42
3. Measure the height of 5 rack units using a tape measure
4. Verify: 5U × 1.75 inches = 8.75 inches (22.2 cm)

**Record your measurements:**
```
5U measured height: _______ inches
Expected: 8.75 inches
Difference: _______ inches
Pass/Fail: _______
```

### Exercise 1.2 — Label Decoding (15 minutes)

Decode each of the following labels:

```
Label 1: DH20        Decoded: ______________________________
Label 2: NA05        Decoded: ______________________________
Label 3: NB13        Decoded: ______________________________
Label 4: SCA         Decoded: ______________________________
Label 5: SCB         Decoded: ______________________________

Cable Label: DH20-SW1-P14T → SCA-P44D
  Source rack: ________________
  Source device: ______________
  Source port: ________________
  Port position: ______________
  Destination rack: ___________
  Destination device: _________
  Destination port: ___________
  Port position: ______________
```

**Answers:**
```
Label 1: Data Hall D, Column H, Position 20
Label 2: Network Cabinet A, Position 05
Label 3: Network Cabinet B, Position 13
Label 4: Supercore Cabinet A
Label 5: Supercore Cabinet B

Cable: Source = Rack DH20, Switch 1, Port 14 Top
       Destination = Supercore Cabinet A, Port 44 Bottom
```

### Exercise 1.3 — Cable Path Tracing (20 minutes)

**Using a rack diagram or physical rack, trace the following:**

Given: A yellow single mode fiber cable entering from the overhead tray.

1. Identify where the cable enters the rack (overhead, top entry)
2. Trace the cable down the VCM
3. Identify at which rack unit level the cable branches off to equipment
4. Identify the equipment port it connects to
5. Read the label on the cable

**Document your trace:**
```
Entry point: _______________________
VCM path: _________________________
Branch-off at: RU ___________________
Destination device: _________________
Destination port: ___________________
Cable label: _______________________
```

---

# LAB 2: FIBER OPTIC INSPECTION AND CLEANING

## Objective
Develop proper fiber inspection and cleaning technique.

## Prerequisites
- Completion of Module 4 (Single Mode Fiber)
- Signed safety briefing (never look into active fiber)

## Materials Needed
- Fiber inspection scope (FOSI / video scope)
- One-click cleaners (LC type)
- IPA (99% isopropyl alcohol)
- Fiber cleaning swabs
- Several LC fiber jumpers
- Dust caps

## SAFETY REMINDER
```
⚠️  CRITICAL: Always assume any fiber may be ACTIVE (carrying laser light).
⚠️  NEVER look directly into a fiber connector with the naked eye.
⚠️  ALWAYS use the fiber inspection scope — it safely images the end face.
⚠️  SAFETY GLASSES must be worn during all fiber work.
```

---

### Exercise 2.1 — Fiber Inspection (20 minutes)

**Step-by-step inspection procedure:**

1. Put on safety glasses
2. Power on fiber inspection scope
3. Insert LC adapter for the scope
4. Take Fiber Sample A (intentionally dirty — touched with finger)
5. Insert connector into scope adapter
6. View end face image on screen
7. Complete the inspection form:

```
FIBER INSPECTION FORM

Sample: A
Date: ___________   Technician: ___________

ZONE A (Core):
  Contamination present? YES / NO
  Type: ________________________
  Location on core: ____________

ZONE B (Cladding):
  Contamination present? YES / NO
  Type: ________________________

RESULT:  □ PASS   □ FAIL (needs cleaning)

Cleaning required: YES / NO
```

### Exercise 2.2 — Fiber Cleaning (20 minutes)

**Using a dirty sample from Exercise 2.1:**

**Method A: One-Click Cleaner**
1. Position one-click cleaner at connector end face
2. Press once — the cleaning mechanism advances
3. Re-inspect with scope
4. Record result: PASS / FAIL

**Method B: Wet/Dry (if one-click cleaner insufficient)**
1. Prepare IPA-moistened cleaning swab
2. Insert moistened swab into ferrule cleaning cup
3. Insert dry swab
4. Re-inspect with scope
5. Repeat if needed (max 3 cycles before escalating)

```
CLEANING LOG

Sample: ___   Initial: FAIL
Cleaning Method Used: ______________________
After Cleaning Inspection: PASS / FAIL
Number of cleaning attempts: ___
Final Result: PASS / FAIL
Technician sign-off: ___________________
```

### Exercise 2.3 — Proper Connector Connection (10 minutes)

1. Inspect two fiber connectors (both must PASS inspection)
2. Remove dust caps from both destination ports
3. Insert source connector — verify it clicks into latch
4. Insert destination connector — verify it clicks
5. Observe link light: is it GREEN?
6. Gently wiggle the cable — does the link stay up?
7. Disconnect properly — press latch and pull

**Document:**
```
Pre-connection inspection: PASS / FAIL
Source connector insertion: CLICKED / DID NOT CLICK
Destination connector: CLICKED / DID NOT CLICK
Link light after connection: GREEN / AMBER / NONE
Link stability (wiggle test): STABLE / UNSTABLE
```

---

# LAB 3: CAT6 CABLE IDENTIFICATION AND TESTING

## Objective
Identify CAT6 cable types by color, test connectivity, and verify wiring standard.

## Materials Needed
- Green CAT6 patch cables (various lengths)
- Blue CAT6 patch cables (various lengths)
- RJ45 continuity tester
- RJ45 inline coupler
- Labels and label printer

---

### Exercise 3.1 — Color Code Identification (10 minutes)

Sort the following cables into their correct categories:

```
Cable #1: Yellow jacket, green LC connectors      → ___________________
Cable #2: Green jacket, RJ45 connectors           → ___________________
Cable #3: Blue jacket, RJ45 connectors            → ___________________
Cable #4: Black jacket, QSFP-DD connectors        → ___________________

ANSWERS:
Cable #1 → Single Mode Fiber (SMF)
Cable #2 → CAT6 Data cable (rack-to-rack or management)
Cable #3 → CAT6 Management/PDU cable
Cable #4 → AEC / Rocky cable
```

### Exercise 3.2 — Blue Cable Assignment (10 minutes)

You are given 3 blue CAT6 cables entering a rack from the overhead tray. Assign them to their correct destinations:

```
Given cables: Blue #1, Blue #2, Blue #3

Assignment rules:
Blue #___ → PDU-A management port
Blue #___ → PDU-B management port
Blue #___ → Rack Management switch

ANSWER: Blue #1 → PDU-A, Blue #2 → PDU-B, Blue #3 → Rack Management
```

### Exercise 3.3 — CAT6 Continuity Test (20 minutes)

1. Take a green CAT6 patch cable of approximately 3 meters
2. Plug both ends into a RJ45 continuity tester
3. Power on tester
4. Observe LED sequence:
   - Pins 1 through 8 should light in sequence: 1-2-3-4-5-6-7-8
5. A crossed pin indicates a wiring error

```
PIN TEST RESULTS:
Pin 1: PASS / FAIL
Pin 2: PASS / FAIL
Pin 3: PASS / FAIL
Pin 4: PASS / FAIL
Pin 5: PASS / FAIL
Pin 6: PASS / FAIL
Pin 7: PASS / FAIL
Pin 8: PASS / FAIL

Overall: PASS / FAIL
If fail — which pin failed? ___
Likely cause: ___________________
```

### Exercise 3.4 — Cable Labeling (15 minutes)

You have installed a new green CAT6 cable from DH20-SW1-P01 to DH21-SW1-P01.

1. Write the label for the source end:
   `____________________`

2. Write the label for the destination end:
   `____________________`

3. Print labels using label printer (Brady or Dymo)
4. Apply labels to connector boot, facing outward
5. Verify labels are readable from the front of the rack without moving cables

**ANSWER:**
```
Source end label:      DH20-SW1-P01 → DH21-SW1-P01
Destination end label: DH21-SW1-P01 → DH20-SW1-P01
```

---

# LAB 4: PDU POWER ARCHITECTURE SIMULATION

## Objective
Understand dual power architecture, load balancing, and PDU management.

## Materials Needed
- PDU load calculation worksheet
- Calculator
- Pen/paper

---

### Exercise 4.1 — Load Balance Calculation (20 minutes)

Given the following data for Rack DH20:

**Current PDU loads (before new server):**
- PDU-A: 11.5 Amps (from 20A circuit)
- PDU-B: 8.8 Amps (from 20A circuit)

**New server specs:**
- PSU-1 max draw: 1.5 Amps
- PSU-2 max draw: 1.5 Amps
- Plan: PSU-1 → PDU-A, PSU-2 → PDU-B

**Calculate:**
```
PDU-A current load %: (11.5 / 20) × 100 = ____%
PDU-B current load %: (8.8 / 20) × 100 = ____%

After adding new server:
PDU-A new load: 11.5 + 1.5 = ___ Amps
PDU-A new load %: (___ / 20) × 100 = ____%

PDU-B new load: 8.8 + 1.5 = ___ Amps
PDU-B new load %: (___ / 20) × 100 = ____%

Is it SAFE to add this server?
PDU-A after: ___% (must be ≤ 50%)
PDU-B after: ___% (must be ≤ 50%)

ANSWER:
PDU-A before: 57.5% — ALREADY OVER 50%!
This requires escalation before adding any more servers!
```

### Exercise 4.2 — Failure Scenario Analysis (15 minutes)

**Scenario:** Rack DH22 has 8 servers with the following configuration:
- All servers have PSU-1 connected to PDU-A
- All servers have PSU-2 connected to PDU-B
- PDU-A carries: 16.5A / 20A = 82.5%
- PDU-B carries: 16.5A / 20A = 82.5%

**Question 1:** If PDU-A loses power, what happens?
```
Answer: ________________________________________________
(PSU-2 on PDU-B will carry full load. 
PDU-B would need to supply 16.5+16.5 = 33A from a 20A circuit → OVERLOAD!
All servers would lose power when PDU-B circuit breaker trips.)
```

**Question 2:** How could this situation have been prevented?
```
Answer: ________________________________________________
(Keep each PDU at ≤50% load. With 82.5% on each PDU, failure of one
PDU would overload the other. Maximum acceptable = 50% per PDU.)
```

**Question 3:** What is the maximum load per server (equally distributed) to safely maintain the 50% rule on a 20A PDU feeding 8 servers?
```
Calculation:
20A × 50% = 10A maximum total per PDU
10A ÷ 8 servers = 1.25A maximum per PSU per server
```

---

# LAB 5: COMPLETE RACK CABLING EXERCISE

## Objective
Cable a simulated rack from scratch following all standards.

## Materials Needed
- Rack cabinet (physical or simulated with cardboard/markers)
- Fiber jumpers (yellow, LC-LC)
- CAT6 cables (green and blue)
- VCM and HCM (physical or simulated)
- Velcro straps
- Label printer
- ESD wrist strap

---

### Exercise 5.1 — Pre-Cable Preparation (15 minutes)

1. Verify ESD wrist strap is worn and connected
2. Install VCM (Vertical Cable Manager) on the right side of rack
3. Install HCM (Horizontal Cable Manager) at rack units: 7, 14, 21, 28, 35
4. Install blanking panels in all empty rack units
5. Document: are all blanking panels installed? YES / NO

### Exercise 5.2 — Cable Path Planning (15 minutes)

Before touching any cables, plan your route:

```
CABLE ROUTING PLAN for Rack DH25

Cable Type          From                  To                Route
─────────────────────────────────────────────────────────────────────
Yellow SMF #1       Overhead Tray         U14 SW Port 1     VCM→HCM@U14
Yellow SMF #2       Overhead Tray         U14 SW Port 2     VCM→HCM@U14
Green CAT6 #1       Overhead Tray         U10 Server Port   VCM→HCM@U10
Blue CAT6 #1(PDU-A) Overhead Tray         PDU-A Mgmt Port   VCM→Rear
Blue CAT6 #2(PDU-B) Overhead Tray         PDU-B Mgmt Port   VCM→Rear
Blue CAT6 #3(Mgmt)  Overhead Tray         U1 Mgmt Switch    VCM→HCM@U1
```

### Exercise 5.3 — Cable Dressing Execution (30 minutes)

1. **Start with fiber** — Run yellow SMF cables first
   - Route from overhead tray entry, down VCM
   - Secure with Velcro every 12 inches
   - Check bend radius at top-entry curve — minimum 30mm
   - Branch off at U14 level via HCM
   - Connect to switch port (inspect and clean connectors first!)

2. **Run copper cables next** — Keep separate from fiber in VCM
   - Green CAT6 → route in separate VCM section from fiber
   - Blue CAT6 cables → route to PDU ports and management switch

3. **Final dressing check:**
   - Can you individually trace each fiber cable? YES / NO
   - Are all Velcro straps in place? YES / NO
   - Is the minimum fiber bend radius maintained? YES / NO
   - Are all cables labeled at both ends? YES / NO
   - Are all connections making link lights? YES / NO

### Exercise 5.4 — QC Sign-Off (10 minutes)

Complete the QC checklist:

```
QUALITY CONTROL SIGN-OFF — Rack DH25

LABELS:
  □ All fiber cables labeled at both ends
  □ All CAT6 cables labeled at both ends
  □ Labels are legible and permanent
  □ Labels match work order specifications

FIBER:
  □ All connectors inspected before connection
  □ All connectors cleaned if needed
  □ Dust caps on all unused ports
  □ No visible bend radius violations
  □ Velcro straps every 12-18 inches

COPPER:
  □ Blue cables: PDU-A, PDU-B, Management correctly assigned
  □ Green cables: routed to correct destination
  □ No cables draped across equipment faces

POWER:
  □ PDU-A management port connected (Blue #1)
  □ PDU-B management port connected (Blue #2)
  □ Rack management connected (Blue #3)

VERIFICATION:
  □ Link lights active on all connections
  □ Rack doors close fully
  □ No cables on rack floor
  □ All blanking panels in place

Technician signature: ___________________   Date: ___________
Supervisor signature: ___________________   Date: ___________
```

---

# LAB 6: IPMI MANAGEMENT SIMULATION

## Objective
Practice IPMI command usage for remote server management.

## Materials Needed
- Computer with ipmitool installed
- Access to test BMC/IPMI system (lab environment)
- IPMI credentials (provided by instructor)

---

### Exercise 6.1 — Connect to BMC (5 minutes)

```bash
# Test connectivity to BMC
ping 192.168.10.50   # Replace with actual lab BMC IP

# Check IPMI version and info
ipmitool -H 192.168.10.50 -U admin -P Lab@1234 mc info
```

**Record results:**
```
BMC firmware version: ___________
IPMI version: ___________
Device name: ___________
```

### Exercise 6.2 — Power Status Check (5 minutes)

```bash
ipmitool -H 192.168.10.50 -U admin -P Lab@1234 power status
```

**Record:**
```
Current power status: ON / OFF
```

### Exercise 6.3 — Sensor Readings (10 minutes)

```bash
# Get all sensor data
ipmitool -H 192.168.10.50 -U admin -P Lab@1234 sdr list

# Get CPU temperature specifically
ipmitool -H 192.168.10.50 -U admin -P Lab@1234 sdr type Temperature

# Get fan speeds
ipmitool -H 192.168.10.50 -U admin -P Lab@1234 sdr type Fan
```

**Record findings:**
```
CPU Temperature: _______ °C    Status: Normal / Warning / Critical
Fan 1 Speed: _______ RPM       Status: Normal / Warning / Failed
Fan 2 Speed: _______ RPM       Status: Normal / Warning / Failed
```

### Exercise 6.4 — System Event Log Review (10 minutes)

```bash
# Get last 10 system events
ipmitool -H 192.168.10.50 -U admin -P Lab@1234 sel list last 10
```

**Record the most recent 3 events:**
```
Event 1: Date/Time ___________  Type: ___________  Status: ___________
Event 2: Date/Time ___________  Type: ___________  Status: ___________
Event 3: Date/Time ___________  Type: ___________  Status: ___________
```

---

# LAB 7: TROUBLESHOOTING SCENARIOS

## Objective
Apply troubleshooting methodology to realistic data center scenarios.

---

### Scenario 7.1 — Dark Fiber Link

**Situation:** A fiber link between DH20 and SCA-P44 has gone dark. No traffic is passing.

**Using the troubleshooting methodology:**

Step 1: What is the first physical check you perform?
```
Answer: ________________________________________________
(Check that both connectors are fully seated and latched)
```

Step 2: Both connectors appear seated. What next?
```
Answer: ________________________________________________
(Inspect both fiber end faces with FOSI scope)
```

Step 3: Inspection shows Zone A contamination on the DH20 end. What do you do?
```
Answer: ________________________________________________
(Clean with one-click cleaner, re-inspect, connect, verify link light)
```

Step 4: After cleaning, link light is still absent. What next?
```
Answer: ________________________________________________
(Try a known-good fiber jumper to isolate cable vs port failure;
check transceiver seating; verify wavelength compatibility;
measure optical power at far end with optical power meter)
```

### Scenario 7.2 — Server Not Reachable

**Situation:** Server at DH20, U24 is not responding to pings on the production network.

**Using IPMI to diagnose:**

Step 1: Can you reach the BMC management IP?
```
If YES → ____________________  (proceed to Step 2)
If NO →  ____________________  (BMC itself unreachable — check management cable)
```

Step 2: Check power status via IPMI. Result: "Power OFF"
```
Next step: ________________________________________________
(Investigate WHY it's off before powering on — check SEL first!)
```

Step 3: SEL shows "System power loss" at 2:15 AM. Check PDU.
```
PDU-A circuit breaker status: ___________________________
PDU-B circuit breaker status: ___________________________
Action if one breaker tripped: _________________________
```

### Scenario 7.3 — Incorrect Label Found

**Situation:** During auditing, you find a cable labeled "DH20-SW1-P14T → SCA-P44D" but when you trace the cable physically, it actually goes to SCA-P45D (not P44D).

**What do you do?**

```
Step 1: ________________________________________________
(Verify your trace is correct — re-trace cable a second time)

Step 2: ________________________________________________
(Check DCIM to see what the system shows for both P44D and P45D)

Step 3: ________________________________________________
(If DCIM shows P44D but cable is at P45D, report the discrepancy)

Step 4: ________________________________________________
(Create a DCIM update ticket, update the correct port information,
print and apply new accurate labels at both ends)

NEVER move or change the cable itself without a proper change ticket!
```

---

# LAB COMPLETION CRITERIA

A student passes each lab by demonstrating:

| Lab | Passing Criteria |
|-----|-----------------|
| Lab 1 | Correctly decodes all labels; accurately traces cable path |
| Lab 2 | Correctly identifies dirty/clean connectors; successfully cleans to PASS |
| Lab 3 | Cables correctly identified; continuity test performed correctly; labels applied |
| Lab 4 | Load calculations correct; failure scenarios correctly analyzed |
| Lab 5 | QC sign-off checklist complete; supervisor verification of physical work |
| Lab 6 | All IPMI commands executed; results recorded; interpretation correct |
| Lab 7 | All scenarios solved with correct methodology documented |

---

*End of Practical Lab Exercises*  
*Students must complete all 7 labs before the certification exam.*
