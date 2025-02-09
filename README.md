# BioMed Grant Writing Agent Team

## Workflow
```mermaid
flowchart LR
    A["User Needs Agent"] --> B["Product Requirement Agent"]
    B --> C["Risk Analysis Agent\n(Identify Risks)"]
    C --> D["Identify key\nrequirements and Risks that\ngrant will address"]
    D --> E["Commercialization Plan Agent"]
    E --> F["Grant Writing Agent"]
    F --> G["Prototype\n(Will require for preliminary\nresults to include in grant)"]
    
    subgraph Submission["Submission Rules and prompts"]
        H1["ARPA-H"]
        H2["MTEC"]
        H3["NIH"]
        H4["NSF"]
    end
    
    Submission --> F
```

## Setup

1. Install uv (if not already installed)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository
```bash
git clone https://github.com/designplex/grant-writing-team.git
cd grant-writing-team
```

3. Setup Python environment
```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Usage

Run the grant writing team with a prompt:
```bash
python swarm.py "Describe the user needs for a novel blood glucose monitoring device"
```