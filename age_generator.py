# ==== AGE ==== #
# O gerador de idade terá uma lista de idades para cada raça,
# bem como a range das épocas da vida (criança, jovem, adulto, idoso)
# Deve permitir que o usuario entre uma idade manualmente (obrigatorio se escolher "other" na raça)
# ou gere aleatoriamente uma idade:
# 'Full random', totalmente aleatório
# 'Semi random', o usuário escolhe uma época de vida, o programa dá uma idade aleatória dentro dessa range

# ==== Como as idades de cada raça foram calculadas ==== #
# O Player's Handbook tem informações sobre a idade máxima de cada raça
# e quando atinge a maturidade (jovem)
# Tomando humanos como base, temos uma idade máxima de 90 e jovem a 18. Então:
# Idade mínima, considerado criança: 10 a 17
# Jovem adulto: 18 a 21
# Adulto: 22 a 59
# Senior: 60 a 90
# Com isso eu deduzi as seguinte fórmulas e apliquei para cada raça, sabendo a idade máxima:
# (idades mínimas, sempre arredondando para cima)
# Criança: jovem / 2
# Jovem adulto: (dado pelo livro)
# Adulto: jovem + criança
# Senior: idade máxima * (2/3)

import random

# ==== HUMAN ==== #
human = {"min_age": 9,
         "max_age": 90,
         "child_age": [9, 17],
         "young_age": [18, 26],
         "adult_age": [27, 59],
         "senior_age": [60, 90]
        }

# ==== DWARF ==== #
dwarf = {"min_age": 25,
         "max_age": 400,
         "child_age": [25, 49],
         "young_age": [50, 74],
         "adult_age": [75, 269],
         "senior_age": [270, 400]
        }

# ==== ELF ==== #
elf = {"min_age": 50,
         "max_age": 750,
         "child_age": [50, 99],
         "young_age": [100, 149],
         "adult_age": [150, 499],
         "senior_age": [500, 750]
        }

# ==== HALFLING ==== #
halfling = {"min_age": 10,
         "max_age": 250,
         "child_age": [10, 19],
         "young_age": [20, 29],
         "adult_age": [30, 169],
         "senior_age": [170, 250]
        }

# ==== DRAGONBORN ==== #
dragonborn = {"min_age": 8,
         "max_age": 80,
         "child_age": [8, 14],
         "young_age": [15, 22],
         "adult_age": [23, 54],
         "senior_age": [55, 80]
        }

# ==== GNOME ==== #
gnome = {"min_age": 20,
         "max_age": 500,
         "child_age": [20, 39],
         "young_age": [40, 59],
         "adult_age": [60, 334],
         "senior_age": [335, 500]
        }

# ==== HALF-ELF ==== #
halfelf = {"min_age": 10,
         "max_age": 200,
         "child_age": [10, 19],
         "young_age": [20, 29],
         "adult_age": [30, 134],
         "senior_age": [135, 200]
        }

# ==== HALF-ORC ==== #
halforc = {"min_age": 7,
         "max_age": 75,
         "child_age": [7, 13],
         "young_age": [14, 20],
         "adult_age": [21, 49],
         "senior_age": [50, 75]
        }

# ==== TIEFLING ==== #
tiefling = {"min_age": 9,
         "max_age": 95,
         "child_age": [9, 17],
         "young_age": [18, 27],
         "adult_age": [28, 64],
         "senior_age": [65, 95]
        }


def age_select(race, age):
    selected_age = []
    if "child" in age:
        selected_age.append(random.randint(eval(race)["child_age"][0], eval(race)["child_age"][1]))
    if "young" in age:
        selected_age.append(random.randint(eval(race)["young_age"][0], eval(race)["young_age"][1]))
    if "adult" in age:
        selected_age.append(random.randint(eval(race)["adult_age"][0], eval(race)["adult_age"][1]))
    if "senior" in age:
        selected_age.append(random.randint(eval(race)["senior_age"][0], eval(race)["senior_age"][1]))
    if not age:
        selected_age = random.randint(eval(race)["min_age"], eval(race)["max_age"])
        return selected_age
    result_age = random.choice(selected_age)
    return result_age
