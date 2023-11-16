from time import sleep
import psycopg2
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

# Importez les variables d'environnement de votre fichier docker-compose.yml
import os


class Command(BaseCommand):
    """Django command to wait for the database."""

    def handle(self, *args, **options):
        """Entrypoint for the command."""
        self.stdout.write("Waiting for the database...")
        db_up = False
        while db_up is False:
            try:
                # Utilisez les variables d'environnement pour les
                # informations de connexion
                db_connection = psycopg2.connect(
                    host=os.environ.get("DB_HOST"),
                    database=os.environ.get("DB_NAME"),
                    user=os.environ.get("DB_USER"),
                    password=os.environ.get("DB_PASS"),
                )
                # Fermez la connexion
                db_connection.close()
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
