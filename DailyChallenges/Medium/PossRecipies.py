#2115. Find All Possible Recipes from Given Supplies
from collections import defaultdict, deque
from typing import List
class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        graph = defaultdict(list)
        incoming_edges = defaultdict(int)
        for recipe, required_ingredients in zip(recipes, ingredients):
            for ingredient in required_ingredients:
                graph[ingredient].append(recipe)
            incoming_edges[recipe] += len(required_ingredients)
        queue = deque(supplies)
        available_recipes = []
        while queue:
            for _ in range(len(queue)):
                ingredient = queue.popleft()
                for recipe in graph[ingredient]:
                    incoming_edges[recipe] -= 1
                    if incoming_edges[recipe] == 0:
                        available_recipes.append(recipe)
                        queue.append(recipe)
        return available_recipess