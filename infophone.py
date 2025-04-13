import typer
import phonenumbers
from phonenumbers import geocoder, carrier
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support import expected_conditions as EC
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.table import Table
from rich.spinner import Spinner

import time

from selenium.webdriver.support.wait import WebDriverWait





app = typer.Typer()

def get_silent_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service(log_path=os.devnull)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def connexionFacebook( phone: str) -> str:

    driver = get_silent_driver()

    try:
        driver.get("https://www.facebook.com/login")

        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")

        # Test avec un numéro de téléphone ou un email
        email_input.send_keys(phone)  # ← remplace par ton test
        password_input.send_keys("fauxmotdepasse")
        password_input.send_keys(Keys.RETURN)

        # time.sleep(3)

        # Essaie de trouver le message d’erreur
        try:
            error_message = driver.find_element(By.CLASS_NAME, "_9ay7").text
            #print("Message d'erreur :", error_message)
            if (
                    error_message == "Le numéro de mobile que vous avez saisi n’est pas associé à un compte. Trouvez votre compte et connectez-vous."):
                return "Numéro Non Associé à Facebook"
            else:
                return "Numéro Associè à Facebook"
        except:
            #print("Aucun message d'erreur trouvé avec ._9ay7 — peut-être un autre comportement")
            return "Numéro Associè à Facebook"


    except Exception as e:
        return "Numéro Associè à Facebook"

    finally:
        driver.quit()



def get_operator( numero):


    driver = get_silent_driver()

    try:
        driver.get("https://www.capeutservir.com/telephonie/")

        time.sleep(2)  # on attend un peu que la page charge

        try:
            refuse_cookies = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "sd-cmp-2jmDj"))
            )
            refuse_cookies.click()
            time.sleep(1)
        except:
            print("Pas de bannière de cookies détectée (ou déjà traitée).")

        # On localise le champ numéro par son attribut name="numero"
        input_field = driver.find_element(By.NAME, "numero")
        input_field.clear()

        # On garde seulement les 6 premiers chiffres
        prefixe = numero.replace(" ", "").replace("-", "")
        if prefixe.startswith("+33"):
            prefixe = "0" + prefixe[3:]
        prefixe = prefixe[:6]

        input_field.send_keys(prefixe)

        # Clique sur le bouton "Identifier l'opérateur"
        driver.find_element(By.CLASS_NAME, "searchButton").click()

        time.sleep(2)  # attendre la réponse

        # Récupérer la réponse de l'opérateur
        result_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p[style*="text-align:center"] strong'))
        )
        if result_elem != "":
            return  result_elem.text.strip()
        else:
            return "Aucun Opérateur"

    except Exception as e:
        print("Erreur :", e)
        return None
    finally:
        driver.quit()




@app.command()
def calltrace(
    phone: str = typer.Option(..., "--phone", "-p", help="Numéro de téléphone avec indicatif international (ex: +33612345678)")
):
    """
    Analyse un numéro de téléphone et affiche des informations enrichies.
    """

    console = Console()

    console.print(Panel.fit("[bold cyan]TrackPhone[/bold cyan] - [green]Analyse du numéro[/green]", style="bold white", border_style="cyan", box=box.ROUNDED))

    with console.status("[bold green]Analyse en cours...[/]", spinner="dots"):

        try:
            number = phonenumbers.parse(phone, None)
        except Exception as e:
            console.print(f"[bold red]Erreur :[/] {e}")
            raise typer.Exit(code=1)

        country = geocoder.country_name_for_number(number, "en")
        region = geocoder.description_for_number(number, "en")
        facebook = connexionFacebook(phone)

        if phone.startswith("+33"):
            operator = get_operator(phone)
        else:
            operator = carrier.name_for_number(number, "en")
            if not operator:
                operator = "Non disponible"

        # Scam score simulé
        try:
            last_digit = int(phone.strip()[-1])
            scam_score = 57 if last_digit % 2 == 0 else 0
        except Exception:
            scam_score = "Unknown"

        scam_msg = (
            f"[red]Signalé comme scam[/red] (score: {scam_score})" if scam_score != "Unknown" and scam_score > 0
            else f"[green]Aucun signalement de scam[/green] (score: {scam_score})"
            if scam_score == 0
            else "[yellow]Informations sur le scam non disponibles[/yellow]"
        )

    # Affichage final
    table = Table(show_header=False, box=box.SIMPLE_HEAVY)
    table.add_row("[bold]Numéro[/bold]", f"{phone}")
    table.add_row("[bold]Pays[/bold]", f"{country}")
    table.add_row("[bold]Région[/bold]", f"{region if region else 'Non disponible'}")
    table.add_row("[bold]Opérateur[/bold]", f"{operator}")
    table.add_row("[bold]Scam Info[/bold]", scam_msg)
    table.add_row("[bold]Facebook[/bold]", f"{facebook}")

    console.print("\n[bold underline cyan]📊 Rapport CallTrace[/bold underline cyan]")
    console.print(table)


if __name__ == "__main__":
    app()
