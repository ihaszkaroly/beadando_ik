# Python Projekt: Mini Rajzoló

Ihász Károly | FKHSEP

## Feladat leírása

A program egy egyszerű rajzoló alkalmazás, amely a `tkinter` grafikus könyvtárat használja. Lehetővé teszi a felhasználó számára, hogy:
* Szabadkézzel rajzoljon a vászonra.
* Színt válasszon egy színválasztó palettáról.
* Véletlenszerű színt generáljon egy gombnyomásra.
* Beállítsa az ecset méretét.
* Letörölje a vásznat.
* Rendszerinformációkat jelenítsen meg az `os` modul segítségével.

## Használt modulok és függvények

### 1. Tanult modulok

* **`tkinter`**: A grafikus felület (GUI) alapja.
    * `Tk`: A fő ablak létrehozása.
    * `Frame`: Konténer a vezérlőgombok számára.
    * `Button`: Interaktív gombok (Szín, Törlés, Info, stb.).
    * `Canvas`: A rajzolási felület.
    * `simpledialog.askinteger`: Dialógusablak az ecsetméret bekéréséhez.
    * Konstansok: `TOP`, `LEFT`, `X`, `BOTH`, `SUNKEN`, `ROUND`, `TRUE`.
* **`tkinter.colorchooser`**:
    * `askcolor`: Rendszer-specifikus színválasztó ablak megnyitása.
* **`tkinter.messagebox`**:
    * `showinfo`: Információs ablak megjelenítése.
* **`random`**:
    * `randint`: Véletlen egész szám generálása (a véletlen színhez).

### 2. Bemutatandó modul

* **`os`**: Operációs rendszerrel kapcsolatos funkciók.
    * `getcwd()`: Visszaadja az aktuális munkakönyvtár elérési útját.
    * `cpu_count()`: Visszaadja a rendszerben lévő CPU magok számát.
    * `path.basename(__file__)`: Visszaadja a futtatott szkriptfájl nevét.

### 3. Saját modul

* **`projekt_IK.py`**: ebben van benne.

## Osztály(ok)

* **`RajzoloApp_IK`**:
    * Ez a saját osztály.
    * Ez felel az alkalmazás teljes felépítéséért, a grafikus elemek (widgetek) létrehozásáért és az eseménykezelés (egérkattintás, egérmozgatás, gombnyomások) lekezeléséért.

## Saját függvény(ek)

* **`get_random_color_IK`**:
    * Ez a saját függvény.
    * A `random` modul segítségével generál egy véletlenszerű hexadecimális színkódot (pl. `#ff0033`).
