# DATA CENTER TROUBLESHOOTING GUIDE
## Comprehensive Problem-Solving Reference
### xAI-Style Data Center Environment

---

## HOW TO USE THIS GUIDE

This guide follows a structured troubleshooting methodology:

1. **IDENTIFY** the symptom (what is wrong?)
2. **ISOLATE** the scope (what is affected — one server? one rack? one link?)
3. **INVESTIGATE** systematically (check most likely causes first)
4. **IMPLEMENT** a fix (with proper change ticket)
5. **VERIFY** the fix worked
6. **DOCUMENT** everything

```
GOLDEN RULE OF DATA CENTER TROUBLESHOOTING:
"Never assume. Always verify."

Before touching anything, gather information.
Before changing anything, have a change ticket.
After changing anything, verify and document.
```

---

# SECTION 1: FIBER OPTIC TROUBLESHOOTING

## Problem 1.1: No Link Light After Fiber Connection

**Symptoms:** Port shows "down" or no link LED after patching fiber.

**Diagnostic Flowchart:**

```
FIBER LINK DOWN
      │
      ▼
Check: Are both connectors fully seated?
      │
   YES ──────────────────────────────────────►─────────────────
      │                                                         │
      NO                                              Check: Transceivers
      │                                               fully seated?
      ▼                                                         │
Re-seat both connectors.                           NO → Re-seat transceivers
Check link light again.                                         │
Still down? Continue ↓                             YES ↓
                                                               │
                                              ▼
                                   Inspect both fiber end faces
                                   with FOSI scope
                                              │
                                   Dirty? → Clean → Re-inspect
                                   Clean? → Continue ↓
                                              │
                                              ▼
                                   Try known-good fiber jumper
                                              │
                                   Link UP? → Original cable failed
                                   Link DOWN? → Port or transceiver issue
                                              │
                                              ▼
                                   Swap transceiver with known-good
                                              │
                                   Link UP? → Transceiver failed
                                   Link DOWN? → Switch port hardware issue
                                   → Escalate to network team
```

**Checklist for No-Link Investigation:**
- [ ] Both connectors clicked into latch position
- [ ] Dust caps removed from both sides (seems obvious but often missed)
- [ ] Fiber end faces inspected — Zone A clean on both connectors
- [ ] Transceivers fully seated in both ends
- [ ] Transceiver type matches (1310nm vs 1310nm; not 1310nm vs 1550nm)
- [ ] Cable polarity correct (TX to RX, RX to TX) for LC duplex
- [ ] Fiber jumper swapped with known-good cable
- [ ] No obvious physical damage (kink, sharp bend, crush point) in cable path

---

## Problem 1.2: Intermittent Fiber Link

**Symptoms:** Link goes up and down without physical intervention; errors visible in interface statistics.

**Most Common Causes:**

| Cause | Symptom Pattern | Fix |
|-------|----------------|-----|
| Partially dirty connector | Link drops when rack vibrates | Clean all connectors |
| Loose connector latch | Drops when anyone works near rack | Push firmly until click |
| Fiber bent near minimum radius | Correlates with temperature changes (thermal expansion) | Re-route with proper bend radius |
| Failing transceiver | Gradual degradation, increasingly frequent drops | Replace transceiver |
| Near end-of-life fiber | Cracks along cable path | Inspect full cable run with OTDR |

**Investigation Steps:**
1. Note the pattern — when does it drop? When servers in the rack vibrate? When HVAC cycles on/off?
2. Inspect all connectors with FOSI on both ends — look for contamination on cladding (may move when vibrated)
3. Check optical receive power — is it marginally above minimum? (Near the cliff edge means small disturbances cause drops)
4. Walk the cable path looking for sharp bends, cable zip ties too tight, or cable routed under heavier cables
5. If OTDR available, run OTDR test to locate any anomaly along fiber path

---

## Problem 1.3: Fiber Link Up but High Error Rate

**Symptoms:** Physical link is up but network shows high bit error rate (BER), packet loss, or slow performance.

**Diagnostic Steps:**

1. **Check optical power levels:**
   - Use optical power meter at both TX and RX ends
   - Compare received power to transceiver's minimum receiver sensitivity
   - If received power is within 2dB of minimum threshold, you have a marginal link

2. **Check connector polish type mismatch:**
   - APC connectors (green, angled) must connect to APC
   - UPC connectors (blue/green, flat) must connect to UPC
   - Mixing APC and UPC causes high return loss, which degrades signal

3. **Verify loss budget:**
   ```
   Acceptable total loss = TX power - Receiver sensitivity
   Example: TX = +5dBm, Rx sensitivity = -25dBm → Budget = 30dB
   
   Calculate actual losses:
   - Each LC connector pair: ~0.3dB
   - Each splice: ~0.1dB
   - Fiber per km at 1310nm: 0.4dB/km
   
   If actual losses > budget → Link will be error-prone or fail
   ```

4. **Check for damaged fiber:**
   - Look for pinch points, sharp bends, or crush damage
   - Small amounts of fiber damage cause scattering losses

---

## Problem 1.4: Cannot Clean Fiber to Pass Inspection

**Symptoms:** Zone A contamination persists after multiple cleaning attempts.

**Protocol:**
1. Maximum 3 cleaning attempts with one-click cleaner
2. If still failing, try wet/dry method (IPA + swab, then dry swab)
3. Still failing? The connector may be physically scratched
4. Use fiber inspection scope at higher magnification to distinguish between:
   - **Contamination** (can be cleaned) — appears as particles/smears
   - **Scratches** (cannot be cleaned) — appear as lines across the core
5. A scratched connector must be replaced (new fiber jumper or re-polish/re-terminate if trained)

---

# SECTION 2: CAT6 AND COPPER TROUBLESHOOTING

## Problem 2.1: CAT6 Link Not Coming Up

**Diagnostic Steps:**

1. **Physical verification:**
   - Is the RJ45 connector firmly clicked into the port?
   - Is the latch (tab) broken on the RJ45? If so, replace cable.
   - Is the link LED lit on the switch port?

2. **Continuity test:**
   - Use RJ45 cable tester
   - All 8 pins must pass
   - Pay attention to pin sequence: straight-through (1-2-3-4-5-6-7-8 both ends)

3. **Common wiring faults:**
   ```
   FAULT TYPE          TESTER SHOWS           CAUSE
   ─────────────────────────────────────────────────────────
   Open               Pin(s) fail completely  Broken wire or bad crimp
   Short              Two pins light together  Wires touching
   Crossed pair       Pins out of sequence    Wrong wiring standard
   Split pair         Marginal pass, high NEXT Pairs split to wrong pins
   Wrong standard     Pins 1-2 swap with 3-6   T568A vs T568B mismatch
   ```

4. **Network-layer issues (cable passes physical test):**
   - Verify switch port is not disabled or in error-disable state
   - Check VLAN assignment
   - Check speed/duplex configuration (auto-negotiate vs hardcoded mismatch)
   - Verify MAC address is not blocked by port security

---

## Problem 2.2: PDU Management Not Reachable

**Symptoms:** Blue CAT6 cable to PDU-A or PDU-B management port is not registering in PDU management system.

**Investigation Flow:**

```
PDU MANAGEMENT UNREACHABLE
         │
         ▼
Check: Is the blue CAT6 (Cable #1 for PDU-A, #2 for PDU-B) connected
       to the PDU management port AND to the management switch?
         │
  NOT CONNECTED → Connect and verify
         │
     CONNECTED ↓
         │
         ▼
Check: Is the management port LED on the PDU illuminated?
         │
  LED OFF → Try a different patch cable (cable may be faulty)
         │
  LED ON ↓
         │
         ▼
Check: Is the PDU configured with the correct IP address?
       (Physical button/display on PDU may show current IP)
         │
  WRONG IP → Follow PDU vendor procedure to set correct IP
         │
  CORRECT IP ↓
         │
         ▼
Check: Is the management switch port configured for the
       correct VLAN and speed?
         │
  Check with network team → configure port correctly
```

---

# SECTION 3: POWER AND PDU TROUBLESHOOTING

## Problem 3.1: Server Will Not Power On

**Step 1: Check Physical Power Connections**
- Both PSU cables must be connected: PSU-1 → PDU-A outlet; PSU-2 → PDU-B outlet
- Check that power cables are fully seated at both PDU outlet and PSU inlet
- Verify PDU-A and PDU-B circuit breakers are NOT tripped

**Step 2: Check PDU Circuit Breaker**
- Walk to the rear of the rack
- Visually inspect PDU-A and PDU-B circuit breakers
- Tripped breaker = switch in middle position or fully "off" position
- Reset procedure (with change ticket): Push breaker fully to "off" position, then firmly to "on"

**Step 3: Verify via IPMI (if BMC is reachable)**
```bash
ipmitool -H <BMC_IP> -U admin -P password power status
# If "Chassis Power is off" → power on command:
ipmitool -H <BMC_IP> -U admin -P password power on
```

**Step 4: Check SEL for Power Events**
```bash
ipmitool -H <BMC_IP> -U admin -P password sel list
# Look for: "System power loss", "AC loss", "System power off"
```

**Step 5: Hardware Issues**
If power is available at PDU but server still won't power on:
- PSU may have failed (usually indicated by amber PSU LED on server rear)
- Motherboard may have failed
- BMC may need firmware recovery
- Escalate to hardware replacement team

---

## Problem 3.2: Server Unexpectedly Shut Down

**Immediate actions:**
1. Do NOT power it back on immediately — investigate first
2. Check IPMI SEL for shutdown reason:

```
COMMON SEL EVENTS AND MEANINGS:

"Critical interrupt" → Hardware error (memory, PCIe, CPU fault)
"Temperature" critical → Thermal shutdown — check cooling before restart
"Voltage" event → Power quality issue — check UPS and power
"Fan failure" → Cooling insufficient — check fans before restart
"System power loss" → PDU or upstream power issue
"Graceful shutdown" → OS-initiated (normal OS halt, kernel panic)
"Hard reset" → Watchdog or IPMI reset command
```

3. Never restart after thermal shutdown without resolving the thermal issue
4. Check current temperature sensors: `ipmitool sdr type Temperature`
5. If temperature is normal → investigate root cause before assuming safe restart

---

## Problem 3.3: PDU Circuit Breaker Keeps Tripping

**This is a CRITICAL condition requiring immediate escalation.**

**Immediate actions:**
1. Do NOT reset the breaker again without investigation
2. Calculate current PDU load vs. circuit rating:
   - Sum all active outlets' current draws
   - If total draw exceeds ~80% of breaker rating, the circuit is overloaded
3. Identify which outlets/servers are contributing most
4. Notify management and facilities/electrical team

**Do NOT:**
- Replace the breaker with a higher-rated one without engineering approval
- Keep resetting a tripping breaker — this indicates a real electrical problem
- Add any load to that PDU until the issue is resolved

---

# SECTION 4: RACK AND PHYSICAL TROUBLESHOOTING

## Problem 4.1: Cannot Locate a Specific Rack

**Symptoms:** Technician cannot find rack DH20 or similar.

**Solution:**
1. Consult the floor plan in the DCIM system
2. Use the aisle/row/position naming convention:
   - Row letters: aisles are labeled A, B, C... or corridors are numbered
   - In DH20: D = Data Hall section, H = Column H, 20 = position 20 in that column
3. Physical racks have labels on the front AND rear doors at eye level
4. If floor plan is not available, walk the rows methodically reading labels

---

## Problem 4.2: Equipment Overheating

**Symptoms:** Temperature alarms from servers in a specific rack; server thermal shutdowns.

**Investigation:**

```
OVERHEATING DIAGNOSIS TREE

Is only ONE server overheating?
         │
         YES → Check: Is that server's fan all running?
               Check: Is the airflow direction correct for that server?
               Check: Is dust blocking this server's intake?
               
         NO → Multiple/all servers in rack are hot?
               │
               ▼
               Check: Are blanking panels in all empty rack spaces?
               Check: Is there an open gap in the rack (missing server, no blanking panel)?
               Check: Is the front rack door closed? (must be closed for hot aisle containment)
               Check: Is the CRAC/CRAH unit for this row operational?
               Check: Is the cold aisle fully enclosed (containment doors closed)?
               Check: Are cable bundles blocking airflow through the rack?
```

**Hot air recirculation — the #1 cause of rack overheating:**
- When blanking panels are missing, hot air from the rear of the rack recirculates to the front intakes
- Even one missing blanking panel in a dense AI rack can raise inlet temperature by several degrees
- Solution: Install all missing blanking panels immediately

---

## Problem 4.3: Cable Cannot Be Traced

**Symptoms:** Technician cannot identify where a cable goes or where it comes from.

**Tracing Procedure:**

For fiber:
1. Using a fiber tone tool (NOT A LASER — some tone tools use visible red light at safe power levels for tracing)
2. Inject tone at one end of the cable
3. Walk the suspected path with a fiber tone detector
4. The cable carrying the tone will be detected

For CAT6:
1. Use a network cable tracer/toner
2. Inject tone from one end
3. Use the tracer probe along cable paths — the loudest tone indicates the cable

**When physical tracing is impossible:**
1. Check DCIM — if the cable was documented, the DCIM will show both ends
2. Disconnect one end and check which network port loses link (visible as port going down in network management)
3. Note: Never disconnect a cable without a change ticket and understanding of what it connects

---

# SECTION 5: IPMI TROUBLESHOOTING

## Problem 5.1: Cannot Reach BMC Management IP

**Investigation Steps:**

1. Verify the BMC network cable is connected:
   - Is blue CAT6 #3 (Rack Management) connected from the overhead tray to the management switch in the rack?
   - Is the BMC port on the server (usually labeled "MGMT" or "iDRAC" or "iLO") connected to the correct switch port?

2. Verify the management switch port is active:
   - Check if the link LED on the management switch port is lit
   - Check if the management switch port is configured for the correct VLAN

3. Verify BMC IP configuration:
   - BMC IP address may not be configured
   - Connect physical keyboard and display to server if needed to access BMC setup
   - Or use ipmitool via the server's OS (in-band) to check BMC IP: `ipmitool lan print 1`

4. Verify routing:
   - Are you on the correct management VLAN?
   - Can you ping other BMCs in the same rack? If yes, this specific BMC may have wrong IP.

---

## Problem 5.2: IPMI SEL Shows Hardware Errors

**Common Hardware Errors and Responses:**

| SEL Error | Meaning | Response |
|-----------|---------|----------|
| CPU Machine Check Error | CPU hardware fault | Document; may need CPU or motherboard replacement |
| DIMM ECC Uncorrectable | Memory failure | Replace failed DIMM module (check which DIMM from BMC) |
| PCIe Slot Error | GPU or card failure | Check GPU/card seating; replace if necessary |
| PSU Failure | Power supply hardware fault | Replace PSU (dual-supply = hot-swap possible) |
| Fan Fault | Fan hardware failure | Replace fan (identify which fan from SEL/sensor) |
| Storage Device Failure | Drive failure | Replace drive per standard drive replacement procedure |
| VR (Voltage Regulator) Fault | Motherboard power circuitry issue | Likely motherboard replacement needed |
| Thermal Shutdown | CPU/system temp exceeded limit | Fix cooling before restart |

---

# SECTION 6: DOCUMENTATION TROUBLESHOOTING

## Problem 6.1: DCIM Doesn't Match Physical Reality

**Symptoms:** Cable documented in DCIM as going to Port A, but physically it goes to Port B.

**Resolution Procedure:**

1. Physically re-verify both ends of the cable (trace it completely)
2. Document your findings: what DCIM shows vs. what is physically present
3. Create a discrepancy ticket in the ticketing system
4. Determine the correct state (what should it be?)
   - If physical is wrong: create change ticket to move cable to correct port
   - If DCIM is wrong: create a documentation update ticket
5. After confirming and correcting, update DCIM and mark discrepancy ticket resolved
6. **NEVER change DCIM to match an incorrect physical state** without confirming which state is correct

---

## Problem 6.2: Missing Labels

**Symptoms:** Cable(s) found with no label or illegible label.

**Response Procedure:**

1. Do NOT remove or move cables during investigation
2. Trace the cable(s) to both ends
3. Identify source and destination from physical port positions and DCIM lookup
4. If DCIM has the connection documented: print accurate labels and apply
5. If DCIM does NOT have the connection: document the discovery, trace what devices are connected, update DCIM, then apply labels
6. Flag the situation if it represents a significant undocumented change (could indicate unauthorized work)

---

# SECTION 7: QUICK REFERENCE TROUBLESHOOTING TABLES

## Fiber Quick Reference

| Symptom | Most Likely Cause | First Action |
|---------|------------------|-------------|
| No link after patch | Dirty connector | Inspect with FOSI scope |
| Intermittent drops | Loose connector or dirty | Re-seat firmly; inspect/clean |
| Link up, high errors | Near-threshold power | Measure optical power |
| Cannot clean to PASS | Scratched connector | Replace fiber jumper |
| Link down after move | Bent below radius | Check cable routing |

## Copper Quick Reference

| Symptom | Most Likely Cause | First Action |
|---------|------------------|-------------|
| No link after patch | Bad connector crimp | Test continuity |
| Intermittent drops | Partially-made crimp | Test and replace cable |
| Slow speed | Duplex mismatch | Check port settings |
| PDU mgmt unreachable | Wrong VLAN | Check switch port config |

## Power Quick Reference

| Symptom | Most Likely Cause | First Action |
|---------|------------------|-------------|
| Server won't power on | PDU breaker tripped | Check PDU breakers |
| Unexpected shutdown | Thermal or power event | Check IPMI SEL |
| Breaker keeps tripping | Overloaded circuit | Calculate load vs. rating |
| PDU at 85% load | Too many servers | Load rebalancing needed |

## Physical Quick Reference

| Symptom | Most Likely Cause | First Action |
|---------|------------------|-------------|
| Servers overheating | Missing blanking panels | Inspect rack for gaps |
| Cannot trace cable | No labels | Use tone tracer + DCIM |
| Server won't slide in | Wrong U position | Re-measure from bottom |
| Door won't close | Cable in the way | Re-dress cables |

---

*End of Troubleshooting Guide*  
*When in doubt, stop and ask. The cost of asking is low. The cost of a mistake is high.*
