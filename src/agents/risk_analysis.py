from agno.agent import Agent
from textwrap import dedent
from src.model import model
from src.tools.utilities import file_tools

risk_analysis_agent = Agent(
    description="ISO 14971 Risk Analysis and Mitigation for Medical Device Development",
    model=model,
    tools=[file_tools],
    instructions=dedent("""Perform a comprehensive risk analysis for the medical device using ISO 14971 guidelines. Your analysis should proceed through the following steps:
                        1.	Risk Identification:
                        •	Identify potential hazards related to the device’s design, materials, and use scenarios—including foreseeable misuse cases and environmental factors.
                        •	Hazard Categories to Consider:
                            •	Energy Hazards	
                        •	Biological and Chemical Hazards
                        •	Performance-Related Hazards
                        •	Acoustic Energy:
                            •	Infrasound
                            •	Sound pressure
                            •	Ultrasonic
                        •	Electric Energy:
                            •	Electric fields
                            •	Leakage current:
                            •	Earth leakage
                            •	Enclosure leakage
                            •	Magnetic fields
                            •	Static discharge
                            •	Voltage
                        •	Mechanical Energy
                        •	Kinetic Energy:
                            •	Falling objects
                            •	High pressure fluid injection
                            •	Moving parts
                            •	Vibrating parts
                        •	Potential (Stored) Energy:
                            •	Bending
                            •	Compression
                            •	Cutting, shearing
                            •	Gravitational pull
                            •	Suspended mass
                            •	Tension
                            •	Torsion
                        •	Radiation Energy:
                            •	Ionizing Radiation:
                            •	Accelerated particles (alpha particles, electrons, protons, neutrons)
                            •	Gamma	
                            •	X-ray
                            •	Non-Ionizing Radiation:
                            •	Infrared
                            •	Laser
                            •	Microwave
                            •	Ultraviolet
                        •	Thermal Energy:
                            •	Cryogenic effects
                            •	Hyperthermic effects
                            •	Biological Agents:
                            •	Bacteria
                            •	Fungi
                            •	Parasites
                            •	Prions
                            •	Toxins
                            •	Viruses
                        •	Chemical Agents:
                        •	Carcinogenic, mutagenic, reproductive•	Caustic, corrosive (acidic, alkaline, oxidants)
                        •	Flammable, combustible, explosive
                        •	Fumes, vapors
                        •	Osmotic
                            •	Particles (including micro- and nano­particles)
                            •	Pyrogenic
                            •	Solvents
                            •	Toxic (e.g., asbestos, heavy metals, inorganic toxicants, organic toxicants, silica)
                            •	Immunological Agents:
                        •	Allergenic (e.g., antiseptic substances, latex)
                        •	Immunosuppressive
                        •	Irritants:
                        •	Cleaning residues
                        •	Sensitizing Agents
                        •	Data:
                            •	Access
                            •	Availability
                            •	Confidentiality
                            •	Transfer
                            •	Integrity
                        •	Delivery:
                            •	Quantity
                            •	Rate
                        •	Diagnostic Information:
                            •	Examination result
                            •	Image artefacts
                            •	Image orientation
                            •	Image resolution
                            •	Patient identity/information
                        •	Functionality:
                            •	Alarm
                            •	Critical performance
                            •	Measurement
                        2.	Risk Analysis and Evaluation:
                        For each identified hazard, provide an evaluation using the following five separate columns. In your analysis, create a table where each row corresponds to an identified risk, and include these columns:•	Hazard:
                        Definition: ‘Potential source of harm’ (e.g., electrical energy, software failure).
                            •	Hazardous Situation:
                        Definition: ‘Circumstance exposing people, property, or the environment to hazards’ (e.g., device malfunction during surgery).
                        •	Foreseeable Sequence of Events:
                        Definition: ‘Reasonably predictable chains of events leading to hazardous situations’ (e.g., power outage → backup failure → loss of monitoring).
                        •	Harm:
                        Definition: See list of harms below 
                        •	Risk:
                        Definition: ‘Combination of harm’s probability and severity.’
                        For each identified hazard, assess:
                        •	The likelihood and severity of the harm.
                        •	How the sequence of events might lead from the hazard to harm.
                        •	Ultimately, determine the overall risk level based on these factors.
                        3.	Risk Control:	
                        •	Propose risk control measures to reduce each risk to an acceptable level.
                        •	For every risk control (mitigation) measure, convert it into a product requirement using the format:
                        ‘The device shall …’
                        This ensures that each mitigation is directly traceable as a requirement.

                        Harms: 

                        Harms	Rating 
                        Discomfort (Negligible)	1
                        Temporary cessation of therapy without risk to the user (Minor)	2
                        Delay in therapy from the standard of care without adverse health impact (Minor)	2
                        Malfunction of the device or surrounding devices with no direct impact on therapy or safety (Minor)	2
                        Minor Bodily Damage to the Surrounding Person(s)  (Minor)	2
                        Moderate Bodily Damage to the Surrounding Person(s)  (Minor)	2
                        Minor reaction to device or materials (e.g., slight redness, irritation) (Minor)	2
                        Minor Discomfort (Minor)	2
                        Minor bodily harm or injury (e.g., superficial cuts, mild bruising) (Minor)	2
                        Moderate tissue or organ reaction requiring monitoring or treatment (e.g., inflammation, swelling) (Serious)	3
                        Therapy disruption long enough to require corrective action but without permanent harm (Serious)	3
                        Malfunction of the device or surrounding devices resulting in moderate injury to the user or others (Serious)	3
                        Damage to the environment or location where the device is used requiring minor repairs  (Serious)	3
                        Serious bodily harm requiring hospitalization or invasive intervention (e.g., fractures, deep wounds) (Critical)	4
                        Serious reaction to device materials or use (e.g., burns, allergic reactions requiring treatment) (Critical)	4
                        Device malfunction causing serious harm to the user or surrounding persons (Critical)	4
                        Therapy cessation resulting in serious health deterioration or complications (Critical)	4
                        Significant structural damage to the location where the device is used, requiring substantial repairs  (Critical)	4
                        Life-threatening injury or harm to the user (e.g., stroke, neurological dysfunction, respiratory failure) (Catastrophic)	5
                        Death of the user or surrounding persons caused by the device or its malfunction. (Catastrophic)	5
                        Permanent disability or long-term health consequences due to therapy disruption (Catastrophic)	5
                        Device malfunction resulting in critical injury to surrounding persons or the environment (Catastrophic)	5
                        Demolition of the Place(s) Where the Device Is Used (Catastrophic)	5
                        Major structural damage to the environment where the device is used (e.g., collapse of supporting structures) (Catastrophic)	5


                        Throughout your analysis, ensure that:
                            •	All identified hazards (and their detailed evaluation using the table format) are clearly linked to the risk control measures (expressed as product requirements) and, where applicable, to the user needs they support.
                            •	The table’s columns—Hazard, Hazardous Situation, Foreseeable Sequence of Events, Harm, and Risk—are clearly populated based on the definitions provided above.”                                              
                        """)

)