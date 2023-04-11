with open('11_test_input.txt', 'r') as f:
    lines = f.readlines()
    notes = [l.strip() for l in lines]

class Monkey:
    def __init__(self, notes) -> None:
        self.id = int(notes[0][-2])
        self.items = [int(word) for word in notes[1].replace(':', '').replace(',', '').split(' ') if word.isdigit()]
        self.operation = notes[2].split(' ')[-2]
        self.operand = notes[2].split(' ')[-1]
        self.test = int(notes[3].split(' ')[-1])
        self.test_true = int(notes[4].split(' ')[-1])
        self.test_false = int(notes[5].split(' ')[-1])
        self.inspections = 0
    
    def modify_worry_level(self, item):
        # increment worry level after monkey inspection
        if self.operation == '+':
                self.items[0] += int(self.operand)
        if self.operation == '*':
            if self.operand.isdigit():
                self.items[0] *= int(self.operand)
            else:
                self.items[0] *= item
        # relief item is not broken
        self.items[0] = item//3
        
    def receive_item(self, item):
        # targeted monkey receive the thrown item
        self.items.append(item)
    
    def throw_item(self):
        # throw item
        return self.items.pop(0)
        
    def target_monkey(self, item):
        # test item on its worry level to return targeted monkey
        if item % self.test == 0:
            return self.test_true
        else:
            return self.test_false
        
    def inspect_item(self):
        # increment inspection counter
        self.inspections += 1    
            
    def print_items(self):
        return print(f"Monkey {self.id}: {', '.join([str(item) for item in self.items])}")
   
# list monkeys 
monkeys = []
while len(notes) > 0:
    monkeys.append(Monkey(notes))
    notes = notes[7:] if len(notes) > 7 else []

# 20 rounds
round = 0
while round < 20:
    round += 1
    print(f'After round {round}, the monkeys are holding items with these worry levels: ')
    # round
    for monkey in monkeys:
        # turn
        monkey_items = monkey.items
        for item in monkey_items:
            # increment inspection counter
            monkey.inspect_item()           
            # increment worry level after monkey inspection, then relief item is not broken
            monkey.modify_worry_level(item)
            # throw item after testing worry level          
            monkeys[monkey.target_monkey(item)].receive_item(monkey.throw_item())
            
            print(f"Monkey {monkey.id}: {monkey.items} ")
            
        # print worry level of carried items for each monkeys
        monkey.print_items()
    print('-------------\n')

# check monkey business ; multiply the inspections of the two most active monkeys
inspections = [monkey.inspections for monkey in monkeys]

for i,n in enumerate(inspections):
    print('Monkey {i} inspected items {n} times.')

inspections.sort(reverse=True)
monkey_business = inspections[0]*inspections[1]

print(f'day 11, part 1 : {monkey_business}')
