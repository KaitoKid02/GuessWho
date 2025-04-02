# README - TrackPhone

## Description du Projet

**TrackPhone** est un outil OSINT développé dans le cadre d'un projet universitaire (Master 2 Sécurité des systèmes d'information) pour l'UE *Threat Intelligence & Forensics*. Ce script Python permet de collecter automatiquement des informations à partir d'un numéro de téléphone fourni en ligne de commande.

Il est conçu pour aider à la sensibilisation aux dangers des fuites d'informations personnelles accessibles publiquement.

## Fonctionnalités

- Recherche d'informations via l'API CallTrace :

  - Localisation géographique (pays, région)
  - Opérateur (si disponible)
  - Signalement potentiel comme numéro de scam ou spam
  - Score de confiance ou de suspicion *(fonctionnalité prévue - en cours d'amélioration)*

- Vérification de l'attribution d'un numéro français via l'API de l'ARCEP *(en cours d'implémentation)*

- Détection d'association à un compte Facebook ou Instagram *(fonctionnalité prévue)*

- Gestion des erreurs si aucune donnée n'est disponible

- Support des indicateurs internationaux (ex: +1 pour USA, +33 pour France)

- Recherche d'informations via l'API CallTrace :

  - Localisation géographique (pays, région)
  - Opérateur (si disponible)
  - Signalement potentiel comme numéro de scam ou spam
  - Score de confiance ou de suspicion

- Gestion des erreurs si aucune donnée n'est disponible

- Support des indicateurs internationaux (ex: +1 pour USA, +33 pour France)

## Exemple de Rendu (CLI)

```bash
$ python track2.py "+13032222222"

--- Rapport CallTrace ---
Numéro      : +13032222222
Pays        : United States
Région     : Colorado
Opérateur  : Non disponible
```

## Limitations

- L'efficacité dépend des données accessibles via CallTrace et autres sources publiques.
- Les informations peuvent ne pas être disponibles pour tous les préfixes ou pays.

## Technologies Utilisées

- Python 3
- Requêtes HTTP : `requests`
- Analyse JSON : `json`

## Installation

1. Cloner le dépôt GitHub :

```bash
git clone https://github.com/KaitoKid02/TrackPhone.git
cd TrackPhone
```

2. Installer les dépendances Python :

```bash
pip install -r requirements.txt
```

3. Lancer le script :

```bash
python track2.py "+33749892482"
```

## Utilisation

### Argument requis

- &#x20;Numéro de téléphone à rechercher (avec indicatif international)

### Exemple :

```bash
python track2.py ""+17146175189"
```



## Projet initial et perspectives d’évolution (GuessWho)

Le projet TrackPhone est issu d’un projet plus ambitieux initialement nommé GuessWho, qui avait pour but de réaliser un outil d’OSINT complet permettant d’obtenir des informations à partir d’une identité numérique : nom, prénom, pseudo ou email.

### Objectifs initiaux du projet GuessWho :

Rechercher une personne à partir de --name, --last, --id, --email

Utilisation d’outils OSINT comme :

- sherlock (trouver les pseudos sur les réseaux sociaux)

- Maigret (profilage multi-plateforme d’un utilisateur)

Utilisation de DeepFace (librairie IA) pour comparer les photos de profils récupérées et ne conserver que celles appartenant à la même personne.

Vérification des emails dans les bases de données de fuites (HaveIBeenPwned)

Affichage d’un rapport complet avec les comptes associés, photos, données publiques, et score de correspondance facial.

Exportation possible des résultats en .json, .csv ou .pdf

## Éthique et Conformité

### Respect de la vie privée

- Aucune donnée n'est stockée localement ou envoyée vers un serveur privé.
- L'outil exploite uniquement des API publiques et légales.

### Conformité RGPD

- Le projet est à usage éducatif uniquement.
- Aucune donnée personnelle n'est conservée ou exploitée à des fins commerciales.
- Toute utilisation doit respecter les lois locales sur la protection des données.

## Licence

TrackPhone est distribué sous la licence **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.
Cela signifie :

- Aucune utilisation commerciale
- Pas de modification ou d'adaptation
- Attribution obligatoire

Plus d'infos : [https://creativecommons.org/licenses/by-nc-nd/4.0/](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## Contributions

Les contributions sont acceptées pour améliorer les sources d'information, corriger les bugs ou proposer des améliorations.
Merci de respecter les principes éthiques et la conformité RGPD.

## Avertissement

Ce script est fourni à des fins éducatives.
Toute utilisation abusive, commerciale ou illicite de ce script est interdite. L'auteur décline toute responsabilité.

