"""
Kestrel Pit asset re-skin: deal AI4I 2020 rows to a synthetic mining asset register.

RULE: a row's quality tier (L/M/H) constrains which assets it can be dealt to.
      An H row can only land on an H-tier asset, never L or M. Same for L and M.

Reproducible: fixed random seed. Re-running this script reproduces the exact
same deal, which is what makes the re-skin auditable rather than hand-waved.
"""
import pandas as pd
import numpy as np

SEED = 20260821
rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------
# 1. The synthetic asset register: 48 machines
#    Tier = criticality (consequence of failure), not machine size.
#    Fixed plant sits at H because it is a single point of failure:
#    one crusher down stops the whole site; one haul truck down is
#    absorbed by the rest of the fleet.
# ---------------------------------------------------------------
ASSETS = [
    # --- HIGH criticality (5): fixed plant, single points of failure
    ("PC-01",  "Primary Jaw Crusher",        "Metso Nordberg C160",      "Fixed plant - crushing",  "H", "Primary Crushing Circuit"),
    ("SC-01",  "Secondary Cone Crusher",     "Sandvik CH870i",           "Fixed plant - crushing",  "H", "Primary Crushing Circuit"),
    ("ML-01",  "Ball Mill",                  "Outotec 7.3m",             "Fixed plant - grinding",  "H", "Grinding / CIL Circuit"),
    ("CV-01",  "Overland Conveyor (1.4 km)", "Continental steel-cord",   "Fixed plant - conveying", "H", "Conveyor Corridor"),
    ("TH-01",  "CIL Thickener Drive",        "Outotec high-rate",        "Fixed plant - processing","H", "Grinding / CIL Circuit"),

    # --- MEDIUM criticality (14): core production fleet
    ("EX-01",  "Hydraulic Excavator",        "Komatsu PC2000-11",        "Mobile - loading",        "M", "Open Pit - Stage 3"),
    ("EX-02",  "Hydraulic Excavator",        "Hitachi EX1900-6",         "Mobile - loading",        "M", "Open Pit - Stage 3"),
    ("EX-03",  "Hydraulic Excavator",        "Liebherr R 9200",          "Mobile - loading",        "M", "Open Pit - Stage 2"),
    ("HT-01",  "Rigid Dump Truck",           "Caterpillar 793F",         "Mobile - hauling",        "M", "Open Pit - Stage 3"),
    ("HT-02",  "Rigid Dump Truck",           "Caterpillar 793F",         "Mobile - hauling",        "M", "Open Pit - Stage 3"),
    ("HT-03",  "Rigid Dump Truck",           "Caterpillar 793F",         "Mobile - hauling",        "M", "Open Pit - Stage 3"),
    ("HT-04",  "Rigid Dump Truck",           "Caterpillar 793F",         "Mobile - hauling",        "M", "Open Pit - Stage 2"),
    ("HT-05",  "Rigid Dump Truck",           "Komatsu HD785-8",          "Mobile - hauling",        "M", "Open Pit - Stage 2"),
    ("HT-06",  "Rigid Dump Truck",           "Komatsu HD785-8",          "Mobile - hauling",        "M", "ROM Pad"),
    ("LD-01",  "Wheel Loader",               "Caterpillar 992K",         "Mobile - loading",        "M", "ROM Pad"),
    ("LD-02",  "Wheel Loader",               "Komatsu WA600-8",          "Mobile - loading",        "M", "ROM Pad"),
    ("DR-01",  "Rotary Blasthole Drill",     "Epiroc Pit Viper 271",     "Mobile - drilling",       "M", "Open Pit - Stage 3"),
    ("DR-02",  "Rotary Blasthole Drill",     "Sandvik DR410i",           "Mobile - drilling",       "M", "Open Pit - Stage 2"),
    ("DR-03",  "Down-the-Hole Drill",        "Epiroc SmartROC D65",      "Mobile - drilling",       "M", "Open Pit - Stage 2"),

    # --- LOW criticality (29): support, auxiliary, redundant
    ("GR-01",  "Motor Grader",               "Caterpillar 16M3",         "Mobile - road maint.",    "L", "Haul Road Network"),
    ("GR-02",  "Motor Grader",               "Caterpillar 16M3",         "Mobile - road maint.",    "L", "Haul Road Network"),
    ("DZ-01",  "Track Dozer",                "Caterpillar D10T2",        "Mobile - earthmoving",    "L", "Open Pit - Stage 3"),
    ("DZ-02",  "Wheel Dozer",                "Komatsu WD600-6",          "Mobile - earthmoving",    "L", "ROM Pad"),
    ("WC-01",  "Water Cart",                 "Caterpillar 777 (74 kL)",  "Mobile - dust supp.",     "L", "Haul Road Network"),
    ("WC-02",  "Water Cart",                 "Caterpillar 777 (74 kL)",  "Mobile - dust supp.",     "L", "Haul Road Network"),
    ("WC-03",  "Water Cart",                 "Caterpillar 773 (55 kL)",  "Mobile - dust supp.",     "L", "Open Pit - Stage 3"),
    ("WC-04",  "Water Cart",                 "Caterpillar 773 (55 kL)",  "Mobile - dust supp.",     "L", "Open Pit - Stage 2"),
    ("PMP-01", "Pit Dewatering Pump",        "Grundfos S-series",        "Fixed - water mgmt",      "L", "Open Pit - Stage 3"),
    ("PMP-02", "Pit Dewatering Pump",        "Grundfos S-series",        "Fixed - water mgmt",      "L", "Open Pit - Stage 2"),
    ("PMP-03", "Tailings Transfer Pump",     "Warman AH-series",         "Fixed - water mgmt",      "L", "Tailings Storage Facility"),
    ("PMP-04", "Process Water Pump",         "Warman AH-series",         "Fixed - water mgmt",      "L", "Grinding / CIL Circuit"),
    ("GEN-01", "Standby Generator",          "Cummins C1100 D5",         "Fixed - power",           "L", "Primary Crushing Circuit"),
    ("GEN-02", "Standby Generator",          "Cummins C1100 D5",         "Fixed - power",           "L", "Grinding / CIL Circuit"),
    ("GEN-03", "Standby Generator",          "Cummins C700 D5",          "Fixed - power",           "L", "Maintenance Workshop"),
    ("GEN-04", "Standby Generator",          "Cummins C700 D5",          "Fixed - power",           "L", "Tailings Storage Facility"),
    ("CMP-01", "Workshop Air Compressor",    "Atlas Copco GA75",         "Fixed - support",         "L", "Maintenance Workshop"),
    ("CMP-02", "Workshop Air Compressor",    "Atlas Copco GA75",         "Fixed - support",         "L", "Maintenance Workshop"),
    ("CMP-03", "Plant Air Compressor",       "Atlas Copco GA160",        "Fixed - support",         "L", "Grinding / CIL Circuit"),
    ("FD-01",  "Apron Feeder",               "Metso apron feeder",       "Fixed plant - feed",      "L", "Primary Crushing Circuit"),
    ("FD-02",  "Belt Feeder",                "Metso belt feeder",        "Fixed plant - feed",      "L", "ROM Pad"),
    ("SV-01",  "Service / Lube Truck",       "Isuzu FVZ service body",   "Mobile - field maint.",   "L", "Haul Road Network"),
    ("SV-02",  "Service / Lube Truck",       "Isuzu FVZ service body",   "Mobile - field maint.",   "L", "Maintenance Workshop"),
    ("LV-01",  "Light Vehicle",              "Toyota LandCruiser 79",    "Mobile - light vehicle",  "L", "Open Pit - Stage 3"),
    ("LV-02",  "Light Vehicle",              "Toyota LandCruiser 79",    "Mobile - light vehicle",  "L", "Open Pit - Stage 2"),
    ("LV-03",  "Light Vehicle",              "Toyota LandCruiser 79",    "Mobile - light vehicle",  "L", "ROM Pad"),
    ("LV-04",  "Light Vehicle",              "Toyota LandCruiser 79",    "Mobile - light vehicle",  "L", "Maintenance Workshop"),
    ("LV-05",  "Light Vehicle",              "Toyota HiLux",             "Mobile - light vehicle",  "L", "Haul Road Network"),
    ("LV-06",  "Light Vehicle",              "Toyota HiLux",             "Mobile - light vehicle",  "L", "Tailings Storage Facility"),
]

cols = ["Asset ID", "Asset Name", "Make / Model", "Equipment Class", "Criticality Tier", "Location"]
register = pd.DataFrame(ASSETS, columns=cols)
register.to_csv("/home/claude/reskin/asset-register.csv", index=False)

# ---------------------------------------------------------------
# 2. Deal the rows, tier-constrained
# ---------------------------------------------------------------
df = pd.read_csv("/mnt/user-data/uploads/MyProject/ai4i2020.csv")

assigned = pd.Series(index=df.index, dtype=object)

for tier in ["L", "M", "H"]:
    tier_rows   = df.index[df["Type"] == tier].to_numpy()
    tier_assets = register.loc[register["Criticality Tier"] == tier, "Asset ID"].to_numpy()

    # Deal like cards: build a deck where each asset appears an equal number of
    # times (remainder spread over the first few), shuffle it, then hand rows out.
    n_rows, n_assets = len(tier_rows), len(tier_assets)
    base, extra = divmod(n_rows, n_assets)
    deck = np.repeat(tier_assets, base)
    if extra:
        deck = np.concatenate([deck, rng.choice(tier_assets, size=extra, replace=False)])
    rng.shuffle(deck)
    assigned.loc[tier_rows] = deck

df["Asset ID"] = assigned.values
out = df.merge(register, on="Asset ID", how="left", suffixes=("", "_reg"))

# Reorder so asset identity sits up front, before the sensor readings
front = ["UDI", "Asset ID", "Asset Name", "Make / Model", "Equipment Class",
         "Criticality Tier", "Location"]
out = out[front + [c for c in out.columns if c not in front]]
out.to_csv("/home/claude/reskin/ai4i2020-kestrel.csv", index=False)

# ---------------------------------------------------------------
# 3. Verify the rule actually held
# ---------------------------------------------------------------
violations = (out["Type"] != out["Criticality Tier"]).sum()
print("TIER RULE VIOLATIONS (must be 0):", violations)
print("Rows dealt:", len(out), "| Assets:", len(register), "| Unassigned:", out["Asset ID"].isna().sum())
print()
print("Register tier split:")
print(register["Criticality Tier"].value_counts().reindex(["H","M","L"]).to_string())
print()
print("Rows + failures per tier:")
print(out.groupby("Criticality Tier").agg(
    rows=("UDI","size"), assets=("Asset ID","nunique"),
    failures=("Machine failure","sum")).reindex(["H","M","L"]).to_string())
print()
print("Readings per asset (spread check):")
c = out["Asset ID"].value_counts()
print(f"  min {c.min()} | max {c.max()} | mean {c.mean():.1f}")
print()
print("Top 12 assets by failure count:")
top = out.groupby(["Asset ID","Asset Name","Criticality Tier"])["Machine failure"].agg(["sum","size"])
top.columns = ["failures","readings"]
top["rate %"] = (top["failures"]/top["readings"]*100).round(2)
print(top.sort_values("failures", ascending=False).head(12).to_string())
