# -*- coding: utf-8 -*-
import numpy as np

initial_boss = {'HP': 58,
        'Damage': 9} 

initial_player = {'HP': 50,
          'Mana': 500,
          'Armor': 0}

#The number of turns left with the effect active
#effects = np.array([0,0,0])

spells = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']

def applyEffects(effects, player, boss_hp):
    new_player = player.copy()
    #Shield
    if effects[0] > 0:
        new_player['Armor'] = 7
    else:
        new_player['Armor'] = 0
    #Poison
    if effects[1] > 0:
        boss_hp -= 3
    #Recharge
    if effects[2] > 0:
        new_player['Mana'] = player.get('Mana') + 101
    new_effects = [max(0, effect-1) for effect in effects]
    return new_effects, new_player, boss_hp
        
def playerAttack(effects, spell, player, boss_hp):
    mana = player.get('Mana')
    new_player = player.copy()
    new_effects = effects.copy()
    match spell:
        case 'Magic Missile':
            if mana < 53:
                return [], {}, 0, -1
            new_player['Mana'] = mana - 53
            boss_hp -= 4
            mana_spent = 53
        case 'Drain':
            if mana < 73:
                return [], {}, 0, -1
            new_player['Mana'] = mana - 73
            new_player['HP'] = player.get('HP') + 2
            boss_hp -= 2
            mana_spent = 73 
        case 'Shield':
            if mana < 113 or effects[0] > 0:
                return [], {}, 0, -1
            new_player['Mana'] = mana - 113
            new_effects[0] = 6
            mana_spent = 113
        case 'Poison':
            if mana < 173 or effects[1] > 0:
                return [], {}, 0, -1
            new_player['Mana'] = mana - 173
            new_effects[1] = 6
            mana_spent = 173
        case 'Recharge':
            if mana < 229 or effects[2] > 0:
                return [], {}, 0, -1
            new_player['Mana'] = mana - 229
            new_effects[2] = 5
            mana_spent = 229
    return new_effects, new_player, boss_hp, mana_spent
    
def bossAttack(player):
    new_player = player.copy()
    new_player['HP'] = player.get('HP') - max(1, 9 - player.get('Armor'))
    return new_player


def minMana(player, boss_hp, effects, mana_spent, spells_hist):
    #print('Hasta ahora tiré ', spells_hist, ' gastando ', mana_spent)
    #print('y el boss quedó: ', boss)
    new_effects, new_player, new_boss_hp = applyEffects(effects, player, boss_hp)
    if new_boss_hp <= 0:
        #print(spells_hist, mana_spent)
        return mana_spent
    min_mana = np.inf
    for spell in spells:
        new_spells_hist = spells_hist.copy()
        new_effects_spell, new_player_spell, new_boss_hp_spell, mana_cost = playerAttack(new_effects, spell, new_player, new_boss_hp)
        if mana_cost == -1:
            #Cant cast this spell
            continue
        new_spells_hist.append(spell)
        new_effects_spell, new_player_spell, new_boss_hp_spell = applyEffects(new_effects_spell, new_player_spell, new_boss_hp_spell)
        if new_boss_hp_spell <= 0:
            min_mana = min(min_mana, mana_spent + mana_cost)
            #print(new_spells_hist, mana_spent + mana_cost)
            #Battle is over
            continue
        new_player_spell = bossAttack(new_player_spell)
        if new_player_spell.get('HP') <= 0:
            #Battle is over
            continue
        min_mana = min(min_mana, minMana(new_player_spell, new_boss_hp_spell, new_effects_spell, mana_spent + mana_cost, new_spells_hist))
    return min_mana
        
         
#mas de 1249
print(minMana(initial_player,58,np.array([0,0,0]),0, []))
        