import pandas as pd
import my_names as mn
import NextTech_db as db

"""ρ=m/V
m=V·ρ
V=m/ρ"""


def get_print_cost_from_mass(machine, material, unit, amount):
    df = db.sql_select_material_from_query(f"SELECT cost, unit, density, process, printType FROM materialSpecifications WHERE machine = '{machine}' AND materialId = '{material}'")

    if df["unit"][0] == f"$/kg":
        cost = df["cost"][0] * float(amount)
        return cost
    elif df["unit"][0] == f"$/L":
        cost = (df["cost"][0] * (float(amount)) / df["density"][0])
        return cost

def get_print_cost_from_volume(machine, material, unit, amount):
    df = db.sql_select_material_from_query(f"SELECT cost, unit, density, process, printType FROM materialSpecifications WHERE machine = '{machine}' AND materialId = '{material}'")

    if df["unit"][0] == f"$/kg":
        cost = df["cost"][0] * float(amount) * df["density"][0]
        return cost
    elif df["unit"][0] == f"$/L":
        cost = df["cost"][0] * float(amount)
        return cost