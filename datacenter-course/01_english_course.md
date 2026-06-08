# DATA CENTER TECHNICIAN TRAINING COURSE
## Professional Training Manual — English Version
### Based on xAI-Style Data Center Environment

---

**Course Level:** Beginner to Intermediate  
**Target Audience:** New Data Center Technicians  
**Environment:** Modern AI-Scale Data Center  
**Version:** 1.0  

---

## TABLE OF CONTENTS

1. Introduction to Data Centers
2. Data Center Safety
3. Rack Cabinets — Structure and Navigation
4. Single Mode Fiber Optics
5. SU Cabinets and Architecture
6. Supercore Infrastructure
7. IPMI Management Infrastructure
8. CAT6 Copper Cabling
9. Blue CAT6 and PDU Connections
10. PDU — Power Distribution Units
11. AEC Cables — Active Electrical Cables
12. Rocky Cables
13. Label Reading and Interpretation
14. Cable Dressing Standards
15. Quality Control Procedures
16. Real-World Technician Daily Work
17. Documentation and Reporting
18. Final Certification Review

---

# MODULE 1: INTRODUCTION TO DATA CENTERS

## Lesson 1.1 — What Is a Data Center?

### Theory

A data center is a physical facility that houses computer systems, networking equipment, storage systems, and the supporting infrastructure needed to operate them continuously. Modern AI-scale data centers like those built by xAI, Meta, Google, and Amazon can contain tens of thousands of servers running 24 hours a day, 7 days a week, 365 days a year.

### Real-World Explanation

Think of a data center as the "brain" behind every app, website, and AI model you use. When you search something on the internet, send a message, or use an AI assistant, your request travels to a data center somewhere in the world, gets processed by servers, and sends back an answer — all within milliseconds.

As a Data Center Technician, you are the person who physically installs, maintains, connects, labels, and troubleshoots all the equipment that makes this possible.

### The xAI-Style Environment

In a modern AI data center (like xAI's Colossus facility in Memphis, Tennessee), the environment is built specifically to run massive AI workloads. This means:

- Extremely dense GPU server deployments
- High-speed interconnects between servers
- Redundant power systems
- Complex fiber optic networking
- Strict cable management standards
- Precise labeling systems

Everything you do as a technician in this environment has a direct impact on whether thousands of AI computations succeed or fail.

### Photo Explanation Section

When you walk into a modern data center floor, you will see:

1. **Rows of tall metal cabinets** — These are rack cabinets, each holding multiple servers
2. **Overhead cable trays** — Metal trays mounted near the ceiling carrying thousands of cables
3. **Colorful cables** — Yellow fibers, green CAT6, blue CAT6, black AEC cables
4. **Blinking LEDs** — Status lights showing whether equipment is operating normally
5. **Cold/Hot aisles** — Alternating rows that direct airflow for cooling

### Terminology

| Term | Definition |
|------|-----------|
| **Data Center** | A facility housing computing infrastructure |
| **Server** | A computer that provides services to other computers |
| **Rack** | A metal cabinet that holds servers and networking equipment |
| **Uptime** | The percentage of time a system is operational |
| **SLA** | Service Level Agreement — guaranteed uptime targets |
| **Redundancy** | Having backup systems so one failure doesn't cause an outage |
| **Hot Aisle** | The aisle where hot exhaust air from servers exits |
| **Cold Aisle** | The aisle where cold supply air enters servers |
| **Overhead Tray** | Metal channel above racks carrying cables |
| **Patch** | The act of connecting a cable between two ports |

### Practical Example

A senior technician receives a ticket: "Server rack DH20, unit 14, is offline." As a new technician observing, you note:

1. The senior locates rack DH20 using the label system
2. They count rack units from the bottom to unit 14
3. They check the power LEDs — all off
4. They trace the power cable back to the PDU
5. They find a tripped circuit breaker on PDU-A
6. They reset the breaker and power is restored

This simple scenario involves label reading, rack unit navigation, power tracing, and PDU understanding — all topics in this course.

### Troubleshooting Section

**Common Issue:** New technician cannot find a specific rack.  
**Solution:** Learn the label naming convention. Racks are labeled with letters and numbers (DH20, NA05, etc.). Row letters indicate the cabinet row; numbers indicate position in that row.

**Common Issue:** New technician is confused by the many cable colors.  
**Solution:** Each cable color has a specific purpose (covered in detail in later modules). Start by learning: yellow = single mode fiber, green = CAT6 data, blue = CAT6 PDU/management.

### Knowledge Check Questions

1. What is the primary purpose of a data center?
2. What does "redundancy" mean in data center context?
3. What is the difference between a hot aisle and cold aisle?
4. What does a Data Center Technician do daily?
5. Why is proper labeling important in a data center?

### Module 1 Quiz

**Q1.** A data center provides which of the following?
- A) Housing for employees
- B) Housing for computing infrastructure ✓
- C) Power generation for cities
- D) Internet service to homes

**Q2.** What does "uptime" measure?
- A) Server processing speed
- B) How high a rack is
- C) The percentage of time a system is operational ✓
- D) The temperature of a server room

**Q3.** In an AI data center, AEC cables are primarily used for:
- A) Power distribution
- B) High-speed server interconnects ✓
- C) Management access
- D) Building lighting

**Q4.** What is a PDU?
- A) A type of server processor
- B) Power Distribution Unit ✓
- C) A fiber optic connector
- D) Protocol Data Unit (in this context)

**Q5.** Which cable color typically indicates Single Mode Fiber?
- A) Blue
- B) Green
- C) Yellow ✓
- D) Red

---

# MODULE 2: DATA CENTER SAFETY

## Lesson 2.1 — Safety Fundamentals

### Theory

Data center safety encompasses electrical safety, physical safety, fire safety, and procedural safety. A large data center may have tens of megawatts of live electrical power running continuously. Failure to follow safety procedures can result in serious injury, death, equipment damage, or data loss affecting millions of users.

### Real-World Explanation

You are working in an environment where:
- Individual rack cabinets may draw 15–30 kilowatts of power
- A full row of racks can consume hundreds of kilowatts
- Fiber cables, when bent or damaged, can expose hazardous laser light
- Heavy equipment (servers can weigh 30–60 lbs each) must be lifted safely
- Static electricity can destroy sensitive electronics worth thousands of dollars

### Safety Rules for Data Center Technicians

**Rule 1: Always wear your ESD wrist strap when handling equipment**
Electrostatic discharge (ESD) can instantly destroy server components. Always connect your ESD strap to a grounded point before touching any PCB, memory, drive, or network card.

**Rule 2: Never open live electrical enclosures without authorization**
PDUs and power panels contain live high-voltage electricity. Only qualified electrical staff may work inside these with proper lock-out/tag-out (LOTO) procedures.

**Rule 3: Never look directly into a fiber optic cable end**
Single Mode fiber uses invisible infrared laser light. Looking directly into an active fiber can permanently damage your eyes. Always assume a fiber is active unless you have confirmed it is disconnected from both ends.

**Rule 4: Use proper lifting techniques**
Servers are heavy. Bend at the knees, keep your back straight, and use a two-person lift or a rail-mount lift for heavy equipment (over 35 lbs).

**Rule 5: Keep cables organized and off the floor**
Cables on walkway floors are a serious trip hazard. All cables must be properly routed through cable managers and trays.

**Rule 6: Follow the Change Management process**
Never make changes to live production equipment without an approved change ticket. Unauthorized changes can cause outages affecting the entire data center.

**Rule 7: Maintain aisle integrity**
Hot aisle containment systems keep cold and hot air separated. Never block cold aisle vents, remove blanking panels, or leave rack doors open unnecessarily.

### Terminology

| Term | Definition |
|------|-----------|
| **ESD** | Electrostatic Discharge — static electricity that damages electronics |
| **LOTO** | Lock-Out/Tag-Out — safety procedure for de-energizing equipment |
| **PPE** | Personal Protective Equipment (safety glasses, gloves, etc.) |
| **MSDS** | Material Safety Data Sheet — chemical safety information |
| **Change Ticket** | Documented approval to make a change to infrastructure |
| **Blanking Panel** | Plastic/metal filler panel to block unused rack unit spaces |
| **Hot Aisle Containment** | Physical barriers that separate hot exhaust from cold supply air |

### Practical Example

Before starting any fiber work:
1. Obtain an approved work order
2. Confirm the fiber circuit is dark (no signal) using an optical power meter
3. Put on safety glasses with side shields
4. Use a fiber inspection scope before connecting any fiber
5. Cap all disconnected fiber ends immediately with dust caps
6. Never leave fiber ends exposed or on the floor

### Knowledge Check Questions

1. Why must you never look into an active fiber optic cable?
2. What is ESD and why is it dangerous?
3. When is it acceptable to make changes to live equipment without a change ticket?
4. What is the purpose of blanking panels in a rack?
5. Describe proper lifting technique for a heavy server.

---

# MODULE 3: RACK CABINETS — STRUCTURE AND NAVIGATION

## Lesson 3.1 — Understanding Rack Cabinets

### Theory

A rack cabinet (also called a server rack or equipment rack) is a standardized metal enclosure designed to house and organize computing equipment. The industry standard is the 19-inch rack, defined by the EIA-310 standard. Equipment is measured in "Rack Units" (RU or U), where 1U = 1.75 inches of vertical space.

### Real-World Explanation

Think of a rack cabinet as a very tall, narrow bookshelf designed for computers. Every server, switch, and piece of networking equipment is designed to fit into this standard format. A typical data center rack is:

- **Height:** 42U to 48U (approximately 7 feet tall)
- **Width:** 19 inches between mounting rails (standard)
- **Depth:** 900mm to 1200mm
- **Weight capacity:** 1,000 to 2,500+ lbs

### Cable Entry — The Standard Path

In the xAI-style environment, cables enter racks from overhead trays. The standard cable path is:

```
OVERHEAD CABLE TRAY
        ↓
    TOP ENTRY
   (top of rack)
        ↓
VERTICAL CABLE MANAGER
   (runs down the side
    of the rack interior)
        ↓
HORIZONTAL CABLE MANAGER
   (runs across a specific
    rack unit level)
        ↓
   EQUIPMENT PORTS
  (server, switch, etc.)
```

This top-entry design is used in hot-aisle/cold-aisle environments where cable management must not interfere with airflow.

### Rack Cabinet Components

**1. Mounting Rails (Front and Rear)**
The two vertical rails on the front and rear of the rack where equipment is bolted. Rails have numbered holes (rack unit positions) for easy equipment placement.

**2. Vertical Cable Manager (VCM)**
A vertical channel on one or both sides of the rack interior. Cables from the top entry run down the VCM to their destination level. The VCM keeps cables organized and allows individual cables to branch off at the correct height.

**3. Horizontal Cable Manager (HCM)**
Mounted between equipment in the rack. HCMs guide cables horizontally from the VCM to the equipment ports. They typically have finger ducts or rings to hold cables neatly.

**4. Cable Tray / Brush Strip (Top Entry)**
At the top of the rack, a brush strip or open tray allows cables to enter from the overhead tray. The brush strip prevents pests, maintains fire separation, and guides cables smoothly.

**5. Blanking Panels**
These fill unused rack unit spaces. They are critical for maintaining proper airflow — without them, hot air from the rear circulates back to the front, reducing cooling efficiency.

**6. PDU (Power Distribution Unit)**
Mounted vertically on the rear sides of the rack. PDUs take incoming power and distribute it to individual servers through C13/C19 power outlets.

**7. Rear Cable Managers**
Some racks have rear vertical cable managers for organizing rear-panel connections such as power cords.

### Rack Unit Counting

Rack units are counted **from the bottom up** in most environments (though some facilities count from the top). Always verify the convention used in your facility.

```
42U ← TOP
41U
40U
...
 3U
 2U
 1U ← BOTTOM
```

When a ticket says "Install server at U14," you count 14 units up from the bottom of the rack.

### Photo Explanation Section

When examining a rack cabinet from the front:

1. **Top area:** You should see cables entering through a brush strip or open top. Yellow fibers, green/blue CAT6, and black AEC cables may all enter here.

2. **Vertical Cable Manager (left or right side):** A channel filled with organized cables running vertically. Cables should be bundled with Velcro straps, not zip ties (zip ties can damage fibers).

3. **Horizontal Cable Managers:** Small trays between equipment. Cables should fan out neatly, not hang loosely.

4. **Equipment faces:** Server fronts visible through the rack door. Each server should have a label visible from outside.

5. **Blanking panels:** Any empty rack unit should have a blanking panel. A rack with open gaps indicates incomplete installation or a removed server.

### Terminology

| Term | Definition |
|------|-----------|
| **RU / U** | Rack Unit — 1.75 inches of vertical rack space |
| **19-inch Rack** | Standard rack width (19" between mounting rails) |
| **42U** | A rack that is 42 rack units tall (most common) |
| **VCM** | Vertical Cable Manager |
| **HCM** | Horizontal Cable Manager |
| **Blanking Panel** | Filler for unused rack unit space |
| **PDU** | Power Distribution Unit (rack-mounted) |
| **Brush Strip** | Flexible strip sealing top/bottom cable entry openings |
| **Rail** | Mounting channel inside a rack where equipment slides in |
| **EIA-310** | Industry standard defining rack dimensions |

### Practical Example — Reading a Rack

You receive a work order: "Replace failed drive in server at DH20, U24."

Steps:
1. Locate rack labeled **DH20** in the data center floor map
2. Open the front rack door
3. Count rack units from the bottom: 1, 2, 3... up to 24
4. Identify the server at U24
5. Verify the server label matches the work order
6. Proceed with the drive replacement

### Troubleshooting Section

**Problem:** Cannot find rack unit 24 because rack has no unit markings.  
**Solution:** Use a rack unit ruler or count manually from the bottom. Each U = 1.75 inches.

**Problem:** Equipment doesn't fit — screw holes don't align.  
**Solution:** Check if the rack uses square holes (cage nuts needed) or round holes (screws go directly in). Also check if you are measuring from front or rear rails.

**Problem:** After removing a server, the nearby servers are getting hot.  
**Solution:** Install blanking panels immediately in the empty space to prevent hot air recirculation.

### Knowledge Check Questions

1. What does "1U" represent in rack measurements?
2. Describe the cable path from overhead tray to equipment port.
3. Why are blanking panels important?
4. Where are PDUs typically mounted inside a rack?
5. How do you locate rack unit 30 in a 42U rack?

### Module 3 Quiz

**Q1.** One Rack Unit (1U) equals:
- A) 1 inch
- B) 1.75 inches ✓
- C) 2 inches
- D) 19 inches

**Q2.** Cables in the xAI-style environment enter racks from:
- A) The floor
- B) The rear
- C) The overhead cable trays ✓
- D) The front door

**Q3.** The purpose of a Vertical Cable Manager is to:
- A) Provide power to equipment
- B) Organize cables running vertically through the rack ✓
- C) Mount servers to the rack
- D) Measure temperature

**Q4.** What is the first step when equipment at U24 needs attention?
- A) Open the work order
- B) Locate the rack by its label ✓
- C) Call the customer
- D) Power down the rack

---

# MODULE 4: SINGLE MODE FIBER OPTICS

## Lesson 4.1 — Single Mode Fiber — Complete Guide

### Theory

Optical fiber is a hair-thin strand of glass that transmits data as pulses of light. Single Mode Fiber (SMF) is designed for long-distance, high-bandwidth transmission. The "single mode" refers to the fact that only one mode (path) of light travels through the fiber core — making it ideal for very long distances and high speeds without signal degradation.

**Physical Characteristics:**
- **Core diameter:** 8–10 micrometers (thinner than a human hair)
- **Cladding diameter:** 125 micrometers
- **Cable jacket color:** Yellow (industry standard)
- **Connector color:** Green (typically LC connectors with green housings)
- **Wavelengths used:** 1310nm and 1550nm (infrared — invisible to the human eye)

### Real-World Explanation

Imagine you are shouting into a long tunnel. If the tunnel is very narrow, your voice (light) travels straight without bouncing around — this is single mode. If the tunnel is wide, your voice bounces off the walls and arrives distorted — this is multimode.

In a data center, single mode fiber allows signals to travel from one rack to another rack 100 meters away, or to a Supercore switch 500 meters away, with essentially zero signal loss. This is why large data centers like xAI's facilities use single mode fiber for their primary interconnects.

### Where Single Mode Fiber Is Used in This Environment

1. **Rack → SU Cabinet connections** — Each rack connects to an SU (Storage Unit or Switching Unit) cabinet via single mode fiber
2. **Rack → Supercore connections** — Racks connect to the Supercore switching layer via single mode fiber
3. **IPMI Management paths** — The management infrastructure also uses single mode fiber for reliability

### Fiber Cable Construction (Layers from Inside Out)

```
Center Core (8-10µm glass)
        ↓
    Cladding (125µm glass)
        ↓
  Coating / Buffer (250µm)
        ↓
  Tight Buffer or Loose Tube
        ↓
    Kevlar Strength Members
        ↓
   Outer Jacket (Yellow)
```

### Connector Types

**LC Connector (Most Common in Data Centers)**
- Small form factor — allows high-density patching
- Has a push-pull latch mechanism
- Green housing = Single Mode
- Beige/cream housing = Multimode (OM1/OM2)
- Aqua housing = Multimode (OM3/OM4)

**SC Connector**
- Larger square connector
- Push-pull mechanism
- Less common in modern high-density environments
- Green = Single Mode

**MPO/MTP Connector**
- Multi-fiber connector (12 or 24 fibers in one connector)
- Used for high-density trunk cables
- Critical in spine-leaf architectures

### Fiber Cleaning — Critical Procedure

**Why cleaning matters:** A single dust particle or fingerprint on a fiber end face is like placing a boulder in the middle of a highway — it blocks or severely degrades the light signal. Even one dirty connector can cause:
- High insertion loss (weak signal)
- Back reflections
- Complete link failure

**Cleaning Procedure:**

1. **STOP** — Never connect a fiber without inspecting it first
2. **Inspect** — Use a fiber inspection scope (FOSI or video scope)
3. **Assess** — If dirty, clean it. If clean, connect it.
4. **Dry Clean First** — Use a one-click cleaner tool on the connector
5. **Wet/Dry Clean if Needed** — Use IPA (isopropyl alcohol) on a fiber cleaning stick, then dry wipe
6. **Re-Inspect** — Always inspect again after cleaning before connecting
7. **Connect** — Only connect clean, inspected fibers

**Cleaning Tools:**
- One-Click Cleaner (most common — single use per press)
- Fiber Cleaning Pen
- Fiber Cleaning Swabs
- IPA (99% isopropyl alcohol — NOT rubbing alcohol)
- Fiber Inspection Scope / FOSI (Fiber Optic Scope and Inspection)

### Fiber Inspection Standards

The IEC 61300-3-35 standard defines cleanliness zones on a fiber end face:

```
Zone A (Core) — innermost circle
Zone B (Cladding) — surrounding core
Zone C (Contact) — outer cladding area
Zone D (Adhesive/Ferrule) — outermost area
```

**Zone A (Core) must be completely clean** — even one particle in Zone A will cause signal loss.

### Fiber Dressing Rules

1. **Minimum bend radius:** Single mode fiber must NEVER be bent tighter than 10x the cable diameter (typically 30mm / ~1.25 inch minimum bend radius for standard cable). Violating bend radius causes signal loss and eventual fiber cracking.

2. **No sharp bends:** Never wrap fiber around corners. Use fiber guides and slack management spools.

3. **Velcro only:** Never use zip ties on fiber optic cables. Zip ties create point pressure that can cause microbending losses.

4. **Separate from copper:** Keep fiber separated from power cables and heavy copper cables that can crush fibers.

5. **Service loops:** Always leave a 1-2 meter service loop at each end of a fiber run. This allows future re-termination without pulling new cable.

6. **Label every fiber:** Every fiber cable must be labeled at both ends with matching labels indicating source port and destination port.

7. **Dust caps:** Every unconnected fiber port and every unused fiber connector must have a dust cap installed immediately.

### Fiber Optic Loss Budget

When running single mode fiber between two points, you must calculate whether the signal will be strong enough to arrive properly. This is called a **loss budget**.

Typical loss values:
- LC connector pair: 0.3 dB loss
- Each splice: 0.1 dB loss
- Fiber itself: 0.4 dB/km at 1310nm

Most 100G transceivers have a power budget of 10 dB, meaning total losses in the link must be under 10 dB.

### Photo Explanation Section

When looking at single mode fiber in a data center:

1. **Overhead trays:** Yellow fiber trunks (MPO cables) run in bundles, often labeled with port-to-port information

2. **Entry into rack:** Yellow fibers enter from the top brush strip and immediately run down the vertical cable manager in organized bundles secured with Velcro

3. **At patch panel or switch:** Yellow fibers fan out from the VCM, each with a labeled green LC connector plugged into the appropriate port

4. **Slack management:** Excess fiber is coiled in slack storage spools or neatly looped in the HCM to maintain proper bend radius

5. **Dust caps:** Any unused ports should have green dust caps installed

### Terminology

| Term | Definition |
|------|-----------|
| **SMF** | Single Mode Fiber |
| **Core** | The light-carrying center of the fiber (8-10µm) |
| **Cladding** | Glass layer surrounding the core that reflects light inward |
| **Insertion Loss** | Signal strength reduction when passing through a connection |
| **Return Loss** | Signal reflected back toward the source (bad) |
| **OTDR** | Optical Time Domain Reflectometer — fiber testing tool |
| **dB** | Decibel — unit measuring optical signal strength |
| **nm** | Nanometer — unit measuring light wavelength |
| **LC** | Lucent Connector — small form factor fiber connector |
| **MPO** | Multi-fiber Push-On — multi-strand connector |
| **FOSI** | Fiber Optic Scope and Inspection tool |
| **One-Click Cleaner** | Single-use fiber end-face cleaning tool |
| **Bend Radius** | The minimum curve radius allowed for a fiber cable |
| **Microbending** | Microscopic bending causing optical signal loss |
| **OS2** | Optical Single-mode specification for modern SMF |

### Practical Example — Fiber Patch Procedure

**Task:** Patch single mode fiber from Switch Port A1 to Patch Panel Port 14.

1. Obtain cleaned, tested fiber jumper of correct length
2. Inspect both connector end faces with FOSI scope
3. Clean any dirty end faces with one-click cleaner
4. Re-inspect after cleaning
5. Remove dust caps from destination ports (Port A1 and PP-14)
6. Connect fiber — ensure latch clicks into place
7. Verify link lights on both ends (green = link up, amber = activity)
8. Document the connection in the DCIM system
9. Apply labels to fiber at both ends if not pre-labeled
10. Dress fiber back through the HCM maintaining bend radius

### Troubleshooting Section

**Problem:** Fiber link shows "no signal" after patching.
**Possible Causes:**
1. Dirty connector — inspect and clean both ends
2. Wrong polarity — LC duplex cables have TX/RX pairs; check polarity
3. Bent fiber beyond minimum radius — check routing
4. Transceiver not fully seated — re-seat the SFP/QSFP
5. Wrong wavelength — 1310nm transceiver with 1550nm transceiver won't work

**Problem:** Intermittent link drops.
**Possible Causes:**
1. Partially dirty connector (contamination moves when vibrated)
2. Fiber routed too tightly, causing stress at connector
3. Loose connector — not fully latched
4. Damaged fiber due to sharp bend in cable path

**Problem:** High bit error rate (BER) on fiber link.
**Possible Causes:**
1. Insufficient power budget — too many splices or long distance
2. Mixed connector polish types (APC vs UPC mismatch)
3. Dirty connectors causing partial blockage
4. Cracked fiber from physical damage

### Knowledge Check Questions

1. What is the jacket color of single mode fiber?
2. What is the minimum bend radius rule for single mode fiber?
3. Why must you never use zip ties on fiber optic cables?
4. What tool do you use to inspect a fiber end face?
5. What does "insertion loss" mean?
6. List the 7 steps of proper fiber cleaning procedure.
7. What is the difference between an LC and MPO connector?
8. Why must you never look directly into a fiber optic cable?

### Module 4 Quiz

**Q1.** Single Mode Fiber jacket color is:
- A) Orange
- B) Aqua
- C) Yellow ✓
- D) Blue

**Q2.** LC connector color for Single Mode Fiber is:
- A) Beige
- B) Green ✓
- C) Aqua
- D) Black

**Q3.** Minimum bend radius for single mode fiber is:
- A) 5mm
- B) 10mm
- C) 30mm ✓
- D) 100mm

**Q4.** What tool is used to inspect fiber end faces?
- A) Multimeter
- B) OTDR only
- C) Fiber Inspection Scope (FOSI) ✓
- D) Flashlight

**Q5.** Why are zip ties NOT used on fiber cables?
- A) They are too expensive
- B) They create point pressure causing microbending loss ✓
- C) They are the wrong color
- D) They are too loose

**Q6.** A one-click cleaner is used for:
- A) Cleaning the outside of fiber cables
- B) Cleaning fiber end faces ✓
- C) Testing fiber continuity
- D) Measuring fiber length

---

# MODULE 5: SU CABINETS

## Lesson 5.1 — SU Cabinets — Purpose and Architecture

### Theory

SU Cabinets (Switch Unit or Storage Unit Cabinets, depending on deployment) serve as the aggregation point for groups of rack cabinets. In a typical AI data center design, an SU cabinet contains higher-density switching equipment that aggregates the connections from multiple rack-level switches into a smaller number of uplinks heading toward the core network.

### Real-World Explanation

Imagine a city's road system. Individual houses (servers) connect to street-level roads (rack switches). Those streets connect to arterial roads (SU cabinets). From the arterial roads, traffic flows to the highway interchange (Supercore). This hierarchy allows efficient traffic management at every level.

In our environment:
- Each rack cabinet has equipment with ports connecting via single mode fiber to the SU cabinet
- The SU cabinet aggregates these connections
- The SU cabinet then has uplinks going to the Supercore level

### Signal Flow: Rack → SU

```
RACK CABINET
[Server NIC / GPU NIC]
        ↓
[Top-of-Rack (ToR) Switch]
        ↓ (Single Mode Fiber — yellow)
        ↓ (Green LC connectors)
[SU Cabinet Patch Panel]
        ↓
[SU Cabinet Aggregation Switch]
        ↓ (Uplinks to Supercore)
```

### SU Cabinet Physical Characteristics

- Often contain high-density patch panels at the front
- Aggregation switches (100G, 400G, or 800G class)
- Extensive fiber management due to high port count
- Multiple incoming fiber bundles from rack cabinets
- Outgoing fiber uplinks to Supercore
- Managed power infrastructure (dual-feed PDUs)
- Dedicated management ports connected to IPMI infrastructure

### Network Architecture Significance

In a spine-leaf architecture (the most common AI data center topology):
- **Leaf layer:** ToR switches in rack cabinets
- **Spine layer:** Aggregation switches in SU cabinets (sometimes called "spine switches")
- **Super-spine:** Supercore switches connecting multiple pods

The SU cabinet is the physical home of the spine layer in many AI cluster designs.

### Terminology

| Term | Definition |
|------|-----------|
| **SU Cabinet** | Switch/Storage Unit cabinet — aggregation point |
| **ToR Switch** | Top-of-Rack switch — switch inside a rack cabinet |
| **Spine-Leaf** | Modern data center network topology |
| **Aggregation** | Combining multiple connections into fewer higher-capacity links |
| **Uplink** | Connection going toward the core/upstream device |
| **Downlink** | Connection going toward servers/downstream devices |
| **Port Density** | Number of ports on a switch or in a cabinet |

### Practical Example

A rack cabinet contains 8 servers, each with 2x 100G NICs connecting to a ToR switch. The ToR switch has 16x 100G downlinks (to servers) and 4x 400G uplinks going to the SU cabinet. Inside the SU cabinet, these 4x 400G links terminate on an aggregation switch that has similar uplinks from 8 other rack cabinets, then sends traffic up to the Supercore via 4x 800G links.

### Knowledge Check Questions

1. What is the primary purpose of an SU cabinet?
2. In a spine-leaf topology, what layer does the SU cabinet typically represent?
3. What type of cables connect rack cabinets to SU cabinets?
4. What is an "uplink"?
5. Why is aggregation important in large-scale AI clusters?

---

# MODULE 6: SUPERCORE INFRASTRUCTURE

## Lesson 6.1 — Supercore — The Centralized Backbone

### Theory

The Supercore (also called Super-spine, Core, or Centralized Switching Layer) is the highest level of the network hierarchy in an AI data center. It interconnects all SU cabinets (and sometimes directly connects multiple AI computing pods), providing a fully non-blocking or near-non-blocking fabric that allows any server to communicate with any other server at full speed.

### Real-World Explanation

The Supercore is the "highway system" of the data center. While SU cabinets are arterial roads connecting neighborhoods, the Supercore is the interstate highway system that connects entire cities. At xAI's Colossus facility, the Supercore connects all GPU clusters together so that 100,000 H100 GPUs (or more) can communicate seamlessly as a single computing unit.

### Why Large AI Data Centers Need Supercore

1. **Scale:** AI training requires all-to-all communication between thousands of GPUs. The Supercore provides the bandwidth for this.

2. **Non-blocking fabric:** Modern AI workloads fail if any switch in the path becomes a bottleneck. The Supercore provides sufficient bandwidth that no single switch limits performance.

3. **Centralized redundancy:** Supercore switches are themselves redundant — if one fails, traffic reroutes through the others automatically.

4. **Pod interconnection:** A data center may have multiple "pods" (groups of racks and SU cabinets). The Supercore connects all pods together.

### Network Hierarchy Diagram

```
                    SUPERCORE
                  (Core Switches)
                /       |        \
           SC-1        SC-2      SC-3
          /    \      /    \    /    \
      SU-01  SU-02  SU-03  SU-04  SU-05
      / \    / \    / \    / \    / \
    R01 R02 R03 R04 R05 R06 R07 R08 R09
    
    R = Rack Cabinet
    SU = SU Cabinet
    SC = Supercore Cabinet
```

### Physical Environment

In our observed xAI-style environment:
- Rack cabinets connect to Supercore via single mode fiber (direct connection in some architectures)
- The Supercore cabinets are physically located in a dedicated centralized area
- Supercore cabinets are typically larger (42U-48U) and contain high-port-count switches
- Cable management in the Supercore area is extremely complex — hundreds of fiber bundles must be organized

### Terminology

| Term | Definition |
|------|-----------|
| **Supercore** | Highest level of network hierarchy in a data center |
| **Super-spine** | Alternative name for Supercore layer |
| **Non-blocking** | Fabric where all ports can operate at full speed simultaneously |
| **Pod** | A self-contained group of racks sharing SU infrastructure |
| **Fat-Tree** | Network topology commonly used in AI clusters |
| **ECMP** | Equal Cost Multi-Path — allows traffic to use multiple paths simultaneously |
| **Oversubscription** | Ratio of potential traffic to actual available bandwidth |

### Practical Example

In a 10,000 GPU cluster:
- 10,000 GPUs → 2,500 servers (4 GPUs/server)
- 2,500 servers → 250 racks (10 servers/rack)
- 250 racks → 25 SU cabinets (10 racks/SU)
- 25 SU cabinets → 4 Supercore switches (25/4 = ~6 SUs per Supercore switch)

Each connection level uses higher-speed links: 100G to servers, 400G to SU, 800G/1.6T at Supercore.

### Knowledge Check Questions

1. What is the Supercore's role in data center network hierarchy?
2. Why is a "non-blocking fabric" important for AI workloads?
3. In our environment, what cable type connects racks to the Supercore?
4. What is "oversubscription" and why should it be minimized in AI clusters?
5. Describe a 3-tier network hierarchy from server to Supercore.

---

# MODULE 7: IPMI MANAGEMENT INFRASTRUCTURE

## Lesson 7.1 — IPMI and Out-of-Band Management

### Theory

IPMI (Intelligent Platform Management Interface) is a standardized hardware-level management interface built into server motherboards. It provides a way to monitor and control servers independently of the main operating system — even when the server is powered off, crashed, or in a failed state.

In our environment, single mode fiber is used for the IPMI management infrastructure, providing a dedicated, separate network path that never competes with production traffic.

### Real-World Explanation

Imagine you have a smart home but your main internet is down. You have a backup cellular connection on a separate device that lets you control everything even when the main connection fails. IPMI is that backup connection for servers — it gives data center technicians "eyes and hands" inside a server no matter what state the server is in.

### What IPMI Provides

1. **Remote Power Control:** Power on, power off, reset, or force a power cycle on any server remotely
2. **Serial Console Access:** Access the server's terminal output even during boot or kernel panic
3. **Hardware Sensor Monitoring:** Real-time temperature, fan speed, voltage, and power consumption data
4. **Remote KVM:** Keyboard/Video/Mouse access — see the server's screen remotely
5. **System Event Log (SEL):** Hardware event log showing errors, warnings, and state changes
6. **Remote Media Mount:** Boot servers from ISO images hosted on a remote system
7. **Firmware Updates:** Update BIOS/UEFI and firmware remotely

### Out-of-Band vs In-Band Management

| Aspect | In-Band Management | Out-of-Band (IPMI) |
|--------|-------------------|-------------------|
| Path | Through production NIC and OS | Through dedicated BMC hardware |
| Works when OS crashes? | No | Yes |
| Works when server is off? | No | Yes |
| Network used | Production network | Dedicated management network |
| Security | Less isolated | More secure (separate network) |
| Speed | High bandwidth | Low bandwidth (enough for management) |

### IPMI Infrastructure Architecture

```
MANAGEMENT SWITCH
(Dedicated IPMI/BMC Network)
        |
    ────┼────────────────────────────
        |           |           |
    SERVER-01   SERVER-02   SERVER-03
    (BMC Port)  (BMC Port)  (BMC Port)
    
Management traffic is completely separate from production data traffic.
In our environment: Single Mode Fiber paths carry the management network signals.
```

### BMC — Baseboard Management Controller

The BMC is the hardware chip on the server motherboard that implements IPMI. The BMC:
- Has its own processor, memory, and firmware
- Has a dedicated network port (separate from production NICs)
- Runs independently even when main power is off (uses standby power)
- Can communicate with the management network at all times
- Supports industry standards: IPMI 2.0, Redfish API, iDRAC (Dell), iLO (HP)

### Common IPMI Tools

**ipmitool (Linux CLI):**
```bash
# Check power status
ipmitool -H 192.168.1.100 -U admin -P password power status

# Power on server
ipmitool -H 192.168.1.100 -U admin -P password power on

# Get temperature readings
ipmitool -H 192.168.1.100 -U admin -P password sdr type Temperature

# Get System Event Log
ipmitool -H 192.168.1.100 -U admin -P password sel list
```

**Web-based BMC interface:**
Each BMC has a web interface accessible at its IP address. This provides a graphical dashboard for all IPMI functions.

**Redfish API:**
Modern BMCs support the Redfish RESTful API standard for programmatic management — important in large-scale automation.

### IPMI Security

Because IPMI provides full control of servers, the management network must be:
- **Physically isolated** from the production network
- **Access controlled** — only authorized personnel and management tools
- **Monitored** — all IPMI access should be logged
- **Segmented** — different management VLANs for different security zones

In our environment, the use of single mode fiber for IPMI paths provides physical layer separation from the production copper and fiber infrastructure.

### Terminology

| Term | Definition |
|------|-----------|
| **IPMI** | Intelligent Platform Management Interface |
| **BMC** | Baseboard Management Controller — the hardware IPMI chip |
| **OOB** | Out-of-Band — management that bypasses the OS |
| **KVM** | Keyboard/Video/Mouse — remote console access |
| **SEL** | System Event Log — hardware event record |
| **iDRAC** | Dell's implementation of BMC/IPMI |
| **iLO** | HP/HPE's implementation of BMC/IPMI |
| **Redfish** | Modern RESTful API standard for server management |
| **Standby Power** | Low-level power keeping BMC alive when server is "off" |

### Practical Example

**Scenario:** A server in rack DH20 at U24 is completely unresponsive. The OS is not responding and the server cannot be reached on the production network.

**Without IPMI:**
- Physical visit required
- Manual power button press
- Unknown root cause
- Potentially hours to resolve

**With IPMI:**
1. Connect to BMC management IP for that server
2. Check SEL log — find "CPU temperature critical" event at 3:47 AM
3. View current sensor data — CPU temperature still elevated
4. Check fan speeds — three fans reporting failure
5. Use remote KVM to see OS state — kernel panic message on screen
6. Check power consumption — server is in throttled state
7. Issue graceful shutdown via IPMI
8. Schedule hardware maintenance for fan replacement
9. Power server back on remotely after fans replaced

This entire investigation and initial resolution happened remotely, without anyone physically touching the server.

### Troubleshooting Section

**Problem:** Cannot connect to IPMI/BMC of a server.
**Possible Causes:**
1. BMC network cable not connected
2. BMC not configured with correct IP address
3. Management network VLAN not configured properly
4. BMC firmware corrupt — needs physical access for recovery
5. Wrong password — check credentials management system

**Problem:** IPMI shows wrong sensor readings.
**Possible Causes:**
1. Outdated BMC firmware — update BMC firmware
2. Sensor calibration issue — reset BMC
3. Physical sensor failure — may need hardware replacement

### Knowledge Check Questions

1. What does IPMI stand for?
2. What is the difference between in-band and out-of-band management?
3. What is a BMC and where is it located?
4. List 4 things you can do with IPMI that you cannot do with normal OS access.
5. Why is the IPMI network kept separate from production networks?
6. What does "SEL" mean and what is it used for?

---

# MODULE 8: CAT6 COPPER CABLING

## Lesson 8.1 — CAT6 — Copper Ethernet Cabling

### Theory

Category 6 (CAT6) is a standardized twisted-pair copper cable standard for Ethernet networks. It supports data transmission at up to 10 Gigabits per second (10GbE) at distances up to 55 meters, and 1 Gigabit per second (1GbE) at distances up to 100 meters.

**Physical Characteristics:**
- 4 pairs of twisted copper conductors (8 wires total)
- Each pair is twisted at a different rate to reduce crosstalk
- Internal spline separator in CAT6 to further reduce crosstalk
- RJ45 connectors (8P8C modular connectors)
- Green jacket color in our environment for data CAT6

### Real-World Explanation

If single mode fiber is the highway, CAT6 copper cable is the local road network. CAT6 is used for shorter-distance connections where optical fiber would be overkill or too expensive. In our environment, green CAT6 cables are used for rack-to-rack data connections and management connections where the distance is short enough for copper.

### CAT6 in Our Environment

**Green CAT6:** Used for data connections between racks or for management infrastructure within short distances.

**Blue CAT6:** Three blue CAT6 cables enter each rack with specific dedicated purposes:
- Blue Cable #1 → PDU A (power management)
- Blue Cable #2 → PDU B (power management)
- Blue Cable #3 → Rack Management

### RJ45 Connector

The RJ45 (Registered Jack 45, or more precisely 8P8C — 8 Position 8 Contact) is the standard connector for CAT6. It has 8 contacts arranged in a row, each making contact with one of the 8 wires in the cable.

**T568B Wiring Standard (Most Common in North America):**
```
Pin 1: White/Orange
Pin 2: Orange
Pin 3: White/Green
Pin 4: Blue
Pin 5: White/Blue
Pin 6: Green
Pin 7: White/Brown
Pin 8: Brown
```

**T568A Wiring Standard:**
```
Pin 1: White/Green
Pin 2: Green
Pin 3: White/Orange
Pin 4: Blue
Pin 5: White/Blue
Pin 6: Orange
Pin 7: White/Brown
Pin 8: Brown
```

**Important:** Both ends of a cable must use the SAME standard (either both T568A or both T568B) for a straight-through cable. If one end is T568A and the other is T568B, you have a crossover cable (rarely needed with modern equipment that supports Auto-MDI/MDIX).

### Network Speeds

| Standard | Speed | Distance |
|----------|-------|---------|
| CAT5e | 1 Gbps | 100m |
| CAT6 | 1 Gbps | 100m |
| CAT6 | 10 Gbps | 55m |
| CAT6A | 10 Gbps | 100m |
| CAT7 | 10 Gbps | 100m |
| CAT8 | 25-40 Gbps | 30m |

### CAT6 Testing Methods

**Continuity Tester:**
- Simplest tool — checks that all 8 pins connect from one end to the other
- Cannot test speed or crosstalk
- Good for quick "is it wired correctly" check

**Cable Certifier (Fluke DSX, etc.):**
- Full certification testing
- Measures: wire map, length, attenuation, NEXT, FEXT, return loss
- Produces pass/fail result per TIA-568 standard
- Required for formal structured cabling installations

**Network Analyzer:**
- Tests actual network performance
- Can identify packet loss, errors, and speed

### Proper CAT6 Installation

1. **Minimum bend radius:** 4x cable diameter (approximately 1 inch for standard CAT6)
2. **No tie wraps too tight:** Crushing the cable deforms the twisted pairs and causes crosstalk
3. **No sharp kinks:** Never create sharp bends — creates permanent impedance changes
4. **Separate from power cables:** Keep CAT6 away from power cables to prevent EMI
5. **Support at regular intervals:** Horizontal runs need support every 5 feet to prevent sagging

### Terminology

| Term | Definition |
|------|-----------|
| **CAT6** | Category 6 copper cable standard |
| **RJ45** | 8-pin modular connector used with CAT6 |
| **NEXT** | Near-End Crosstalk — interference between wire pairs |
| **Attenuation** | Signal weakening over distance |
| **EMI** | Electromagnetic Interference from motors, power cables, etc. |
| **Patch Cable** | Short pre-made cable with RJ45 on both ends |
| **Horizontal Cable** | Fixed cable run from patch panel to equipment |
| **MDIX** | Medium Dependent Interface Crossover — auto-crossover in modern NICs |
| **GbE** | Gigabit Ethernet |
| **10GbE** | 10 Gigabit Ethernet |

### Practical Example

**Task:** Connect two rack cabinets (DH20 and DH21) with a green CAT6 cable.

1. Measure cable path distance — approximately 3 meters
2. Route cable through overhead tray between racks
3. Dress cable down VCM in each rack
4. Verify cable length has service loop at each end
5. Terminate cable into patch panel or directly into switch port
6. Test with continuity tester — verify all 8 pins pass
7. Label both ends: DH20-SW1-P12 → DH21-SW1-P12
8. Document connection in DCIM system

### Troubleshooting Section

**Problem:** CAT6 cable tests pass on continuity tester but network won't connect.
**Check:**
1. Speed/duplex mismatch on switch ports
2. VLAN configuration incorrect
3. MAC address issue
4. MTU mismatch
5. SFP vs copper port configuration

**Problem:** Intermittent network drops on CAT6 link.
**Check:**
1. Cable too long (over 100m)
2. Cable routed near electrical interference source
3. Connector not fully crimped — will fail when cable moves
4. Patch panel port not fully terminated
5. Cable pinched or kinked somewhere in the run

### Knowledge Check Questions

1. What is the maximum distance for CAT6 at 1 Gbps?
2. How many conductors does CAT6 cable contain?
3. What is the difference between T568A and T568B wiring?
4. Why must CAT6 be kept away from power cables?
5. What does NEXT stand for and why is it important?

---

# MODULE 9: BLUE CAT6 — PDU AND MANAGEMENT CONNECTIONS

## Lesson 9.1 — Blue CAT6 Cable Assignments

### Theory

In our xAI-style data center environment, blue CAT6 cables have specific, standardized assignments. Each rack receives exactly 3 blue CAT6 cables entering from the overhead tray, with each cable having a distinct, dedicated purpose. This color-coding and standardization is critical for quick identification and prevents accidental mis-connections.

### The Three Blue Cable Assignments

```
OVERHEAD CABLE TRAY
        ↓
    THREE BLUE CAT6 CABLES ENTER EACH RACK
        ↓
┌─────────────────────────────────────────┐
│                                         │
│  Blue Cable #1 ──────→ PDU A            │
│  (Power management, A-side PDU)         │
│                                         │
│  Blue Cable #2 ──────→ PDU B            │
│  (Power management, B-side PDU)         │
│                                         │
│  Blue Cable #3 ──────→ Rack Management  │
│  (Out-of-band rack management device)   │
│                                         │
└─────────────────────────────────────────┘
```

### PDU Management Connections (Blue #1 and #2)

Modern intelligent PDUs have a network management port. This port allows:
- Remote monitoring of per-outlet power consumption
- Remote outlet switching (turn individual servers on/off remotely)
- Environmental monitoring (temperature sensors on the PDU)
- Alerting when circuits reach threshold loads
- Integration with DCIM (Data Center Infrastructure Management) systems

The blue CAT6 to PDU-A (cable #1) and PDU-B (cable #2) provide this management connectivity to each PDU independently. Having separate connections to each PDU ensures that if one management connection fails, the other PDU is still manageable.

### Rack Management Connection (Blue #3)

The third blue CAT6 cable connects to the rack's out-of-band management device. This might be:
- A console server (provides serial console access to all servers)
- A KVM-over-IP switch
- A smart PDU management interface
- A rack-level environmental monitoring sensor

This connection is part of the IPMI management infrastructure discussed in Module 7.

### Why Standardization Matters

In a large data center with 500+ racks, having every rack use the same blue cable assignment means:
- Technicians can quickly identify management cables
- Troubleshooting is faster — "blue cable to PDU-A" is always the same
- New technicians can learn the standard once and apply it everywhere
- Auditing and documentation are consistent

### Practical Example

**Scenario:** PDU-A in rack DH20 is not showing up in the PDU management system.

1. Locate rack DH20
2. Trace the first blue CAT6 cable (Cable #1)
3. Verify it connects from the overhead tray down to PDU-A's network management port
4. Check for physical damage to the cable
5. Verify the RJ45 connector is fully seated in PDU-A's management port
6. Check PDU-A's management port LED — is it lit?
7. If LED is dark, try a different patch cable to rule out cable failure
8. If LED is lit, check network switch configuration for that port

### Knowledge Check Questions

1. How many blue CAT6 cables enter each rack in our environment?
2. What is the purpose of each blue cable?
3. Why are PDU-A and PDU-B management connections kept separate?
4. What functions does a PDU network management port provide?
5. Why is standardization important in large-scale deployments?

---

# MODULE 10: PDU — POWER DISTRIBUTION UNITS

## Lesson 10.1 — PDU Architecture and Dual Power Design

### Theory

A Power Distribution Unit (PDU) is a device that receives a single high-amperage power input and distributes it to multiple lower-amperage outlets for individual servers and equipment. In data center environments, PDUs are rack-mounted vertically along the rear sides of rack cabinets.

### PDU Types

**Basic PDU:**
- Receives power input, distributes to outlets
- No monitoring or remote control
- Simple and reliable but no visibility

**Metered PDU:**
- Displays total power consumption
- No remote control
- Provides basic visibility

**Monitored PDU:**
- Network management port
- Per-outlet power monitoring
- Temperature/humidity sensors
- SNMP alerts
- Web interface

**Switched/Intelligent PDU:**
- All features of monitored PDU PLUS
- Remote per-outlet switching
- Scheduled on/off control
- Individual outlet current metering
- API access for automation

In our environment, the blue CAT6 cables to PDU-A and PDU-B suggest intelligent/switched PDUs are in use.

### Dual Power Architecture — A-Side and B-Side

**The most critical power design concept in a data center:**

Every server in a production data center should have TWO independent power supplies:
- **Power Supply Unit 1 (PSU1)** → connects to **PDU-A** (A-side power)
- **Power Supply Unit 2 (PSU2)** → connects to **PDU-B** (B-side power)

```
DATA CENTER POWER FLOW:

UTILITY GRID ──→ TRANSFORMER ──→ UPS-A ──→ PDU-A (A-Side)
                                                │
                                         [Outlets 1-20]
                                                │
                                         SERVER PSU-1
                                                │
                                      ══════════╪══════════
                                                │
                                         SERVER PSU-2
                                                │
                                         [Outlets 1-20]
                                                │
UTILITY GRID ──→ TRANSFORMER ──→ UPS-B ──→ PDU-B (B-Side)
```

### Why Dual Power Is Non-Negotiable

If a server has only one power supply and that supply fails, the server goes down. In a data center with 10,000 servers, single-supply designs mean any PSU failure causes a server outage.

With dual power:
- PSU-1 on PDU-A and PSU-2 on PDU-B
- If PDU-A loses power (circuit breaker trips, UPS fails), PSU-2 on PDU-B keeps the server running
- If PDU-B loses power, PSU-1 on PDU-A keeps the server running
- Both PDUs must fail simultaneously to lose a server — extremely rare

### Power Monitoring

Intelligent PDUs provide critical data:
- **Per-outlet current** (amps): Identify which server is using how much power
- **Total circuit load** (% of capacity): Alert before circuit overloads
- **Voltage monitoring**: Detect under/over voltage conditions
- **kWh metering**: Track energy consumption for billing and efficiency
- **Temperature monitoring**: Detect hot spots inside the rack

### PDU Naming Conventions

In our environment, PDUs are typically labeled:
- **PDU-A** or **PDU-L** (Left/A-side): The A-side power distribution unit
- **PDU-B** or **PDU-R** (Right/B-side): The B-side power distribution unit

Every outlet on the PDU is numbered and mapped to a specific server's PSU in the documentation system (DCIM).

### Load Balancing

Critical rule: **Never load one PDU significantly more than the other.**

Best practice: Aim for balanced load between PDU-A and PDU-B. If PDU-A carries 60% load and PDU-B carries 40% load, failure of PDU-A would require PDU-B to carry everything — possibly exceeding its capacity.

Target: Each PDU at no more than 50% of rated capacity. This ensures either PDU can carry the full rack load if the other fails.

### Terminology

| Term | Definition |
|------|-----------|
| **PDU** | Power Distribution Unit |
| **PSU** | Power Supply Unit — server's internal power supply |
| **UPS** | Uninterruptible Power Supply — battery backup |
| **A-Side** | The "A" branch of redundant power infrastructure |
| **B-Side** | The "B" branch of redundant power infrastructure |
| **kW** | Kilowatt — unit of power (1,000 watts) |
| **kWh** | Kilowatt-hour — unit of energy (power × time) |
| **Amps** | Unit of electrical current |
| **SNMP** | Simple Network Management Protocol — used for PDU monitoring |
| **DCIM** | Data Center Infrastructure Management — tracking software |
| **Load Balancing** | Distributing power load evenly between PDU-A and PDU-B |

### Practical Example

**Task:** Install new 2U server in rack DH20 at U16/U17.

1. Connect PSU-1 power cord to PDU-A, outlet 7 (document this)
2. Connect PSU-2 power cord to PDU-B, outlet 7 (document this)
3. Check current PDU-A load: 12.3A / 20A = 61% ← WARNING: Too high!
4. Check current PDU-B load: 8.1A / 20A = 40.5%
5. Consult load balancing plan — consider moving another server's PSU-1 to PDU-B
6. After balancing: PDU-A 51%, PDU-B 50% — acceptable
7. Document all PSU-to-PDU connections in DCIM

### Troubleshooting Section

**Problem:** Server unexpectedly powered off.
**Check:**
1. Is PDU-A breaker tripped? (If only PSU-1 on PDU-A and A-side lost power)
2. Is PDU-B breaker tripped?
3. Is the server actually connected to both PDU-A and PDU-B?
4. Did the server have only one PSU connected? (design flaw — should be flagged)
5. Check SEL via IPMI for power events

**Problem:** PDU-A load is at 95% of capacity.
**Immediate actions:**
1. Alert NOC and management — this is a critical condition
2. Do not add any more load to PDU-A
3. Identify servers that could have PSUs redistributed to PDU-B
4. Create a load balancing plan
5. Implement changes during a maintenance window

### Knowledge Check Questions

1. What is the purpose of a PDU?
2. What is the difference between A-side and B-side power?
3. Why should each PDU be kept at no more than 50% load?
4. What additional functions does an intelligent PDU provide over a basic PDU?
5. Where are blue CAT6 cables connected on a PDU?
6. What happens to a dual-power server if one PDU loses power?

---

# MODULE 11: AEC CABLES — ACTIVE ELECTRICAL CABLES

## Lesson 11.1 — AEC Technology and AI Cluster Interconnects

### Theory

Active Electrical Cable (AEC) is a short-distance, high-speed cable technology that uses active electronic components (amplifiers, signal conditioners) embedded in the cable assembly itself to transmit data at very high speeds over copper conductors. AECs bridge the gap between passive copper cables (which work at short distances) and optical fiber (which is expensive and fragile).

**Key characteristics:**
- Copper conductors (not fiber)
- Active electronics in the connector housing (hence "active")
- Very short distances: typically 1–7 meters
- Extremely high data rates: 25G, 100G, 400G, 800G per cable
- Uses standard QSFP, QSFP28, QSFP-DD, or OSFP form factor connectors
- Significantly cheaper than optical modules + fiber at the same speeds

### Real-World Explanation

Imagine you need to yell across a room (transmit data). If you whisper (passive copper), the signal is too weak to reach far. If you use a megaphone (AEC), you can shout clearly across the same room. The "megaphone" electronics are built right into the cable's end connectors. The cable handles signal boosting internally.

In AI data centers, AEC cables connect servers within the same rack, or between immediately adjacent racks. For GPU-to-GPU communication within a node or a pair of nodes, AECs provide the speed of optics at a fraction of the cost.

### AEC vs Fiber vs Passive Copper Comparison

| Feature | Passive Copper | AEC | Optical Fiber |
|---------|---------------|-----|--------------|
| Distance | <3m | 1-7m | 10m to 40km |
| Speed | Up to 400G (short) | 100G-800G | 100G-800G+ |
| Cost | Lowest | Medium | Highest |
| Fragility | Robust | Robust | Fragile |
| Power consumption | None | Low (active circuits) | Low-Medium |
| Latency | Lowest | Very low | Very low |
| Flexibility | Good | Good | Limited (bend radius) |
| Use in AI clusters | Very common | Very common | Less common at short range |

### Rocky Cables

Rocky cables are a specific implementation/brand of AEC cables used in the xAI environment. In high-density AI GPU clusters like xAI's Colossus, Rocky cables provide:

1. **GPU NVLink interconnects** — Connecting GPUs within a server or across adjacent nodes
2. **High-bandwidth switch-to-server connections** — Where 400G or 800G copper connections are sufficient distance
3. **Dense node interconnects** — Between compute nodes within a rack

Rocky cables get their name from their robust design intended for the extremely dense, high-vibration environment of AI server racks. The "active" electronics in Rocky cables can handle the signal integrity challenges of high-density rack environments.

### Physical Appearance

AEC/Rocky cables typically have:
- Black exterior jacket
- Bulkier ends (larger connector housing containing active electronics)
- Visible heat sink fins on the connector ends (dissipate heat from active circuits)
- QSFPxx or OSFP form factor on each end
- Short lengths (0.5m to 5m for most AEC, up to 7m for high-quality AEC)
- Very dense bundling — a typical AI rack may have dozens of AEC cables

### Use Cases in AI Clusters

**1. Intra-node GPU connections:**
Within a single AI server, multiple GPUs must communicate at very high speed. AECs provide 400G or 800G connections between GPUs and the NVLink/Infinity Fabric switches.

**2. Intra-rack connections:**
Between the compute servers and the Top-of-Rack switch within the same rack cabinet. This is often the densest cabling in the entire data center.

**3. Adjacent rack connections:**
Where two racks are side by side, AECs can reach across without needing optical fiber.

### Terminology

| Term | Definition |
|------|-----------|
| **AEC** | Active Electrical Cable |
| **Rocky Cable** | AEC variant used in xAI/AI GPU cluster environments |
| **QSFP** | Quad Small Form-factor Pluggable — high-speed transceiver format |
| **QSFP28** | 100G QSFP module standard |
| **QSFP-DD** | QSFP Double Density — 400G format |
| **OSFP** | Octal Small Form Factor Pluggable — 400G/800G format |
| **NVLink** | NVIDIA's high-speed GPU interconnect technology |
| **Signal Integrity** | How accurately a signal arrives after traveling through a cable |
| **Passive Copper** | Standard copper cable without active electronics |
| **DAC** | Direct Attach Copper — passive short-distance cable |

### Practical Example

**Scenario:** Installing a new 8-GPU AI training server.

Each NVIDIA H100 GPU has 4x NVSwitch-facing ports at 400G each.
- 8 GPUs × 4 ports = 32 high-speed ports
- Each port needs a cable to the NVSwitch fabric
- Short distance (1-3 meters) → AEC cables are ideal
- Total AEC cables for one server: 32 cables
- A rack with 4 such servers = 128 AEC cables just for NVLink!

This explains why AI server racks look extremely cable-dense and why proper cable management is critical.

### Troubleshooting Section

**Problem:** AEC cable link shows "not present" or no link light.
**Check:**
1. Verify cable is fully seated (AEC connectors can be stiff)
2. Check for bent pins in the QSFP cage (look with bright light)
3. Verify the cable type matches the port (QSFP28 cable in QSFP-DD port won't work)
4. Check cable part number against compatibility list
5. Try cable in a known-good port to isolate cable vs. port failure

**Problem:** AEC link shows up but has high error rate.
**Check:**
1. Cable too long for this speed — AECs have maximum distances per speed
2. Excessive heat — AEC active electronics are temperature sensitive
3. Cable bent too sharply — even copper AECs have minimum bend radius
4. Incompatible firmware — some AEC cables require updated port firmware

### Knowledge Check Questions

1. What does "Active" mean in Active Electrical Cable?
2. What is the typical maximum distance for an AEC cable?
3. How do AECs compare to fiber optics in terms of cost and fragility?
4. What are Rocky cables and where are they used?
5. Why do AI server racks have so many AEC cables?
6. What connector format do most AEC cables use?

---

# MODULE 12: LABEL READING AND INTERPRETATION

## Lesson 12.1 — Data Center Label System

### Theory

Labels are the fundamental navigation and documentation system of a data center. Every rack, server, port, cable, and connection must be clearly labeled to enable efficient operations, fast troubleshooting, and accurate documentation. In a large data center with thousands of racks and millions of ports, clear labeling is as critical as any piece of hardware.

### Standard Label Examples in Our Environment

From the observed xAI-style environment, the following label patterns are used:

| Label | Type | Meaning |
|-------|------|---------|
| **DH20** | Rack ID | Row D, Column H, Position 20 |
| **NA05** | Rack/Network ID | Network A, Position 05 |
| **NB13** | Rack/Network ID | Network B, Position 13 |
| **SCA** | Switch/Cabinet ID | Supercore Cabinet A |
| **SCB** | Switch/Cabinet ID | Supercore Cabinet B |
| **RU** | Position Indicator | Rack Unit number |
| **T** | Port Indicator | Top (upper port in a dual port) |
| **D** | Port Indicator | Down/Bottom (lower port in a dual port) |

### Decoding Label Conventions

**Rack Label Format:** [Row Letter][Column Letter][Position Number]
- Example: **DH20**
  - **D** = Data Hall D (or specific room/zone D)
  - **H** = Column H in that hall
  - **20** = Position 20 in column H

**Network Cabinet Labels:** [Type][Tier][Number]
- Example: **NA05**
  - **N** = Network cabinet
  - **A** = Tier A (SU-level A, or network tier A)
  - **05** = Cabinet number 5

- Example: **NB13**
  - **N** = Network cabinet
  - **B** = Tier B
  - **13** = Cabinet number 13

**Supercore Labels:** [SC][Letter]
- **SCA** = Supercore Cabinet A
- **SCB** = Supercore Cabinet B

**Port Labels:** [T] and [D]
- **T** = Top port (of a dual-port transceiver or dual-stacked ports)
- **D** = Down/Bottom port

### Cable Label Reading

Cables have labels at BOTH ends, and the label tells you:
- Where the cable comes FROM (source)
- Where the cable goes TO (destination)

**Label format on cable:**
```
[SOURCE RACK]-[SOURCE DEVICE]-[SOURCE PORT] → [DEST RACK]-[DEST DEVICE]-[DEST PORT]
```

Example cable label:
```
DH20-SW1-P14T → SCA-P44D
```
Reads as: "This cable goes from Rack DH20, Switch 1, Port 14 Top — to Supercore Cabinet A, Port 44 Bottom"

### Why Consistent Labeling Matters

**Scenario without good labels:**
- Technician receives ticket: "Fix broken link between server and Supercore"
- No labels on cables
- Must trace 500 cables to find the right one
- Takes 3 hours

**Scenario with proper labels:**
- Technician receives ticket: "Fix broken link DH20-SW1-P14T → SCA-P44D"
- Walks to rack DH20, finds cable labeled DH20-SW1-P14T
- Follows cable to SCA port P44D
- Identifies issue in 5 minutes

### Rack Unit (RU) Labels

Inside racks, RU labels are marked on the rails at every rack unit position. These allow precise location identification:
- **RU14** = Rack Unit 14 (counted from bottom)
- Equipment tickets and documentation always reference the RU position

### Labeling Standards Best Practices

1. **Every cable gets labeled at both ends** — no exceptions
2. **Labels face outward** — so they can be read without moving cables
3. **Labels use permanent, smear-proof ink** — laser-printed labels preferred
4. **Labels include both source and destination** — "A→B" not just "A"
5. **Labels are consistent** — same format throughout the facility
6. **Labels are replaced when illegible** — faded or damaged labels must be replaced immediately

### Label Equipment Used

- **Label printer** (Brady, Dymo, etc.) — for professional printed labels
- **Wrap-around labels** — for cable labels at connector ends
- **Flag labels** — for larger cable bundles
- **Rack unit labels** — pre-numbered adhesive strips for rack rail positions
- **Port labels** — small labels for individual port identification

### Practical Exercises

**Exercise 1:** Decode these labels:
- DH20 → Data Hall D, Column H, Position 20
- NA05 → Network Cabinet A, Position 5
- SCB → Supercore Cabinet B

**Exercise 2:** Read this cable label:
`NA05-AGG1-P7T → DH20-SW1-P1D`
Answer: "Cable from Network Cabinet A05, Aggregation Switch 1, Port 7 Top — to Data Hall D, Column H, Position 20, Switch 1, Port 1 Bottom"

**Exercise 3:** A technician finds a cable with label `RU14-DH20` on one end and no label on the other. What should they do?
Answer: Trace the cable to its destination port, then properly label both ends with complete source-destination information.

### Terminology

| Term | Definition |
|------|-----------|
| **DCIM** | Data Center Infrastructure Management — system storing label data |
| **Asset Tag** | Unique identifier label on physical equipment |
| **Port Label** | Label identifying a specific port on equipment |
| **Cable ID** | Unique identifier assigned to each cable in the DCIM system |
| **Row** | A line of rack cabinets running front-to-back |
| **Aisle** | Space between two rows of racks |
| **Rack ID** | Unique alphanumeric identifier for a specific rack cabinet |

### Knowledge Check Questions

1. Decode the label: NB13
2. What does "T" and "D" indicate in port labels?
3. Why must cables be labeled at BOTH ends?
4. What format is used for cable labels in our environment?
5. What is the risk of having unlabeled cables in a large data center?

---

# MODULE 13: CABLE DRESSING STANDARDS

## Lesson 13.1 — Professional Cable Management

### Theory

Cable dressing is the art and science of organizing, routing, and securing cables in a neat, functional, and maintainable way. In a data center, proper cable dressing is not merely aesthetic — it directly impacts:
- **Airflow** (poorly dressed cables block cooling)
- **Safety** (trip hazards, crush hazards)
- **Troubleshooting speed** (organized cables = fast identification)
- **Signal integrity** (too-tight bundling causes crosstalk; crushed cables fail)
- **Scalability** (well-dressed infrastructure can be easily expanded)

### Vertical Dressing Standards

**Rules for vertical cable runs (in VCM):**

1. **Fiber first:** Single mode fiber runs must be on the outside of copper cable bundles to avoid being crushed by heavier copper
2. **Separation:** Fiber cables and copper cables should be separated — different sides of the VCM or clearly separate sections
3. **Gentle curves:** At the top entry, cables must curve from horizontal (in the tray) to vertical (in the VCM) using a smooth radius, not a sharp bend
4. **Velcro straps every 12-18 inches:** Cables are bundled and secured to the VCM cable fingers with Velcro straps (never zip ties on fiber)
5. **No excess slack:** Cables should have appropriate length — enough for a service loop but not so much that they pile up

### Horizontal Dressing Standards

**Rules for horizontal cable runs (in HCM and at equipment ports):**

1. **Fan out cleanly:** As cables leave the VCM toward equipment, they should fan out in organized groups, not randomly
2. **Consistent direction:** Cables going left should not cross cables going right unnecessarily
3. **90-degree turns using guides:** Where cables must turn, use cable guides/fingers in the HCM to maintain bend radius
4. **Dress to port, not to equipment face:** The cable should land directly at its port, not drape across the equipment face
5. **Length management:** Each cable should be exactly the right length — too short creates tension, too long creates messy loops

### Velcro Usage

**Always use Velcro on fiber; strongly prefer on copper:**
- Velcro allows easy re-routing without cutting and wasting
- Velcro does not create point pressure on fiber like zip ties do
- Velcro straps should be installed with the soft side against cables
- Never over-tighten — if you can't slide Velcro along the cable without effort, it's too tight
- Space Velcro bundles every 12-18 inches vertically
- Use appropriately sized Velcro for bundle diameter

**Zip ties — limited use:**
- Acceptable for copper cable management only, never fiber
- Must be tensioned appropriately — never cranked tight
- Use low-force zip tie guns
- Cut tails flush to prevent scratching

### Service Loops

A service loop is deliberate extra cable length built into a cable run, allowing for:
- Future re-termination without pulling new cable
- Physical adjustment of equipment position
- Stress relief (prevents cables from being pulled tight when equipment is slid out)

**Service loop guidelines:**
- At each patch panel or switch port: 6-12 inches of extra length
- At each rack: 1-2 meter coil for long fiber runs
- Store service loops in dedicated slack managers (spools) or neatly coiled in HCMs
- Never allow service loops to sit on the floor of the rack

### Cable Separation Rules

1. **Power cables (C13/C19) separate from data cables** — keep on different sides of the rack
2. **Single mode fiber separate from copper data** — fiber is fragile; copper is heavy
3. **AEC cables separate from management cables** — different speed/purpose, easier troubleshooting
4. **A-side PDU cords and B-side PDU cords** — keep on opposite sides of the rack

### Fiber Protection

Fiber cables are delicate and require special attention:
1. **Never bend beyond minimum radius** — irreversible damage
2. **Never step on fiber** — a human foot can easily crack the glass core
3. **Never place fiber under other cables** where it can be crushed
4. **Use fiber guides** in all HCMs where fiber is run
5. **Cap all disconnected ends** immediately
6. **Never pull fiber by the connector** — pull by the cable jacket
7. **Route fiber on the outside of bundles** so it's not compressed

### Common Dressing Mistakes

| Mistake | Problem | Correct Practice |
|---------|---------|-----------------|
| Zip ties on fiber | Point pressure causing microbending | Use Velcro only |
| Cables draped over equipment face | Blocks status LEDs, looks unprofessional | Route behind equipment, land at port |
| Cables hanging over hot aisle | Blocks airflow | Route in cable managers |
| Mixed fiber and power cables | EMI on fiber signals (negligible but messy), crush risk | Separate into different cable managers |
| No service loop | Next re-term requires new cable | Always leave service loop |
| Unlabeled cables | Impossible to trace | Label every cable at both ends |
| Over-bundling | Creates rigid cables that can't be individually traced | Manageable bundle sizes |
| Under-supporting horizontal runs | Cables sag and pull on ports | Support every 12-18 inches |

### Practical Example — Dressing a New Rack

**Scenario:** New rack DH25 is being commissioned with 8 servers and associated cabling.

Step 1: Before any cables — install VCM, HCM, and blanking panels  
Step 2: Route overhead fibers down VCM with gentle curves  
Step 3: Secure fiber bundles with Velcro every 12 inches in VCM  
Step 4: Route copper cables in separate VCM section from fiber  
Step 5: At each equipment level, branch cables from VCM into HCM  
Step 6: Dress each cable to its target port with appropriate service loop  
Step 7: Label every cable at both ends  
Step 8: Final inspection — check bend radii, bundle tightness, airflow clearance  
Step 9: Photograph and document in DCIM  

### Quality Standards

A well-dressed rack should:
- Allow a single cable to be individually traced from end to end
- Have no cables touching the equipment face unnecessarily
- Allow rack doors to close without any cable interference
- Have consistent, neat appearance throughout
- Pass airflow inspection (no blocked vents)

### Knowledge Check Questions

1. Why should fiber cables be on the outside of cable bundles?
2. Why are zip ties not acceptable on fiber cables?
3. What is a service loop and why is it important?
4. List three consequences of poor cable dressing.
5. How often should Velcro straps be placed in a vertical cable run?

---

# MODULE 14: QUALITY CONTROL PROCEDURES

## Lesson 14.1 — QC Verification Standards

### Theory

Quality Control (QC) in a data center is the systematic process of verifying that all work meets defined standards before it is considered complete. Every installation, move, add, or change (IMAC) must pass QC verification before the work ticket is closed. Poor QC leads to outages, wasted time, and difficult troubleshooting.

### QC Checklist for New Cable Installations

**Label Verification:**
- [ ] All cables labeled at source end (format: RACK-DEVICE-PORT)
- [ ] All cables labeled at destination end
- [ ] Labels are legible, permanent, and correctly oriented
- [ ] Label content matches DCIM documentation
- [ ] No duplicate label IDs in the system

**Port Verification:**
- [ ] Cable connects to the correct port (as specified in work order)
- [ ] Port number matches documentation
- [ ] No cable in wrong port (verify by comparing physical port to DCIM)
- [ ] Link light present on both ends (if active circuit)
- [ ] Correct cable type for the port (AEC/DAC vs optic, CAT6 vs fiber)

**Fiber Inspection:**
- [ ] All fiber connectors inspected before connection
- [ ] All fiber connectors cleaned (one-click cleaner used)
- [ ] No fibers with visible damage (scratches, cracks, contamination on end face)
- [ ] Dust caps on all unconnected ports
- [ ] Dust caps on all installed cable ends when not in use

**Visual Inspection:**
- [ ] All cables properly dressed (Velcro, no zip ties on fiber)
- [ ] Minimum bend radius maintained throughout
- [ ] Service loops present and properly stored
- [ ] No cables draped across equipment faces
- [ ] Blanking panels in all empty rack units
- [ ] Rack doors close fully without cable interference
- [ ] No cables on rack floor (trip hazard, crush hazard)

**Documentation:**
- [ ] DCIM updated with all new connections
- [ ] Cable IDs assigned and recorded
- [ ] Port assignments documented
- [ ] Work order updated with completion notes
- [ ] Any deviations from plan documented with explanation
- [ ] Photos taken of completed work (where required)

### Fiber Inspection Procedure (Detailed)

1. Obtain fiber inspection scope
2. Insert scope adapter for LC connector
3. Place connector in scope adapter
4. View end face on screen
5. Assess cleanliness by zone:
   - Zone A (core): Zero contamination allowed
   - Zone B (cladding): Minor contamination in outer areas acceptable
6. If contamination found in Zone A or B: Clean and re-inspect
7. Document inspection result (PASS/FAIL)
8. Proceed with connection only after PASS

### Acceptance Testing for New Fiber Links

After completing a fiber link installation:
1. **Visual inspection** of all connectors and routing
2. **Optical power test** — measure received power at far end
3. **Compare to loss budget** — is received power within acceptable range?
4. **BERT test** (if required) — Bit Error Rate Test for mission-critical links
5. **Document results** — record optical power readings in DCIM

### Pre-Launch Checklist for New Rack Commissioning

Before a new rack goes live:

**Power:**
- [ ] PDU-A connected and powered
- [ ] PDU-B connected and powered
- [ ] Both PDUs showing on management network
- [ ] Load balance between PDU-A and PDU-B verified
- [ ] All server PSU-1 on PDU-A, PSU-2 on PDU-B

**Network:**
- [ ] All fiber connections tested and documented
- [ ] All switch ports configured per network plan
- [ ] All management connections active (IPMI reachable)
- [ ] VLAN configuration verified
- [ ] All servers reachable via IPMI

**Physical:**
- [ ] All blanking panels installed
- [ ] All rack doors can close fully
- [ ] Cable management complete per standards
- [ ] All labels applied and verified
- [ ] Temperature sensors reporting normal
- [ ] Rack properly grounded

### Terminology

| Term | Definition |
|------|-----------|
| **QC** | Quality Control — systematic verification of standards |
| **IMAC** | Install, Move, Add, Change — work order categories |
| **Acceptance Testing** | Verification that installed work meets specifications |
| **BERT** | Bit Error Rate Test — test for data transmission accuracy |
| **DCIM** | Data Center Infrastructure Management system |
| **Change Ticket** | Documented authorization for changes to infrastructure |
| **Punch List** | List of items that still need to be completed or corrected |

### Knowledge Check Questions

1. What are the five main areas of a QC checklist for cable installations?
2. What is the acceptable contamination level for Zone A of a fiber end face?
3. What is a BERT test used for?
4. List five items on a pre-launch checklist for a new rack.
5. Why must all deviations from plan be documented?

---

# MODULE 15: REAL-WORLD TECHNICIAN DAILY WORK

## Lesson 15.1 — Daily Responsibilities

### A Day in the Life of a Data Center Technician

Data center technicians perform a wide range of physical and technical tasks. Here is a realistic picture of daily work in an xAI-style data center:

### Morning Start-Up

1. **Review overnight tickets** — Check what alerts or issues occurred while you were off
2. **Review your work queue** — What installations, replacements, or repairs are scheduled today?
3. **Get your tools** — Gather fiber scope, cleaning supplies, Velcro, label printer, flashlight, ESD strap
4. **Check safety** — Is your PPE available? Is there any special permit required for today's work?

### Common Daily Tasks

**1. Dressing and Patching**

Dressing and patching is the most common physical task. It involves:
- Running new cables from one point to another
- Connecting (patching) cables to the correct ports
- Dressing cables neatly according to standards
- Labeling both ends of every cable

A good technician can:
- Plan the cable route before touching any cable
- Route cables without disturbing existing dressed cables
- Achieve neat, consistent dressing that matches the surrounding work
- Complete patching accurately on the first attempt

**2. Server Rack-and-Stack**

Installing new servers into racks:
- Verify server at correct rack unit per work order
- Mount rails in rack
- Slide server onto rails
- Connect PSU cables to PDU-A and PDU-B
- Connect NIC cables (fiber or AEC) per connectivity plan
- Connect BMC/IPMI cable
- Verify server powers on and is reachable via IPMI
- Document all port connections in DCIM

**3. Hardware Replacement**

Replacing failed components (drives, fans, PSUs, NICs):
- Open change ticket before starting
- Identify failed component via IPMI/monitoring
- Verify replacement part matches exactly (part number, speed, capacity)
- Power considerations — is hot-swap possible?
- Replace component following proper procedures
- Verify replacement is recognized by the system
- Close change ticket with result documentation

**4. Fiber Troubleshooting**

When a fiber link goes dark:
- Check both ends — are connectors fully seated?
- Inspect both fiber connectors with FOSI scope
- Clean connectors if dirty
- Measure optical power if possible
- Try a known-good fiber jumper to isolate cable vs. port failure
- Check transceiver seating
- Verify there are no over-bent sections in the cable run

**5. Labeling Campaigns**

Periodically, unlabeled or incorrectly labeled cables must be identified and labeled:
- Work methodically from one end of a row to the other
- Trace each cable from one end to the other to verify accuracy
- Create accurate labels and apply them
- Update DCIM with any discoveries

**6. Documentation Updates**

Accurate documentation is non-negotiable:
- Every change must be documented before the ticket is closed
- DCIM must reflect physical reality at all times
- Discrepancies between physical and DCIM are flagged and resolved

### Patching Procedure — Step by Step

**For a single mode fiber patch:**

1. Review work order — source port and destination port
2. Select correct fiber jumper (LC-LC duplex, correct length, OS2)
3. Inspect connectors — use FOSI scope
4. Clean connectors if needed
5. Remove dust caps from target ports
6. Insert source end connector — press until latch clicks
7. Insert destination end connector — press until latch clicks
8. Verify link lights on both devices
9. Apply labels to both ends of cable
10. Dress cable per standards
11. Update DCIM
12. Update work order as complete

**For a CAT6 copper patch:**

1. Review work order
2. Select correct patch cable (length, color, CAT6)
3. Route cable per cable management standards
4. Insert RJ45 connector firmly until it clicks
5. Verify link light on both devices
6. Apply labels
7. Dress cable
8. Update documentation

### Testing Standards

Every installed cable must be tested before the work ticket is closed:

**Fiber:**
- Inspect end faces before connection
- Verify link light after connection
- Measure optical power for critical links
- Record results in DCIM

**Copper (CAT6):**
- Verify link light after connection
- Test continuity for new terminations
- Certify new structured cabling runs with cable certifier

### Knowledge Check Questions

1. What tools should a technician always carry on the data center floor?
2. List the 10 steps of a fiber patching procedure.
3. What must be done before closing any work ticket?
4. What is the difference between a "patch" and a "run"?
5. Why is documentation considered a core technician responsibility?

### Module 15 Quiz

**Q1.** Before replacing a failed server drive, the technician must:
- A) Just replace it — drives are hot-swap
- B) Open an approved change ticket first ✓
- C) Power off the entire rack
- D) Notify all customers

**Q2.** After patching a fiber cable, the first thing to verify is:
- A) The label color matches
- B) The documentation is updated
- C) Link lights are active on both devices ✓
- D) The cable has a service loop

**Q3.** ESD wrist straps are required when:
- A) Walking on the data center floor
- B) Handling PCBs, memory, drives, or network cards ✓
- C) Running fiber cables only
- D) Using a label printer

---

# MODULE 16: DOCUMENTATION AND REPORTING

## Lesson 16.1 — DCIM and Documentation Standards

### Theory

Documentation is the invisible infrastructure of a data center. While cables and servers are visible, documentation records what everything is, where it is, what it's connected to, and its current state. Without accurate documentation, a large data center becomes unmanageable.

### DCIM — Data Center Infrastructure Management

DCIM software (such as ServiceNow, Sunbird, nlyte, or custom tools) manages:
- **Asset tracking:** Every physical device catalogued with make, model, serial number, location
- **Capacity management:** How much power, space, and cooling is used vs. available
- **Connectivity management:** What is connected to what (cable-level detail)
- **Environmental monitoring:** Temperature, humidity, power drawn from sensors
- **Change management:** Tracking approved changes vs. actual changes
- **Incident management:** Recording and tracking outages and their resolution

### Documentation Obligations

After every completed task:
1. **Asset record update:** If equipment was moved, added, or removed
2. **Connectivity update:** Every new or removed cable connection documented
3. **Label record update:** Labels added or changed recorded in DCIM
4. **Work order notes:** Completion notes including any deviations from plan
5. **Photos:** Before/after photos for significant installations

### What Makes Good Documentation

- **Accurate:** Matches physical reality exactly
- **Complete:** No gaps — every cable, every connection
- **Consistent:** Same format throughout
- **Current:** Updated in real-time as changes are made, not later from memory
- **Accessible:** Stored in a system accessible to all authorized staff

### Knowledge Check Questions

1. What is DCIM and what does it manage?
2. Why must documentation be updated immediately after making changes?
3. List 5 types of records in a DCIM system.
4. What is the consequence of inaccurate documentation in a large data center?

---

# MODULE 17: FINAL CERTIFICATION REVIEW

## Lesson 17.1 — Comprehensive Review

### Core Concepts Summary

**Infrastructure Hierarchy:**
- Server/GPU → Top-of-Rack Switch → SU Cabinet → Supercore

**Cable Types and Colors:**
- Yellow jacket = Single Mode Fiber (green LC connectors)
- Green jacket = CAT6 data cables
- Blue jacket = CAT6 PDU and management cables (3 per rack)
- Black = AEC/Rocky cables (short-distance high-speed interconnects)

**Power Redundancy:**
- Blue Cable #1 → PDU-A
- Blue Cable #2 → PDU-B
- Blue Cable #3 → Rack Management
- PDU-A + PDU-B = Dual-feed redundancy
- Each PDU should not exceed 50% capacity

**Management Infrastructure:**
- Single Mode Fiber used for IPMI management paths
- BMC = hardware chip on server for out-of-band management
- IPMI allows remote power, console, sensor monitoring

**Label System:**
- DH20 = Data Hall D, Column H, Position 20
- NA05 = Network Cabinet A, Position 5
- SCA/SCB = Supercore Cabinet A/B
- T = Top port, D = Down/Bottom port

**Quality Standards:**
- Fiber end faces must pass Zone A inspection before connection
- Every cable labeled at both ends
- All blanking panels installed
- Documentation updated with every change

---

*End of English Training Course — Version 1.0*

*Proceed to Certification Exam for assessment.*
