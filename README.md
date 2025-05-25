# Poszukiwanie bibliotek o określonej funkcjonalności

## Web Scraping
- ` Biblioteka: requests + BeautifulSoup `
- ` Biblioteka: Scrapy `
## Pliki

- `filmweb_premiere_requests.py` - prosty scraper wykorzystujący requests i BeautifulSoup do pobrania tytułów, gatunków i roku produkcji filmów.
- `filmweb_premiere_scrapy.py` - scraper napisany w Scrapy, realizujący podobne zadanie z wykorzystaniem frameworka.

## Instrukcje

1. Aby uruchomić `filmweb_premiere_requests.py`, potrzebujesz zainstalować:
   ```
   pip install requests beautifulsoup4
   ```
   Następnie uruchom:
   ```
   python filmweb_premiere_requests.py
   ```

2. Aby uruchomić projekt Scrapy:
   - Zainstaluj scrapy:
   ```
   pip install scrapy
   ```
   - Uruchom spidera:
   ```
   scrapy runspider filmweb_premiere_scrapy.py
   ```

## Opis

Projekty pobierają listę premier filmowych ze strony Filmweb, wypisując tytuł, gatunek i rok produkcji.
