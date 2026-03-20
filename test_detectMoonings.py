import unittest
from detectMoonings import is_fast_dump, get_price, wait_for_price
from unittest.mock import patch, MagicMock
from datetime import date, datetime, timedelta

class TestDetectMoonings(unittest.TestCase):
    def test_is_fast_dump_false(self):
        prices = [100, 101, 102]
        self.assertFalse(is_fast_dump(prices, threshold_drop=5, window=3))

    def test_is_fast_dump_true(self):
        prices = [100, 120, 110]
        self.assertTrue(is_fast_dump(prices, threshold_drop=8, window=3))

    def test_get_price_returns_dict(self):
        import detectMoonings
        # Mock client globalmente
        detectMoonings.client = MagicMock()
        detectMoonings.client.get_all_tickers.return_value = [
            {'symbol': 'BTCUSDT', 'price': '50000'},
            {'symbol': 'ETHUSDT', 'price': '4000'}
        ]
        # Dependências globais simuladas
        detectMoonings.tickers = ['BTC', 'ETH']
        detectMoonings.PAIR_WITH = 'USDT'
        detectMoonings.FIATS = []
        detectMoonings.CUSTOM_LIST = True
        detectMoonings.historical_prices = [{} for _ in range(5)]
        detectMoonings.hsp_head = 0
        result = get_price(add_to_historical=False)
        self.assertIn('BTCUSDT', result)
        self.assertIn('ETHUSDT', result)

    def test_wait_for_price_runs(self):
        import detectMoonings
        # Mock funções
        detectMoonings.pause_bot = MagicMock()
        detectMoonings.get_price = MagicMock()
        # Mock config para proteção contra dump rápido
        detectMoonings.config = {
            'trading_options': {
                'FAST_DUMP_PROTECTION': {
                    'ENABLED': True,
                    'THRESHOLD_DROP': 2,
                    'WINDOW': 3
                }
            }
        }
        # Dependências globais simuladas
        detectMoonings.historical_prices = [
            {'BNBUSDT': {'price': '100', 'time': datetime.now()}},
            {'BNBUSDT': {'price': '110', 'time': datetime.now()}},
            {'BNBUSDT': {'price': '120', 'time': datetime.now()}},
        ]
        detectMoonings.hsp_head = 2
        detectMoonings.volatility_cooloff = {}
        detectMoonings.session_profit = 0
        detectMoonings.session_usd_profit = 0
        detectMoonings.coins_bought = []
        detectMoonings.MAX_COINS = 10
        detectMoonings.CHANGE_IN_PRICE = 5
        detectMoonings.TIME_DIFFERENCE = 2
        detectMoonings.RECHECK_INTERVAL = 1
        detectMoonings.PAIR_WITH = 'USDT'
        # Executa sem erro
        try:
            wait_for_price()
        except Exception as e:
            self.fail(f'wait_for_price() raised {e}')

if __name__ == '__main__':
    unittest.main()
