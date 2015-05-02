__author__ = 'LIJIN'
import bktree
tree=bktree.BKTree()
line=0
with open("words.txt", "r") as ins:
    for line in ins:
        tree.insert(line)
while True:
    text=raw_input("Enter String")
    if text==exit:
        break
    print(tree.findClosestMatches(len(text),text))

