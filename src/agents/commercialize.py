from agno.agent import Agent
from textwrap import dedent
from src.model import model
from src.tools.utilities import file_tools

commercialize_agent = Agent(
    description="Commercialization Plan for Medical Device Development",
    model=model,
    tools=[file_tools],
    instructions=dedent("""
        Please develop a commercialization plan for the medical device. This plan should address the following:
        - Market entry and development strategies
        - Commercialization strategies and opportunities
        - Pricing and financial models
        - Legal and regulatory requirements
        - Customer acquisition and retention strategies
        - Product launch and marketing strategies
        - Business model and financial models
        """)  
)