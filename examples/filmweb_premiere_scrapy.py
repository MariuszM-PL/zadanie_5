"""
Przykład prostego spidera Scrapy.

Ten spider pobiera dane o nowych serialach z Filmweb (sekcja premiery seriali).
Dla każdego serialu wydobywa i wypisuje:
- tytuł serialu,
- gatunki,
- rok produkcji.

Wyniki są również zwracane w formie słownika (yield).
"""

import scrapy
import logging

# Ustawiamy poziom logów Scrapy na WARNING, aby ograniczyć ilość wypisywanych informacji
logging.getLogger('scrapy').setLevel(logging.WARNING)

class FilmwebPremiereSpider(scrapy.Spider):
    # Unikalna nazwa spidera
    name = "filmweb_premiere"
    # Lista adresów startowych, od których zaczyna crawling
    start_urls = ['https://www.filmweb.pl/ranking/premiere/serial']
    print("Nowe najlepsze seriale ze świata:")
    def parse(self, response):
        # Przechodzimy po każdym elemencie z klasą 'rankingType' - jeden film/serial to jeden element
        for film in response.css('div.rankingType'):
            # Pobieramy tytuł serialu (tekst linku <a> w elemencie z klasą 'rankingType__titleWrapper')
            title = film.css('div.rankingType__titleWrapper a::text').get()
            if not title:
                # Gdy tytuł nie jest dostępny, przypisujemy placeholder
                title = "brak tytułu"
            else:
                title = title.strip()

            # Pobieramy wszystkie gatunki jako listę tekstów (elementy <span> wewnątrz linków <a> z klasą 'tag rankingGerne')
            genres = film.css('div.rankingType__genres a.tag.rankingGerne span::text').getall()
            if genres:
                # Usuwamy zbędne spacje z każdego gatunku i łączymy przecinkiem
                genres_str = ', '.join([g.strip() for g in genres])
            else:
                genres_str = "brak gatunków"

            # Pobieramy rok produkcji jako tekst elementu <span> z klasą 'rankingType__year'
            year = film.css('span.rankingType__year::text').get()
            year = year.strip() if year else "brak roku"

            # Wypisujemy wynik na konsolę
            print(f"- {title} | Gatunki: {genres_str} | Rok: {year}")

            # Zwracamy wynik jako słownik
            yield {
                'title': title,
                'genres': genres,
                'year': year
            }
