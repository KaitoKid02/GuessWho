import typer
import phonenumbers
from phonenumbers import geocoder, carrier
import requests

app = typer.Typer()

def get_operator_from_arcep(phone: str) -> str:
    """
    Appelle l'API ARCEP pour obtenir l'opérateur d'un numéro français.
    Ici, on simule l'appel à l'API.
    """
    # URL fictive de l'API ARCEP
    url = "https://api.arcep.fr/operateur"
    params = {"phone": phone}
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # On suppose que la réponse contient une clé "operator"
            return data.get("operator", "Non disponible")
        else:
            typer.echo(f"Avertissement: API ARCEP retourne le status {response.status_code}.")
            return "Non disponible"
    except Exception as e:
        typer.echo(f"Erreur lors de l'appel à l'API ARCEP: {e}")
        return "Non disponible"

@app.command()
def calltrace(
    phone: str = typer.Option(..., "--phone", "-p", help="Numéro de téléphone avec indicatif international (ex: +33612345678)")
):
    """
    Analyse un numéro de téléphone et affiche des informations sur le pays, la région et l'opérateur.
    Pour les numéros français, l'opérateur est récupéré via l'API ARCEP.
    Simule également une détection de scam.
    """
    try:
        number = phonenumbers.parse(phone, None)
    except Exception as e:
        typer.echo(f"Erreur lors de l'analyse du numéro : {e}")
        raise typer.Exit(code=1)

    # Récupère le nom du pays et la description de la région
    country = geocoder.country_name_for_number(number, "en")
    region = geocoder.description_for_number(number, "en")
    
    # Pour l'opérateur, on vérifie si le numéro est français
    if phone.startswith("+33"):
        operator = get_operator_from_arcep(phone)
    else:
        operator = carrier.name_for_number(number, "en")
        if not operator:
            operator = "Non disponible"

    # Simulation d'une vérification de scam :
    # Méthode simple : si le dernier chiffre du numéro est pair, on attribue un score de scam de 57, sinon 0.
    scam_score = 0
    try:
        last_digit = int(phone.strip()[-1])
        scam_score = 57 if last_digit % 2 == 0 else 0
    except Exception:
        scam_score = "Unknown"

    typer.echo("=== Rapport CallTrace ===")
    typer.echo(f"Numéro     : {phone}")
    typer.echo(f"Pays       : {country}")
    typer.echo(f"Région     : {region if region else 'Non disponible'}")
    typer.echo(f"Opérateur  : {operator}")
    if scam_score == "Unknown":
        scam_message = "Informations sur le scam non disponibles"
    else:
        scam_message = "Signalé comme scam" if scam_score > 0 else "Aucun signalement de scam"
    typer.echo(f"Scam Info  : {scam_message} (score: {scam_score})")

if __name__ == "__main__":
    app()
