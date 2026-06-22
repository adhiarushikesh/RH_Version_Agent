from urllib.request import urlopen
from bs4 import BeautifulSoup  # type: ignore
import re

BASE_OPS = "https://docs.redhat.com/en/documentation/openshift_container_platform/{}/html/operators/cluster-operators-reference"

def get_operator_versions(version):
    url = BASE_OPS.format(version)
    soup = BeautifulSoup(urlopen(url).read(), "html.parser")

    operators = {}
    for link in soup.select("a[href*='project']"):
        name = link.text.strip()
        op_url = "https://docs.redhat.com" + link["href"]

        op_page = BeautifulSoup(urlopen(op_url).read(), "html.parser")
        version_tag = op_page.find(text=re.compile("Version", re.I))

        operators[name] = version_tag.find_next().text.strip() if version_tag else "unknown"

    return operators


def get_component_versions(version):
    return {
        "kubernetes": "1.34",
        "cri-o": "1.34 aligned",
        "etcd": "3.5.x",
        "rhel_coreos": f"{version} stream",
        "ovn_kubernetes": "v23.x",
        "prometheus": "v2.52+",
        "alertmanager": "v0.27+"
    }
