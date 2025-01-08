# -*- coding: utf-8 -*-


boss = {'HP': 104,
        'Damage': 8,
        'Armor': 1} 

player = {'HP': 100,
          'Damage': 0,
          'Armor': 0}

def damageDealt(attaker, defender):
    return max(1, attaker.get('Damage') - defender.get('Armor'))

weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
#The last armor models not building any armor
armor = [(13, 1), (31, 2), (53, 3), (75, 4), (102, 5), (0, 0)]
#The last ring models not building any ring
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0)]

def win(player, boss):
    boss_hp = boss.get('HP')
    player_hp = player.get('HP')
    while True:
        #Player attaks
        boss_hp -= damageDealt(player, boss)
        if boss_hp <= 0:
            return True
        #Boss attaks
        player_hp -= damageDealt(boss, player)
        if player_hp <= 0:
            return False

#The player cannot spend more than 356
min_cost = 400
#Build weapon
for weapon in weapons:
    weapon_cost = weapon[0]
    weapon_dmg = weapon[1]
    #Build armor
    for armor_used in armor:
        armor_cost = armor_used[0]
        armor_armor = armor_used[1]
        #Build first ring
        for ring1 in rings:
            ring1_cost = ring1[0]
            ring1_dmg = ring1[1]
            ring1_armor = ring1[2]
            for ring2 in rings:
                #You cant buy the same ring twice except the "not build any ring"
                if ring1 == ring2 != (0, 0, 0):
                    continue
                else:
                    ring2_cost = ring2[0]
                    ring2_dmg = ring2[1]
                    ring2_armor = ring2[2]
                    armored_player = player.copy()
                    armored_player['Damage'] = weapon_dmg + ring1_dmg + ring2_dmg
                    armored_player['Armor'] = armor_armor + ring1_armor + ring2_armor
                if win(armored_player, boss):
                    build_cost = weapon_cost + armor_cost + ring1_cost + ring2_cost
                    min_cost = min(min_cost, build_cost)
                    

print(min_cost)
#---------------------------- Part 2 ----------------------------


max_cost = 0
#Build weapon
for weapon in weapons:
    weapon_cost = weapon[0]
    weapon_dmg = weapon[1]
    #Build armor
    for armor_used in armor:
        armor_cost = armor_used[0]
        armor_armor = armor_used[1]
        #Build first ring
        for ring1 in rings:
            ring1_cost = ring1[0]
            ring1_dmg = ring1[1]
            ring1_armor = ring1[2]
            for ring2 in rings:
                #You cant buy the same ring twice except the "not build any ring"
                if ring1 == ring2 != (0, 0, 0):
                    continue
                else:
                    ring2_cost = ring2[0]
                    ring2_dmg = ring2[1]
                    ring2_armor = ring2[2]
                    armored_player = player.copy()
                    armored_player['Damage'] = weapon_dmg + ring1_dmg + ring2_dmg
                    armored_player['Armor'] = armor_armor + ring1_armor + ring2_armor
                if not win(armored_player, boss):
                    build_cost = weapon_cost + armor_cost + ring1_cost + ring2_cost
                    max_cost = max(max_cost, build_cost)
                    
print(max_cost)