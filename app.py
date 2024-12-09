# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:13:59 2024

@author: pc
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Data for orientation suggestions
courses = {
    "science": ["BTS SIO", "DUT Informatique", "Licence Physique", "Prépa scientifique (MPSI, PCSI)"],
    "arts": ["Licence Arts Plastiques", "BTS Design Graphique", "Beaux-Arts"],
    "commerce": ["Licence Économie et Gestion", "BTS Commerce International", "École de Commerce Post-Bac"],
    "health": ["Licence Biologie", "BTS Diététique", "Médecine (PACES)", "Infirmier (IFSI)"],
}

@app.route('/')
def home():
    return render_template("home.html")





@app.route('/orientation', methods=['POST'])
def orientation():
    # Retrieve form data
    name = request.form.get("name")
    interest = request.form.get("interest")

    # Suggest courses based on interest
    suggestions = courses.get(interest.lower(), ["Orientation non disponible."])

    return render_template("result.html", name=name, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
