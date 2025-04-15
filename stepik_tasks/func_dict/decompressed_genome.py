path = r"C:\Git_repository\first_project\stepik_tasks\dataset_3363_2.txt"
with open(path, "r") as inf:
    genome = inf.readline().strip()
genome = [*genome]

for i in range(len(genome) - 1, 0, -1):
    if genome[i].isdigit() and genome[i - 1].isdigit():
        genome[i] = genome[i - 1] + genome[i]
        genome.pop(i - 1)

new_genome = []

for i in range(len(genome)):
    if genome[i].isalpha():
        new_genome += genome[i]
    else:
        n = int(genome[i])
        new_genome += genome[i - 1] * n
        new_genome.pop()

new_genome = "".join(new_genome)

with open("C:\\Git_repository\\first_project\\stepik_tasks\\text2.txt", "w") as ouf:
    ouf.write(new_genome)
