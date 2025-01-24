# README - GuessWho

## Description du Projet
Projet universitaire (Master 2 Sécurité des systèmes d'information) pour l'UE threat intelligence &amp; forensics.
GuessWho est un script Python conçu pour rechercher des informations disponibles publiquement sur Internet à partir de données d'entrée comme un nom, un identifiant ou un email. Ce projet est destiné à des fins éducatives dans le cadre du module Threat Intelligence & Forensics et vise à illustrer les risques liés à la divulgation d'informations personnelles.

## Fonctionnalités
- Recherche d'informations basée sur des noms, prénoms, identifiants ou emails (à l'aide d'options comme `--name`, `--last`, `--id`, `--email`).
- Vérification des fuites de données associées à un email via HaveIBeenPwned.
- Exploration des réseaux sociaux à l'aide de moteurs de recherche pour localiser des comptes.
- Exportation des résultats en JSON ou CSV.
- Option d'affichage des photos associées à la personne recherchée, avec comparaison des visages via des services tiers gratuits.
- Gestion des erreurs avec des messages explicatifs si aucune information n'est trouvée.

## Limitations
- Le script fonctionne exclusivement pour des recherches individuelles (éviter les recherches en masse).
- Le projet est conçu pour être exécuté principalement sous Linux. Une compatibilité Windows pourrait être envisagée dans un conteneur Docker.
- Les données exportées dans des fichiers (CSV, JSON) ne sont pas destinées à être stockées ou partagées.

## Technologies Utilisées
- **Requêtes et scraping** : `requests`, `BeautifulSoup`, `selenium`
- **Gestion des fuites de données** : API HaveIBeenPwned
- **Comparaison d'images** : OpenCV, Face Recognition ou Google Lens (via un service tiers gratuit)
- **Exportation des résultats** : `pandas`, `reportlab`
- **Optimisation** : `concurrent.futures` pour le multi-threading

## Installation
1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-repo/guesswho.git
   cd guesswho
   ```
2. Installez les dépendances Python nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Exécutez le script :
   ```bash
   python guesswho.py --name "John" --last "Doe"
   ```

## Utilisation
### Options disponibles
- `--name` : Prénom de la personne à rechercher
- `--last` : Nom de famille
- `--id` : Identifiant ou pseudo
- `--email` : Adresse email

### Exemple
Pour rechercher des informations sur une personne appelée John Doe :
```bash
python guesswho.py --name "John" --last "Doe"
```

## Éthique et Conformité
### Conformité RGPD
- Aucune donnée n'est stockée dans le code ou dans une base de données.
- Les recherches sont effectuées en temps réel sans conservation des résultats par le script.
- Les utilisateurs doivent respecter les régulations en matière de protection des données.

### Limites
- Le script est conçu à des fins éducatives uniquement.
- L’auteur ne peut être tenu responsable des usages malveillants.
- Les utilisateurs doivent obtenir un consentement explicite avant de rechercher des informations sur une tierce personne.

## Licence
GuessWho est distribué sous la licence Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0). Cette licence interdit l’utilisation commerciale du script et n’autorise pas les modifications.

Pour plus d’informations sur la licence, consultez le lien : https://creativecommons.org/licenses/by-nc-nd/4.0/

## Contributions
Les contributions sont les bienvenues, mais elles doivent respecter les principes éthiques et la conformité RGPD. Les suggestions peuvent être soumises via des issues ou des pull requests sur GitHub.

## Avertissement
Ce script est destiné à des fins éducatives dans le cadre de la cybersécurité. Toute utilisation malveillante est strictement interdite et l’auteur décline toute responsabilité pour les conséquences découlant d’un usage abusif.
