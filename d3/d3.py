from __future__ import annotations
from typing import Type


class node:
    value: str
    positions: list[tuple]
    adjList: set[Type[node]]

    def __init__(self):
        self.value = ""
        self.positions = []
        self.adjList = set()


sum = 0
nodes: dict[tuple, node] = {}
map = []
maxX = 139
maxY = 139


def format_node(n):
    return {
        "key": n[0],
        "value": n[1].value,
        "positions": n[1].positions,
        "adjList": [adj_node.value for adj_node in n[1].adjList],
    }


def makeList():
    with open("./input.txt") as iFile:
        for i, line in enumerate(iFile):
            line = line[:-1]
            # maxX = len(line)
            # maxY = i+1
            map.append(line)


def populateDict(part2: bool):
    for posY, line in enumerate(map):
        for posX, c in enumerate(line):
            # numeric node
            if c.isdigit():
                if posX == 0 or not line[posX - 1].isdigit():
                    n = node()
                    n.positions.append((posX, posY))
                    n.value = c
                    nodes.update(dict.fromkeys([(posX, posY)], n))
                else:
                    n = nodes[(posX - 1, posY)]
                    n.positions.append((posX, posY))
                    n.value += c
                    nodes.update(dict.fromkeys(n.positions, n))
            # symbolic node
            elif c != "." and not part2:
                n = node()
                n.positions.append((posX, posY))
                n.value = "*"
                nodes.update(dict.fromkeys(n.positions, n))
            elif c == "*":
                n = node()
                n.positions.append((posX, posY))
                n.value = c
                nodes.update(dict.fromkeys(n.positions, n))


def findAdj():
    for i, x in nodes.items():
        if x.value == "*":
            if i[0] > 0:
                n = nodes.get((i[0] - 1, i[1]))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[0] < maxX:
                n = nodes.get((i[0] + 1, i[1]))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[1] > 0:
                n = nodes.get((i[0], i[1] - 1))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[1] < maxY:
                n = nodes.get((i[0], i[1] + 1))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[0] > 0 and i[1] > 0:
                n = nodes.get((i[0] - 1, i[1] - 1))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[0] < maxX and i[1] > 0:
                n = nodes.get((i[0] + 1, i[1] - 1))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[0] < maxX and i[1] < maxY:
                n = nodes.get((i[0] + 1, i[1] + 1))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)
            if i[0] > 0 and i[1] < maxY:
                n = nodes.get((i[0] - 1, i[1] + 1))
                if n and n.value.isnumeric():
                    nodes[i].adjList.add(n)


if __name__ == "__main__":
    # part 1
    makeList()
    populateDict(False)
    findAdj()
    for x in nodes.values():
        if x.value == "*":
            for n in x.adjList:
                sum += int(n.value)
    print("sum p1:", sum)

    # part 2
    sum = 0
    nodes: dict[tuple, node] = {}
    populateDict(True)
    findAdj()
    for x in nodes.values():
        if x.value == "*" and len(x.adjList) == 2:
            prod = 1
            for n in x.adjList:
                prod*=int(n.value)
            sum+=prod
    print("sum p2:", sum)
