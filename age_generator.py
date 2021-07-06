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

# ==== HUMAN ==== #
human_min_age = 9
human_max_age = 90
human_child_age = (9, 17)
human_young_age = (18, 26)
human_adult_age = (27, 59)
human_senior_age = (60, 90)

# ==== DWARF ==== #
dwarf_min_age = 25
dwarf_max_age = 400
dwarf_child_age = (25, 49)
dwarf_young_age = (50, 74)
dwarf_adult_age = (75, 269)
dwarf_senior_age = (270, 400)

# ==== ELF ==== #
elf_min_age = 50
elf_max_age = 750
elf_child_age = (50, 99)
elf_young_age = (100, 149)
elf_adult_age = (150, 499)
elf_senior_age = (500, 750)

# ==== HALFLING ==== #
halfling_min_age = 10
halfling_max_age = 250
halfling_child_age = (10, 19)
halfling_young_age = (20, 29)
halfling_adult_age = (30, 169)
halfling_senior_age = (170, 250)

# ==== DRAGONBORN ==== #
dragonborn_min_age = 8
dragonborn_max_age = 80
dragonborn_child_age = (8, 14)
dragonborn_young_age = (15, 22)
dragonborn_adult_age = (23, 54)
dragonborn_senior_age = (55, 80)

# ==== GNOME ==== #
gnome_min_age = 20
gnome_max_age = 500
gnome_child_age = (20, 39)
gnome_young_age = (40, 59)
gnome_adult_age = (60, 334)
gnome_senior_age = (335, 500)

# ==== HALF-ELF ==== #
halfelf_min_age = 10
halfelf_max_age = 200
halfelf_child_age = (10, 19)
halfelf_young_age = (20, 29)
halfelf_adult_age = (30, 134)
halfelf_senior_age = (135, 200)

# ==== HALF-ORC ==== #
halforc_min_age = 7
halforc_max_age = 75
halforc_child_age = (7, 13)
halforc_young_age = (14, 20)
halforc_adult_age = (21, 49)
halforc_senior_age = (50, 75)

# ==== TIEFLING ==== #
tiefling_min_age = 9
tiefling_max_age = 95
tiefling_child_age = (9, 17)
tiefling_young_age = (18, 27)
tiefling_adult_age = (28, 64)
tiefling_senior_age = (64, 95)
