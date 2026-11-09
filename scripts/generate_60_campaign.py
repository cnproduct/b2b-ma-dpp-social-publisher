#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_60_campaign.py
Generates 60-day comprehensive MA-DPP B2B Multi-Platform Campaign:
- LinkedIn Company Page (Broadcast & Scheduled)
- Facebook Official Page (Meta Business Suite Verified)
- Reddit Community Graph (Odd Days: Anchor Discussion Topics; Even Days: Value-Add Expert Replies)
For Cosine Nanoelectronics (cosinechips.com).
"""

import os
import json
from datetime import datetime, timedelta

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKSPACE_DIR = "/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_60_campaign"
os.makedirs(WORKSPACE_DIR, exist_ok=True)
os.makedirs(os.path.join(WORKSPACE_DIR, "html_cards"), exist_ok=True)
os.makedirs(os.path.join(WORKSPACE_DIR, "images"), exist_ok=True)

# 60-Day Catalog Matrix: SKU, Focus, Subreddit, Key Themes
CAMPAIGN_TOPICS = [
    # Days 1-10: Regulatory & DPP Silicon Standards
    ("REGULATORY", "EU ESPR 2024/1781", "The 2026 Semiconductor Digital Product Passport Mandate", "How EU Ecodesign Regulation Reshapes Component Procurement for Global Tier-1 OEMs", "r/embedded", "ESPR 2024/1781"),
    ("ARCHITECTURE", "ISO/IEC 15459", "Deconstructing Node 100015: Cryptographic Silicon Identity", "How Cosine Implements Open Ucode & GS1 Interoperability at Sub-Micron Scale", "r/supplychain", "Node 100015"),
    ("VALIDATION", "SGS CSTC Certified", "Cryptographically Sealed: SGS CSTC Laboratory Validation", "Permanent Binding of Independent Chemical & Immunity Test Dossiers to Each Die Run", "r/ECE", "SGS RoHS"),
    ("PROVENANCE", "Wafer-to-Gate", "From Ingot to Tray: Eliminating Broker Blindspots in Silicon Sourcing", "Why Direct Foundry Lot Provenance Protects Against Counterfeit Recalls", "r/electronics", "counterfeit IC"),
    ("INTEGRATION", "API & JSON-LD", "Decentralized Registry Architecture for Enterprise BOM Verification", "Real-Time Machine-Readable DPP Schema Ingestion for Tier-1 PLM Systems", "r/SupplyChainTalks", "BOM compliance"),
    ("RECYCLABILITY", "Circular Silicon", "Lifecycle Carbon Footprint (PCF) & Materials Circularity in Power ICs", "Standardized GHG Protocol Scope 1-3 Disclosures for Green Tech Compliance", "r/sustainability", "Scope 3 emissions"),
    ("AUDITABILITY", "SHA-256 Ledger", "Zero-Knowledge Verifiable Credentials in High-Reliability Electronics", "How Cryptographic Hashes Guarantee Technical Data Sheet Immutability", "r/hardware", "SHA-256 hardware"),
    ("COMPLIANCE_API", "RESTful Passport", "Querying the Live MA-DPP Node: Automated ERP Ingestion for Supply Chain Directors", "How Procurement Teams Automate RoHS/REACH/ESD Certificate Retrieval", "r/embedded", "automated BOM"),
    ("TIER1_STRATEGY", "OEM Onboarding", "Bridging the Gap: What European Customs (Rotterdam/Hamburg) Will Check at Port", "Practical Guidelines for Electronics Exporters Facing Mandatory ESPR Checks", "r/supplychain", "Rotterdam customs"),
    ("STANDARDS_REVIEW", "Global Harmonization", "Comparing EU ESPR, US Clean Tech Mandates, and Asian Fab DPP Standards", "Building a Single Silicon Passport Valid Across Global Regulatory Borders", "r/ECE", "global compliance"),

    # Days 11-20: Industrial RS-485 / RS-422 Interface Transceivers
    ("COS3485E", "Drop-in MAX3485", "COS3485E 3.3V RS-485: ±15kV ESD Protection for Industrial Smart Meters", "Drop-in Replacement for MAX3485 / SN65HVD12 with Upgraded Transient Immunity", "r/AskElectronics", "MAX3485 replacement"),
    ("COS13487E", "Auto-Direction Control", "Eliminating Firmware RTS Toggle: COS13487E Auto-Direction RS-485 Transceiver", "Hardware-Driven Automatic Flow Direction for Isolated Multi-Drop Sensor Buses", "r/embedded", "RS-485 auto direction"),
    ("COS485", "5V Legacy Robustness", "COS485 5V High-Speed RS-485: Robust Communication in High-Voltage PLC Nodes", "Pin-to-Pin Alternative to ADM485 and SN75176 with 1/8 Unit Load (256 Nodes)", "r/PrintedCircuitBoard", "ADM485 alternative"),
    ("COS1487", "Low Power Industrial", "Low-Power Slew-Rate Limited RS-485 for Long-Haul Building Automation", "Reducing EMI Radiated Emissions in Multi-Kilometer Cable Runs", "r/electronics", "RS-485 EMI"),
    ("COS3088", "High-Speed 20Mbps", "COS3088 20Mbps High-Speed RS-485: Real-Time Motion Control & Servo Bus", "Ultra-Low Propagation Delay for High-Throughput Industrial Robotics", "r/ECE", "high speed RS485"),
    ("COS2587", "Isolated Transceiver", "Galvanic Isolation Meets DPP Traceability: COS2587 Integrated Isolated RS-485", "2.5kVRMS Signal & Power Isolation for EV Fast Chargers and Solar Inverters", "r/embedded", "isolated RS485"),
    ("COS3485ESA", "Smart Grid Grade", "COS3485ESA in Substation Automation: Withstanding Surge & Lightning Pulses", "Field-Proven Reliability under IEC 61000-4-5 Surge Standards", "r/hardware", "lightning surge IC"),
    ("COS491", "Full-Duplex RS-422", "COS491 Full-Duplex RS-422 / RS-485: Independent RX/TX for High-Duty Telemetry", "Drop-in for MAX491 / SN65HVD3088 in Industrial Scanners and CNC Controllers", "r/AskElectronics", "full duplex RS422"),
    ("COS13487_APP", "BMS Daisy Chain", "Case Study: RS-485 Bus Resilience in Megawatt Battery Energy Storage (BESS)", "Solving Ground Potential Shift and Common Mode Noise in Energy Storage Racks", "r/PrintedCircuitBoard", "BMS RS485"),
    ("INTERFACE_SUMMARY", "Pin-to-Pin Matrix", "The Complete TI/ADI/Maxim Interface IC Cross-Reference Guide & DPP Hub", "Over 50 Interface SKUs in Stock with Immediate Engineering Sample Dispatch", "r/ECE", "TI ADI cross reference"),

    # Days 21-30: Automotive & Industrial CAN Transceivers
    ("COS1050", "AEC-Q100 CAN", "COS1050 High-Speed CAN Transceiver: Automotive Grade Physical Layer", "Drop-in Replacement for TJA1050 / MCP2551 with Superior EMC Immunity", "r/embedded", "TJA1050 replacement"),
    ("COS1042", "CAN FD 5Mbps", "COS1042 CAN FD: 5Mbps Flexible Data-Rate for Next-Gen Automotive Telematics", "Low-Power Standby Mode with Remote Wake-Up for Electric Vehicle Body Controllers", "r/electronics", "CAN FD 5Mbps"),
    ("COS1044", "VIO Level Shifter", "COS1044 CAN FD with 1.8V / 3.3V Logic Level Interfacing: Direct MCU Connect", "Eliminating External Voltage Translators in Modern Dual-Voltage ECU Architectures", "r/PrintedCircuitBoard", "CAN VIO logic"),
    ("COS2542", "Isolated CAN FD", "5kVRMS Isolated CAN FD in High-Voltage Traction Inverters & DC-DC Converters", "Reinforced Isolation Barrier with Integrated Thermal Shutdown Protection", "r/hardware", "isolated CAN traction"),
    ("COS1051", "Silent Mode CAN", "COS1051 CAN Transceiver with Silent Mode: Diagnostic Port Security & Calibration", "Preventing Bus Jamming and Protocol Hijacking in Industrial IoT Gateways", "r/ECE", "CAN bus silent mode"),
    ("CAN_EMC_AUDIT", "CISPR 25 Class 5", "Pass Without Chokes: CAN Transceiver EMC Optimization & SGS Test Evidence", "How Cosine's Symmetrical Driver Architecture Minimizes Common-Mode RF Radiation", "r/embedded", "CAN bus EMC"),
    ("COS1040", "Fault-Tolerant CAN", "Low-Speed Fault-Tolerant CAN in Harsh Industrial Control Networks", "Sustaining Communication During Wire Break, Ground Short, or Battery Short", "r/AskElectronics", "fault tolerant CAN"),
    ("AEC_Q100_DEEP", "Zero Defect Fab", "AEC-Q100 Grade 1 Certification: Thermal Cycling (-40°C to +125°C) & Fab Controls", "Cryptographic Packaging of AEC-Q100 Stress Test Dossiers in Cosine MA-DPP", "r/supplychain", "AEC-Q100 qualification"),
    ("CAN_ROBOTICS", "AGV Fleets", "Field Telemetry: CAN FD Implementation in 24/7 Autonomous Mobile Robots (AMR)", "Mitigating Inductive Kickback and Ground Loops in Motor-Heavy Chassis", "r/hardware", "robotics CAN bus"),
    ("CAN_PORTFOLIO", "Cross-Reference Hub", "Complete Automotive CAN & CAN FD Cross-Reference: In-Stock Inventory & Samples", "Seamless Migration from NXP / Microchip / TI to Cosine with Direct DPP Access", "r/ECE", "NXP CAN alternative"),

    # Days 31-40: Precision Operational Amplifiers & Signal Chain
    ("COS721", "Low Noise CMOS", "COS721 1.8V Low-Noise RRIO Op-Amp: Precision Sensing in Battery-Powered IoT", "Ultra-Low 1pA Input Bias Current for Photodiode and Gas Sensor Amplification", "r/electronics", "low noise opamp"),
    ("COS822", "Dual Precision", "COS822 Dual Rail-to-Rail I/O Op-Amp: 10MHz Bandwidth for High-Gain Active Filters", "Drop-in for OPA2333 / AD8606 in Medical Diagnostics and Precision Instrumentation", "r/AskElectronics", "AD8606 drop in"),
    ("COS8552", "Zero-Drift Chopper", "COS8552 Zero-Drift Chopper Op-Amp: Sub-Microvolt Offset for Strain Gauge & Load Cells", "Eliminating 1/f Flicker Noise with 0.005µV/°C Thermal Drift Stability", "r/PrintedCircuitBoard", "zero drift opamp"),
    ("COS321", "General Purpose", "COS321 General Purpose 1MHz Op-Amp: High Value Signal Conditioning for Appliances", "Low Supply Current (60µA) and Wide 2.5V-5.5V Supply for Consumer White Goods", "r/embedded", "LM321 alternative"),
    ("COS824", "Quad RRIO", "COS824 Quad Precision Op-Amp: Multi-Channel ADC Input Driver in PLC Analog Modules", "Clean Settling Time and Rail-to-Rail Swing for 16-Bit SAR Data Acquisition", "r/ECE", "quad opamp ADC driver"),
    ("COS6001", "Nano-Power", "COS6001 600nA Ultra-Low-Power Op-Amp: Decade-Long Coin-Cell Battery Operation", "Always-On Environmental Sensor Front-Ends and Wearable Medical Patches", "r/hardware", "nanopower opamp"),
    ("COS8333", "Micro-Power Chopper", "COS8333 17µA Micro-Power Zero-Drift Op-Amp: Precision Without Thermal Throttle", "Thermocouple Cold-Junction Compensation with Flawless Gain Linearity", "r/AskElectronics", "thermocouple signal chain"),
    ("OPAMP_NOISE", "Noise Spectrum", "Benchmarking Input Voltage Noise & Distortion: Cosine Precision Op-Amps vs Tier-1", "Total Harmonic Distortion + Noise (THD+N) Analysis with SGS Verified Reports", "r/electronics", "opamp noise analysis"),
    ("BMS_CURRENT_SENSE", "Current Shunt", "Bi-Directional High-Side Current Sensing in EV Battery Packs Using COS8552", "Surviving High Common-Mode Transients While Resolving Milliamp Accuracy", "r/PrintedCircuitBoard", "high side current sense"),
    ("ANALOG_MATRIX", "Signal Chain Guide", "Cosine Analog Signal Chain Master Matrix: Cross-Reference to TI, ADI & Microchip", "Full Pin-to-Pin Compatibility & 48-Hour Sample Dispatch for Global Designers", "r/ECE", "analog cross reference"),

    # Days 41-50: High-Voltage Gate Drivers & Power Switching
    ("COS2113", "600V Half-Bridge", "COS2113 600V High- and Low-Side Gate Driver: 2A Peak Sink/Source for Si & IGBT", "Drop-in for IR2113 / FAN7390 in Motor Drives and Solar Micro-Inverters", "r/embedded", "IR2113 replacement"),
    ("COS2104", "Half-Bridge with DT", "COS2104 Half-Bridge Gate Driver: Integrated 520ns Dead-Time for Shoot-Through Prevention", "Protecting Power MOSFET Bridges in Brushless DC (BLDC) Drone and E-Bike Controllers", "r/PrintedCircuitBoard", "dead time gate driver"),
    ("COS2101", "High-Voltage Driver", "COS2101 High-Voltage High-Side Driver: Floating Channel Rated up to +600V", "Negative Transient Voltage Immunity (VS Spikes) in Inductive Hard-Switching Loads", "r/hardware", "high side gate driver"),
    ("COS2106", "Independent Inputs", "COS2106 High/Low Side Driver with Independent Inputs: Flexible Digital Control", "Direct 3.3V / 5V MCU Interface with Matched Propagation Delays Across Channels", "r/ECE", "MOSFET driver propagation"),
    ("COS4420", "High-Speed Low-Side", "COS4420 6A Single High-Speed Low-Side Driver: Ultra-Fast 25ns Rise/Fall Times", "Driving High-Capacitance Power MOSFETs in Server Synchronous Rectifiers", "r/electronics", "6A gate driver"),
    ("GATE_DRIVER_ROBUST", "dv/dt Immunity", "Withstanding 50V/ns dv/dt Slew Rates in GaN and Silicon Carbide (SiC) Applications", "Engineered Noise Immunity for Next-Generation Wide Bandgap Switching Stages", "r/hardware", "SiC gate driver noise"),
    ("COS2184", "Dead-Time Programmable", "COS2184 Half-Bridge Driver with Programmable Dead-Time via Single External Resistor", "Optimizing Switching Efficiency and Thermal Dissipation in Induction Heaters", "r/AskElectronics", "programmable dead time"),
    ("BLDC_MOTOR_CASE", "Industrial Servos", "Case Study: 3-Phase BLDC Inverter Design with Triple COS2113 Gate Drivers", "Thermal Dissipation, Bootstrap Diode Selection & Layout Best Practices", "r/PrintedCircuitBoard", "3 phase BLDC inverter"),
    ("GATE_DRIVER_DPP", "Silicon Identity", "Power Silicon Provenance: Why Counterfeit Gate Drivers Cause Catastrophic Fab Explosions", "Binding Wafer Lot Metallization and Bond Wire Integrity to MA-DPP Digital Credentials", "r/supplychain", "counterfeit power IC"),
    ("POWER_PORTFOLIO", "Driver Selection Hub", "Cosine Power Management & Gate Driver Cross-Reference: Drop-in for Infineon & TI", "Stocked in Shenzhen & Hong Kong Free Trade Zones for Immediate Global Air Freight", "r/ECE", "Infineon driver drop in"),

    # Days 51-60: Comparators, LDOs & Ecosystem Wrap-Up
    ("COS393", "Dual Comparator", "COS393 Low-Power Dual Voltage Comparator: 2.0V-36V Rail with Open-Collector Output", "Drop-in for LM393 / BA10393 with Ultra-Low Supply Current in Protection Circuits", "r/electronics", "LM393 drop in"),
    ("COS339", "Quad Comparator", "COS339 Quad Voltage Comparator: Multi-Point Over-Voltage & Under-Voltage Monitoring", "Precision Voltage Thresholds for Telecom Rectifiers and Industrial Power Shelves", "r/AskElectronics", "quad comparator circuit"),
    ("COS1117", "1A LDO Regulator", "COS1117 1A Low-Dropout Linear Regulator: Fixed & Adjustable 1.2V to 5.0V Outputs", "Stable with Low-ESR Ceramic Capacitors: Pin-Compatible Replacement for AMS1117", "r/PrintedCircuitBoard", "AMS1117 replacement"),
    ("COS7333", "Ultra-Low Iq LDO", "COS7333 3.3V Low-Dropout Regulator: 2µA Quiescent Current for IoT Sensors", "Extending Shelf Life in Battery-Powered Smoke Detectors and Asset Trackers", "r/embedded", "low quiescent LDO"),
    ("COS3401", "Power MOSFET P-Ch", "COS3401 -30V P-Channel Trench Power MOSFET: High-Density Reverse Battery Protection", "Low RDS(ON) (45mΩ) in Compact SOT-23 for Portable Handheld Equipment", "r/hardware", "reverse battery protection"),
    ("DPP_BOM_TOOL", "Automated Checker", "Introducing Cosine BOM Match & MA-DPP Auto-Check: Instant Compliance for 10,000+ SKUs", "Upload Your Altium/KiCad BOM and Download Cryptographically Validated Dossiers in 60s", "r/SupplyChainTalks", "BOM compliance tool"),
    ("GLOBAL_LOGISTICS", "48-Hour Dispatch", "Air Express Dispatch in 48 Hours: Tape & Reel Packaging for SMT High-Speed Mounters", "Full Reel MSL Level 1 Moisture Protection with Vacuum-Sealed Silica Desiccant", "r/supplychain", "component logistics"),
    ("OEM_CASE_STUDY", "European Tier-1", "How a Leading German Industrial Automation OEM Replaced Legacy ICs with Zero Line Stoppage", "Full Pin-to-Pin Drop-In Verification, EMI Compliance & DPP Dossier Approval", "r/ECE", "German OEM replacement"),
    ("COMMUNITY_AMA", "Engineering AMA", "Ask Us Anything: Semiconductor Design, Pin-to-Pin Drop-ins & EU DPP Compliance in 2026", "Cosine Senior Silicon Architects Answering Hardware Design & Supply Chain Questions", "r/embedded", "hardware AMA"),
    ("ECOSYSTEM_FINALE", "Full Passport Hub", "60-Day Technical Recap: The Semiconductor Digital Product Passport Hub is Live", "Direct Die-Level Silicon Traceability from Wafer to Board: Explore www.cosinechips.com", "r/ECE", "semiconductor traceability")
]

start_date = datetime(2026, 11, 9)

# Standard B2B Publishing Times
TIMES = ["09:15", "14:30", "10:45", "16:15", "11:30", "15:45", "11:00", "14:15", "09:45", "16:30"]

campaign_60 = []

for idx, item in enumerate(CAMPAIGN_TOPICS):
    day_num = idx + 1
    cur_date = start_date + timedelta(days=idx)
    date_str = cur_date.strftime("%Y-%m-%d")
    time_str = TIMES[idx % len(TIMES)]
    sku, badge, title, subtitle, target_sub, keyword = item

    is_topic = (day_num % 2 == 1) # Odd day: Topic/Question; Even day: Reply/Expert Answer

    # 1. LinkedIn Copy
    linkedin_copy = f"""🚀 [Day {day_num}/60: Cosine Semiconductor MA-DPP Technical Series] ⚡

{title}
{subtitle}

Under the EU Ecodesign for Sustainable Products Regulation (ESPR 2024/1781) and ISO/IEC 15459 Node 100015, semiconductor procurement is transitioning to decentralized cryptographic verification. 

Key Technical Highlights for {sku}:
✅ Standardized Pin-to-Pin drop-in replacement for legacy industrial ICs
✅ Direct foundry wafer-to-packaging provenance with SHA-256 digital seals
✅ Permanent binding to SGS CSTC accredited laboratory test dossiers (RoHS 2.0 / REACH / ESD)
✅ Instant QR-code & machine-readable JSON-LD Schema integration for enterprise PLM/ERP

🔍 Explore the Live MA-DPP Silicon Hub & Datasheets:
https://www.cosinechips.com/ma-dpp

📦 Samples Dispatch: Tape & Reel samples dispatch within 48 hours for qualification.
Direct Engineering Contact: sales@cosinechips.com | WhatsApp: +86 159 5954 3210

#CosineChips #Semiconductor #MADPP #EUESPR #AnalogIC #{sku} #ElectronicsEngineering #HardwareDesign #SupplyChainTraceability #ISO15459"""

    # 2. Facebook Copy (Strictly formatted with text + links + tags)
    facebook_copy = f"""[Day {day_num}/60: Cosine Semiconductor MA-DPP Series] ⚡

{title}
{subtitle}

Is your component supply chain prepared for mandatory EU ESPR 2024/1781 compliance? 

Today's Spotlight: {sku} ({badge})
Why European and global Tier-1 OEMs trust Cosine Nanoelectronics:
✓ Direct wafer lot die-level batch authentication via Node 100015 decentralized registry
✓ 100% BOM Traceability with immutable SHA-256 cryptographic test dossiers
✓ Instant mobile QR access to SGS accredited lab test reports
✓ Seamless pin-to-pin drop-in replacement—no PCB re-layout required!

🏆 Key Specifications:
• Category: {badge}
• Traceability Node: ISO/IEC 15459 Node 100015
• Sample Fulfillment: Dispatched within 48 hours

🔍 Inspect the verified silicon passport and download qualification reports:
https://www.cosinechips.com/ma-dpp

💬 Technical inquiries or volume pricing: Message us directly or email sales@cosinechips.com!

#CosineChips #MADPP #Semiconductor #ElectronicsEngineering #IndustrialAutomation #AnalogIC #{sku} #RoHS #ISO15459"""

    # 3. Reddit Content (Differentiated by Odd vs Even Day)
    if is_topic:
        reddit_mode = "create_topic"
        reddit_title = f"{title} - How are engineers addressing this for component BOMs?"
        reddit_body = f"""Hey {target_sub},

As EU ESPR 2024/1781 (Ecodesign for Sustainable Products Regulation) deadlines approach, our silicon engineering and quality team has been working on implementing decentralized Digital Product Passports (MA-DPP) compliant with ISO/IEC 15459 Node 100015.

Specifically regarding **{sku}** ({badge}):
{subtitle}

Key technical considerations we have encountered:
1. **Direct Die-Level Authentication**: Eliminating broker blindspots by linking raw wafer fab lot metallization to cryptographic SHA-256 seals.
2. **Lab Dossier Immutability**: SGS CSTC chemical compliance (RoHS 2.0 / REACH SVHC) and ESD transient reports (IEC 61000-4-2) permanently bound to QR/JSON-LD endpoints.
3. **Drop-in Compatibility**: Maintaining exact pin-to-pin drop-in compatibility so hardware teams do not face redesign cycles.

Curious to hear from practicing hardware and embedded design engineers:
- How is your team planning to aggregate sub-tier component compliance data?
- Are you seeing customers ask for automated API verification rather than static PDF declarations?

Technical whitepapers & live passport schema available for peer review at:
https://www.cosinechips.com/ma-dpp

Looking forward to hearing how others are handling this architecture transition."""
        reddit_reply_keywords = [keyword, sku, "ESPR", "DPP", "drop-in"]
        reddit_reply_template = ""
    else:
        reddit_mode = "reply_and_engage"
        reddit_title = f"Expert Technical Clarification: Addressing {sku} ({keyword}) in Industrial Applications"
        reddit_body = ""
        reddit_reply_keywords = [keyword, sku, "replacement", "alternative", "transceiver", "opamp", "gate driver"]
        reddit_reply_template = f"""Regarding {keyword} and drop-in replacements for industrial applications:

One common failure mode in noisy environments (such as factory automation, solar inverters, or battery management systems) is inadequate transient protection on the bus pins. When evaluating alternatives to legacy parts, consider:

1. **ESD Immunity**: Look for transceivers/ICs tested to IEC 61000-4-2 (±15kV Air / ±8kV Contact) with third-party lab verification (e.g. SGS CSTC).
2. **Unit Load & Node Count**: 1/8 unit load allows up to 256 nodes on a single physical bus without requiring repeaters.
3. **Traceability (EU ESPR / DPP)**: With new EU Ecodesign regulations, having verified die-level provenance and machine-readable compliance dossiers saves weeks of audit headaches.

For hardware engineers working on {sku} compatible designs, pin-to-pin specifications, waveform test benchmarks, and cryptographic passports are documented at:
https://www.cosinechips.com/ma-dpp

Hope this provides a useful reference for circuit reliability."""

    entry = {
        "day": day_num,
        "date": date_str,
        "time": time_str,
        "tz": "CET (UTC+1)",
        "sku": sku,
        "badge": badge,
        "title": title,
        "subtitle": subtitle,
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "image_filename": f"day_{day_num:02d}.png",
        "linkedin_copy": linkedin_copy,
        "facebook_copy": facebook_copy,
        "reddit": {
            "mode": reddit_mode, # "create_topic" or "reply_and_engage"
            "target_subreddit": target_sub,
            "flair": "Discussion" if is_topic else "Technical",
            "title": reddit_title,
            "body": reddit_body,
            "keywords": reddit_reply_keywords,
            "reply_template": reddit_reply_template
        }
    }
    campaign_60.append(entry)

# Write to Skill directory and Workspace
skill_json_path = os.path.join(SKILL_DIR, "campaign_manifest_60_days.json")
workspace_json_path = os.path.join(WORKSPACE_DIR, "campaign_manifest_60_days.json")

with open(skill_json_path, "w", encoding="utf-8") as f:
    json.dump(campaign_60, f, ensure_ascii=False, indent=2)

with open(workspace_json_path, "w", encoding="utf-8") as f:
    json.dump(campaign_60, f, ensure_ascii=False, indent=2)

# Initialize schedule_status_60_days.json
status_60 = []
for item in campaign_60:
    status_60.append({
        "day": item["day"],
        "date": item["date"],
        "time": item["time"],
        "sku": item["sku"],
        "title": item["title"],
        "linkedin_scheduled": False,
        "facebook_scheduled": False,
        "reddit_executed": False,
        "linkedin_status": "Pending",
        "facebook_status": "Pending",
        "reddit_status": "Pending"
    })

with open(os.path.join(SKILL_DIR, "schedule_status_60_days.json"), "w", encoding="utf-8") as f:
    json.dump(status_60, f, ensure_ascii=False, indent=2)

with open(os.path.join(WORKSPACE_DIR, "schedule_status_60_days.json"), "w", encoding="utf-8") as f:
    json.dump(status_60, f, ensure_ascii=False, indent=2)

print(f" Successfully generated 60-Day Campaign Manifest ({len(campaign_60)} items)!")
print(f"Skill Path: {skill_json_path}")
print(f"Workspace Path: {workspace_json_path}")
