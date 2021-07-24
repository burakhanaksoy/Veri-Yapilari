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

---

<h3>Binary Search Tree</h3>

>A binary tree is a type of data structure for storing data such as numbers in an organized way.

Binary Search Tree is not a sorting algorithm! It's a data structure in which we can implement search, insertion, and deletion operations with time and space complexities as follows:

<div align="center">
    
Algorithm | Average | Worst Case
--------- | --------- | --------- 
Space | O(n) | O(n)
Search | O(log n) | O(n)
Insert | O(log n) | O(n)
Delete | O(log n) | O(n)
    
</div>

<h4>Differences Between Binary Tree and Binary Search Tree</h4>

1- In BST, every node's left node is less than the parent node, and the right node is greater than the parent node.

<div align="center">
    <img width="350" height="250" src="https://user-images.githubusercontent.com/31994778/126863914-0b00b32d-04f0-41a8-9f89-70387a13cde7.png">
    </div>
    
2- In BST, insertion sequence of numbers is important. Inserting 100 first and 150 second won't produce the same binary tree as inserting 150 first and 100 second.

<div align="center">
<img width="350" height="300" alt="Screen Shot 2021-07-24 at 12 24 23 PM" src="https://user-images.githubusercontent.com/31994778/126864310-1e24b33f-2224-448e-a490-97794b922657.png">
    </div>
    
   <p align="center">
    Inserting 100 first and 150 second
    </p>
    
   <div align="center">
    <p>
<img width="350" height="300" alt="Screen Shot 2021-07-24 at 12 27 16 PM" src="https://user-images.githubusercontent.com/31994778/126864336-2891b566-f898-47c4-867a-1f684b8fa891.png">
    </p>
    </div>
    
   <p align="center">
    Inserting 150 first and 100 second
    </p>
    
<h5>Comparison</h5>

BST | BT
---- | ----
BINARY SEARCH TREE is a node based binary tree which further has right and left subtree that too are binary search tree. | BINARY TREE is a non linear data structure where each node can have two child nodes at most.
Insertion, deletion, searching of an element is faster in BINARY SEARCH TREE than BINARY TREE due to the ordered characteristics | BINARY TREE is unordered hence slower in process of insertion, deletion and searching.
IN BINARY SEARCH TREE the left subtree has elements less than the nodes element and the right subtree has elements greater than the nodes element. | IN BINARY TREE there is no ordering in terms of how the nodes are arranged

<h4>Implementation</h4>

Firstly, we need a Node class to hold value of itself, value of left and right child nodes.

```py
class Node:

	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
```

Then, BST class

```py
class BST:
	
	def __init__(self, root=None):
		self.root = root

	def insert(val, node=None):	
		if self.root == None:
			self.root.val = val
			self.root.left = None
			self.root.right = None

		if val < self.node.val:
			if self.node.left == None:
				self.node.left = val
				return
			self.insert(val, self.node.left)

		if val > self.node.val:
			if self.node.right == None:
				self.node.right = val
				return
			self.insert(val, self.node.right)
```

<h4>Traversing BST</h4>

There are different ways to implement traverse operation.

<div align="center">
    <p>
<img width="368" alt="Screen Shot 2021-07-24 at 4 42 31 PM" src="https://user-images.githubusercontent.com/31994778/126870364-91d283c8-84c3-4655-bee5-3d832e11cbbb.png">
    </p>
    </div>
    
   <p align="center">
    A Display of parent node (N) with child nodes (L and R).
    </p>

1- Infix: LNR, RNL (N is on the mid)

2- Prefix: NLR, NRL (N comes first)

3- Postfix: LRN, RLN (N comes last)

We will make use of Infix (LNR).

<div align="center">
    <p>
<img width="350" height="250" src="https://user-images.githubusercontent.com/31994778/126870428-f4f2a605-736d-47f1-bbfd-8aeb28dd1cdf.png">
    </p>
    </div>
    
Using LNR, we will have

`1 3 4 6 7 8 10 13 14`

If we used RNL, we would have

`14 13 10 8 7 6 4 3 1`

<b>As it is seen from the examples above, BST is ordered</b>

<h4>Traversing</h4>

Done recursively, as follows:

```py
def traverse(self, node):
        # Traverse using "prefix" L, N, R
        if node is None:
            pass
        else:
            self.traverse(node.left)  # L
            print(node.val, end=' ')  # N
            self.traverse(node.right)  # R
```


