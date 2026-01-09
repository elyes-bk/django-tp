import json
from pathlib import Path

from django.core.management.base import BaseCommand

from main.models import (
    Site,
    Olympiade,
    Typologie,
    Denomination,
    DateReference,
)


class Command(BaseCommand):
    help = "Import des sites depuis un fichier JSON"

    def handle(self, *args, **options):
        json_path = Path("data/sites.json")

        if not json_path.exists():
            self.stderr.write("❌ Fichier JSON introuvable")
            return

        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        count = 0

        for item in data:
            site = Site.objects.create(
                nom=item.get("appellation", ""),
                description=item.get("historique_et_description", ""),
                adresse=item.get("adresse_com", ""),
                commune=item.get("commune", ""),
                departement=item.get("departement", 0),
                code_postal=item.get("code_postal", ""),
                latitude=item.get("latitude"),
                longitude=item.get("longitude"),
                url_image=item.get("url_image", ""),
                credits=item.get("credits", ""),
                datation=item.get("datation", ""),
            )

            # ---------- 1-N : Olympiade ----------
            olympiade_nom = item.get("site_olympique")
            if olympiade_nom:
                olympiade, _ = Olympiade.objects.get_or_create(
                    nom=olympiade_nom
                )
                site.olympiade = olympiade
                site.save()

            # ---------- N-N : Typologie ----------
            for nom in item.get("typologie", []):
                typologie, _ = Typologie.objects.get_or_create(nom=nom)
                site.typologies.add(typologie)

            # ---------- N-N : Denomination ----------
            for nom in item.get("denomination", []):
                denomination, _ = Denomination.objects.get_or_create(nom=nom)
                site.denominations.add(denomination)

            # ---------- N-N : DateReference ----------
            for valeur in item.get("date_s_de_reference", []):
                date_ref, _ = DateReference.objects.get_or_create(valeur=valeur)
                site.dates_reference.add(date_ref)

            count += 1

        self.stdout.write(
            self.style.SUCCESS(f"✅ Import terminé : {count} sites importés")
        )
