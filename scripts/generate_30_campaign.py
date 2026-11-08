#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_30_campaign.py
Generates 30-day comprehensive MA-DPP B2B Campaign content, schedule, and high-def HTML infographics
for Cosine Nanoelectronics (cosinechips.com) LinkedIn & Facebook Company Pages.
"""

import os
import json
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = BASE_DIR
HTML_DIR = os.path.join(OUTPUT_DIR, "html_cards")
os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "images"), exist_ok=True)

# 30-Day Master Campaign Data Matrix
CAMPAIGN_DATA = [
    # Phase 1: Regulatory Imperative & Architectural Foundation (Days 1–6)
    {
        "day": 1,
        "date": "2026-11-09",
        "time": "09:15",
        "tz": "CET (UTC+1)",
        "sku": "REGULATORY",
        "badge": "EU ESPR 2024/1781",
        "title": "The 2026 Semiconductor Digital Product Passport Mandate",
        "subtitle": "How EU Ecodesign Regulation Reshapes Component Procurement for Global Tier-1 OEMs",
        "highlight": "ISO/IEC 15459 Cryptographic Identity",
        "stats": [
            {"val": "100%", "lbl": "BOM Traceability"},
            {"val": "Node 100015", "lbl": "Universal Identifier"},
            {"val": "SHA-256", "lbl": "Tamper-Proof Proof"}
        ],
        "key_takeaways": [
            "Mandatory lifecycle carbon footprint & recyclability reporting under EU ESPR 2024/1781",
            "Zero broker blindspots: Direct die-level batch authentication via decentralized MA-DPP node",
            "Instant QR-scan access to SGS accredited lab chemical and ESD test dossiers"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Regulatory Architecture"
    },
    {
        "day": 2,
        "date": "2026-11-10",
        "time": "14:30",
        "tz": "CET (UTC+1)",
        "sku": "ARCHITECTURE",
        "badge": "ISO/IEC 15459",
        "title": "Deconstructing Node 100015: Cryptographic Silicon Identity",
        "subtitle": "How Cosine Implements Open Ucode & GS1 Interoperability at Sub-Micron Scale",
        "highlight": "Decentralized Registry Bond",
        "stats": [
            {"val": "128-bit", "lbl": "Unique Serial UID"},
            {"val": "0 Broker Risk", "lbl": "Authenticity Guarantee"},
            {"val": "API-Ready", "lbl": "Automated ERP Sync"}
        ],
        "key_takeaways": [
            "Hierarchical identification: MA.15602.315.1029 / CategoryCode / SKU / LotID",
            "Machine-readable JSON-LD Schema integrated directly with European circular data spaces",
            "Real-time validation against authorized factory test fixtures and fab lot runs"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Digital Standards"
    },
    {
        "day": 3,
        "date": "2026-11-11",
        "time": "10:45",
        "tz": "CET (UTC+1)",
        "sku": "VALIDATION",
        "badge": "SGS CSTC Certified",
        "title": "Cryptographically Sealed: SGS CSTC Laboratory Validation",
        "subtitle": "Permanent Binding of Independent Chemical & Immunity Test Dossiers to Each Die Run",
        "highlight": "Indivisible Legal Seal",
        "stats": [
            {"val": "IEC 61000-4-2", "lbl": "±15kV ESD Immunity"},
            {"val": "RoHS 2.0", "lbl": "10 Substances Pass"},
            {"val": "REACH SVHC", "lbl": "240+ Chemicals Clear"}
        ],
        "key_takeaways": [
            "Formal SGS test reports permanently embed product MA-DPP code on front cover and report seal",
            "Direct cryptographic hash comparison ensures zero unauthorized post-test doc modification",
            "Sub-ppm precision in lead-free solderability and halogen-free compound verification"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Third-Party Audit"
    },
    {
        "day": 4,
        "date": "2026-11-12",
        "time": "16:15",
        "tz": "CET (UTC+1)",
        "sku": "SUSTAINABILITY",
        "badge": "Full Material Declaration",
        "title": "Chemical Transparency: RoHS 2.0 & REACH SVHC Compliance",
        "subtitle": "100% Full Material Declaration (FMD) Down to Trace Element PPM Concentrations",
        "highlight": "Pure Silicon & Alloy Copper",
        "stats": [
            {"val": "<100 ppm", "lbl": "Halogen Content (IEC 61249)"},
            {"val": "Matte Sn", "lbl": "100% Lead-Free Leadframe"},
            {"val": "MSL 1 / MSL 3", "lbl": "JEDEC Moisture Sensitivity"}
        ],
        "key_takeaways": [
            "Complete elemental breakdown of wafer die, copper alloy leadframe, gold bonding wires, and molding resin",
            "Elimination of all hazardous polybrominated biphenyls and phthalate plasticizers",
            "Accelerates customer European CE & RoHS technical documentation filing by 80%"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Material Science"
    },
    {
        "day": 5,
        "date": "2026-11-13",
        "time": "11:20",
        "tz": "CET (UTC+1)",
        "sku": "AUTOMOTIVE",
        "badge": "AEC-Q100 Qualified",
        "title": "Automotive Ruggedness Meets Digital Traceability",
        "subtitle": "Grade 1 Temperature Endurance (-40°C to +125°C) with Complete Lot Provenance",
        "highlight": "Zero-Defect Philosophy",
        "stats": [
            {"val": "-40°C ~ +125°C", "lbl": "Operating Ambient Range"},
            {"val": "Grade 1", "lbl": "AEC-Q100 Stress Test"},
            {"val": "PPAP Level 3", "lbl": "Documentation Ready"}
        ],
        "key_takeaways": [
            "1000-hour High Temperature Operating Life (HTOL) and thermal cycling validated",
            "MA-DPP passport tracks wafer fab lot, assembly line, and final ATE testing lot data",
            "Crucial for EV battery management systems (BMS), telematics gateways, and powertrain modules"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Automotive Quality"
    },
    {
        "day": 6,
        "date": "2026-11-14",
        "time": "15:00",
        "tz": "CET (UTC+1)",
        "sku": "SECURITY",
        "badge": "Anti-Counterfeit",
        "title": "Eliminating Grey-Market Silicon: Real-Time QR Verification",
        "subtitle": "Protecting Industrial Infrastructure from Relabeled, Degraded, and Counterfeit Chips",
        "highlight": "Tamper-Proof Verification",
        "stats": [
            {"val": "3 Seconds", "lbl": "Mobile Field Verification"},
            {"val": "100%", "lbl": "Chain of Custody"},
            {"val": "Zero Clones", "lbl": "Cryptographic Hash"}
        ],
        "key_takeaways": [
            "Physical package laser etching matches digital passport record to prevent remarking fraud",
            "Field service engineers and incoming QC teams scan box or tape reel QR to instantly verify legitimacy",
            "Provides procurement leaders absolute legal defensibility against fraudulent broker batches"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Supply Chain Security"
    },

    # Phase 2: High-Reliability Industrial Transceivers (Days 7–12)
    {
        "day": 7,
        "date": "2026-11-15",
        "time": "08:50",
        "tz": "CET (UTC+1)",
        "sku": "COS13487",
        "badge": "RS-485 / RS-422",
        "title": "COS13487 MA-DPP: High-Speed 16Mbps RS-485 Transceiver",
        "subtitle": "±15kV ESD Protection, 1/8-Unit Load Supporting Up to 256 Nodes on Harsh Fieldbuses",
        "highlight": "Direct Pin-Compatible Alternative to MAX13487 / ADM3485",
        "stats": [
            {"val": "16 Mbps", "lbl": "High-Speed Baud Rate"},
            {"val": "±15 kV", "lbl": "IEC 61000-4-2 Air ESD"},
            {"val": "256 Nodes", "lbl": "True 1/8 Unit Load"}
        ],
        "key_takeaways": [
            "AutoDirection control eliminates explicit RTS line toggling in industrial PLCs",
            "Full digital passport reveals gold wire bonding, sulfur-resistant leadframe, and MSL1 packing",
            "SGS certified report SHA-256: d5a8e327... downloadable in one click"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos13487",
        "category": "Industrial Transceiver"
    },
    {
        "day": 8,
        "date": "2026-11-16",
        "time": "13:40",
        "tz": "CET (UTC+1)",
        "sku": "COS3485",
        "badge": "3.3V Low-Power",
        "title": "COS3485 MA-DPP: 3.3V RS-485 for Smart Metering & Grid",
        "subtitle": "Ultra-Low Quiescent Current with Slew-Rate Limiting for Reduced EMI and Grid Stability",
        "highlight": "Direct SN65HVD3082 / MAX3485 Pin-to-Pin Replacement",
        "stats": [
            {"val": "3.0V ~ 3.6V", "lbl": "Single Supply Operation"},
            {"val": "<1 µA", "lbl": "Ultra-Low Shutdown Current"},
            {"val": "10 Mbps", "lbl": "Max Data Rate"}
        ],
        "key_takeaways": [
            "Engineered for utility smart meters, solar microinverters, and building energy gateways",
            "Fail-safe receiver circuitry guarantees logic-high output under open/shorted bus conditions",
            "Passport includes thermal shock test data across 500 thermal cycles (-55°C to +150°C)"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos3485",
        "category": "Grid Infrastructure"
    },
    {
        "day": 9,
        "date": "2026-11-17",
        "time": "10:15",
        "tz": "CET (UTC+1)",
        "sku": "COS485",
        "badge": "5V Industrial Rugged",
        "title": "COS485 MA-DPP: 5V High-Noise Immunity RS-485 Transceiver",
        "subtitle": "Classic Robustness for Factory Floor Motor Drives, CNC Controls, and Substation Automation",
        "highlight": "Industry Standard Footprint: SOP-8 / DIP-8",
        "stats": [
            {"val": "5.0V ±10%", "lbl": "Robust Power Supply"},
            {"val": "-7V ~ +12V", "lbl": "Common-Mode Range"},
            {"val": "±15 kV", "lbl": "HBM ESD Protection"}
        ],
        "key_takeaways": [
            "Thermal shutdown protection defends against bus contention and fault conditions",
            "Verified RoHS lead-free alloy composition guarantees zero whisker risk over 15-year deployments",
            "Direct factory audit trail accessible via official MA-DPP Node 100015 ledger"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos485",
        "category": "Factory Automation"
    },
    {
        "day": 10,
        "date": "2026-11-18",
        "time": "15:45",
        "tz": "CET (UTC+1)",
        "sku": "COS1042",
        "badge": "CAN 2.0B / CAN-FD",
        "title": "COS1042 MA-DPP: High-Speed CAN Transceiver for Industrial Robotics",
        "subtitle": "Complete Galvanic Isolation Support, Standby Mode, and Low-Power Wake-Up Routing",
        "highlight": "TJA1042 / MCP2561 Compatible",
        "stats": [
            {"val": "5 Mbps", "lbl": "CAN-FD Timing Compliant"},
            {"val": "±58V", "lbl": "Bus Fault Voltage Protection"},
            {"val": "<5 µA", "lbl": "Low-Power Standby Current"}
        ],
        "key_takeaways": [
            "Advanced receiver filter prevents false wake-ups caused by electrical transients",
            "Full digital passport includes electromagnetic compatibility (EMC) spectral emissions scan",
            "Critical component for robotic joints, automated guided vehicles (AGV), and battery racks"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos1042",
        "category": "Robotics & Motion"
    },
    {
        "day": 11,
        "date": "2026-11-19",
        "time": "11:05",
        "tz": "CET (UTC+1)",
        "sku": "COS128",
        "badge": "Next-Gen CAN-FD",
        "title": "COS128 MA-DPP: Ultra-Fast CAN-FD Transceiver for Automotive Bus",
        "subtitle": "Symmetric TXD-to-RXD Propagation Delays for Demanding 5Mbps Flexible Data-Rate Networks",
        "highlight": "AEC-Q100 Grade 1 Automotive Validation",
        "stats": [
            {"val": "5 Mbps", "lbl": "ISO 11898-2:2016 Speed"},
            {"val": "±70V", "lbl": "Extended Bus Pin Tolerance"},
            {"val": "3.3V / 5V", "lbl": "VIO Logic Compatibility"}
        ],
        "key_takeaways": [
            "Dedicated VIO pin allows seamless interfacing with modern 3.3V and 1.8V microcontrollers",
            "MA-DPP passport binds factory ATE parameter distributions directly to wafer lot number",
            "Ensures strict compliance with EU circular economy disassembly protocols for end-of-life vehicles"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos128",
        "category": "Automotive CAN"
    },
    {
        "day": 12,
        "date": "2026-11-20",
        "time": "16:50",
        "tz": "CET (UTC+1)",
        "sku": "COS3232",
        "badge": "RS-232 / Charge Pump",
        "title": "COS3232 MA-DPP: 3.0V–5.5V RS-232 Transceiver with 0.1µF Caps",
        "subtitle": "High-Efficiency Dual Charge-Pump Architecture for Diagnostic Consoles and Telecom Radios",
        "highlight": "MAX3232 / SP3232 Equivalent",
        "stats": [
            {"val": "250 kbps", "lbl": "Guaranteed Data Rate"},
            {"val": "4 x 0.1µF", "lbl": "Minimal External BOM"},
            {"val": "300 µA", "lbl": "Low Operating Current"}
        ],
        "key_takeaways": [
            "Internal voltage doubler and inverter deliver EIA/TIA-232 levels from a single 3.3V rail",
            "MA-DPP details chemical breakdown of leadframe plating, proving 100% RoHS & REACH compliance",
            "Immediate availability in SOP-16 and TSSOP-16 with tamper-proof serialized packaging"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos3232",
        "category": "Telecom Interfaces"
    },

    # Phase 3: Ultra-Precision Analog & Zero-Drift Signal Chain (Days 13–18)
    {
        "day": 13,
        "date": "2026-11-21",
        "time": "09:30",
        "tz": "CET (UTC+1)",
        "sku": "COS333",
        "badge": "Zero-Drift Chopper",
        "title": "COS333 MA-DPP: 0.05µV/°C Ultra-Precision Zero-Drift Op-Amp",
        "subtitle": "Eliminating 1/f Flicker Noise with Continuous Internal Auto-Calibration for Strain Gauges",
        "highlight": "OPA333 / AD8628 Class-Leading Performance",
        "stats": [
            {"val": "0.05 µV/°C", "lbl": "Ultra-Low Offset Drift"},
            {"val": "10 µV max", "lbl": "Precision Input Offset"},
            {"val": "17 µA", "lbl": "Low Quiescent Current"}
        ],
        "key_takeaways": [
            "Rail-to-rail input and output swing enables dynamic range maximization in battery-powered instrumentation",
            "Digital product passport provides noise spectral density curves and die wafer yield metrics",
            "Crucial for medical patient monitoring, high-precision weigh scales, and thermocouple interfaces"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos333",
        "category": "Precision Op-Amps"
    },
    {
        "day": 14,
        "date": "2026-11-22",
        "time": "14:15",
        "tz": "CET (UTC+1)",
        "sku": "COS2182",
        "badge": "36V High-Voltage",
        "title": "COS2182 MA-DPP: 36V Dual High-Voltage Precision Op-Amp",
        "subtitle": "Sub-Microvolt Noise and Zero Thermal Drift for High-Voltage Industrial Control Loops",
        "highlight": "Direct AD8676 / OP2177 Equivalent",
        "stats": [
            {"val": "±2.5V ~ ±18V", "lbl": "Wide Supply Voltage"},
            {"val": "2.8 nV/√Hz", "lbl": "Ultra-Low Noise Density"},
            {"val": "10 MHz", "lbl": "Gain Bandwidth Product"}
        ],
        "key_takeaways": [
            "Bipolar input stages optimized for high-impedance sensor conditioning and industrial 4-20mA transmitters",
            "Passport tracks cleanroom environmental monitoring data and die attach curing profiles",
            "Fully compatible with automated pick-and-place tape/reel standards according to EIA-481"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos2182",
        "category": "High-Voltage Analog"
    },
    {
        "day": 15,
        "date": "2026-11-23",
        "time": "10:35",
        "tz": "CET (UTC+1)",
        "sku": "COS1177",
        "badge": "Ultra-Low Noise",
        "title": "COS1177 MA-DPP: Single Precision Low-Noise Operational Amplifier",
        "subtitle": "Uncompromising Signal Fidelity for Seismic Sensors, Audio Analysis, and Laser Spectroscopy",
        "highlight": "OP1177 / OPA177 Pin-Compatible",
        "stats": [
            {"val": "60 µV max", "lbl": "Input Offset Voltage"},
            {"val": "0.7 µV/°C", "lbl": "Offset Voltage Drift"},
            {"val": "130 dB", "lbl": "Common-Mode Rejection (CMRR)"}
        ],
        "key_takeaways": [
            "Laser-trimmed resistor network provides exceptional linearity across full industrial temperature extremes",
            "MA-DPP document proves absence of Conflict Minerals (3TG) compliant with OECD guidelines",
            "Immediate engineering sample dispatch with complete physical laboratory test dossiers"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos1177",
        "category": "Instrumentation"
    },
    {
        "day": 16,
        "date": "2026-11-24",
        "time": "15:20",
        "tz": "CET (UTC+1)",
        "sku": "COS2227",
        "badge": "Dual Bipolar Low-Noise",
        "title": "COS2227 MA-DPP: Dual Low-Noise Bipolar Precision Amplifier",
        "subtitle": "High Open-Loop Gain (120dB) and Fast Slew Rate for Automated Test Equipment (ATE)",
        "highlight": "OP227 / AD797 Family Class",
        "stats": [
            {"val": "3.2 nV/√Hz", "lbl": "Input Voltage Noise at 1kHz"},
            {"val": "11 V/µs", "lbl": "High Slew Rate"},
            {"val": "8 MHz", "lbl": "Gain Bandwidth"}
        ],
        "key_takeaways": [
            "Matched channel-to-channel tracking simplifies multichannel data acquisition system layout",
            "Integrated digital passport verifies MSL1 moisture resistance under JEDEC standard J-STD-020E",
            "SGS CSTC chemical testing validates lead-free matte tin finish with zero hazardous flame retardants"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos2227",
        "category": "ATE & Test Systems"
    },
    {
        "day": 17,
        "date": "2026-11-25",
        "time": "11:45",
        "tz": "CET (UTC+1)",
        "sku": "COS2171",
        "badge": "Single-Supply Precision",
        "title": "COS2171 MA-DPP: High-Precision Single-Supply Sensor Driver",
        "subtitle": "Rail-to-Rail Output Swing with Low Input Bias Current for Photodiode Amplification",
        "highlight": "OPA171 / AD8605 Industrial Equivalent",
        "stats": [
            {"val": "2.7V ~ 36V", "lbl": "Flexible Supply Rails"},
            {"val": "10 pA", "lbl": "Ultra-Low Input Bias"},
            {"val": "Rail-to-Rail", "lbl": "Dynamic Output Swing"}
        ],
        "key_takeaways": [
            "Eliminates negative supply rail requirements in distributed industrial sensor pods",
            "Full digital passport links directly to EU ESPR recyclability and material recovery directives",
            "Available in compact SOT-23-5 and MSOP-8 packages for dense PCB routing"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos2171",
        "category": "Sensor Signal Chain"
    },
    {
        "day": 18,
        "date": "2026-11-26",
        "time": "16:05",
        "tz": "CET (UTC+1)",
        "sku": "COS1333",
        "badge": "Micropower Zero-Drift",
        "title": "COS1333 MA-DPP: 15µA Zero-Drift Op-Amp for Medical Wearables",
        "subtitle": "Continuous Auto-Zeroing Architecture for Portable Diagnostics and Biosensors",
        "highlight": "Ultra-Low Power Precision",
        "stats": [
            {"val": "15 µA", "lbl": "Typical Supply Current"},
            {"val": "20 µV max", "lbl": "Input Offset Voltage"},
            {"val": "1.8V ~ 5.5V", "lbl": "Low-Voltage Battery Operation"}
        ],
        "key_takeaways": [
            "Prolongs wearable battery lifespan while preserving high CMRR (120dB) and PSRR (120dB)",
            "Digital product passport provides cleanroom particulate certification and bio-compatibility declarations",
            "Enables Tier-1 medical device builders to satisfy both EU MDR 2017/745 and EU ESPR 2024/1781"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos1333",
        "category": "Medical Electronics"
    },

    # Phase 4: General-Purpose, Low-Power & Rail-to-Rail Analog (Days 19–24)
    {
        "day": 19,
        "date": "2026-11-27",
        "time": "09:00",
        "tz": "CET (UTC+1)",
        "sku": "COS8552",
        "badge": "Rail-to-Rail Precision",
        "title": "COS8552 MA-DPP: Dual Rail-to-Rail I/O Precision Operational Amplifier",
        "subtitle": "High Common-Mode Rejection Across Entire Supply Range for Current Shunt Monitoring",
        "highlight": "AD8552 / MCP6022 Drop-In Replacement",
        "stats": [
            {"val": "5 MHz", "lbl": "Bandwidth Product"},
            {"val": "0.1 µV/°C", "lbl": "Zero-Drift Temperature Stability"},
            {"val": "Rail-to-Rail", "lbl": "Full Dynamic Input & Output"}
        ],
        "key_takeaways": [
            "Ideal for high-side and low-side current sensing in motor controllers and DC-DC converters",
            "MA-DPP verifies epoxy molding compound thermal degradation profiles and halogen-free compliance",
            "SGS CSTC test report permanently anchored under SHA-256 digital fingerprint"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos8552",
        "category": "Power Sensing"
    },
    {
        "day": 20,
        "date": "2026-11-28",
        "time": "14:40",
        "tz": "CET (UTC+1)",
        "sku": "COS8551",
        "badge": "Single Rail-to-Rail",
        "title": "COS8551 MA-DPP: Single Zero-Drift Rail-to-Rail Op-Amp in SOT-23",
        "subtitle": "Compact Footprint for Space-Constrained IoT Sensor Nodes and Handheld Calibrators",
        "highlight": "Ultra-Dense High-Precision Design",
        "stats": [
            {"val": "SOT-23-5", "lbl": "Ultra-Small Form Factor"},
            {"val": "1 µV", "lbl": "Typical Offset Voltage"},
            {"val": "130 dB", "lbl": "High Open-Loop Gain"}
        ],
        "key_takeaways": [
            "Permits micro-board placement close to transducers, reducing inductive noise pick-up",
            "Digital passport details packaging recycling codes (PAP 22 / PET 01) and storage MSL ratings",
            "Full compliance documentation instantly retrieved via ERP API connector"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos8551",
        "category": "IoT & Handheld"
    },
    {
        "day": 21,
        "date": "2026-11-29",
        "time": "10:20",
        "tz": "CET (UTC+1)",
        "sku": "COS8052",
        "badge": "High-Speed 250MHz",
        "title": "COS8052 MA-DPP: 250MHz High-Speed Rail-to-Rail Video Buffer",
        "subtitle": "Low Distortion (SFDR 85dB) and High Output Drive for Video Amplification & ADC Drivers",
        "highlight": "AD8052 / OPA2830 Compatible",
        "stats": [
            {"val": "250 MHz", "lbl": "Wide Bandwidth (-3dB)"},
            {"val": "180 V/µs", "lbl": "Ultra-Fast Slew Rate"},
            {"val": "4.5 mA/ch", "lbl": "Power-Efficient High Speed"}
        ],
        "key_takeaways": [
            "Drives differential ADCs and active filters with zero crossover distortion",
            "MA-DPP documents dielectric breakdown characteristics and bonding wire metallurgical purity",
            "Accelerates customs clearance across EU member states via verified digital certificate"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos8052",
        "category": "High-Speed Analog"
    },
    {
        "day": 22,
        "date": "2026-11-30",
        "time": "15:35",
        "tz": "CET (UTC+1)",
        "sku": "COS721",
        "badge": "1.8V Micropower",
        "title": "COS721 MA-DPP: 1.8V Low-Noise CMOS Operational Amplifier",
        "subtitle": "Sub-Volt Operation for Coin-Cell Powered Bluetooth Beacons and Environmental Tags",
        "highlight": "LMV721 / MCP6001 Direct Substitute",
        "stats": [
            {"val": "1.8V ~ 5.5V", "lbl": "Direct Battery Rail Support"},
            {"val": "10 MHz", "lbl": "High Bandwidth Efficiency"},
            {"val": "1 pA", "lbl": "CMOS Low Input Current"}
        ],
        "key_takeaways": [
            "Delivers 10MHz bandwidth with modest 950µA quiescent current for smart building telemetry",
            "MA-DPP passport highlights carbon emissions per 10,000 units manufactured in green certified fabs",
            "In stock for rapid delivery in high-volume tape and reel packaging"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos721",
        "category": "Low-Power CMOS"
    },
    {
        "day": 23,
        "date": "2026-12-01",
        "time": "11:10",
        "tz": "CET (UTC+1)",
        "sku": "COS6001",
        "badge": "600nA Nano-Amp",
        "title": "COS6001 MA-DPP: 600nA Sub-Microamp Op-Amp for 10-Year Lifespans",
        "subtitle": "Nano-Power Consumption for Smoke Detectors, Gas Sensors, and Remote Infrastructure Monitors",
        "highlight": "Decade-Long Battery Endurance",
        "stats": [
            {"val": "600 nA", "lbl": "Ultra-Low Quiescent Current"},
            {"val": "1.4V ~ 5.5V", "lbl": "Deep Battery Depletion Support"},
            {"val": "350 kHz", "lbl": "Bandwidth Product"}
        ],
        "key_takeaways": [
            "Maintains essential continuous signal monitoring on ultra-low standby budgets",
            "MA-DPP digital passport documents shelf-life preservation and zero moisture absorption packaging",
            "SGS chemical reports confirm zero restricted phthalates or brominated flame retardants"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos6001",
        "category": "Nano-Power"
    },
    {
        "day": 24,
        "date": "2026-12-02",
        "time": "16:25",
        "tz": "CET (UTC+1)",
        "sku": "COS7202",
        "badge": "Dual Nano-Comparator",
        "title": "COS7202 MA-DPP: Dual Nano-Power High-Speed Rail-to-Rail Comparator",
        "subtitle": "Built-In Hysteresis and Push-Pull Outputs for Window Detectors and Battery Level Alarms",
        "highlight": "TLV7202 / MCP6542 Functional Equivalent",
        "stats": [
            {"val": "4 µA", "lbl": "Supply Current per Comparator"},
            {"val": "160 ns", "lbl": "Fast Propagation Delay"},
            {"val": "4 mV", "lbl": "Internal Noise Hysteresis"}
        ],
        "key_takeaways": [
            "Internal hysteresis prevents parasitic oscillations when driven by slow-moving analog inputs",
            "Digital passport verifies copper leadframe annealing temperature and corrosion resistance",
            "Simplifies compliance auditing across European and North American tier-1 customers"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos7202",
        "category": "Comparators"
    },

    # Phase 5: Power Management, Gate Drivers & Specialized ICs (Days 25–28)
    {
        "day": 25,
        "date": "2026-12-03",
        "time": "08:40",
        "tz": "CET (UTC+1)",
        "sku": "COS4420",
        "badge": "6A High-Speed Driver",
        "title": "COS4420 MA-DPP: 6A High-Speed Dual MOSFET Driver for Solar Inverters",
        "subtitle": "Sub-25ns Rise/Fall Times with Heavy 2500pF Capacitive Loads for SiC and GaN Stages",
        "highlight": "TC4420 / MCP1407 Compatible",
        "stats": [
            {"val": "6A Peak", "lbl": "Output Gate Drive Current"},
            {"val": "25 ns", "lbl": "Ultra-Fast Rise Time"},
            {"val": "4.5V ~ 18V", "lbl": "Wide Operating Voltage"}
        ],
        "key_takeaways": [
            "Lowers switching losses in high-frequency DC-DC converters, motor drives, and solar inverters",
            "MA-DPP passport details thermal resistance parameters (Theta-JA) and die shear test results",
            "Cryptographically binds SGS electrical safety testing directly to physical reel barcodes"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos4420",
        "category": "Power Management"
    },
    {
        "day": 26,
        "date": "2026-12-04",
        "time": "13:55",
        "tz": "CET (UTC+1)",
        "sku": "COS4427",
        "badge": "Dual Non-Inverting",
        "title": "COS4427 MA-DPP: 1.5A Dual High-Speed MOSFET / IGBT Gate Driver",
        "subtitle": "Matched Propagation Delays and Latch-Up Immune Construction for Switching Power Supplies",
        "highlight": "TC4427 / MIC4427 Pin-for-Pin Fit",
        "stats": [
            {"val": "1.5A Peak", "lbl": "Symmetrical Drive Strength"},
            {"val": "20 ns", "lbl": "Delay Matching Between Channels"},
            {"val": ">500 mA", "lbl": "Reverse Latch-Up Current"}
        ],
        "key_takeaways": [
            "Eliminates cross-conduction in synchronous rectifiers and push-pull converter topologies",
            "MA-DPP tracks certified mold compound compositions and solder ball shear test stats",
            "Essential for European industrial heat pumps and commercial LED lighting drivers"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos4427",
        "category": "Gate Drivers"
    },
    {
        "day": 27,
        "date": "2026-12-05",
        "time": "10:50",
        "tz": "CET (UTC+1)",
        "sku": "COS603VGA",
        "badge": "Variable Gain (VGA)",
        "title": "COS603VGA MA-DPP: Low-Noise Differential Variable Gain Amplifier",
        "subtitle": "Continuous dB-Linear Gain Tuning for Ultrasonic Testing, Sonar, and Ultrasound Systems",
        "highlight": "AD603 / VCA810 Class Precision",
        "stats": [
            {"val": "90 MHz", "lbl": "Broadband Signal Bandwidth"},
            {"val": "40 dB", "lbl": "Precise Dynamic Gain Range"},
            {"val": "1.3 nV/√Hz", "lbl": "Low Input Voltage Noise"}
        ],
        "key_takeaways": [
            "Linear-in-dB gain control minimizes calibration overhead in automated non-destructive test rigs",
            "Digital product passport provides frequency response Bode plots and harmonic distortion tables",
            "Guarantees seamless regulatory compliance with EU ESPR and medical CE traceability standards"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos603vga",
        "category": "RF & Ultrasound"
    },
    {
        "day": 28,
        "date": "2026-12-06",
        "time": "15:15",
        "tz": "CET (UTC+1)",
        "sku": "COS12A12511",
        "badge": "Analog Mux / Demux",
        "title": "COS12A12511 MA-DPP: Low-Charge Injection Multi-Channel Analog Switch",
        "subtitle": "Ultra-Flat On-Resistance (0.5Ω) for Multichannel Battery Cell Voltage Monitoring (BMS)",
        "highlight": "High-Isolation Low-Leakage Multiplexing",
        "stats": [
            {"val": "0.5 Ω", "lbl": "Flat On-State Resistance"},
            {"val": "<5 pC", "lbl": "Low Charge Injection"},
            {"val": "±15V", "lbl": "Wide Dual-Supply Range"}
        ],
        "key_takeaways": [
            "Prevents measurement inaccuracies during micro-volt battery cell voltage balancing in EV packs",
            "MA-DPP passport certifies raw silicon wafer supplier provenance and assembly defect PPM",
            "Available in high-density QFN and TSSOP packages with zero leaded impurities"
        ],
        "dpp_url": "https://www.cosinechips.com/dpp-cos12a12511",
        "category": "Battery Management"
    },

    # Phase 6: Enterprise Procurement & Global Tier-1 Integration (Days 29–30)
    {
        "day": 29,
        "date": "2026-12-07",
        "time": "09:45",
        "tz": "CET (UTC+1)",
        "sku": "API_INTEGRATION",
        "badge": "Enterprise API",
        "title": "Automating BOM Compliance Audits via Cosine DPP API",
        "subtitle": "How Tier-1 EMS and Automotive Purchasing Teams Eliminate Manual Component Vetting",
        "highlight": "Machine-to-Machine Integration",
        "stats": [
            {"val": "REST / JSON", "lbl": "Standardized OpenAPI 3.0"},
            {"val": "<50 ms", "lbl": "Instant Verification Latency"},
            {"val": "100%", "lbl": "Automated ERP Matching"}
        ],
        "key_takeaways": [
            "Seamless webhook and REST endpoints connect Cosine product passports to SAP and Siemens Teamcenter",
            "Automated red-flagging if any component in your BOM approaches regulatory obsolescence",
            "Eliminates hundreds of engineering hours wasted requesting manual declarations and certificates"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Enterprise Systems"
    },
    {
        "day": 30,
        "date": "2026-12-08",
        "time": "14:10",
        "tz": "CET (UTC+1)",
        "sku": "SUPPLY_CHAIN",
        "badge": "48H Dispatch Guarantee",
        "title": "48-Hour Sample Dispatch & Full DPP Access: The Cosine Commitment",
        "subtitle": "Accelerating European Engineering Timelines with Pre-Certified, Production-Ready Silicon",
        "highlight": "Zero Supply Chain Bottlenecks",
        "stats": [
            {"val": "48 Hours", "lbl": "Sample Engineering Dispatch"},
            {"val": "52 ➔ 4 Wks", "lbl": "Lead Time Compression"},
            {"val": "100%", "lbl": "Fully Documented Passports"}
        ],
        "key_takeaways": [
            "Receive physical evaluation samples along with instantaneous access to full MA-DPP dossier",
            "Comprehensive replacement cross-reference matrix for TI, ADI, NXP, Maxim, and Renesas",
            "Direct engineering consultation with Cosine analog field application engineers within 4 hours"
        ],
        "dpp_url": "https://www.cosinechips.com/ma-dpp",
        "category": "Procurement Partnership"
    }
]

def generate_social_copies(item):
    """Generates targeted LinkedIn and Facebook copies."""
    day = item["day"]
    date = item["date"]
    time = item["time"]
    tz = item["tz"]
    sku = item["sku"]
    title = item["title"]
    subtitle = item["subtitle"]
    highlight = item["highlight"]
    badge = item["badge"]
    stats = item["stats"]
    takeaways = item["key_takeaways"]
    dpp_url = item["dpp_url"]
    
    # LinkedIn Copy (Professional, Technical, Executive B2B tone)
    li_bullets = "\n".join([f"🔹 {t}" for t in takeaways])
    li_stats = " | ".join([f"{s['lbl']}: {s['val']}" for s in stats])
    
    linkedin_copy = f"""🚨 EU ESPR Compliance Alert | Day {day} of 30: {title}

Under European Union Regulation 2024/1781 (ESPR) and international standard ISO/IEC 15459, semiconductor traceability is no longer optional—it is a non-negotiable prerequisite for placing electronics on the European single market.

{subtitle}

Key Engineering & Compliance Highlights:
{li_bullets}

📊 Verified Performance Metrics:
{li_stats}

🔐 Cryptographic Verification:
Every Cosine semiconductor integrates Node 100015 identity, tying wafer fab lots, AEC-Q100 stress tests, and official SGS CSTC chemical assays directly to an immutable SHA-256 digital fingerprint.

👉 Inspect the live Digital Product Passport & download the SGS lab dossier:
{dpp_url}

Need samples for qualification testing? Our engineering team guarantees dispatch within 48 hours. Connect with us at sales@cosinechips.com.

#Semiconductor #DigitalProductPassport #MADPP #EUESPR #AnalogIC #{sku} #SupplyChainCompliance #AutomotiveElectronics #CosineNanoelectronics #IndustrialAutomation"""

    # Facebook Copy (Engaging, Visual Storytelling, Clear CTA)
    fb_bullets = "\n".join([f"✓ {t}" for t in takeaways])
    
    facebook_copy = f"""[Day {day}/30: Cosine Semiconductor MA-DPP Series] ⚡

Is your component supply chain ready for the EU ESPR 2024/1781 mandate? 

Today, Cosine Nanoelectronics showcases the {title}—fully certified under international standard ISO/IEC 15459 Node 100015!

{subtitle}

Why European and global OEMs choose Cosine:
{fb_bullets}

🏆 Highlights:
• {stats[0]['lbl']}: {stats[0]['val']}
• {stats[1]['lbl']}: {stats[1]['val']}
• {stats[2]['lbl']}: {stats[2]['val']}

🔍 Scan or click to view the cryptographically verified passport and download official SGS test reports:
{dpp_url}

💬 Questions about pin-to-pin replacements or custom volume pricing? Message us directly or email sales@cosinechips.com!

#CosineChips #MADPP #Semiconductor #ElectronicsEngineering #SmartGrid #Robotics #RoHS #ISO15459"""

    return linkedin_copy, facebook_copy

def generate_html_card(item):
    """Generates high-definition HTML infographic card (1080x1350, 4:5 portrait ratio)."""
    day = item["day"]
    title = item["title"]
    subtitle = item["subtitle"]
    badge = item["badge"]
    highlight = item["highlight"]
    stats = item["stats"]
    takeaways = item["key_takeaways"]
    dpp_url = item["dpp_url"]
    category = item["category"]

    takeaways_html = "".join([f"""
        <div class="takeaway-item">
            <div class="check-icon">✓</div>
            <div class="takeaway-text">{t}</div>
        </div>
    """ for t in takeaways])

    stats_html = "".join([f"""
        <div class="stat-card">
            <div class="stat-val">{s['val']}</div>
            <div class="stat-lbl">{s['lbl']}</div>
        </div>
    """ for s in stats])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
        width: 1080px;
        height: 1350px;
        background: linear-gradient(135deg, #090D16 0%, #0F172A 50%, #1E293B 100%);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        color: #F8FAFC;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 64px 56px;
    }}
    /* Silicon Grid Background Effect */
    body::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: 
            linear-gradient(rgba(14, 165, 233, 0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(14, 165, 233, 0.04) 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
        z-index: 1;
    }}
    /* Ambient Glows */
    .glow-cyan {{
        position: absolute;
        top: -120px;
        right: -120px;
        width: 480px;
        height: 480px;
        background: radial-gradient(circle, rgba(6, 182, 212, 0.22) 0%, transparent 70%);
        pointer-events: none;
        z-index: 1;
    }}
    .glow-amber {{
        position: absolute;
        bottom: 80px;
        left: -100px;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(245, 158, 11, 0.15) 0%, transparent 70%);
        pointer-events: none;
        z-index: 1;
    }}
    
    .content-wrap {{
        position: relative;
        z-index: 2;
        display: flex;
        flex-direction: column;
        height: 100%;
        justify-content: space-between;
    }}

    /* Header */
    .header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
        padding-bottom: 28px;
    }}
    .brand-group {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .brand-logo-text {{
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #38BDF8, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .brand-sub {{
        font-size: 14px;
        color: #94A3B8;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-left: 2px solid rgba(255, 255, 255, 0.2);
        padding-left: 14px;
    }}
    .day-pill {{
        background: rgba(14, 165, 233, 0.15);
        border: 1px solid rgba(14, 165, 233, 0.4);
        color: #38BDF8;
        font-size: 16px;
        font-weight: 700;
        padding: 8px 20px;
        border-radius: 999px;
        letter-spacing: 0.5px;
    }}

    /* Title Section */
    .title-sec {{
        margin-top: 36px;
    }}
    .badge-row {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
    }}
    .tech-badge {{
        background: #0EA5E9;
        color: #04101E;
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 5px 14px;
        border-radius: 6px;
    }}
    .category-label {{
        color: #F59E0B;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .main-title {{
        font-size: 46px;
        font-weight: 800;
        line-height: 1.18;
        color: #FFFFFF;
        margin-bottom: 16px;
        letter-spacing: -0.5px;
    }}
    .main-sub {{
        font-size: 20px;
        color: #94A3B8;
        line-height: 1.45;
        max-width: 900px;
    }}

    /* Stats Grid */
    .stats-row {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin: 32px 0;
    }}
    .stat-card {{
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 16px;
        padding: 24px 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }}
    .stat-val {{
        font-size: 34px;
        font-weight: 900;
        color: #38BDF8;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }}
    .stat-lbl {{
        font-size: 13px;
        color: #CBD5E1;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}

    /* Highlight Banner */
    .highlight-box {{
        background: linear-gradient(90deg, rgba(245, 158, 11, 0.12), rgba(14, 165, 233, 0.08));
        border-left: 4px solid #F59E0B;
        padding: 16px 24px;
        border-radius: 8px;
        margin-bottom: 28px;
    }}
    .highlight-lbl {{
        font-size: 12px;
        color: #F59E0B;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 4px;
    }}
    .highlight-text {{
        font-size: 18px;
        color: #F8FAFC;
        font-weight: 600;
    }}

    /* Takeaways */
    .takeaways-card {{
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px 32px;
        margin-bottom: 32px;
    }}
    .takeaways-head {{
        font-size: 16px;
        color: #38BDF8;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
    }}
    .takeaway-item {{
        display: flex;
        gap: 16px;
        align-items: flex-start;
        margin-bottom: 16px;
    }}
    .takeaway-item:last-child {{
        margin-bottom: 0;
    }}
    .check-icon {{
        width: 26px;
        height: 26px;
        background: rgba(14, 165, 233, 0.2);
        color: #38BDF8;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 14px;
        flex-shrink: 0;
        margin-top: 2px;
    }}
    .takeaway-text {{
        font-size: 18px;
        color: #E2E8F0;
        line-height: 1.45;
        font-weight: 500;
    }}

    /* Footer Trust Area */
    .footer {{
        border-top: 1px solid rgba(255, 255, 255, 0.12);
        padding-top: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .trust-badges {{
        display: flex;
        gap: 14px;
    }}
    .trust-pill {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 8px;
        padding: 6px 14px;
        font-size: 12px;
        font-weight: 700;
        color: #94A3B8;
        text-transform: uppercase;
    }}
    .qr-cta {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .qr-box {{
        width: 72px;
        height: 72px;
        background: #FFFFFF;
        border-radius: 8px;
        padding: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .qr-box svg {{
        width: 100%;
        height: 100%;
    }}
    .cta-text-group {{
        text-align: right;
    }}
    .cta-title {{
        font-size: 15px;
        color: #FFFFFF;
        font-weight: 800;
        letter-spacing: 0.5px;
    }}
    .cta-url {{
        font-size: 13px;
        color: #38BDF8;
        font-weight: 600;
    }}
</style>
</head>
<body>
<div class="glow-cyan"></div>
<div class="glow-amber"></div>

<div class="content-wrap">
    <!-- Header -->
    <div class="header">
        <div class="brand-group">
            <div class="brand-logo-text">COSINE</div>
            <div class="brand-sub">Nanoelectronics · Official MA-DPP Hub</div>
        </div>
        <div class="day-pill">Day {day} / 30</div>
    </div>

    <!-- Title Section -->
    <div class="title-sec">
        <div class="badge-row">
            <span class="tech-badge">{badge}</span>
            <span class="category-label">{category}</span>
        </div>
        <h1 class="main-title">{title}</h1>
        <p class="main-sub">{subtitle}</p>
    </div>

    <!-- Stats Matrix -->
    <div class="stats-row">
        {stats_html}
    </div>

    <!-- Feature Highlight -->
    <div class="highlight-box">
        <div class="highlight-lbl">Engineering Benchmark</div>
        <div class="highlight-text">{highlight}</div>
    </div>

    <!-- Takeaways -->
    <div class="takeaways-card">
        <div class="takeaways-head">EU ESPR & ISO/IEC 15459 Technical Evidence</div>
        {takeaways_html}
    </div>

    <!-- Footer Trust Area -->
    <div class="footer">
        <div class="trust-badges">
            <div class="trust-pill">ISO/IEC 15459</div>
            <div class="trust-pill">SGS CSTC Sealed</div>
            <div class="trust-pill">RoHS 2.0 / REACH</div>
            <div class="trust-pill">AEC-Q100</div>
        </div>
        <div class="qr-cta">
            <div class="cta-text-group">
                <div class="cta-title">Scan / Query Digital Passport</div>
                <div class="cta-url">cosinechips.com/ma-dpp</div>
            </div>
            <div class="qr-box">
                <svg viewBox="0 0 100 100" fill="#0F172A">
                    <!-- Standard QR Aesthetic Representation -->
                    <rect x="10" y="10" width="28" height="28" rx="4" fill="none" stroke="#0F172A" stroke-width="8"/>
                    <rect x="20" y="20" width="8" height="8" fill="#0F172A"/>
                    <rect x="62" y="10" width="28" height="28" rx="4" fill="none" stroke="#0F172A" stroke-width="8"/>
                    <rect x="72" y="20" width="8" height="8" fill="#0F172A"/>
                    <rect x="10" y="62" width="28" height="28" rx="4" fill="none" stroke="#0F172A" stroke-width="8"/>
                    <rect x="20" y="72" width="8" height="8" fill="#0F172A"/>
                    <rect x="46" y="20" width="8" height="18" fill="#0F172A"/>
                    <rect x="46" y="46" width="18" height="8" fill="#0F172A"/>
                    <rect x="20" y="46" width="18" height="8" fill="#0F172A"/>
                    <rect x="72" y="46" width="8" height="24" fill="#0F172A"/>
                    <rect x="46" y="62" width="18" height="18" fill="#0F172A"/>
                    <rect x="72" y="78" width="18" height="12" fill="#0F172A"/>
                </svg>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
    return html

def main():
    print(f"🚀 Generating 30-Day MA-DPP Campaign for Cosine Nanoelectronics...")
    full_manifest = []

    for item in CAMPAIGN_DATA:
        day = item["day"]
        li_copy, fb_copy = generate_social_copies(item)
        html_card = generate_html_card(item)
        
        # Save HTML card
        html_path = os.path.join(HTML_DIR, f"day_{day:02d}.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_card)
        
        # Manifest entry
        manifest_item = {
            "day": day,
            "date": item["date"],
            "time": item["time"],
            "tz": item["tz"],
            "sku": item["sku"],
            "badge": item["badge"],
            "category": item["category"],
            "title": item["title"],
            "subtitle": item["subtitle"],
            "dpp_url": item["dpp_url"],
            "html_path": html_path,
            "image_filename": f"day_{day:02d}.png",
            "linkedin_copy": li_copy,
            "facebook_copy": fb_copy
        }
        full_manifest.append(manifest_item)
    
    # Save manifest JSON
    manifest_path = os.path.join(OUTPUT_DIR, "campaign_manifest_30_days.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(full_manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated 30 HTML cards in {HTML_DIR}")
    print(f"✅ Saved campaign manifest with 30 posts to {manifest_path}")

if __name__ == "__main__":
    main()
