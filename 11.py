with open('11/11_input.txt', 'r') as f:
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
        
        
    def inspect_item(self):
        # increment inspection counter
        self.inspections += 1
        
        # increment worry level after monkey inspection
        if self.operation == '+':
                self.items[0] += int(self.operand)
        if self.operation == '*':
            if self.operand.isdigit():
                self.items[0] *= int(self.operand)
            else:
                self.items[0] *= self.items[0]
                
                
    def get_bored(self):
        # relief item is not broken
        self.items[0] = self.items[0]//3
    
    
    def test_item(self, item):
        # test item on its worry level to return targeted monkey
        if item % self.test == 0:
#             print(f'  Current worry level is divisible by {monkey.test}.')
            return self.test_true
        else:
#             print(f'  Current worry level is not divisible by {monkey.test}.')
            return self.test_false
        
        
    def throw_item(self):
        # throw item
        return self.items.pop(0)
        
        
    def receive_item(self, item):
        # targeted monkey receive the thrown item
        self.items.append(item)

        
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
    
    # round
    for monkey in monkeys:
#         print(f'Monkey {monkey.id}:')
        
        # turn
        while len(monkey.items) > 0:
            
#             print(f'Monkey inspects an item with a worry level of {monkey.items[0]}.')
            
            # increment inspection counter + worry level after monkey inspection
            monkey.inspect_item()
#             print(f'  Worry level is {monkey.operation} by {monkey.operand} to {monkey.items[0]}.')
            
            # relief item is not broken
            monkey.get_bored()
#             print(f'  Monkey gets bored with item. Worry level is divided by 3 to {monkey.items[0]}.')

            # define target monkey testing worry level
            target_monkey_id = monkey.test_item(monkey.items[0])
            
            # throw item to target monkey
#             print(f'  Item with worry level {monkey.items[0]} is thrown to monkey {target_monkey_id}.')
            monkeys[target_monkey_id].receive_item(monkey.throw_item())
            
    # print worry level of carried items for each monkeys
#     print(f'After round {round}, the monkeys are holding items with these worry levels: ')
#     for monkey in monkeys:
#         monkey.print_items()
#     print('\n')

# check monkey business ; multiply the inspections of the two most active monkeys
inspections = [monkey.inspections for monkey in monkeys]

for i,n in enumerate(inspections):
    print(f'Monkey {i} inspected items {n} times.')

inspections.sort(reverse=True)
monkey_business = inspections[0]*inspections[1]

print(f'day 11, part 1 : {monkey_business}')


