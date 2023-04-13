with open('11_input.txt', 'r') as f:
    lines = f.readlines()
    notes = [l.strip() for l in lines]

    
class Monkey:
    def __init__(self, id, items, operation, test_condition, test_true, test_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.test_condition = test_condition
        self.test_true = test_true
        self.test_false = test_false
        self.inspections = 0        
        
        
    def inspect_item(self):
        # increment inspection counter
        self.inspections += 1
#       print(f'Monkey inspects an item with a worry level of {monkey.items[0]}.')

        # increment worry level after monkey inspection
        old = self.items[0]
        self.items[0] = eval(self.operation)
#       print(f'  Worry level is {monkey.operation[4:]} to {monkey.items[0]}.')

        # relief item is not broken
        self.items[0] = self.items[0]//3
#       print(f'  Monkey gets bored with item. Worry level is divided by 3 to {monkey.items[0]}.')

        # test item on its worry level to return targeted monkey
        if self.items[0] % self.test_condition == 0:
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
#         print(f'  Item with worry level {monkey.items[0]} is thrown to monkey {target_monkey_id}.')

        
    def print_items(self):
        return print(f"Monkey {self.id}: {', '.join([str(item) for item in self.items])}")
    

# list monkeys 
monkeys = []
for k in range(0,len(notes),7):
    monkeys.append(Monkey(
        int(notes[k][-2]),
        [int(word) for word in notes[k+1].replace(':', '').replace(',', '').split(' ') if word.isdigit()],
        notes[k+2][17:],
        int(notes[k+3].split(' ')[-1]),
        int(notes[k+4].split(' ')[-1]),
        int(notes[k+5].split(' ')[-1])
    ))
    
# 20 rounds
nb_rounds = 20

for round in range(nb_rounds):
    for monkey in monkeys:
#         print(f'Monkey {monkey.id}:')

        while len(monkey.items) > 0:
        
            # define target monkey after inspecting the item
            target_monkey_id = monkey.inspect_item()
            
            # throw item to target monkey
            monkeys[target_monkey_id].receive_item(monkey.throw_item())

            
    # print worry level of carried items for each monkeys
    print(f'After round {round}, the monkeys are holding items with these worry levels: ')
    for monkey in monkeys:
        monkey.print_items()
    print('\n')

    
# check monkey business ; multiply the inspections of the two most active monkeys
inspections = [monkey.inspections for monkey in monkeys]

for i,n in enumerate(inspections):
    print(f'Monkey {i} inspected items {n} times.')

inspections.sort(reverse=True)
monkey_business = inspections[0]*inspections[1]


print(f'day 11, part 1 : {monkey_business}')