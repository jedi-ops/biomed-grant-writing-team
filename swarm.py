import argparse

from agno.agent import Agent, RunResponse 
from textwrap import dedent
from src.model import model
from src.agents.product_requirements import product_requirement_agent
from src.agents.user_needs import user_needs_agent
from src.agents.risk_analysis import risk_analysis_agent
from src.agents.commercialize import commercialize_agent
from src.agents.grant_writing import grant_writing_agent
from src.tools.utilities import file_tools


def create_grant_writing_team():
    return Agent(
        description="Grant Writing Team",
        model=model,
        team=[
            user_needs_agent,
            product_requirement_agent,
            risk_analysis_agent,
            commercialize_agent,
            grant_writing_agent
        ],
        tools=[file_tools],
        instructions=dedent("""
            1. User Needs Agent analyzes and documents user requirements and needs
            2. Product Requirement Agent converts user needs into specific product requirements
            3. Risk Analysis Agent identifies potential risks associated with the project
            4. Key requirements and risks are identified that the grant will address
            5. Commercialization Plan Agent develops the commercialization strategy
            6. Grant Writing Agent composes the grant application, incorporating:
            - User needs
            - Product requirements
            - Risk analysis
            - Commercialization plan
            - Input from submission rules (ARPA-H, MTEC, NIH, NSF)
            7. Prototype development (Required for preliminary results in grant)

            Note: The Grant Writing Agent will specifically consider submission rules and prompts from:
            - ARPA-H
            - MTEC
            - NIH
            - NSF
            """) 
    )

def main():
    parser = argparse.ArgumentParser(description='BioMed Grant Writing Team')
    parser.add_argument('prompt', type=str, help='The prompt to send to the grant writing team')
    args = parser.parse_args()
    
    team = create_grant_writing_team()
    response = team.run(args.prompt)
    print_response(response)

def print_response(response):
    print("\nGrant Writing Team Response:")
    print("-" * 40)
    print(response)
    print("-" * 40)

if __name__ == "__main__":
    main()
