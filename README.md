# RH Version Agent

This repository contains an autonomous agent that:
- Scrapes all Cluster Operator versions for any OpenShift release
- Scrapes core component versions (Kubernetes, CRI-O, etc.)
- Outputs JSON files under /output
- Runs automatically every night using GitHub Actions

## Run locally
pip install -r scraper/requirements.txt
python scraper/agent.py --version 4.21

## Output
output/ocp-<version>.json

## Automation
GitHub Actions workflow runs daily at 2 AM IST.



RH_Version_Agent/
│
├── scraper/
│   ├── agent.py
│   ├── parser.py
│   ├── utils.py
│   ├── __init__.py
│   └── requirements.txt
│
├── output/
│   └── .gitkeep
│
├── README.md
│
└── .github/
    └── workflows/
        └── ocp-agent.yml
