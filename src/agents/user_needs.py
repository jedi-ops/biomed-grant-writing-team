from agno.agent import Agent
from textwrap import dedent
from src.model import model
from src.tools.utilities import file_tools

user_needs_agent = Agent(
    description="User Needs Identification for Medical Device Development",
    model=model,
    tools=[file_tools],
    instructions=dedent("""Please identify the key user needs for a new medical device. For each need, use the following format:
                    'As a [PERSONA], I need [NEED] so that [OUTCOME].'
                    Keep in mind that:
                        •	  Each user need must later be addressed by at least one product requirement.
                        •	  It is acceptable-and sometimes necessary-to have multiple product requirements address one user need in order to fully characterize it.
                        •	  Consider diverse personas (e.g., patients, clinicians, technicians) and use methods such as interviews, focus groups, ethnographic studies, and observations to uncover both explicit and latent needs.
                        •	  Document the needs clearly as high-level, actionable statements that will guide the development process."
                        •	Each User Needs need scientific rationale to support it. 

                    Include an Indications for Use, Intended Use, and Contraindications section as well. This will not be in the User Needs Format stated above. ")
                    """
                )
)