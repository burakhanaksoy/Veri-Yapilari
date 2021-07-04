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

