from agno.agent import Agent
from textwrap import dedent
from src.model import model
from src.tools.utilities import file_tools

grant_writing_agent = Agent(
    description="Grant Writing Agent for Medical Device Development",
    model=model,
    tools=[file_tools],
    instructions=dedent("""
        Please write a grant application for the medical device. The grant application should address the following:
        - User needs
        - Product requirements
        - Risk analysis
        - Commercialization plan
        """)
)