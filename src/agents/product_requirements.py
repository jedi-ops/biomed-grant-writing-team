from agno.agent import Agent
from textwrap import dedent
from src.model import model
from src.tools.utilities import file_tools

product_requirement_agent = Agent(
    description="Product Requirements for Medical Device Development",
    model=model,
    tools=[file_tools],
    instructions=dedent("""Based on the provided user needs, please translate each need into actionable and measurable product requirements. Each requirement should begin with:
                        'The device shall...'
                        Ensure that:
                            •	﻿﻿Every user need is addressed by at least one product requirement (note that one user need may require multiple requirements to be fully characterized).
                            •	﻿﻿All requirements follow the MTV criteria (Measurable, Testable, or Verifiable) and are design-neutral.
                            •	﻿﻿In addition to translating user needs, also integrate any risk mitigations (from the risk analysis outputs) as product requirements.
                            •	﻿﻿Maintain clear traceability by linking each requirement back to its corresponding user need (s)."
                            •	Every requirement needs scientific rationale to support it. 
                        """)
)