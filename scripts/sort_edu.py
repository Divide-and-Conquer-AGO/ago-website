import json
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# List of siege weapon unit names (add more as needed)
siege_units = {
    "Ballista", "Catapult", "Trebuchet", "Mangonel", "Boat", "Ship",
    "Westron Ballista", "Dwarven Ballista", "Elven Ballista", "Snaga Ballista",
    "Snaga Catapult", "Westron Catapult", "Dwarven Catapult", "Elven Catapult",
    "Mordor Catapult", "Misty Mangonel", "Gondor Trebuchet", "Human Boat",
    "Gondor Boat", "Gondor Ship", "Elven Boat", "Elven Ship", "Enedwaith Boat",
    "Adunaim Boat", "Adunaim Ship"
}

def is_siege(unit_name):
    for siege in siege_units:
        if siege.lower() in unit_name.lower():
            return True
    return False

def get_faction(unit):
    era = unit.get("EraZero", [])
    return era[0] if era else "zzz"

def is_general(unit):
    attrs = unit.get("Attributes", [])
    return "general_unit" in attrs or "s_bodyguard" in attrs

def get_cost(unit):
    return unit.get("RecruitCost", float("inf"))

edu_path = os.path.join(os.path.dirname(__file__), "../data/edu.json")
if not os.path.exists(edu_path):
    raise FileNotFoundError(f"Could not find 'edu.json' at {edu_path}")

with open(edu_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Group units by faction, then by type
grouped = {}

for name, unit in data.items():
    era_zero = unit.get("EraZero", [])
    # Accept units with a non-empty EraZero or with a valid Category (for siege units)
    if not (isinstance(era_zero, list) and len(era_zero) > 0):
        # If it's a siege unit, try to assign to a generic "siege" faction
        if is_siege(name) or unit.get("Category") == "siege":
            faction = "siege"
            if faction not in grouped:
                grouped[faction] = {"generals": {}, "regular": {}, "siege": {}}
            grouped[faction]["siege"][name] = unit
        continue
    faction = era_zero[0]
    if faction not in grouped:
        grouped[faction] = {"generals": {}, "regular": {}, "siege": {}}
    if is_siege(name) or unit.get("Category") == "siege":
        grouped[faction]["siege"][name] = unit
    elif is_general(unit):
        grouped[faction]["generals"][name] = unit
    else:
        grouped[faction]["regular"][name] = unit

# Sort each group by RecruitCost ascending
def sort_group(group):
    return dict(sorted(group.items(), key=lambda x: get_cost(x[1])))

for faction in grouped:
    grouped[faction]["generals"] = sort_group(grouped[faction]["generals"])
    grouped[faction]["regular"] = sort_group(grouped[faction]["regular"])
    grouped[faction]["siege"] = sort_group(grouped[faction]["siege"])

with open(edu_path, "w", encoding="utf-8") as f:
    json.dump(grouped, f, indent=2, ensure_ascii=False)
