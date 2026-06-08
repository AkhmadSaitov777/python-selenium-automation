# STUDY PLANS
## Data Center Technician Training Program
### Beginner and Advanced Tracks

---

# PART 1: BEGINNER STUDY PLAN
## "From Zero to Productive Data Center Technician"
### Timeline: 8 Weeks

---

## PROGRAM OVERVIEW

This plan takes a complete beginner with no data center experience and builds the knowledge and skills needed to safely and competently work in an xAI-style AI data center as a Tier 1 Data Center Technician.

**Weekly Commitment:** 10–15 hours per week (5 days × 2–3 hours/day)  
**Format:** Study + Practice + Lab + Review  
**Goal:** Pass the 100-question Certification Exam at 75%+ score

---

## WEEK 1: FOUNDATIONS AND SAFETY

### Monday (2 hours)
**Topic:** What is a Data Center?
- Read: Module 1 — Introduction to Data Centers (full module)
- Study: Terminology table — memorize all 10 terms
- Activity: Draw a simple diagram of a data center from memory after reading
- Quiz: Module 1 quiz (5 questions) — target 5/5

### Tuesday (2 hours)
**Topic:** Data Center Safety
- Read: Module 2 — Safety (full module)
- Memorize: The 7 safety rules (write them out from memory)
- Activity: Create your own "Safety Don'ts" checklist (what NOT to do)
- Quiz: Safety quiz — answer 10 safety questions from memory

### Wednesday (2 hours)
**Topic:** Rack Cabinet Structure
- Read: Module 3 — Rack Cabinets (full module)
- Study: Cable path sequence: Tray → Top Entry → VCM → HCM → Equipment
- Activity: Draw the cable path diagram from memory
- Memorize: 1U = 1.75 inches; 42U rack height; 19-inch standard width

### Thursday (2 hours)
**Topic:** Rack Navigation Practice
- Activity: Print or draw a 42U rack, label every 5th unit
- Exercise: Complete Lab 1 worksheet (Rack Navigation and Label Decoding)
- Practice: Count rack units and decode 10 label examples
- Review: Flashcards for all Week 1 terminology

### Friday (2 hours)
**Topic:** Week 1 Review and Quiz
- Review: All notes from this week
- Take: Practice test — 20 questions from Sections A and B of the Certification Exam
- Target score: 16/20 (80%)
- Identify: Which topics need more study

---

**WEEK 1 CHECKLIST:**
- [ ] Can recite 7 safety rules from memory
- [ ] Understands purpose of hot aisle / cold aisle
- [ ] Can draw cable path from tray to equipment
- [ ] Can count rack units correctly
- [ ] Can decode labels: DH20, NA05, NB13, SCA, SCB
- [ ] Scored 80%+ on Week 1 practice test

---

## WEEK 2: SINGLE MODE FIBER FUNDAMENTALS

### Monday (2 hours)
**Topic:** Introduction to Fiber Optics
- Read: Module 4 — Single Mode Fiber (first half — theory through connectors)
- Watch recommended: YouTube search "single mode fiber basics data center"
- Memorize: Yellow jacket, green LC connector, 8-10µm core, 30mm bend radius
- Flashcards: Create 10 fiber terminology flashcards

### Tuesday (2 hours)
**Topic:** Fiber Safety and Handling
- Read: Module 4 — Fiber safety and handling sections
- Critical memorization: NEVER look into active fiber; NEVER use zip ties on fiber
- Study: Bend radius rules; Velcro spacing rules
- Activity: Draw a fiber cable cross-section from memory (core, cladding, coating, jacket)

### Wednesday (2 hours)
**Topic:** Fiber Inspection and Cleaning
- Read: Module 4 — Fiber cleaning and inspection sections
- Memorize: 7-step inspection/cleaning procedure
- Study: Zone A, B, C, D inspection zones — Zone A must be clean
- Practice: Write out the cleaning procedure step-by-step without looking

### Thursday (2 hours)
**Topic:** Fiber Connections and Patching
- Read: Module 4 — Connectors and practical patching example
- Study: 10-step patching procedure
- Activity: Complete Lab 2 worksheet (fiber inspection concepts)
- Practice: Write the 10-step patching procedure from memory

### Friday (2 hours)
**Topic:** Week 2 Review and Quiz
- Review: All fiber notes
- Take: 15 questions from Section C of Certification Exam (fiber section)
- Target: 12/15 (80%)
- Study: Any missed questions in detail

---

**WEEK 2 CHECKLIST:**
- [ ] Knows: Yellow jacket = SMF; Green connector = LC for SMF
- [ ] Can state minimum fiber bend radius (30mm)
- [ ] Understands Zone A must be 100% clean
- [ ] Can explain the 7-step cleaning procedure
- [ ] Knows why zip ties are forbidden on fiber
- [ ] Scored 80%+ on Week 2 practice test

---

## WEEK 3: NETWORK ARCHITECTURE

### Monday (2 hours)
**Topic:** SU Cabinets
- Read: Module 5 — SU Cabinets (full module)
- Draw: Signal flow diagram Rack → SU (from memory after reading)
- Study: ToR switch concept; spine-leaf topology basics
- Terminology: Aggregation, uplink, downlink, spine, leaf

### Tuesday (2 hours)
**Topic:** Supercore Infrastructure
- Read: Module 6 — Supercore (full module)
- Draw: 3-tier hierarchy: Rack → SU → Supercore (ASCII art)
- Study: Why non-blocking fabric is critical for AI
- Memorize: SCA and SCB label meanings

### Wednesday (2 hours)
**Topic:** Network Hierarchy Review
- Review Diagram 1 (Architecture Diagrams file)
- Practice: Draw the complete network hierarchy from Rack to Supercore
- Activity: Answer these questions without looking at notes:
  1. What connects rack to SU cabinet?
  2. What connects SU to Supercore?
  3. What layer is "spine" in spine-leaf?
  4. What does non-blocking mean?
  5. What is ECMP?

### Thursday (2 hours)
**Topic:** Traffic Flow Understanding
- Review Diagram 8 (GPU-to-GPU traffic flow)
- Trace: How does traffic get from DH01 to DH50?
- Study: Where does Single Mode Fiber appear in the path?
- Study: Where do AEC cables appear in the path?

### Friday (2 hours)
**Topic:** Week 3 Quiz
- Take: 10 questions from Section D of Certification Exam
- Target: 8/10 (80%)
- Review: Any network topics that need reinforcement

---

## WEEK 4: IPMI AND MANAGEMENT

### Monday (2 hours)
**Topic:** IPMI Fundamentals
- Read: Module 7 — IPMI Management (full module)
- Memorize: What IPMI stands for; 7 functions it provides
- Key concept: Out-of-band vs. in-band management table
- Study: BMC definition and capabilities

### Tuesday (2 hours)
**Topic:** IPMI Commands and Tools
- Study: ipmitool command examples
- Practice: Write out commands for: power status, power on, temperatures, SEL
- Review Diagram 9 (IPMI network architecture)
- Study: Why management network must be separate from production

### Wednesday (2 hours)
**Topic:** Practical IPMI Scenario
- Work through: Scenario 7.2 in Troubleshooting Guide (server not reachable)
- Practice: What would you do step-by-step using IPMI to diagnose?
- Create: A "diagnosis card" for the 5 most common SEL error types

### Thursday (2 hours)
**Topic:** IPMI Lab Exercise
- Complete: Lab 6 (IPMI Simulation) in the Practical Labs file
- If no real IPMI system available: Use the lab 6 worksheet to practice command syntax
- Document: All answers in the lab worksheet

### Friday (2 hours)
**Topic:** Week 4 Quiz
- Take: 10 questions from Section E of Certification Exam
- Target: 8/10 (80%)

---

## WEEK 5: CABLES AND POWER

### Monday (2 hours)
**Topic:** CAT6 Copper Cabling
- Read: Module 8 — CAT6 (full module)
- Memorize: Max distances (100m @ 1GbE, 55m @ 10GbE)
- Study: T568B wiring standard pin-out (write from memory)
- Terminology: RJ45, NEXT, EMI, attenuation

### Tuesday (2 hours)
**Topic:** Blue CAT6 Assignments
- Read: Module 9 — Blue CAT6 (full module)
- Memorize: Blue #1 = PDU-A, Blue #2 = PDU-B, Blue #3 = Rack Management
- Review Diagram 5 (Blue cable assignments)
- Practice: Can you explain the 3-cable system without looking?

### Wednesday (2 hours)
**Topic:** PDU and Power Architecture
- Read: Module 10 — PDU (full module)
- Critical rule: Each PDU ≤ 50% load
- Draw: Dual power architecture from memory (Diagram 4)
- Study: Types of PDUs: basic → metered → monitored → switched

### Thursday (2 hours)
**Topic:** AEC and Rocky Cables
- Read: Module 11 — AEC (full module)
- Study: AEC vs. fiber comparison table
- Understand: Why AI racks have so many AEC cables (GPU interconnects)
- Review Diagram 10 (AEC cable density)

### Friday (2 hours)
**Topic:** Power Lab and Quiz
- Complete: Lab 4 (PDU Power Architecture) worksheet
- Take: 20 questions from Sections F, G, H of Certification Exam
- Target: 16/20 (80%)

---

**WEEK 5 CHECKLIST:**
- [ ] Knows CAT6 max distances
- [ ] Can assign blue cables without looking (PDU-A, PDU-B, Rack Mgmt)
- [ ] Understands dual power: PSU-1→PDU-A, PSU-2→PDU-B
- [ ] Knows the 50% PDU load rule
- [ ] Understands what AEC/Rocky cables are used for
- [ ] Can calculate PDU load percentages

---

## WEEK 6: LABELS, DRESSING, AND QC

### Monday (2 hours)
**Topic:** Label Reading and Systems
- Read: Module 12 — Labels (full module)
- Practice: Complete all 3 exercises in Module 12
- Memorize: Full label format for cables and ports
- Create: Flash cards for 20 common label formats

### Tuesday (2 hours)
**Topic:** Cable Dressing Standards
- Read: Module 13 — Cable Dressing (full module)
- Memorize: Dressing rules for fiber vs. copper
- Study: Common dressing mistakes table
- Review Diagram 11 (correct vs. incorrect dressing)

### Wednesday (2 hours)
**Topic:** Quality Control Procedures
- Read: Module 14 — QC (full module)
- Memorize: QC checklist categories (5 areas)
- Practice: Complete QC sign-off form from Lab 5 worksheet

### Thursday (2 hours)
**Topic:** Real-World Technician Work
- Read: Module 15 — Daily Work (full module)
- Study: 10-step patching procedure (fiber and copper)
- Review: Troubleshooting Guide Sections 1 and 2

### Friday (2 hours)
**Topic:** Week 6 Quiz
- Take: 20 questions from Sections I and J of Certification Exam
- Target: 16/20 (80%)

---

## WEEK 7: INTEGRATION AND TROUBLESHOOTING

### Monday (2 hours)
**Topic:** Troubleshooting Methodology
- Read: Full Troubleshooting Guide
- Study: Fiber, copper, power, and physical troubleshooting tables
- Create: Your own troubleshooting flowchart for "dark fiber link"

### Tuesday (2 hours)
**Topic:** Scenario Practice
- Work through: All scenarios in Lab 7 (Troubleshooting Scenarios)
- Write out: Complete step-by-step responses for each scenario
- Practice: Explaining your troubleshooting approach out loud

### Wednesday (2 hours)
**Topic:** Architecture Review
- Review: All Architecture Diagrams (file 08)
- Draw: From memory: complete network hierarchy
- Draw: Dual power architecture
- Draw: Three blue cable assignments

### Thursday (2 hours)
**Topic:** Full Practice Test (Part 1)
- Take: Questions 1–50 of the Certification Exam (full exam)
- Time yourself: 60 minutes maximum for 50 questions
- Score and review: Focus on missed questions

### Friday (2 hours)
**Topic:** Full Practice Test (Part 2)
- Take: Questions 51–100 of the Certification Exam
- Time yourself: 60 minutes maximum
- Calculate: Total score from both halves
- Review: All missed questions in detail

---

## WEEK 8: FINAL PREPARATION AND CERTIFICATION

### Monday–Wednesday (2 hours each)
**Topic:** Targeted Review
- Each day, focus on your weakest section from the practice tests
- Re-read the corresponding module
- Re-do the relevant practice questions
- Use the Cheat Sheet for final reinforcement

### Thursday (2 hours)
**Topic:** Final Integrated Review
- Quick review: Cheat Sheet (one page summary)
- Review: Glossary EN-RU for any uncertain terms
- Mental walk-through: Imagine yourself performing each task
- Confidence check: Quiz yourself on the top 20 most important facts

### Friday
**CERTIFICATION EXAM DAY**
- Arrive rested and on time
- No open-book materials (closed exam)
- 120 minutes for 100 questions
- Target: 75+ correct to certify; 90+ for Advanced certification

---

# PART 2: ADVANCED STUDY PLAN
## "Data Center Infrastructure Engineer"
### For Experienced Technicians Seeking Advancement
### Timeline: 12 Weeks

---

## OVERVIEW

This plan assumes completion of the Beginner track (or equivalent experience) and focuses on deeper technical understanding, architectural design principles, and the ability to train others.

**Prerequisite:** Passed Beginner Certification Exam at 75%+  
**Weekly Commitment:** 12–15 hours/week  
**Goal:** Expert-level understanding; ability to design, implement, and troubleshoot all aspects of the xAI-style data center environment

---

## ADVANCED TRACK MODULES

### Weeks 1–2: Advanced Fiber Optics

**Topics to master:**
- OTDR (Optical Time Domain Reflectometer) testing and trace interpretation
- Loss budget calculations for complex multi-hop fiber paths
- Fiber polarity standards (TIA-568 Method A, B, and C)
- MPO/MTP trunk cable systems and breakout configurations
- Fiber splicing concepts (fusion and mechanical)
- DWDM (Dense Wavelength Division Multiplexing) basics
- Coherent optics for 100G/400G beyond simple SMF

**Study Activities:**
1. Draw and calculate loss budgets for 5 sample fiber paths
2. Research OTDR trace interpretation — identify: breaks, connectors, splices, reflections
3. Study the TIA-568 polarity methods table — create your own summary
4. Research MPO trunk systems used in data centers

**Lab Exercise:**
Using an OTDR (real or simulation software), interpret an OTDR trace and identify:
- Total fiber length
- All connector locations
- Any anomalies (reflections, high-loss points)

---

### Weeks 3–4: Advanced Network Architecture

**Topics to master:**
- InfiniBand (IB) vs. Ethernet in AI clusters — when each is used
- RoCE (RDMA over Converged Ethernet) and its requirements
- BGP and EVPN for large-scale data center routing
- Understanding switch ASICs (Tomahawk, Spectrum, Taishan)
- 400G and 800G transceiver types and standards
- Coherent DWDM for DCI (Data Center Interconnect)
- Network timing and synchronization (PTP/IEEE 1588)

**Study Activities:**
1. Compare InfiniBand HDR/NDR to 400GbE in terms of latency and bandwidth
2. Research what RoCE requires from the network (QoS, ECN, PFC)
3. Draw a fat-tree topology for a 1024-GPU cluster — calculate port counts at each tier

---

### Weeks 5–6: Advanced Power and Cooling

**Topics to master:**
- Data center PUE (Power Usage Effectiveness) calculation
- UPS topologies: online double-conversion vs. line-interactive
- Generator systems: diesel gensets, transfer switching
- Cooling technologies: CRAC, CRAH, rear-door heat exchangers, liquid cooling
- Direct liquid cooling (DLC) for high-density AI servers
- Power capacity planning methodology
- Electrical distribution: from utility to server (complete path)
- Phase balancing in three-phase power systems

**Study Activities:**
1. Calculate PUE for a sample data center given IT load and total facility power
2. Research liquid cooling options for GPU servers
3. Draw a complete power distribution path from utility to server
4. Calculate three-phase load balance for a row of 10 racks

---

### Weeks 7–8: Large-Scale Operations

**Topics to master:**
- DCIM (Data Center Infrastructure Management) systems in depth
- Change management processes in large-scale environments
- Capacity planning: space, power, cooling, network
- Migration planning: moving live workloads without downtime
- Vendor management and escalation procedures
- SLA management and incident response
- Post-incident reviews and root cause analysis

**Study Activities:**
1. Design a capacity planning spreadsheet for a 100-rack deployment
2. Write a change management procedure for upgrading a live ToR switch
3. Create an incident response runbook for "PDU-A failure in production rack"

---

### Weeks 9–10: AI Infrastructure Specifics

**Topics to master:**
- GPU cluster architecture: NVLink, NVSwitch, GPU Direct
- High-performance storage: NVMe over Fabrics, GPFS, Lustre
- Job schedulers: SLURM, Kubernetes, Kubeflow
- GPU health monitoring: DCGM (Data Center GPU Manager)
- Thermal design for extreme GPU density
- Rocky/AEC cable qualification and testing
- AI workload characteristics and infrastructure requirements

**Study Activities:**
1. Research xAI's Colossus facility architecture — compare to what you've learned
2. Study NVIDIA NVLink and NVSwitch architecture documentation
3. Research DCGM monitoring capabilities and common GPU errors

---

### Weeks 11–12: Leadership and Training

**Topics to master:**
- Technical documentation writing
- Training delivery and knowledge transfer
- Building standard operating procedures (SOPs)
- Root cause analysis methodologies
- Technical interview skills
- Infrastructure design review

**Capstone Project:**
Create a complete deployment plan for a new 20-rack AI training pod:
1. Network topology diagram (ASCII or Visio)
2. Power architecture diagram
3. Cable count by type (fiber, CAT6, AEC)
4. Label naming scheme
5. QC verification checklist
6. Operations runbook for common tasks
7. Troubleshooting guide for the deployment

---

## ADVANCED CERTIFICATION CRITERIA

To receive Advanced Data Center Engineer designation:
- Pass Certification Exam with 90%+ score
- Complete all 7 Practical Labs with supervisor sign-off
- Complete the Capstone Project with instructor review
- Demonstrate proficiency in at least 3 practical skills:
  1. Fiber inspection, cleaning, and patching
  2. PDU load calculation and management
  3. IPMI troubleshooting and server management
  4. Cable dressing to professional standard
  5. DCIM documentation and audit

---

# STUDY TIPS FOR BOTH TRACKS

## Memory Techniques

**For cable colors — "YGBK" (say "Yay G-B-K"):**
- **Y**ellow = Fiber (SMF)
- **G**reen = CAT6 data
- **B**lue = Management/PDU
- **B**lack = AEC/Rocky

**For blue cable assignments — "APB" (A-side Power, B-side power, mgt):**
- Blue 1 = **A**-side PDU (PDU-A)
- Blue 2 = **B**-side PDU (PDU-B)
- Blue 3 = Management

**For PDU load rule — "Five-Oh Rule":**
- Each PDU at 50% max. Say it until it's automatic.

**For fiber bend radius — "Thirty is the limit":**
- 30mm minimum. Always. Never less.

## Study Environment Tips

1. **Study in short, focused sessions** (45-60 min with breaks) — not marathon sessions
2. **Write things by hand** — physical writing improves retention
3. **Teach concepts out loud** — explaining it to an imaginary student reveals gaps in understanding
4. **Use the cheat sheet** — refer to it daily; it contains the most critical information
5. **Visit a real data center floor** if possible — seeing it in person accelerates understanding enormously

## Common Beginner Mistakes to Avoid

1. **Rushing through fiber inspection** — always take the time to inspect and clean
2. **Skipping labels** — "I'll come back and label it later" becomes "I can't figure out what this is"
3. **Guessing on troubleshooting** — follow the methodology; don't jump to conclusions
4. **Forgetting change tickets** — even small changes need documentation
5. **Not asking questions** — no question is too basic; asking beats guessing in a live environment

---

*End of Study Plans*  
*Good luck with your Data Center Technician certification!*  
*Желаем успехов в получении сертификата технического специалиста дата-центра!*
