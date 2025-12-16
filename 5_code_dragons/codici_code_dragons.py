'''Flusso dei Frammenti
Ti intrufoli nella Cittadella Velata: sacche di numeri sono rovesciate ovunque. Ricomponi il bottino in un'unica borsa usando `sum_list(nums)`, che somma tutti gli interi in `nums`; se `nums` è vuota, torna `0`. Mantieni la firma esatta e supera ogni test come fossero grate che si alzano.'''
def sum_list(nums: list[int]) -> int:
    somma = 0
    if nums == []:
        return 0
    else:
        for numeri in nums:
            somma += numeri
        return somma
    

'''Picco della Lista

Nella sala del tributo devi individuare la gemma più preziosa tra mucchi disordinati: usa `max_or_none(nums)` per ottenere il valore più alto, oppure `None` se il sacco è vuoto. Mantieni la firma e non far scattare i test-trappola.'''
def max_or_none(nums: list[int]) -> int | None:
    if nums == []:
        return None
    valoreMassimo:int = nums[0]
    for numeri in nums:
        if numeri > valoreMassimo:
            valoreMassimo = numeri
    return valoreMassimo


'''Eco delle Tracce

Nel corridoio successivo le trappole scattano sui duplicati: lascia passare solo le prime impronte usando `dedup_stable(nums)`, che restituisce una nuova lista con la prima comparsa di ogni valore in ordine. Mantieni la firma e scivola oltre i test.'''
def dedup_stable(nums: list[int]) -> list[int]:
    if nums == []:
        return nums
    nums2:list[int] = [nums[0]]

    for numeri in nums:
        if numeri != nums2[-1]:
            nums2.append(numeri)
    return nums2


'''Segmenti Rituali
La camera delle scorte vuole sacche di dimensione fissa. Organizza i pacchi con `chunk(lst, size)`, che divide `lst` in blocchi di `size` (l'ultimo può essere più corto). Mantieni la firma e non allarmare i test.'''
def chunk(lst: list[int], size: int) -> list[list[int]]:
    if lst == []:
        return lst
    
    risultato: list[list[int]] = []
    blocco: list[int] = []   
    for num in lst:
        blocco.append(num)          
        if len(blocco) == size:    
            risultato.append(blocco) 
            blocco = []             
    if blocco:                    
        risultato.append(blocco)
    return risultato
print(chunk([1,2,3,4,5,6,7,8,9,10], 4))


'''Trama Lineare
Prima di fuggire dal magazzino riversa ogni bottino in una singola pila pronta al trasferimento. Fallo con `flatten_once(nested)`, appiattendo di un livello una lista di liste. Mantieni la firma e supera i test come un'uscita pulita.'''
def flatten_once(nested: list[list[int]]) -> list[int]:
    if nested == []:
        return nested
    
    lista_nuova:list[int] = []
    for liste in nested:
        for num in liste:
            lista_nuova.append(num)
    return lista_nuova
print(flatten_once([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]))


'''Sigillo Cercato
Al mercato nero ottieni sempre ciò che cerchi: se il banco è vuoto, usa il ricambio. Fallo con `get_or_default(d, k, default)`, che torna il valore se c'è, altrimenti `default`, senza toccare `d`. Mantieni la firma e sfila tra i test.'''
def get_or_default(d: dict, k, default=None):
    if k in d:
        return d[k]
    return default
    

'''Atlante Fuso
Due mappe del palazzo vanno fuse: per ogni stanza tieni il tracciato più aggiornato. Usa `merge_overwrite(a, b)` per creare un nuovo dizionario con `b` che prevale su `a`. Mantieni la firma e scardina i test.'''
def merge_overwrite(a: dict, b: dict) -> dict:
    for k in b:
        a[k] = b[k]

    return a


'''Alleanze Invertite
Per passare inosservato usi codici invertiti: nessun simbolo deve andare perduto. Attua `invert_unique(d)` per scambiare chiavi e valori (valori univoci). Mantieni la firma e svanisci tra i test.'''
def invert_unique(d: dict) -> dict:
    nuovo_d:dict = {}
    for key, value in d.items():
        nuovo_d[value] = key
    return nuovo_d


'''Pioggia di Lettere
Lettere segrete cadono sul mantello: conta solo i messaggi reali, ignora i sigilli rotti. Usa `letter_count(text)` per mappare frequenze delle sole lettere minuscole, scartando il resto. Mantieni la firma e scavalca i test.'''
def letter_count(text: str) -> dict[str, int]:
    solo_minuscole: list[str] = []
    for char in text:
        if char.isalpha():
            solo_minuscole.append(char.lower())

    dizionario: dict[str, int] = {}
    for char in solo_minuscole:
        if char in dizionario:
            dizionario[char] += 1
        else:
            dizionario[char] = 1

    return dizionario


'''Bastone dei Sentieri
Una guida ti mostra percorsi annidati: seguili uno a uno e, se manca un passaggio, attiva il piano di riserva. Realizza `deep_get(d, path, default)` percorrendo `path` tra dizionari e liste `d`; restituisci il percorso ma, se fallisce, torna `default`. Mantieni la firma e scansa le trappole-test.'''
def deep_get(d: dict | list, path: list, default=None):
    for step in path:
        if isinstance(d, dict):
            if step in d:
                d = d[step]
            else:
                return default
        elif isinstance(d, list):
            if isinstance(step, int) and 0 <= step < len(d):
                d = d[step]
            else:
                return default
        else:
            return default
    
    return d


'''Censimento delle Essenze
Gli informatori vogliono sapere quanti contatti sono davvero diversi, senza doppioni. Rispondi con `unique_count(nums)`: torna la quantità di interi distinti in `nums`. Mantieni la firma e passa i test senza farti notare.'''
def unique_count(nums: list[int]) -> int:
    lista_nuova: list[int] = []
    for elemento in nums:
        if elemento not in lista_nuova:
            lista_nuova.append(elemento)
    return len(lista_nuova)


'''Cristalli Condivisi
Due inventari rubati contengono beni in comune: servono solo quelli condivisi. Implementa `intersection_sorted(a, b)` restituendo gli elementi comuni ai due elenchi, **ordinati** e senza ripetizioni. Mantieni la firma e scivola tra i test.'''
def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []
    for num in a:
        if num in b and num not in c:
            c.append(num)
    return sorted(c)


'''Scintille Divergenti
Per confondere gli inseguitori, tieni ciò che appartiene a un solo inventario. Implementa `symdiff_sorted(a, b)` per restituire gli interi presenti in una sola delle due liste, ordinati e senza duplicati. Mantieni la firma e supera i test.'''
def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []
    for num_a in a:
        if num_a not in b and num_a not in c:
            c.append(num_a)
    for num_b in b:
        if num_b not in a and num_b not in c:
            c.append(num_b)
    return sorted(c)


'''Parole Gemelle
Sul muro compaiono due messaggi cifrati: sono lo stesso anagramma? Risolvi con `are_anagrams(a, b)`, ignorando spazi e differenze di maiuscole/minuscole; ritorna `True` o `False`. Mantieni la firma e non allertare i test.'''
def are_anagrams(a: str, b: str) -> bool:
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


'''Futuri Possibili
Osservi un lotto di chiavi rubate: in quante combinazioni potresti usarle? Rispondi con `powerset_size(n)`, che ritorna la quantità di sottoinsiemi di un set di `n` elementi. Mantieni la firma e passa i test.'''
def powerset_size(n: int) -> int:
    risultato = 2**n
    return risultato


'''Sigillo dell'Addizione
Nel laboratorio dei gadget un trucco rapido unisce due valori senza lasciare tracce: fanne uso con `add(x, y)`, che deve tornare la somma dei due argomenti. Mantieni la firma e scivola oltre i test.'''
def add(x, y):
    somma = x+y
    return somma


'''Rimbalzo Arcano
Per le serrature ostinate ti serve ripetere la stessa mossa due volte: esegui `apply_twice(fn, x)` applicando `fn` a `x` due volte e tornando il risultato. Mantieni la firma e non far scattare i test-trappola.'''
def apply_twice(fn, x):
    return fn(fn(x))


'''Canale Intrecciato
Per la tua trappola servono due stadi: il secondo prepara, il primo neutralizza. Compila `compose(f, g)` in modo che la funzione restituita, data `x`, esegua prima `g(x)` e poi `f(...)`. Mantieni la firma e scivola tra i test.'''
def compose(f, g):
    def h(x):
        return f(g(x))
    return h
# Esempio di utilizzo:
def f(x):
    return x + 1
def g(x):
    return x * 2
h = compose(f, g)
print(h(5))


'''Vincolo della Costante
Ti serve una polvere pronta all'uso che aggiunga sempre lo stesso spostamento a ogni cifra rubata: prepara `curry_add(n)` così da restituire una funzione che somma `n` all'input. Mantieni la firma e non allertare i test.'''
def curry_add(n):
    def spostamento(x):
        return x + n
    return spostamento
add3 = curry_add(3)
print(add3(4))   # stampa 7
add_minus2 = curry_add(-2)
print(add_minus2(10))  # stampa 8


'''Labirinto di Fibonacci
Per depistare gli inseguitori studi la sequenza di Fibonacci, ma memorizzando ogni tratto già percorso: realizza `fib_memo(n)` così da calcolare il valore richiesto evitando ricalcoli inutili. Mantieni la firma e scivola oltre i test.'''
def fib_memo(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


'''Ponte delle Spirali
Nelle catacombe conti i gradini fino al nascondiglio: usa `range_sum(n)` per sommare tutti i numeri da `1` a `n`; se `n` ≤ `0`, restituisci `0`. Mantieni la firma e scivola oltre i test senza far rumore.'''
def range_sum(n: int) -> int:
    somma = 0
    if n <= 0:
        return 0
    else:
        somma = sum(range(1, n+1))
        return somma
    

'''Torce Pari
Nel perimetro vedi sentinelle a distanza regolare: calcola quante occupano posizioni pari con `count_even(nums)`, che conta gli interi **pari** nella lista (incluso `0`). Mantieni la firma e supera i test senza allarmi.'''
def count_even(nums: list[int]) -> int:
    countPari = 0
    for n in nums:
        if n % 2 == 0:
            countPari += 1
    return countPari


'''Tamburo dei Multipli
Per sfuggire ai guardiani devi seguire i passi marcati 3 o 5: realizza `sum_multiples(limit)` sommando tutti i valori **< limit** divisibili per `3` o `5`; per `limit` ≤ `0`, restituisci `0`. Mantieni la firma e scivola tra i test.'''
def sum_multiples(limit: int) -> int:
    somma:int = 0
    if limit <= 0:
        return 0
    for numero in range(1, limit):
        if numero % 3 == 0 or numero % 5 == 0:
            somma += numero
    return somma


'''Fessure Prime
Le casseforti richiedono chiavi prime in sequenza: usa `primes_up_to(n)` per produrre tutti i primi **≤ n** ordinati; se non ce ne sono (`n` < `2`), restituisci `[]`. Mantieni la firma e supera i test.'''
def primes_up_to(n: int) -> list[int]:
    listaPrimi: list[int] = []
    for num in range(2, n + 1):
        numeroPrimo = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                numeroPrimo = False
                break
        if numeroPrimo:
            listaPrimi.append(num)
    return listaPrimi


'''Melodia Compressa
Per inviare messaggi sicuri, comprimi le sequenze senza ridondanza: realizza `rle(s)` che produce `[(char, n), ...]` raggruppando caratteri consecutivi; per stringa vuota, `[]`. Mantieni la firma e passa i test.'''
def rle(s: str) -> list[tuple[str,int]]:
    if not s:
        return []
    listaNuova = []
    count = 1
    prev = s[0]
    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            listaNuova.append((prev, count))
            prev = char
            count = 1
    listaNuova.append((prev, count))
    return listaNuova
print(rle("aaabbcaaa"))  # [('a', 3), ('b', 2), ('c', 1), ('a', 3)]
print(rle(""))           # []


'''Sala dell'Equilibrio
All’ingresso segreto, ogni passo è pesato: arretri, resti fermo o avanzi? Decidilo con `sign(n)`, tornando `-1` per numeri negativi, `0` per `0`, `1` per positivi. Mantieni la firma e scivola oltre i test.'''
def sign(n: int) -> int:
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1
    

'''Rotoli dei Giudici
Il Maestro delle Maschere pretende ranghi chiari. Classifica con `grade(score)`: `A` se `>= 90`, poi `B` `>= 80`, `C` `>= 70`, `D` `>= 60`, altrimenti `F`. Mantieni la firma e non far scattare i test-trappola.'''
def grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    

'''Fontana di Mercurio
Un patto ti chiede una quota solo se il rischio non è zero. Implementa `safe_div(a, b, default=None)`: torna `default` se `b` è `0`, altrimenti il quoziente `a/b` in **float**. Mantieni la firma e scivola tra i test.'''
def safe_div(a: float, b: float, default=None):
    if b == 0:
        return default
    quoziente: float = a / b
    return quoziente


''''''