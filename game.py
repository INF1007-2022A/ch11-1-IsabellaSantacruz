"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils



class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20
	def __init__(self,name:str, power:int, min_level:int) -> None:
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return Weapon("Unarmed", 20,1)
	


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name:str, max_hp:int, attack:int, defense:int, level:int, weapon:Weapon) -> None:
		self.name    = name
		self.max_hp  = max_hp
		self.attack  = attack
		self.defense = defense
		self.level   = level
		self.weapon  = weapon
		self.hp      = self.max_hp
	
	def compute_damage(self, other):
		numerateur = (2*self.level/5 + 2)*self.weapon.power*self.attack/other.defense
		crit = 1
		if random.randint(1,16) == 1:
			crit = 2
		modifier = crit*random.randrange(85,101)/100
		dmg = (numerateur/50 + 2)*modifier
		return dmg

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	dmg = attacker.compute_damage(defender)
	defender.hp = defender.hp-dmg
	sortie = f"{attacker.name} used {attacker.weapon.name}"
	sortie += f"\n  {defender.name} took {dmg} dmg"
	return sortie


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	txt = f"{c1.name} starts a battle with {c2.name}!\n"
	turns = -1
	while c1.hp > 0 and c2.hp > 0:
		turns+=1
		txt += deal_damage(c1,c2) + "\n"
		if c2.hp <= 0:
			break
		txt += deal_damage(c2,c1) + "\n"
	if c1.hp <= 0:
		txt += f"{c1.name} is sleeping with the fishes.\n"
	if c2.hp <= 0:
		txt += f"{c2.name} is sleeping with the fishes.\n"
	txt += f"The battle ended in {turns} turns."
