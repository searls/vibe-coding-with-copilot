import logging
import sys
import os
from lib.adapters.suumo_adapter import fetch_listings
from models import Listing, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main(query, region=None):
    # Set logging to INFO for CLI runs
    logging.basicConfig(level=logging.INFO)
    # Only Suumo uses the new adapter for now
    suumo_result = fetch_listings(query, region)
    print(f"[Suumo] Inserted: {suumo_result['db_stats']['inserted']}, Updated: {suumo_result['db_stats']['updated']}")
    # ...existing code for other scrapers (Lifeful, AtHome) can be refactored similarly later...

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python main.py <keyword> [region_code]')
        exit(1)
    query = sys.argv[1]
    region = sys.argv[2] if len(sys.argv) > 2 else None
    main(query, region)
