"""
Przykład web scrapingu przy użyciu bibliotek requests i BeautifulSoup.

Skrypt pobiera z serwisu Filmweb listę nowych premier filmowych.
Dla każdego filmu wypisuje:
- tytuł filmu,
- gatunki filmowe,
- rok produkcji.

Wykorzystuje requests do pobrania strony HTML oraz BeautifulSoup do parsowania i
wydobywania danych z HTML.
"""

import requests
from bs4 import BeautifulSoup

def main():
    # URL strony z rankingiem nowych premier filmowych na Filmweb
    url = 'https://www.filmweb.pl/ranking/premiere'

    # Wysyłamy zapytanie HTTP GET do podanego URL
    response = requests.get(url)
    # Sprawdzamy, czy odpowiedź jest poprawna (status 200)
    response.raise_for_status()

    # Parsujemy pobrany kod HTML za pomocą BeautifulSoup z parserem html.parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Znajdujemy wszystkie elementy <div> z klasą 'rankingType__titleWrapper',
    # które zawierają tytuły filmów
    items = soup.find_all('div', class_='rankingType__titleWrapper')

    print("Nowe najlepsze filmy ze świata:")
    for item in items:
        # Pobieramy tytuł filmu jako tekst wewnątrz elementu <div>
        title = item.get_text(strip=True)

        # Przechodzimy do rodzica elementu, gdzie znajdują się gatunki i rok produkcji
        parent = item.parent

        # Szukamy wszystkich linków <a> z klasą 'tag rankingGerne' (gatunki filmowe)
        genre_tags = parent.find_all('a', class_='tag rankingGerne')
        # Tworzymy listę nazw gatunków, usuwając spacje i nowe linie
        genres = [g.get_text(strip=True) for g in genre_tags]
        # Łączymy listę gatunków w jeden ciąg tekstowy oddzielony przecinkami
        genres_str = ', '.join(genres) if genres else "brak gatunków"

        # Szukamy elementu <span> z klasą 'rankingType__year', zawierającego rok produkcji
        year_tag = parent.find('span', class_='rankingType__year')
        # Jeśli znaleziono, pobieramy tekst, w przeciwnym wypadku podajemy "brak roku"
        year = year_tag.get_text(strip=True) if year_tag else "brak roku"

        # Wypisujemy informacje o filmie w czytelnym formacie
        print(f"- {title} | Gatunki: {genres_str} | Rok: {year}")

if __name__ == "__main__":
    main()
