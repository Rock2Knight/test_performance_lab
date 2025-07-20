import json
import sys
from pathlib import Path

values_json = sys.argv[1]
test_json = sys.argv[2]
report_json = sys.argv[3]

values_json = Path(values_json).resolve()
test_json = Path(test_json).resolve()
report_json = Path(report_json).resolve()

values_dict = None
test_dict = None

with open(values_json, "r", encoding='utf-8') as f:
    values_dict = json.load(f)
    values_dict = values_dict["values"]
    values_dict = {item["id"]: item["value"] for item in values_dict}


def format_report(test):
    report = test.copy()
    if "value" in report:
        report["value"] = values_dict.get(report["id"])
    if "values" in report:
        report["values"] = [format_report(item) for item in report["values"]]
    return report


with open(test_json, "r", encoding='utf-8') as f:
    test_dict = json.load(f)
    test_dict = test_dict["tests"]

reports = {"tests": [format_report(test) for test in test_dict]}

with open(report_json, "w", encoding='utf-8') as f:
    json.dump(reports, f, indent=4)