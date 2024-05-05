from stack import Stack

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(" ", s.peek())
    print(" ", s.pop())
    print(" ", s.pop())
    print(" ", s.pop())
    print("stack state?", s.is_empty())

if __name__ == "__main__":
    main()
