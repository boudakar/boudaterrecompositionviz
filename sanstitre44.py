# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 01:17:58 2024

@author: pc
"""

import pandas as pd
import matplotlib.pyplot as plt
import random

# Génération des données fictives
def generate_customer_data(num_customers):
    data = {
        'Client': [f'Client {i+1}' for i in range(num_customers)],
        'Âge': [random.randint(18, 65) for _ in range(num_customers)],
        'Dépense moyenne (€)': [random.uniform(50, 500) for _ in range(num_customers)]
    }
    return pd.DataFrame(data)

# Générer les données
customer_data = generate_customer_data(50)

# Visualisation
plt.figure(figsize=(12, 6))
plt.scatter(customer_data['Âge'], customer_data['Dépense moyenne (€)'], color='purple', alpha=0.7)
plt.title("Dépense moyenne par âge")
plt.xlabel("Âge")
plt.ylabel("Dépense moyenne (€)")
plt.grid(True)
plt.tight_layout()
plt.show()
