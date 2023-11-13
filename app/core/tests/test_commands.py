import unittest
from unittest.mock import patch, MagicMock
from django.core.management import call_command
from core.management.commands import wait_for_db


class TestWaitForDBCommand(unittest.TestCase):
    @patch('psycopg2.connect')
    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, mock_sleep, mock_connect):
        # Configurez le mock pour simuler une connexion réussie à la base de données
        mock_connect.return_value = MagicMock()
        
        # Appelez votre commande personnalisée
        call_command('wait_for_db')
        
        # Vérifiez que la méthode de connexion a été appelée une fois
        mock_connect.assert_called_once()
    
    @patch('psycopg2.connect',
           side_effect=[wait_for_db.Psycopg2Error] * 3 + [None])
    @patch('time.sleep', return_value=None)
    def test_wait_for_db_with_retries(self, mock_sleep, mock_connect):
        # Le sleep est simulé pour éviter les délais réels dans les tests
        with self.assertRaises(SystemExit):
            call_command('wait_for_db')
        
        self.assertEqual(mock_connect.call_count, 4)
