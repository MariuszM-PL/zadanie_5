# Raport z analizy bibliotek do web scrapingu

## 1. filmweb_premiere_requests.py
- **Biblioteka:** requests + BeautifulSoup
- **Przeznaczenie:** Pobieranie i parsowanie statycznych stron HTML
- **Główne funkcje:** 
  - requests: pobieranie stron HTTP
  - BeautifulSoup: parsowanie i ekstrakcja danych z HTML

### Zalety:
- Prosta instalacja i użycie
- Szerokie wsparcie i dokumentacja
- Lekka i szybka do prostych zadań scrapingu
- Możliwość precyzyjnej nawigacji w strukturze HTML

### Ograniczenia:
- Brak obsługi JavaScript (nie renderuje dynamicznie generowanych treści)
- Konieczność ręcznego zarządzania nagłówkami i sesjami przy bardziej skomplikowanych stronach

### Linki:
- [requests documentation](https://docs.python-requests.org/)
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

## 2. filmweb_premiere_scrapy.py
- **Biblioteka:** Scrapy
- **Przeznaczenie:** Zaawansowany web scraping i crawlery
- **Główne funkcje:** 
  - Asynchroniczne pobieranie wielu stron
  - Zaawansowane zarządzanie requestami i pipeline
  - Obsługa middleware i rozszerzeń

### Zalety:
- Bardzo szybka i wydajna dzięki asynchroniczności
- Rozbudowane narzędzia do crawl'owania dużych serwisów
- Wiele wbudowanych funkcji (retry, throttling, cache)
- Wsparcie społeczności i bogata dokumentacja

### Ograniczenia:
- Wyższa krzywa nauki niż requests+BeautifulSoup
- Nadmiarowa dla prostych zadań
- Konieczność definiowania klas Spider i struktury projektu

### Linki:
- [Scrapy documentation](https://docs.scrapy.org/en/latest/)