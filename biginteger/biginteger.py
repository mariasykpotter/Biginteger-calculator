class BigInteger:
    '''The class for BigInteger representation'''

    def __init__(self, minus=False, line="0"):
        '''Initialises a BigInteger class'''
        self.head = None
        self.tail = None
        self.minus = minus
        if int(line):
            for el in line:
                new_node = Node(int(el))
                if self.head is None:
                    self.head = self.tail = new_node
                else:
                    new_node.prev = self.tail
                    new_node.next = None
                    self.tail.next = new_node
                    self.tail = new_node

    def append_to_num(self, data):
        '''
        Adds a number to the linked list
        :param data: int
        :return: None
        '''
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def delete(self):
        '''Deletes a linkedlist'''
        self.head = self.tail = None

    def show(self):
        '''
        Shows the two_linked list. Analogic to method toString
        :return: str
        '''
        text = ""
        if self.head is None:
            text = str(None)
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    text += str(current_node.data)
                    break
                else:
                    text += str(current_node.data) + " - "
                    current_node = current_node.next
        return text

    def reverse(self):
        pass

    def __add__(self, rhsInt):
        '''
        Adds two linked lists
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        if self.minus == rhsInt.minus:
            new_num = self.add(rhsInt)
            new_num.minus = self.minus
            return new_num
        elif self.minus and (not rhsInt.minus):
            if self.more_and_eq(rhsInt):
                new_num = self.subtract(rhsInt)
                new_num.minus = self.minus
                return new_num
            else:
                new_num = rhsInt.subtract(self)
                new_num.minus = rhsInt.minus
                return new_num
        elif rhsInt.minus and (not self.minus):
            if self.more_and_eq(rhsInt):
                new_num = self.subtract(rhsInt)
                new_num.minus = self.minus
                return new_num
            else:
                new_num = rhsInt.subtract(self)
                new_num.minus = rhsInt.minus
                return new_num

    def __sub__(self, rhsInt):
        '''
        Subtracrts tow BigInteger numbers
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        if not self.minus and not rhsInt.minus:
            if self.more_and_eq(rhsInt):
                new_num = self.subtract(rhsInt)
                new_num.minus = self.minus
                return new_num
            else:
                new_num = rhsInt.subtract(self)
                new_num.minus = True
                return new_num
        elif self.minus and rhsInt.minus:
            if self.more_and_eq(rhsInt):
                new_num = self.subtract(rhsInt)
                new_num.minus = True
                return new_num
            else:
                new_num = rhsInt.subtract(self)
                new_num.minus = False
                return new_num
        elif self.minus and not rhsInt.minus:
            new_num = rhsInt.add(self)
            new_num.minus = True
            return new_num
        elif not self.minus and rhsInt.minus:
            new_num = rhsInt.add(self)
            new_num.minus = False
            return new_num

    def add(self, rhsInt):
        '''
        Add BigInteger with minus and plus signs
        :param rhsInt:
        :return:
        '''
        lst_values = []
        newnum = BigInteger()
        NodeA = self.tail
        NodeB = rhsInt.tail
        # Add corresponding terms until one list is empty.
        mem = 0
        while NodeA is not None or NodeB is not None:
            if NodeA == None:
                node1 = 0
                node2 = NodeB.data
                NodeB = NodeB.prev
            elif NodeB == None:
                node2 = 0
                node1 = NodeA.data
                NodeA = NodeA.prev
            else:
                node1 = NodeA.data
                node2 = NodeB.data
                NodeA = NodeA.prev
                NodeB = NodeB.prev
            value = (node1 + node2 + mem) % 10
            lst_values.append(value)
            mem = (node1 + node2 + mem) // 10
        if mem:
            lst_values.append(mem)
        lst_values.reverse()
        for el in lst_values:
            newnum.append_to_num(el)

        return newnum

    def subtract(self, rhsInt):
        '''
        Subtract 2 BigIntegers
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        lst_values = []
        newnum = BigInteger()
        NodeA = self.tail
        NodeB = rhsInt.tail
        mem = 0
        while NodeA is not None or NodeB is not None:
            use_memory = False
            if NodeA == None:
                node1 = 0
                node2 = NodeB.data
                NodeB = NodeB.prev
            elif NodeB == None:
                node2 = 0
                node1 = NodeA.data
                NodeA = NodeA.prev
            else:
                node1 = NodeA.data
                node2 = NodeB.data
                NodeA = NodeA.prev
                NodeB = NodeB.prev
            if node1 + mem < node2:
                node1 += 10
                use_memory = True
            value = (node1 - node2 + mem) % 10
            if use_memory:
                mem = -1
            else:
                mem = 0
            lst_values.append(value)
        while lst_values and len(lst_values) >= 2:
            if lst_values[-1] == 0:
                lst_values.pop()
            else:
                break
        lst_values.reverse()
        for el in lst_values:
            newnum.append_to_num(el)
        return newnum

    def mul(self, num):
        '''
        Multiplies BigInteger on num
        :param num: int
        :return: BigInteger
        '''
        lst = []
        mem = 0
        new_num = BigInteger()
        NodeA = self.tail
        while NodeA is not None:
            node1 = NodeA.data
            el1 = num * node1
            value = (el1 + mem) % 10
            mem = (el1 + mem) // 10
            NodeA = NodeA.prev
            lst.append(value)
        if mem:
            lst.append(mem)
        lst.reverse()
        for el in lst:
            new_num.append_to_num(el)
        return new_num

    def __mul__(self, rhsInt):
        '''
        Multiplying one BigInteger on another
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        count = 0
        if len(self) > len(rhsInt):
            NodeB = rhsInt.tail
            obj = self
        else:
            NodeB = self.tail
            obj = rhsInt
        suma = BigInteger()
        suma.append_to_num(0)
        while NodeB is not None:
            multiplier = obj.mul(NodeB.data)
            for i in range(count):
                multiplier.append_to_num(0)
            suma = suma + multiplier
            NodeB = NodeB.prev
            count += 1
        if self.minus == rhsInt.minus:
            suma.minus = False
        else:
            suma.minus = True
        return suma

    def div(self, rhsInt):
        '''
        Divide one BigInteger on another
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        subtraction = self
        count = BigInteger()
        count.append_to_num(1)
        dilnyk = BigInteger()
        dilnyk.append_to_num(0)
        while subtraction.more_and_eq(rhsInt):
            subtraction = subtraction.subtract(rhsInt)
            dilnyk = dilnyk + count
        if self.minus != rhsInt.minus:
            dilnyk.minus = True
        return dilnyk

    def ostacha(self, rhsInt):
        '''
        Ostacha forom division of one BigInteger on another
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        return self - (rhsInt * (self.div(rhsInt)))

    def parne(self):
        '''
        Defines whether the BigInteger is even
        :return:bool
        '''
        new_num = BigInteger("0")
        new_num1 = BigInteger()
        new_num1.append_to_num("2")
        if self.ostacha(new_num1) == new_num:
            return True
        else:
            return False

    def power(self, rhsInt):
        '''
        Brings one BigInteger to another BigInteger degree
        :param rhsInt: BigInteger
        :return: BigInteger
        '''
        new_num = self
        counter = BigInteger()
        counter.append_to_num(1)
        adder = BigInteger()
        adder.append_to_num(1)
        while rhsInt.more(counter):
            new_num = new_num * self
            counter += adder
        return new_num

    def __pow__(self, rhsInt):
        '''
        Brings one BigInteger to another BigInteger degree both with plus or minus sign
        :param rhsInt:
        :return:
        '''
        null = BigInteger()
        null.append_to_num(0)
        odyn = BigInteger()
        odyn.append_to_num(1)
        if rhsInt.minus:
            new_num = odyn.div(self.power(rhsInt))
        else:
            new_num = self.power(rhsInt)
        if self.minus:
            if not rhsInt.parne():
                new_num.minus = True
        return new_num

    def toString(self):
        text = ""
        curNode = self.head
        while curNode is not None:
            text += str(curNode.data)
            curNode = curNode.next
        return text

    def __len__(self):
        '''
        The length of BigInteger
        :return: int
        '''
        size = 0
        curNode = self.head
        while curNode is not None:
            size += 1
            curNode = curNode.next
        return size

    def more(self, other):
        '''
        Compare self with other.Self>Other
        :param other: BigInteger
        :return: bool
        '''
        if len(self) > len(other):
            return True
        elif len(self) == len(other):
            NodeA = self.head
            NodeB = other.head
            while NodeA is not None:
                if NodeA.data > NodeB.data:
                    return True
                else:
                    if NodeA and NodeB:
                        if NodeA.data == NodeB.data:
                            NodeA = NodeA.next
                            NodeB = NodeB.next
                        else:
                            return False
            return False
        else:
            return False

    def more_and_eq(self, other):
        '''
        Compare self with other.Self >= Other
        :param
        other: BigInteger
        :return: bool
        '''
        count = 0
        if len(self) > len(other):
            return True
        elif len(self) == len(other):
            NodeA = self.head
            NodeB = other.head
            while NodeA is not None:
                if NodeA.data > NodeB.data:
                    return True
                else:
                    if NodeA and NodeB:
                        if NodeA.data == NodeB.data:
                            count += 1
                        else:
                            return False
                NodeA = NodeA.next
                NodeB = NodeB.next
            if count == len(self):
                return True
        else:
            return False

    def __eq__(self, other):
        '''
        Compare self with other.Self == Other
        :param
        other: BigInteger
        :return: bool
        '''
        if len(self) == len(other):
            NodeA = self.head
            NodeB = other.head
            while NodeA is not None:
                if NodeA.data == NodeB.data:
                    NodeA = NodeA.next
                    NodeB = NodeB.next
                else:
                    return False
            return True
        else:
            return False

    def bigint_to_bin(self):
        '''
        Converts BigInteger to binary
        :return: BigInteger
        '''
        lst = []
        dwa = BigInteger()
        dwa.append_to_num(2)
        null = BigInteger()
        null.append_to_num(0)
        one = BigInteger()
        one.append_to_num(1)
        new_num = BigInteger()
        ost = self.ostacha(dwa)
        dilene = self.div(dwa)
        lst.append(ost.toString())
        while dilene.more_and_eq(dwa):
            ost = dilene.ostacha(dwa)
            dilene = dilene.div(dwa)
            lst.append(ost.toString())
        lst.append(dilene.toString())
        lst.reverse()
        for el in lst:
            new_num.append_to_num(int(el))
        return new_num

    def bin_to_bigint(self):
        '''
        Converts binary BigInteger back to the BigInteger
        :return: BigInteger
        '''
        new_num = BigInteger()
        new_num.append_to_num(0)
        curnode = self.tail
        i = 0
        while curnode is not None:
            if curnode.data:
                num = BigInteger()
                num.append_to_num(2 ** i)
                new_num = new_num + num
            i += 1
            curnode = curnode.prev
        return new_num

    def bitwise_ops(self, other, operator):
        '''
        Does ^, & or | dependent on the chosen operator.
        :param other: BigInteger
        :param operator: str
        :return: BigInteger
        '''
        try:
            assert self.minus == False and other.minus == False
        except AssertionError:
            print("BigInteger should be more than 0")
        lst = []
        self = self.bigint_to_bin()
        other = other.bigint_to_bin()
        Node1 = self.tail
        Node2 = other.tail
        new_num = BigInteger()
        while Node1 is not None or Node2 is not None:
            if Node1 == None:
                node1 = 0
                node2 = Node2.data
                Node2 = Node2.prev
            elif Node2 == None:
                node2 = 0
                node1 = Node1.data
                Node1 = Node1.prev
            else:
                node1 = Node1.data
                node2 = Node2.data
                Node1 = Node1.prev
                Node2 = Node2.prev
            if operator == "|":
                num = node1 | node2
            elif operator == "&":
                num = node1 & node2
            elif operator == "^":
                num = node1 ^ node2
            lst.append(num)
        lst.reverse()
        for el in lst:
            new_num.append_to_num(el)
        return new_num.bin_to_bigint()

    def shift_right(self, n):
        '''
         Shifts BigInteger on n positions
         :param n: int
         :return: BigInteger
         '''
        try:
            assert self.minus == False
        except AssertionError:
            print("BigInteger should be more than 0")
        new_num = BigInteger()
        new_num.append_to_num(2 ** n)
        self = self.div(new_num)
        return self

    def shift_left(self, n):
        '''
        Shifts BigInteger on n positions
        :param n: int
        :return: BigInteger
        '''
        try:
            assert self.minus == False
        except AssertionError:
            print("BigInteger should be more than 0")
        new_num = BigInteger()
        new_num.append_to_num(2 ** n)
        self = self * (new_num)
        return self


class Node:
    '''Represents a Node class'''

    def __init__(self, data):
        '''
        Initialises Node
        :param data: str
        '''
        self.next = None
        self.data = data
        self.prev = None
