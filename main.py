#Cherniak Sviatoslav



import matplotlib.pyplot as plt

with open('DS5.txt', 'r') as file:
    data = [tuple(map(int, line.strip().split())) for line in file]

fig, ax = plt.subplots(figsize=(960/80, 540/80))

x, y = zip(*data)
ax.scatter(y, x)
#turning axes off
ax.axis('off')

fig.savefig('Rendered_Image.png')
plt.show()