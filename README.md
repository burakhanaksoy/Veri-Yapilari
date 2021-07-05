<h1>Veri-Yapilari</h1>

<b><i>"Veri yapilari, bilgisayar biliminde cok onemli bir yere sahiptir. Bu yapilarin islevlerini bilmek, icsellestirmek ve bir yapinin otekine nazaran artilari ve eksilerini bilmek bir gelistirici icin cok onemlidir."</b></i>

<h2>Linked List</h2>

<b>Bagli liste olarak da gecer.</b> En onemli ozelligi, kendisinden once veya sonra gelen objeyi bir pointer vasitasiyla aklinda tutmasidir.

Bagli listelerin var olabilmeleri icin bir "root node"'a (baslangic dugumu) ihtiyaclari vardir. Root node'u olmayan, ya da silinen bir bagli liste uzayda kaybolur :) (cidden)

```python
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.root = Node()

    def _size(self):
        _i = 0
        cur_node = self.root

        while(cur_node.next):
            _i += 1
            cur_node = cur_node.next
        return _i

    def append(self, val):
        cur_node = self.root
        new_node = Node(val)

        while(cur_node.next):
            cur_node = cur_node.next
        cur_node.next = new_node

    def remove(self, position):
        cur_node = self.root
        prev_node = self.root
        if self._size() <= position:
            return
        for _ in range(position + 1):
            cur_node = cur_node.next
        for _ in range(position):
            prev_node = prev_node.next

        prev_node.next = cur_node.next
        cur_node.next != None

    def get(self, idx):
        cur_node = self.root
        if self._size() <= idx:
            return

        for _ in range(idx + 1):
            cur_node = cur_node.next

        return cur_node.val
```

Bu kodda bence anlasilmasi gereken en onemli nokta yaptigimiz islemlerin hemen hepsinde `cur_node = self.root` ile baslayip, bagli listeyi traverse(tariyor) ediyor olmamiz. <b>Bu da Linked list'in random-access ozelliginin olmamasindan kaynakli.</b>

- Random-access ozelliginin olmamasi, bagli liste'nin herhangi bir index'indeki elemana ulasmamiz icin O(N) zamana ihtiyacimiz oldugunu gosterir.
- Cunku N. index'deki elemana ulasmak icin kendisinden onceki N-1 index'de `cur_node.next` yapmamiz gerekir.
- Bagli olmayan bir listede ise bu karmasiklik O(1)'dir.

<p align="center">
  
<b>List</b> | Linked List
------------ | ------------
Liste elemanina ulasmak : O(1) | Liste elemanina ulasmak : O(N)
Eleman eklerken ve cikartirken hafizayi daha verimsiz kullanir, mesela 4 elemanli bir listeye 5.'yi eklemek listenin hafiza alokasyonunu iki katina cikarir, alokasyon islemi maliyetlidir | Eleman eklerken ve cikartirken hafizayi daha verimli kullanir, elemanlar birer birer eklenir ve eklenen elemanlar icin hafiza alokasyonu yapilmaz
Debug etmek daha kolaydir | Debug etmek daha zordur
kucuk data tipleri (Boolean, integer vb.) icin idealdir | kucuk data tipleri icin onerilmez cunku ekstra olarak pointer tutmak zorundadir
Dinamik olarak buyumez yada kuculmez | Dinamik olarak buyur ya da kuculur

  </p>

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/31994778/124391512-99c93580-dcf9-11eb-9b9e-bba01c8004db.png">
    </p>

---

<h2>Doubly Linked List</h2>

Bagli listelerin bir digeri de cift bagli listedir. Bu listenin ozelligi dugumlerinin kendisinden once ve sonra gelen dugumleri isaret edebiliyor olmasidir.

- Random-access ozelligi yoktur, dugumlere yine traverse ederek ulasiriz.
- Kaynaklarda yazdigi uzere sondaki dugumu silmek O(1) karmasikliga sahiptir.
- Sondaki degeri silmek haricinde linked-list'e karsi cok buyuk bir avantaji yoktur.

```python
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.next = next
        self.val = val
        self.prev = prev

    def __repr__(self):
        return f'{self.val}'


class LinkedList:

    def __init__(self):
        self.root = Node()

    def _size(self):
        _i = 0
        cur_node = self.root

        while(cur_node.next):
            _i += 1
            cur_node = cur_node.next
        return _i

    def push(self, val):
        cur_node = self.root
        new_node = Node(val)

        # get first node
        first_node = cur_node.next

        # get second node
        second_node = first_node.next

        # add new_node as the first node
        cur_node.next = new_node
        new_node.next = first_node
        first_node.prev = new_node

    def append(self, val):
        cur_node = self.root
        new_node = Node(val)

        if not cur_node.next:
            cur_node.next = new_node
            return

        while(cur_node.next):
            cur_node = cur_node.next

        cur_node.next = new_node
        new_node.prev = cur_node

    def print_list(self):
        cur_node = self.root

        print('Traverse in forward direction:')

        while(cur_node.next):
            print(cur_node.next.val, end=" ")
            cur_node = cur_node.next

        print('\nTraverse in reverse direction:')

        while(cur_node):
            print(cur_node.val, end=" ")
            cur_node = cur_node.prev
        print('')

    def remove(self, position):
        cur_node = self.root
        prev_node = self.root
        if self._size() <= position:
            return
        for _ in range(position + 1):
            cur_node = cur_node.next
        for _ in range(position):
            prev_node = prev_node.next

        prev_node.next = cur_node.next
        if cur_node.next != None:
            cur_node.next.prev = prev_node
        cur_node.next = None

    def remove_last(self):
        self.remove(self._size()-1)

    def get(self, idx):
        cur_node = self.root
        if self._size() <= idx:
            return

        for _ in range(idx + 1):
            cur_node = cur_node.next

        return cur_node.val
```
<p align="center">
    <img width="500" src="https://user-images.githubusercontent.com/31994778/124398601-35b96800-dd1f-11eb-903f-a77b04869d32.png">
    </p>
    
---

<h2>Abstract Data Tipleri</h2>

<b><i>"Abstract data tipleri, bir data tipinden cok, o data tipinin kurallarini, yapisini, icerdigi fonksiyonlari belirten bir blueprinttir diyebiliriz. ADT'nin siniri yoktur, cunku ADT array, queue, stack gibi sonlu bir sey degildir, aksine, array, queue, stack gibi data tiplerinin ortaya cikmasina vesile olan bir abstraction (soyutlama)'dir."</b></i>

Bir gelistiricinin bilmesi gereken data tipleri icinde, bagli ve cift-bagli listeden sonra, <b>stack(yigin)</b> ve <b>queue(sira)</b> veri yapilari gelir.

<h3>Stack</h3>

Turkce'ye 'yigin' olarak cevirebiliriz.

Stack'in en belirgin ozelligi LIFO(Last in first out) kurali ile calismasidir.

- Son eklenen obje, ilk cikarilan obje olur.
- En bilinen iki ozelligi pop ve push fonksiyonlaridir.
- <b>Pop</b>, yigindaki en son eklenen objeyi siler ve dondurur.
- <b>Push</b>, yigina obje ekler.
- <b>Top</b>, yigindaki en son eklenen objeyi silmeden dondurur.

<p align="center">
    <img src="https://user-images.githubusercontent.com/31994778/124504995-390d2c00-ddd1-11eb-83af-e6f8f58d20b7.png">
    </p>
    
<h4>Kullanim Alanlari</h4>

- Internet tarayicilarinin gecmis'i tutmasi.
- Parantezlerin (){}[] dogru kapatilip kapatilmadiginin bulunmasi.
- Undoing, backtracking (yapilan islemi geri alma)

---

<h4>Implementasyon</h4>

`Stack` yapisini iki turlu, bagli liste ve dizi, ile implemente edebiliriz.

<h5>Dizi Implementasyonu</h5>

```python
class Stack:
    def __init__(self):
        self.arr = []

    def size(self):
        return len(self.arr)

    def push(self, element):
        self.arr.append(element)

    def pop(self):
        if not len(self.arr) > 0:
            return
        temp = self.arr[len(self.arr) - 1]
        del self.arr[len(self.arr) - 1]
        return temp

    def peek(self):
        if not len(self.arr) > 0:
            return
        print(self.arr[len(self.arr) - 1])

    def show(self):
        print(self.arr[::-1])
```

<h5>Bagli Liste Implementasyonu</h5>

Bagli liste kodunu paylasmadan direk implemente edelim, zaten daha onceden bagli listeyi kodlamistik.

```python
from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.arr = LinkedList()

    def size(self):
        return self.arr._size()

    def push(self, element):
        self.arr.append(element)

    def pop(self):
        if not self.arr._size() > 0:
            return
        temp = self.arr.get(self.arr._size() - 1)
        self.arr.remove(self.arr._size() - 1)
        return temp

    def peek(self):
        if not self.arr._size() > 0:
            return
        print(self.arr.get(self.arr._size() - 1))

    def show(self):
        for i in range(self.arr._size()-1, -1, -1):
            print(self.arr.get(i), end=' ')
        print('')
```

