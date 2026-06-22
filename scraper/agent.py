import argparse
import json
import os
import sys

# Ensure project root is on sys.path so package imports work when running
# this file directly (e.g. `python scraper/agent.py`).
PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

try:
    from scraper.parser import get_operator_versions, get_component_versions
except Exception:
    # Fallback for environments where package import isn't available.
    from parser import get_operator_versions, get_component_versions


def scrape(version):
    data = {
        "ocp_version": version,
        "operators": get_operator_versions(version),
        "components": get_component_versions(version),
    }

    out_dir = os.path.join(PACKAGE_ROOT, "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"ocp-{version}.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[✓] Saved {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="4.21")
    args = parser.parse_args()

    scrape(args.version)
