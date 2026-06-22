import argparse
import json
from parser import get_operator_versions, get_component_versions

def scrape(version):
    data = {
        "ocp_version": version,
        "operators": get_operator_versions(version),
        "components": get_component_versions(version)
    }

    with open(f"output/ocp-{version}.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"[✓] Saved output/ocp-{version}.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="4.21")
    args = parser.parse_args()

    scrape(args.version)
