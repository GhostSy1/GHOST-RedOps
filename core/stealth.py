import random
import time
import itertools

class PhantomStealthEngine:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
        ]
        self.proxies_pool = [
            "socks5://127.0.0.1:9050", # Tor Integration
            "http://185.199.229.156:80",
            "http://198.51.100.42:3128"
        ]

    def get_stealth_headers(self):
        return {
            "User-Agent": random.choice(self.user_agents),
            "X-Forwarded-For": f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}",
            "Via": "1.1 vegur",
            "Cache-Control": "no-cache"
        }

    def evade_waf_delay(self):
        # Random sleep to bypass rate-limiting and WAF blocking
        delay = random.uniform(0.5, 2.0)
        time.sleep(delay)

    def get_proxy(self):
        return random.choice(self.proxies_pool)
