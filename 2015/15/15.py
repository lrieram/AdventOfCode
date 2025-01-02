# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
ingredients = []
for line in file:
    ingredients_properties = line.strip()
    ingredient = ingredients_properties.split(' ')
    #[:-1] to remove the ,
    capacity = int(ingredient[2][:-1])
    durability = int(ingredient[4][:-1])
    flavor = int(ingredient[6][:-1])
    texture = int(ingredient[8][:-1])
    calories = int(ingredient[10])
    ingredients.append((capacity, durability, flavor, texture, calories))

def score(cookie):
    capacity = max(0, cookie[0])
    durability = max(0, cookie[1])
    flavor = max(0, cookie[2])
    texture = max(0, cookie[3])
    return capacity * durability * flavor * texture

def bestCookie(ingredients, teaspoons_left, cookie):
    
    #Already added the 100 teaspoons
    if teaspoons_left == 0:
        return cookie
    
    capacity = cookie[0]
    durability = cookie[1]
    flavor = cookie[2]
    texture = cookie[3]
    
    #If there's only 1 ingredient left
    #put all the teaspoons left of that ingredient
    if len(ingredients) == 1:
        new_capacity = capacity + (ingredients[0][0] * teaspoons_left)
        new_durability = durability + (ingredients[0][1] * teaspoons_left)
        new_flavor = flavor + (ingredients[0][2] * teaspoons_left)
        new_texture = texture + (ingredients[0][3] * teaspoons_left)
        return (new_capacity, new_durability, new_flavor, new_texture)
    
    max_score = 0
    best_cookie = cookie
    for ts in range(1, teaspoons_left+1):
        #Use the first ingredient
        ingredients_left = ingredients[1:]
        new_capacity = capacity + (ingredients[0][0] * ts)
        new_durability = durability + (ingredients[0][1] * ts)
        new_flavor = flavor + (ingredients[0][2] * ts)
        new_texture = texture + (ingredients[0][3] * ts)
        new_cookie = (new_capacity, new_durability, new_flavor, new_texture)
        final_cookie = bestCookie(ingredients_left, teaspoons_left-ts, new_cookie)
        new_score = score(final_cookie)
        if new_score > max_score:
            max_score = new_score
            best_cookie = final_cookie
    return best_cookie
        

print(score(bestCookie(ingredients, 100, (0,0,0,0))))
#---------------------------- Part 2 ----------------------------

def scoreCalories(cookie):
    if cookie[4] != 500:
        return 0
    capacity = max(0, cookie[0])
    durability = max(0, cookie[1])
    flavor = max(0, cookie[2])
    texture = max(0, cookie[3])
    return capacity * durability * flavor * texture

def bestCaloriesCookie(ingredients, teaspoons_left, cookie):
    
    if teaspoons_left == 0:
        return cookie
    
    capacity = cookie[0]
    durability = cookie[1]
    flavor = cookie[2]
    texture = cookie[3]
    calories = cookie[4]
    
    #If there's only 1 ingredient left
    #put all the teaspoons left of that ingredient
    if len(ingredients) == 1:
        new_capacity = capacity + (ingredients[0][0] * teaspoons_left)
        new_durability = durability + (ingredients[0][1] * teaspoons_left)
        new_flavor = flavor + (ingredients[0][2] * teaspoons_left)
        new_texture = texture + (ingredients[0][3] * teaspoons_left)
        new_calories = calories + (ingredients[0][4] * teaspoons_left)
        return (new_capacity, new_durability, new_flavor, new_texture, new_calories)
    
    max_score = 0
    best_cookie = cookie
    for ts in range(1, teaspoons_left+1):
        #I use the first ingredient
        ingredients_left = ingredients[1:]
        new_capacity = capacity + (ingredients[0][0] * ts)
        new_durability = durability + (ingredients[0][1] * ts)
        new_flavor = flavor + (ingredients[0][2] * ts)
        new_texture = texture + (ingredients[0][3] * ts)
        new_calories = calories + (ingredients[0][4] * ts)
        new_cookie = (new_capacity, new_durability, new_flavor, new_texture, new_calories)
        final_cookie = bestCaloriesCookie(ingredients_left, teaspoons_left-ts, new_cookie)
        new_score = scoreCalories(final_cookie)
        if new_score > max_score:
            max_score = new_score
            best_cookie = final_cookie
    return best_cookie


print(scoreCalories(bestCaloriesCookie(ingredients, 100, (0,0,0,0,0))))