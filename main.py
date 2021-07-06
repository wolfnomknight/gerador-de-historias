# Este é um projeto para um programa que gera uma história prévia para um personagem de D&D

import random

# ==== User Input ==== #
# Aqui entram os parametros que o usuario escolhe e o programa usa para gerar a história

allow_children = False  # Especifica se a personagem pode ser criança, desligado por padrão
allow_elderly = False  # Especifica se a personagem pode ser idosa, desligado por padrão

list_of_sexes = ["female", "male", "fluid", "not specified", "other"]  # Lista de opções para o próximo parâmetro
biological_sex = "not specified"  # Especifica o sexo da personagem, ignorado por padrão
# "fluid" seria no caso de espécies que podem alterar o sistema reprodutor de forma natural
# "not specified" significa que as partes da historia que tratam de sexo serão ignoradas, não serão geradas
# "other" deve habilitar um campo para o usuário escrever algo
# Creio que é melhor não entrar na questão de gênero


def random_sex():  # Para seleção aleatória de sexo
    global biological_sex
    biological_sex = random.choice(list_of_sexes)


# Lista de raças para o usuário escolher, ou "other" para habilitar um campo de entrada manual
list_of_races = ["human", "dwarf", "elf", "halfling", "dragonborn", "gnome", "half-elf", "half-orc", "tiefling", "other"]
race = "human"  # Especifica a raça da personagem, humana por padrão


def random_race():  # Para seleção aleatória de raça
    global race
    race = random.choice(list_of_races)


# Lista de classes para o usuário escolher, ou "other" para habilitar um campo de entrada manual
list_of_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue",
                   "sorcerer", "warlock", "wizard", "other"]
character_class = "fighter"  #Especifica a classe da personagem, "fighter" por padrão


def random_class():  # Para seleção aleatória de classe
    global character_class
    character_class = random.choice(list_of_classes)


# ==== Name Generator ==== #
# O gerador de nome terá uma lista de "meio nomes" para formar nomes inteiros aleatoriamente
# Cada sexo de cada raça terá uma lista diferente (estas informações estão presentes no Players Handbook)
# Também deve haver um campo para entrada manual do nome, ou este ser o padrão e um botão para preencher aleatoriamente

# ==== Age Generator ==== #
# O gerador de idade terá uma lista de idades para cada raça,
# bem como a range das épocas da vida (criança, jovem, adulto, idoso)
# Deve permitir que o usuario entre uma idade manualmente (obrigatorio se escolher "other" na raça)
# ou gere aleatoriamente uma idade:
# 'Full random', totalmente aleatório
# 'Semi random', o usuário escolhe uma época de vida, o programa dá uma idade aleatória dentro dessa range
