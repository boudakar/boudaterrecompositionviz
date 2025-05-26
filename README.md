import matplotlib.pyplot as plt

# Rayons en km
layers = ['Croûte', 'Manteau', 'Noyau externe', 'Noyau interne']
radii = [35, 2900, 5100, 6371]  # limites des couches

plt.figure(figsize=(6, 6))
plt.pie([radii[0],
         radii[1]-radii[0],
         radii[2]-radii[1],
         radii[3]-radii[2]],
        labels=layers,
        startangle=90,
        colors=['#f5deb3', '#ffa07a', '#cd5c5c', '#8b0000'],
        autopct='%1.1f%%')
plt.title("Couches de la Terre (en proportion de rayon)")
plt.show()
