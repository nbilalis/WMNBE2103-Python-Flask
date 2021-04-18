name: common
layout: true
class: common

.logo-sae[![SAE Logo](img/logo-sae.png)]
.logo-web[![WEB logo](img/logo-web.png)]

.ruler.one[· · · · · · · ·]
.ruler.two[· · · · · · · ·]
.ruler.three[· · · · · · · ·]
.ruler.four[· · · · · · · ·]
.ruler.five[· · · · · · · ·]
.ruler.six[· · · · · · · ·]
.ruler.seven[· · · · · · · ·]

.footer[Nikos Bilalis - n.bilalis@sae.edu]

---
name: cover
layout: true
template: common
class: cover

---
name: section
layout: true
template: common
class: section, center, middle

---
name: section-details
layout: true
template: common
class: section-details, topbar-space

---
name: chapter
layout: true
template: common
class: chapter, topbar-space

---
name: list
layout: true
template: common
class: list, topbar-space

---
template: cover

## WMNBE2013 | BACK-END DEVELOPMENT

# Python #3

### Control | Sequences | Functions

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- Control statements
  - Conditiοnals
  - Loops
- Sequences
  - `list`
  - `tuple`
  - `dict`
- Functions

---
template: section

![](https://i.imgflip.com/561kk6.jpg)

---
template: section

## Control Statements

---
layout: true
template: chapter

### Control Statements

---

#### `off-side` rule

Όπως έχει ήδη αναφερθεί, η `Python` χρησιμοποιεί τον κανόνα `off-side`. Άρα, για τη σύνταξη των `blocks` λαμβάνεται υπόψη το `indentation`, η στοίχιση των εντολών.

Αντί για τη χρήση ειδικών χαρακτήρων (π.χ. curly brackets) ή συγκεκριμένων keywords (π.χ. begin, end) ο ορισμός των `blocks` γίνεται με τα κενά στην αρχή της γραμμής.

Δύο διαδοχικές γραμμές που είναι "στοιχισμένες" βρίσκονται στο ίδιο `block`. Μία εντολή που βρίσκεται στοιχισμένη πιο δεξιά από την προηγούμενή της, ανήκει στο `block` αυτής της εντολής.

---

#### `if`…`elif`…`else`

Η μοναδική εντολή επιλογής/απόφασης στην `Python` είναι η εντολή `if elif else`.

Απουσιάζει, δηλαδή, εντολή αντίστοιχη μιας `switch`, τουλάχιστον μέχρι την έκδοση _3.9_.

---
layout: true
template: chapter

### `if`…`elif`…`else`

---

#### Σύνταξη

```python
if <condition>:
    <statements>
elif <condition>:
    <statements>
…
else:
    <statements>

```

Τα τμήματα `elif` και `else` είναι προαιρετικά. Μπορούν να υπάρχουν περισσότερα από ένα τμήματα `elif`.

---

#### Λειτουργία

Αν ισχύει η συνθήκη (λογική έκφραση) στην πρώτη γραμμή της `if` εκτελούνται οι εντολές του πρώτου `block`.

Διαφορετικά, εξετάζονται (αν υπάρχουν) οι επόμενες συνθήκες διαδοχικά και εκτελούνται οι εντολές του πρώτου (στη σειρά) `block` για το οποίο ικανοποιείται η αντίστοιχη συνθήκη.

Αν καμία συνθήκη δεν ικανοποιείται, εκτελούνται οι εντολές του `block` `else` (αν υπάρχει).

---

#### Παράδειγμα #1

```python
username = input('Enter your username: ')

if username == 'admin':
    print('Welcome admin!')

```

---

#### Παράδειγμα #2

```python
age = input('Enter your age: ')

if age >= 18:
    print('You may enter!')
else:
    print('Please leave.')

```

---

#### Παράδειγμα #2

```python
grade = input('Enter your grade: ')

if grade >= 18:
    print('Congrats!')
elif grade >= 16:
    print('You did well')
elif grade >= 14:
    print('Good for you')
elif grade >= 10:
    print('You should try a bit harder!')
else:
    print('You shall not pass!')

```

---

#### Shorthands

Αν έχουμε μία μόνο εντολή στο `block`

```python
if x > 0: print('Θετικός αριθμός')

```

Αν έχουμε και τμήμα `else`

```python
print('Θετικός') if x > 0 else print('Μη θετικός')

# Conditional expression (Ternary operator?)
print('Θετικός' if x > 0 else 'Μη θετικός')

```

---
template: section

## Loops

---
layout: true
template: chapter
name: loops

### Loops

---

#### `while`…`else`

Η λειτουργία της εντολής `while` στην `Python` είναι η αναμενόμενη… but with a small twist.

#### Σύνταξη

```python
while <condition>:
    <statements>
else:
    <statements>

```

---
layout: true
template: chapter

### `while`…`else`

---

#### Λειτουργία

Όσο ισχύει η συνθήκη (λογική έκφραση) εκτελούνται οι εντολές στο `block` της `while`.

Αν _δεν διακοπεί_ η επαναλαμβανόμενη λειτουργία της `while` με άλλο τρόπο (πέραν της συνθήκης), θα εκτελεστούν στο τέλος και οι εντολές του `block` `else`.

---

#### Παράδειγμα

Εμφάνισε τους αριθμούς από το _1_ μέχρι και το _10_:

```python
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
else:
    print('\n')

```

---

#### Εντολές `break` & `continue`

Η μόνη περίπτωση να διακοπεί η λειτουργία μιας `while`, πριν η συνθήκη της γίνει `False`, είναι να υπάρχει στο σώμα της μια εντολή `break`.

Η εντολή `break` διακόπει τη λειτουργία της πιο "κοντινής" `while` (ή `for`). Επίσης, δεν ενεργοποιείται το τμήμα `else`.

Η εντολή `continue` μεταφέρει άμεσα τον έλεγχο πίσω στη γραμμή της `while`. Αν ισχύει ακόμα η συνθήκη της ξεκινά η "επόμενη" επανάληψη.

---

#### Παράδειγμα #1

Αναζήτηση του χαρακτήρα _ñ_ μέσα σε μια συμβολοσειρά:

```python
i = 0
s = 'My name is Iñigo Montoya'
while i < len(s):
    if (s[i] == 'ñ'):
        print('Found at pos:', i)
        break;
    i += 1
else:
    print('Not found')

```

---

#### Παράδειγμα #2

Εμφάνισε τους αριθμούς από το _1_ μέχρι και το _100_, εκτός των πολλαπλάσιων του _7_:

```python
i = 0
while i < 100:
    i += 1
    if (i % 7 == 0): continue
    print(i)

```

---

#### Assignment expressions / the walrus operator `:=`

Ο τελεστής _walrus_ κάνει ανάθεση τιμής και επιστρέφει παράλληλα την τιμή αυτή, ως έκφραση.

Η χρήση του μας οδηγεί, σε αρκετές περιπτώσεις, σε αρκετά πιο συνοπτικό κώδικα.

```python
list = []
while (x := int(input('Enter number: '))) != 0:
    if x < 0:
        continue
    list += [x]     # l.append(x)

print(list)

```

---
template: loops

#### `for`…`else`

Η εντολή `for` στην `Python` είναι διαφορετική από μία κλασική `for` μιας κάποιας άλλης γλώσσας.

Θυμίζει περισσότερο τις εντολές / συναρτήσεις `foreach`, `for`…`in`, `for`…`of`, `forEach` άλλων γλωσσών.

Και εδώ, όπως και στην `while`, υπάρχει το τμήμα `else`, με την ίδια λειτουργία.

---
layout: true
template: chapter
name: for

### `for`…`else`

---

#### Σύνταξη

```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>

```

, όπου `sequence` μια ακολουθία στοιχείων, όπως `range`, `list`, `tuple`, `dict`<sup>*</sup>, `set`, `string`.

---

#### Λειτουργία

Εκτελείται μια επανάληψη για κάθε ένα από τα στοιχεία της δεδομένης ακολουθίας στοιχείων.

Το στοιχείο αυτό είναι διαθέσιμο μέσω της μεταβλητής που δηλώθηκε.

Αν η εντολή `for` δεν διακοπεί πρόωρα (μέσω μιας `break`), θα εκτελεστεί και το τμήμα `else`.

---

#### Παράδειγμα #1

Εμφάνισε τα γράμματα μίας λέξης και τις λέξεις μιας φράσης:

```python
for char in 'Montoya':
    print(char)

for word in 'My name is Iñigo Montoya'.split(' '):
    print(word)

```

---

#### Παράδειγμα #2

Αναζήτηση του χαρακτήρα _ñ_ μέσα σε μια συμβολοσειρά:

```python
for char in 'My name is Iñigo Montoya':
    if char == 'ñ':
        print('Found!')
        break
else:
    print('Not found…')

```

---
layout: true
template: for

#### Συνάρτηση `range`

---

Για να λειτουργήσει η `for` με έναν πιο "παραδοσιακό" τρόπο, δηλαδή με μια ακολουθία ακέραιων αριθμών, μπορεί να χρησιμοποιηθεί η συνάρτηση `range`, η οποία παράγει την απαιτούμενη ακολουθία.

---

Αν δοθεί ένα όρισμα _stop_, τότε παράγεται μια ακολουθία αριθμών από το _0_ μέχρι το _stop-1_.

```python
# 10 iterations
# prints numbers between 0 and 9

for i in range(10):
    print(i)

```

---

Αν δοθούν δύο ορίσματα _start_ & _stop_, τότε παράγεται μια ακολουθία αριθμών από το _start_ μέχρι το _stop-1_.

```python
# 5 iterations (10 - 5)
# prints numbers between 5 and 9

for i in range(5, 10):
    print(i)

```

---

Αν δοθεί τιμή και για το όρισμα _step_, τότε δύο διαδοχικοί αριθμοί της ακολουθίας διαφέρουν κατά _step_.

```python
# prints numbers 10, 13, 16, 19

for i in range(10, 20, 3):
    print(i)

```

Όλα τα ορίσματα μπορεί να είναι και αρνητικοί ακέραιοι, αριθμοί. Αν το όρισμα _step_ δε "συμφωνεί" με τα _start_ και _stop_, η ακολουθία θα είναι κενή.

Η τιμή _0_ για το όρισμα _step_ δεν είναι αποδεκτή.

---
layout: true
template: chapter
name: sequences

### Sequences

---

#### `list`

Στην `Python` δεν υπάρχουν πίνακες. Η δομή που προσφέρει η `Python` στη θέση τους είναι η λίστα (`list`).

Η λίστα είναι μία δυναμική δομή δεδομένων και αναπαριστά μια ακολουθία διατεταγμένων στοιχείων, τα οποία μπορούν να προσπελαστούν μέσω κάποιου δείκτη.

Τα στοιχεία δεν είναι απαραίτητα του ίδιου τύπου.

---
layout: true
template: chapter

### `list`

---

#### Δήλωση / Αρχικοποίηση

```python
>>> l1 = []             # empty list
>>> l1 = list()         # empty list
>>> l3 = [1, 2, 3]
>>> l3
[1, 2, 3]
>>> l4 = list('Python')
>>> l4
['P', 'y', 't', 'h', 'o', 'n']

```

---

#### Προσπέλαση

```python
>>> l = [1, 2, 4]
>>> l[0]
1
>>> l[2] = 3
>>> l
[1, 2, 3]

```

---

#### Τελεστές

##### `*` για επανάληψη στοιχείου / στοιχείων

```python
>>> l = [0] * 5
>>> l
[0, 0, 0, 0, 0]

```

##### `+` (`+=`) για προσάρτηση στοιχείων

```python
>>> l = [1, 2]
>>> l += [3, 4]
>>> l
[1, 2, 3, 4]

```

---

#### Μήκος λίστας / πλήθος στοιχείων

```python
>>> l = [1, 2]
>>> len(l)
2
>>> l += [3]
>>> len(l)
3

```

---

#### Slice Notation

Η `Python` έχει ένα μοναδικό τρόπο για να αναφερθεί σε κομμάτι μίας λίστας.

```python
list[start:stop:end]

```

Επιστρέφει τμήμα της λίστας, το οποίο ξεκινά από τη θέση _start_ και σταματά στο στοιχείο **πριν** τη θέση _stop_, με βήμα _step_.

Η σύνταξη αυτή μπορεί να χρησιμοποιηθεί είτε για ανάκτηση, είτε, ακόμα, και για "αντικατάσταση" ενός τμήματος λίστας.

---

#### Παράδειγμα

```python
>>> l = [1, 2, 3, 4, 5]
>>> l[1:]               # all but first
[2, 3, 4, 5]
>>> l[:len(l)-1]        # all but last
[1, 2, 3, 4]
>>> l[1:4]
[2, 3, 4]
>>> l[::-1]             # reverse
[5, 4, 3, 2, 1]
>>> copy = l[:]         # copy

```

---
class: long-text

#### Συναρτήσεις

| Συνάρτηση | Λειτουργία |  |
| :-- | :-- | :-- |
| `.append(x)` | προσθήκη του `x` στο τέλος της λίστας | `a[len(a):] = [x]` |
| `.extend(l)` | προσάρτηση των στοιχείων της λίστας `l` | `a[len(a):] = l` |
| `.insert(i,x)` | εισαγωγή του `x` στη θέση `i` | |
| `.remove(x)` | διαγραφή της πρώτης εμφάνισης του `x` | πιθανό `ValueError` |
| `.pop(i)` | αφαίρεση/ανάκτηση από τη θέση `i` | default `i=len(a)-1` |
| `.index(x)` | η θέση του στοιχείου `x` | πιθανό `ValueError` |
| `.count(x)` | πόσες φορές εμφανίζεται το `x` |
| `.sort()` | ταξινόμηση των στοιχείων |
| `.reverse()` | αντιστροφή των στοιχείων |

---
template: sequences

#### `tuple`

Εναλλακτικά της λίστας, μπορεί να χρησιμοποιηθεί μία πλειάδα.

Η πλειάδα χρησιμοποιείται για αμετάβλητες ακολουθίες συγκεκριμένου μήκους, καθώς η πλειάδα είναι μία _immutable_ δομή δεδομένων, όπως και η συμβολοσειρά.

Ως εκ τούτου, μετά τη δήλωσή τους, δεν μπορούν να προστεθούν, αφαιρεθούν ή αντικατασταθούν στοιχεία.

---
layout: true
template: chapter

### `tuple`

---

#### Δήλωση

Η δήλωση τους γίνεται με τη χρήση των παρενθέσεων, ή και χωρίς αυτές, και με την παράθεση των στοιχείων χωρισμένα με κόμμα.

```python
t1 = (1, 2)
t2 = 3, 4
print(type(t1), type(t2)) # <class 'tuple'> <class 'tuple'>

```

---

#### Προσπέλαση

Η ανάκτηση των δεδομένων γίνεται όμοια με τις λίστες. Τροποποίηση, όπως ειπώθηκε, δεν μπορεί να γίνει.

```python
>>> t = ('Monty', 'Python', 'and', 'the', 'Holy', 'Grail')
>>> t[0]
Monty
>>> t[4:]
('Holy', 'Grail')
>>> a, b = t[:2]
>>> a
Monty
>>> b
Python

```

---

#### Αντιμετάθεση

Η χρήση των `tuple` μας δίνει και έναν πρωτότυπο τρόπο για να κάνουμε αντιμετάθεση δύο μεταβλητών, _the Pythonic way_.

```python
>>> x = 7
>>> y = 4
>>> x, y = y, x
>>> x
4
>>> y
7

```

---

#### `enumerate`

Σε μία τυπική χρήση της εντολής `for` στην `Python`, δεν έχουμε κάποιον μετρητή ώστε να γνωρίζουμε σε ποια επανάληψη (_iteration_) βρισκόμαστε.

Αυτό μπορεί να λυθεί με τη συνάρτηση `enumerate`.

Η `enumerate` δέχεται μία ακολουθία στοιχείων και επιστρέφει μία ακολουθία πλειάδων, όπου το πρώτο στοιχείο (κάθε&nbsp;πλειάδας) είναι το _index_ (το οποίο ξεκινά από την τιμή _start_) και το δεύτερο το αρχικό στοιχείο της ακολουθίας.

```python
enumerate(seq, start)
```

---

#### `enumerate`

```python
>>> list(enumerate(list('Python')))
[(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]

```

```python
grades = [17, 18, 20, 19]
for i, x in enumerate(grades, 1):
    print(f'Grade {i}: {x}')

```

---
template: sequences

#### `dict`

Μία ακόμα, πολύ χρήσιμη, δομή δεδομένων είναι τα λεξικά (_dictionaries_). Στα λεξικά αποθηκεύουμε _key-value pairs_.

Σε αντίθεση με τις λίστες, η αναφορά στα στοιχεία ενός λεξικού γίνεται με ένα _κλειδί_ και όχι με τη θέση.

Παλαιότερα τα λεξικά δεν αποτελούνται από διατεταγμένα στοιχεία, αλλά αυτό άλλαξε μετά την έκδοση _3.6_.

Αυτό σημαίνει πως μπορώ να ανακτήσω τα περιεχόμενα του λεξικού σειριακά, γνωρίζοντας ότι αυτά διατηρούν τη σειρά με την οποία δηλώθηκαν / τοποθετήθηκαν.

---
layout: true
template: chapter

### `dict`

---

#### Δήλωση / Αρχικοποίηση

```python
>>> d1 = {}             # empty dict
>>> d2 = dict()         # empty dict
>>> d3 = {
    'brand': 'Tesla',
    'model': 'Model S',
    '0-60': 2.1
}

```

---

#### Προσπέλαση

```python
…
>>> len(d3)
3
>>> d3['brand']
Tesla
>>> for key in d3:
        print(key, d3[key])
brand Tesla
model Model S
0-60 2.1

```

**Προσοχή**: όταν χρησιμοποιείται `dict` σε εντολή `for`, οι τιμές που παίρνει η μεταβλητή της `for` προκύπτουν από τα _keys_ και όχι από τα _values_.

---

#### Μέθοδος `.items()`

Ανάκτηση των στοιχείων του λεξικού ως πλειάδες.

```python
…
>>> for key, value in d3.items():
        print(key, value)
brand Tesla
model Model S
0-60 2.1

```

---

#### Μέθοδος `.keys()`

Ανάκτηση μόνο των κλειδιών.

```python
…
>>> for key in d3.keys():
        print(key, value)
brand
model
0-60

```

**Σημείωση**: Σε μία `for` η χρήση της μεθόδου `.keys()` δεν είναι ιδιαίτερα χρήσιμη, καθώς και χωρίς αυτή, η μεταβλητή της `for` θα πάρει τιμές από τα κλειδιά του λεξικού.

---

#### Μέθοδος `.values()`

Ανάκτηση μόνο των τιμών.

```python
…
>>> for value in d3.values():
        print(key, value)
Tesla
Model S
2.1

```

---
template: sequences

#### Τελεστής `in`

Ένας χρήσιμος τελεστής για όλες τις προαναφερθείσες δομές δεδομένων είναι ο τελεστής `in`.

Εξετάζει αν υπάρχει ή όχι ένα στοιχείο στη δομή και έχεις ως αποτέλεσμα `True` / `False`, αντίστοιχα.

```python
>>> 3 in [1, 2, 3]
True
>>> 6 in (4, 5)
False
>>> '001' in { '001': 'Python' }
True
>>> 'Python' in { '001': 'Python' }
False

```

---
template: section

## Functions

---
layout: true
template: chapter

### Functions

---

#### Ορισμός / Κλήση

Για τον ορισμό _custom_ συναρτήσεων, στην `Python`, χρησιμοποιούμε το _keyword_ `def`. Το σώμα της συνάρτησης ορίζεται, όπως και κάθε _block_ στην `Python`, μέσω του _indentation_.

Η κλήση γίνεται απλά με το όνομα της συνάρτησης, συνοδευόμενο από παρενθέσεις.

```python
def hello_world():
    print('Hello world!')


hello_world()
hello_world()

```

---

#### Πέρασμα τιμών

Το πέρασμα τιμών σε μια συνάρτηση γίνεται μέσω παραμέτρων.

Οι παράμετροι αυτές ορίζονται μέσα στις παρενθέσεις στη δήλωση της συνάρτησης και μπορεί να είναι και προαιρετικές (_optional_), αρκεί να τους ορίσουμε προεπιλεγμένες (_default_) τιμές.

Για την επιστροφή τιμής (ή και τιμών), από τη συνάρτηση, χρησιμοποιείται η εντολή `return`.

```Python
def min(a, b=0):
    return a if a < b else b

```

---

#### Παράδειγμα #1

```python
def minmax(list):
    min = max = list[0]

    for x in list[1:]:
        if x < min:
            min = x
        if x > max:
            max = x

    return min, max


res = minmax([3, 7, 4, 9, 6])

print(res, type(res))

```

---

#### Παράδειγμα #2

```python
def greet(name, msg="Hello"):
    print(f'{msg} {name}!')


greet('Alice')          # Hello Alice!
greet('Bob', 'Howdy')   # Howdy Bob!

```

---
template: section

## Homework

---
template: chapter

### Homework 1

Γράψτε μία συνάρτηση σε `Python`, η οποία να ζητά την ακτίνα ενός κύκλου και να επιστρέφει την περίμετρο και το εμβαδόν του, ως `tuple`.

> _Περίμετρος_: circumference = 2· π· R
>
> _Εμβαδόν_: area = π· R<sup>2</sup>

---
template: chapter

### Homework 2

Σε κάποιο σύστημα τα ποσά εμφανίζονται σε λάθος μορφή, λόγω κάποιου software bug. Γράψτε μία συνάρτηση σε `Python` η οποία να μετατρέπει ένα ποσό, από τη μορφή `$12,345.67` στη μορφή `€12.345,67`, με τα εξής βήματα:

1. να αφαιρεί τυχόν κενά από την αρχή και το τέλος του `string`
1. να αντικαθιστά την `.` με `,` και το ανάποδο (προσοχή, είναι λίγο δυσκολότερο από ότι φαίνεται αρχικά).
1. να αντικαθιστά το `$` με `€`.
1. να επιστρέφει τη "διορθωμένη" τιμή

---
template: chapter

### Homework 3

Γράψτε μία συνάρτηση σε `Python`, η οποία να δέχεται μία φράση και να εμφανίζει μία μία τις λέξεις της φράσης αυτής.

```python
>>> words('The Life of Brian')
The
Life
of
Brian

```

---
template: list

### Χρήσιμα links

- ![](https://www.google.com/s2/favicons?domain=docs.python.org) 4. More Control Flow Tools — Python 3.9.4 documentation https://docs.python.org/3/tutorial/controlflow.html#the-range-function
- ![](https://www.google.com/s2/favicons?domain=docs.python.org) 5. Data Structures — Python 3.9.4 documentation https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- ![](https://www.google.com/s2/favicons?domain=www.python.org) PEP 8 -- Style Guide for Python Code | Python.org https://www.python.org/dev/peps/pep-0008/
- ![](https://www.google.com/s2/favicons?domain=realpython.com) How to Write Beautiful Python Code With PEP 8 – Real Python https://realpython.com/python-pep8/#tabs-vs-spaces

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - Is there a built-in or more Pythonic way to try to parse a string to an integer - Stack Overflow https://stackoverflow.com/questions/2262333/is-there-a-built-in-or-more-pythonic-way-to-try-to-parse-a-string-to-an-integer
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - What is Truthy and Falsy? How is it different from True and False? - Stack Overflow https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false/39984051#39984051
- ![](https://www.google.com/s2/favicons?domain=hackaday.com) Python Will Soon Support Switch Statements | Hackaday https://hackaday.com/2021/04/02/python-will-soon-support-switch-statements/
- ![](https://www.google.com/s2/favicons?domain=discuss.codecademy.com) What is the difference between sort() and sorted()? - FAQ / Python FAQ - Codecademy Forums https://discuss.codecademy.com/t/what-is-the-difference-between-sort-and-sorted/349679
- ![](https://www.google.com/s2/favicons?domain=blog.teclado.com) Destructuring in Python https://blog.teclado.com/destructuring-in-python/

---
template: section

## Thank You!

![](https://i.makeagif.com/media/6-07-2015/973yy9.gif)
