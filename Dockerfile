# Image légère officielle Python
FROM python:3.11-slim

# Évite que Python génère des fichiers .pyc inutiles
ENV PYTHONDONTWRITEBYTECODE=1
# Affiche les logs en temps réel (pratique pour débugger)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code
COPY . .

# Sécurité : on crée un utilisateur qui n'est pas "root" (admin)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 5000

# On lance avec Gunicorn (4 travailleurs pour gérer les requêtes)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "run:app"]