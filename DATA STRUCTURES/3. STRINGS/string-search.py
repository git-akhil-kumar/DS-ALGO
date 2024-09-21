def containsSubstring(src, key):
    res = []
    for word in src:
        if key in word:
            res.append(word)
    return res


src = [
    "minecraftgame",
    "intelligent",
    "innercrafttalent",
    "craft",
    "craftcraftcissor",
    "stonecrafter",
]
key = "cra"
print(containsSubstring(src, key))
