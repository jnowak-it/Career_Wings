# Porównanie technik promptowania — zadanie: "Napisz krótką bajkę"
 
Zadanie: Wybierz jedno zadanie, na przykład „podsumuj artykuł”, i napisz do niego trzy różne wersje promptu używając 
różnych technik. Udokumentuj w pliku Markdown co zmieniłeś i jak różniły się wyniki.
 
---
 
## Wersja 1 — Prompt bezpośredni (zero-shot)
 
**Technika:** najprostsza możliwa forma: brak dodatkowego kontekstu,
odbiorcy, morału czy wskazówek co do stylu. Pełna swoboda dla modelu.
 
**Prompt:**
```
Napisz krótką bajkę.
```
 
**Otrzymana odpowiedź:**
> **Żółw i motyl**
>
> Żółw wędrował powoli przez łąkę, gdy nad nim przeleciał barwny motyl.
> — Jak możesz żyć tak wolno? — zapytał motyl, śmiejąc się.
> — Powoli, ale dotrę tam, gdzie chcę — odparł żółw.
> Minęło lato. Motyl, jak to motyle, żył tylko kilka tygodni i odleciał
> na zawsze. Żółw wciąż wędrował — powoli, ale pewnie, ku swoim celom.
>
> Morał: Nie tempo się liczy, lecz wytrwałość.
 
**Obserwacje:**
- Model sam wybrał bohaterów, motyw (klasyczne zestawienie "wolno vs
  szybko") i dodał morał na końcu. Napisał typową bajkę.
- Długość i styl w pełni zależne od modelu, nie mamy nad nimi kontroli.
---
 
## Wersja 2 — Prompt z rolą/personą (role prompting)
 
**Technika:** nadanie modelowi konkretnej roli: bajkopisarza piszącego
dla określonego odbiorcy, co zmienia ton, słownictwo i sposób narracji.
 
**Prompt:**
```
Jesteś bajkopisarzem piszącym dla 5-letnich dzieci przed snem.
Napisz krótką, uspokajającą bajkę na dobranoc.
```
 
**Otrzymana odpowiedź:**
> **Mała Chmurka szuka domu**
>
> Mała Chmurka płynęła po niebie i nie wiedziała, gdzie zasnąć na noc.
> Zajrzała za górę — za zimno. Zajrzała nad morze — za głośno od fal.
> W końcu znalazła miękką, ciepłą poduszkę z innych chmurek, przytuliła
> się do nich i zasnęła spokojnie, kołysana wiatrem.
>
> A teraz i Ty zamknij oczy, tak jak Mała Chmurka — jutro znów będzie
> pięknie świecić słońce.
 
**Obserwacje:**
- Zupełnie inne podejście niż w poprzedniej wersji: łagodniejszy język, krótsze
  zdania, brak konfliktu/rywalizacji (żółw vs motyl). Motyw dopasowany do pory czytania, czyli nocy.
- Pojawia się bezpośrednie zwrócenie się do dziecka na końcu ("zamknij
  oczy"). To element, którego nie było w zero-shot, wynikający wprost
  z określenia odbiorcy i celu (bajka na dobranoc).
- Rola wymusiła temat i funkcję tekstu (usypianie), czego prosty prompt w ogóle nie uwzględnił.
---
 
## Wersja 3 — Prompt z przykładem i jawnymi ograniczeniami (few-shot + constraints)
 
**Technika:** podanie przykładu struktury/stylu (few-shot) oraz
konkretnych, wymiernych ograniczeń (liczba zdań, obowiązkowy element,
zakaz morału), by precyzyjnie zawęzić formę odpowiedzi.
 
**Prompt:**
```
Oto przykład bajki w 4 zdaniach, bez jawnego morału na końcu:
"Lis znalazł zgubiony klucz w lesie. Nie wiedział, do czego pasuje,
więc nosił go zawsze przy sobie. Pewnego dnia napotkał zamkniętą,
starą bramę do ogrodu pełnego motyli. Klucz pasował idealnie."
 
Napisz nową bajkę w dokładnie tym samym formacie: 4 zdania,
bez jawnie wypisanego morału, z jednym zwierzęciem jako bohaterem
i jednym "znalezionym przedmiotem" jako motywem przewodnim.
```
 
**Otrzymana odpowiedź:**
> Wrona znalazła błyszczący guzik na skraju drogi i schowała go w swoim
> gnieździe. Przez wiele dni przylatywała, by patrzeć jak lśni w słońcu.
> Pewnego dnia mały chłopiec, szukając zgubionego guzika od płaszcza,
> stanął pod drzewem i zapłakał. Wrona zrzuciła mu guzik prosto do rąk.
 
**Obserwacje:**
- Struktura (4 zdania, brak morału, zwierzę + znaleziony przedmiot)
  odtworzona dokładnie według wzorca z przykładu. J najbardziej
  przewidywalna forma z całej trójki.
- Brak jawnego morału (mimo że to klasyczna cecha gatunku) został
  faktycznie wyegzekwowany — model "domyślił się" przesłania (empatia,
  dzielenie się) bez wypisywania go wprost, dokładnie jak w przykładzie.
- Najmniej "swobody twórczej" ze wszystkich wersji. Model trzyma się
  ściśle podanych ram, kosztem różnorodności motywów i kreatywności.
---
 
## Podsumowanie różnic
 
| Technika | Przewidywalność struktury | Dopasowanie do odbiorcy | Kontrola nad formą |
|---|---|---|---|
| Zero-shot (V1) | Niska | Brak — model zakłada sam | Brak |
| Rola/persona (V2) | Średnia | Wysoka (dzieci, dobranoc) | Częściowa (ton, funkcja tekstu) |
| Few-shot + ograniczenia (V3) | Wysoka | Neutralna — nieokreślona | Wysoka (długość, obecność/brak elementów) |
 
**Wniosek:** Rola/persona najlepiej sprawdza się, gdy zależy nam na
dopasowaniu tekstu do konkretnego odbiorcy i celu (np. bajka na
dobranoc ma inną funkcję niż zwykła bajka), natomiast few-shot z
ograniczeniami daje największą kontrolę nad samą formą i strukturą
tekstu, ale dzieje się to kosztem spontaniczności. Zero-shot pozostaje najszybszy do
napisania, ale oddaje modelowi pełną decyzję o kształcie odpowiedzi.
 
