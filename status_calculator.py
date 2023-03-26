def calculate_stats(base_stats, ivs, evs, level, nature_modifiers):
    stats = {}
    for stat_name, base_stat in base_stats.items():
        if stat_name == "HP":
            if base_stat == 1:  # Shedinja's case
                stats[stat_name] = 1
            else:
                stats[stat_name] = int(((2 * base_stat + ivs[stat_name] + (evs[stat_name] // 4)) * level) // 100) + level + 10
        else:
            raw_stat = int((((2 * base_stat + ivs[stat_name] + (evs[stat_name] // 4)) * level) // 100) + 5)
            stats[stat_name] = int(raw_stat * nature_modifiers[stat_name])
    return stats

def get_evs_from_user():
    evs = {}
    stat_names = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

    print("Enter the Effort Values (EVs) for each stat:")
    for stat_name in stat_names:
        while True:
            try:
                ev = int(input(f"{stat_name}: "))
                if 0 <= ev <= 252:
                    evs[stat_name] = ev
                    break
                else:
                    print(f"Invalid input. {stat_name} EVs should be between 0 and 252.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return evs

def get_nature_modifiers_from_user():
    nature_modifiers = {}
    stat_names = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

    print("Enter the Nature Modifiers for each stat:")
    for stat_name in stat_names:
        while True:
            try:
                modifier = float(input(f"{stat_name}: "))
                if 0.1 <= modifier <= 2.0:
                    nature_modifiers[stat_name] = modifier
                    break
                else:
                    print(f"Invalid input. {stat_name} Nature Modifier should be between 0.1 and 2.0.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return nature_modifiers

base_stats = {
    "HP": 45,
    "Attack": 49,
    "Defense": 49,
    "Sp. Atk": 65,
    "Sp. Def": 65,
    "Speed": 45
}

ivs = {
    "HP": 31,
    "Attack": 31,
    "Defense": 31,
    "Sp. Atk": 31,
    "Sp. Def": 31,
    "Speed": 31
}

evs = {
    "HP": 0,
    "Attack": 0,
    "Defense": 0,
    "Sp. Atk": 0,
    "Sp. Def": 0,
    "Speed": 0
}

level = 50

# Nature modifiers should be given in decimal format
# Example: 1.1 for a 10% increase, 0.9 for a 10% decrease, 1 for no change
nature_modifiers = {
    "HP": 1,
    "Attack": 0.9,
    "Defense": 1,
    "Sp. Atk": 1.1,
    "Sp. Def": 1,
    "Speed": 1
}

stats = calculate_stats(base_stats, ivs, evs, level, nature_modifiers)
print(stats)
