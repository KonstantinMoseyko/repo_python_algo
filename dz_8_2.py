import collections
def makeConnected(n: int, patchcord:list) -> int:
    # определяем кол кабелей и компов для соединнеия
        count_pachcord = len(patchcord)
        if n > count_pachcord + 1:
            return -1

        # создаем словарь с списокм значений,
#         пребираем список, созд ключ значение, pc: [и подкл pc]
        dict_pc = collections.defaultdict(list)
        for pc in patchcord:
            pc1, pc2 = pc
            dict_pc[pc1].append(pc2)
            dict_pc[pc2].append(pc1)

        # создаем дерево поиска в глубину
        trie = set()
        nodes = 0
        def dfs(node):
            trie.add(node) # добавляем узел
            neighbors = dict_pc[node] # определяем соседа pc по узлу
            for n in neighbors:# перебираем соседство
                if n not in trie:
                    dfs(n)

		# коннектит pc
        for i in range(n):
            if i not in trie:
                nodes += 1
                dfs(i)

        return nodes - 1
print(makeConnected(4,[[0,1],[0,2],[1,2]]))
