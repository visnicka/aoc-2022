import re
import regex
import numbers
import time
import math
from sympy import simplify

class Aoc202201():
    def runDay01():
        print('Greetings, boss!')

        # open file for reading
        filename = './inputs/1/input.txt'
        with open(filename,'r') as f:
            # lines = f.readlines()
            # print(f'line count {len(lines)}')
            sum = 0
            max_sum = 0
            total_sum = 0
            check_sum = 0
            line_count = 0           
            sums = []
            for line in f:
                line_count += 1
                # print(line)
                if line == '\n' :
                    if sum > max_sum:
                        max_sum = sum
        
                    sums.append(sum)
                    check_sum += sum
                    sum = 0
                else:
                    amount = int(line)
                    sum += amount
                    total_sum += amount

            sums.append(sum)
            check_sum += sum
            sum = 0

            sums.sort();


        print(f'>>> {sums[len(sums)-1] + sums[len(sums)-2] + sums[len(sums)-3]}')

        print(f'total sum {total_sum}')
        print(f'check sum {check_sum}')
        print(f'max sum {max_sum}')
        print(f'line count {line_count}')
        print(f'sums length {len(sums)}')
    def runDay02():
        print('Greetings, boss!')

        # A(1) for Rock, B(2) for Paper, and C(3) for Scissors
        # X(1) for Rock, Y(2) for Paper, and Z(3) for Scissors
        # score = (1 for Rock, 2 for Paper, and 3 for Scissors) + (0 if you lost, 3 if the round was a draw, and 6 if you won)
        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

        m = {
            "A X": 1 + 3,
            "A Y": 2 + 6,
            "A Z": 3 + 0,
            "B X": 1 + 0,
            "B Y": 2 + 3,
            "B Z": 3 + 6,
            "C X": 1 + 6,
            "C Y": 2 + 0,
            "C Z": 3 + 3
        }
        m2 = {
            "A X": 3 + 0,
            "A Y": 1 + 3,
            "A Z": 2 + 6,
            "B X": 1 + 0,
            "B Y": 2 + 3,
            "B Z": 3 + 6,
            "C X": 2 + 0,
            "C Y": 3 + 3,
            "C Z": 1 + 6
        }
        
        # open file for reading
        filename = './inputs/2/input.txt'
        with open(filename,'r') as f:
            # print(f'line count {len(lines)}')
            line_count = 0
            total_score1 = 0
            total_score2 = 0
            for line in f:
                line = line.strip()
                line_count += 1
                # print(f'opponent: {line.split(" ")[0]} me: {line.split(" ")[1]} line_count: {line_count}')
                
                score = m[line]
                score2 = m2[line]
                total_score1 += score
                total_score2 += score2
                # print(f'{line_count}: score: {score}')
                
            
        print(f'line count {line_count}')
        print(f'total score1 {total_score1}')
        print(f'total score2 {total_score2}')
    def runDay03():
        def to_prio(letter):
            # a==97 z==122 A==65 Z==90
            # Lowercase item types a through z have priorities 1 through 26.
            # Uppercase item types A through Z have priorities 27 through 52.
            letter = ord(letter)
            if letter >= ord('a') and letter <= ord('z'):
                return int(letter)-96
            else:
                return int(letter)-38
                
        def find_common(c1, c2):
            common = []
            for c1_item in c1:
                if c1_item in c2 and c1_item not in common:
                    common.append(c1_item)
            return common

        def find_common2(c1, c2, c3):
            common = []
            for c1_item in c1:
                if c1_item in c2 and c1_item in c3 and c1_item not in common:
                    common.append(c1_item)
            return common

        print('Greetings, boss!')

        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

        # open file for reading
        filename = './inputs/3/input.txt'
        with open(filename,'r') as f:
            # print(f'line count {len(lines)}')
            line_count = 0
            total_prio = 0
            total_groups_prio = 0
            groups = []
            for line in f:
                line = line.strip()
                line_count += 1
                if len(line)%2 != 0:
                    print(f'odd number of items... something silly is going on...')
                    break
                
                rucksack = list(line)
                rucksack = [to_prio(i) for i in rucksack]
                rucksack.sort
                
                comp1 = list(line[:int(len(line)/2)])
                comp1 = [to_prio(i) for i in comp1]
                comp1.sort()
                
                comp2 = list(line[int(len(line)/2):])
                comp2 = [to_prio(i) for i in comp2]
                comp2.sort()

                common = find_common(comp1, comp2)
                print(f'line: {line}\ncompartment1: {comp1}\ncompartment2: {comp2}\ncommon: {common}')
                if len(common) == 0 or len(common) > 1:
                    print(f'unexpected common size... something silly is going on...')
                    break
                total_prio += common[0]

                groups.append(rucksack)
                if line_count % 3 == 0:
                    group_common = find_common2(groups[0], groups[1], groups[2])
                    if len(group_common) == 0 or len(group_common) > 1:
                        print(f'unexpected group_common size... something silly is going on...')
                        break
                    total_groups_prio += group_common[0]
                    print(f'>>> group common: {group_common}')
                    groups.clear()
                
            
        print(f'line count {line_count}')
        print(f'total_prio {total_prio}')
        print(f'total_groups_prio {total_groups_prio}')
    def runDay04():
        print('Greetings, boss!')

        # open file for reading
        filename = './inputs/4/input.txt'
        with open(filename,'r') as f:
            overlap_count = 0
            any_overlap_count = 0
            line_count = 0           
            # sums = []
            for line in f:
                line = line.strip()
                line_count += 1
                overlap = ""
                any_overlap = ""

                elf1 = line.split(",")[0].split("-")
                elf2 = line.split(",")[1].split("-")
                elf1 = [int(i) for i in elf1]
                elf2 = [int(i) for i in elf2]

                if (elf2[0] <= elf1[0] <= elf2[1] and
                    elf2[0] <= elf1[1] <= elf2[1]):
                    overlap_count += 1
                    overlap = ">>"
                elif (elf1[0] <= elf2[0] <= elf1[1] and
                    elf1[0] <= elf2[1] <= elf1[1]):
                    overlap_count += 1
                    overlap = "<<"

                if (elf2[0] <= elf1[0] <= elf2[1] or
                    elf2[0] <= elf1[1] <= elf2[1] or
                    elf1[0] <= elf2[0] <= elf1[1] or
                    elf1[0] <= elf2[1] <= elf1[1]):
                    any_overlap_count += 1
                    any_overlap = "XX"
                print(f'{line_count}: {line} {elf1} {elf2} {overlap} {any_overlap}')


        print(f'line count {line_count}')
        print(f'overlap count {overlap_count}')
        print(f'any overlap count {any_overlap_count}')
    def runDay05():
        print('Greetings, boss!')

        # open file for reading
        filename = './inputs/5/input.txt'
        with open(filename,'r') as f:
            line_count = 0           
            stack_lines = []
            print(f'\nstack setup:')
            for line in f:
                if line == '\n':
                    break                    
                # line = line.strip()
                line_count += 1

                n = 4 # chunk length
                chunks = [line[i:i+n-1] for i in range(0, len(line), n)]
                stack_lines.append(chunks)
            
            stack_lines.pop()
            flipped = list(zip(*stack_lines))
            stacks = [list(flipped[i][::-1]) for i in range(0, len(flipped))]
            
            for stack in stacks:
                for item in stack[::-1]:
                    if item == '   ':
                        stack.pop()

            print(f'stacks: {stacks}')

            print(f'stack count {len(stacks)}')
            print(f'\nmoving setup:')
            line_count = 0           

            for line in f:
                if line == '\n':
                    break                    
                line = line.strip()
                line_count += 1
                x = re.match('^move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)', line)
                inst_move = int(x.group(1))
                inst_from = int(x.group(2))
                inst_to = int(x.group(3))
                print(f'{line_count}: {line} >> move: {x.group(1)} from: {x.group(2)} to: {x.group(3)}')

                # run instructions part 1
                # for i in range(0, inst_move):
                #     print(f'stacks: {stacks}')
                #     print(f'moving {inst_from} >> {inst_to}')
                #     stacks[inst_to-1].append(stacks[inst_from-1].pop())
                #     print(f'stacks: {stacks}\n')

                # run instructions part 2
                print(f'stacks: {stacks}')
                print(f'moving {inst_move} pieces {inst_from} >> {inst_to}')
                shifting = [stacks[inst_from-1].pop() for _ in range(0,inst_move)][::-1]
                stacks[inst_to-1] += shifting
                print(f'stacks: {stacks}\n')

            result = ''
            for stack in stacks:
                result += stack.pop()
            print(result)
            

        print(f'\nline count {line_count}')
    def runDay06():
        print('Greetings, boss!')

        # open file for reading
        filename = './inputs/6/input.txt'
        with open(filename,'r') as f:
            line_count = 0           
            for line in f:
                line_count += 1

                line = line.strip()
                line = list(line)
                # print(f'input: {line}')
                print(f'input length: {len(line)}')

                marker_length = 4
                for i in range(marker_length - 1, len(line)):
                    section = line[i-marker_length+1:i+1]
                    # print(f'i: {i}: {section} set: {set(section)} len {len(section)}')
                    if len(section) == len(set(section)):
                        print(f'part1: msg starts at i: {i+1}')
                        break

                message_marker_length = 14
                for i in range(message_marker_length - 1, len(line)):
                    section = line[i-message_marker_length+1:i+1]
                    # print(f'i: {i}: {section} set: {set(section)} len {len(section)}')
                    if len(section) == len(set(section)):
                        print(f'part2: msg starts at i: {i+1}')
                        break

        print(f'line count {line_count}')
    def runDay07():
        print('Greetings, boss!')

        class FsEntry:
            def __init__(self, type, name, parent, size):
                self.type = type
                self.name = name
                self.parent = parent
                self.size = size
                self.children = []
            def __str__(self):
                return f"{self.name}: {self.type} (p:{self.parent} size:{self.size} children: {self.children})"
            
        class Computer:
            def __init__(self, name):
                self.fsSize = 70000000
                self.name = name
                self.fs = dict()
                self.cfs = None
                self.cwd = []
                fsEntry = FsEntry('dir', '/', None, 0)
                self.fs[fsEntry.name] = fsEntry

            def parseConsoleOutput(self, command, output):
                if (command[0]=='cd'):
                    if (command[1]=='/'):
                        self.cwd = ['/']
                    elif (command[1]=='..'):
                        self.cwd.pop()
                    else:
                        self.cwd.append(command[1]+'/')
                    
                    cwdpath = ''.join(self.cwd)
                    if cwdpath not in self.fs:
                        parentwd = self.cwd.copy()
                        parentwd.pop()
                        parentwdPath = ''.join(parentwd)
                        fsEntry = FsEntry('dir', cwdpath, parentwdPath, 0)
                        parentDirFsEntry = self.fs[fsEntry.parent]
                        parentDirFsEntry.children.append(fsEntry.name)
                        self.fs[fsEntry.name] = fsEntry

                elif (command[0]=='ls'):
                    for i in output:
                        if(i[0] == 'dir'):
                            pass # not interested in dir
                        else: # this is file
                            cwdpath = ''.join(self.cwd)
                            path = cwdpath + i[1]
                            if path not in self.fs:
                                fsEntry = FsEntry('file', path, cwdpath, int(i[0]))
                                parentDirFsEntry = self.fs[fsEntry.parent]
                                parentDirFsEntry.children.append(fsEntry.name)
                                self.fs[fsEntry.name] = fsEntry
                            
            def computeDir(self, dirFsEntry):
                totalSize = 0
                for childName in dirFsEntry.children:
                    fsEntry = self.fs[childName]
                    if (fsEntry.type == 'dir'):
                        self.computeDir(fsEntry)
                    totalSize += fsEntry.size
                dirFsEntry.size = totalSize

            def computeDirSizes(self):
                print('computing sizes...')
                dirFsEntry = self.fs['/']
                self.computeDir(dirFsEntry)
                print(dirFsEntry.size)

            def printFs(self):
                print('filesystem....')
                for i in self.fs.values():
                    print(i)

            def printSpecialSizes(self):
                print('special sized only...')
                sum = 0
                for i in self.fs.values():
                    if i.type == 'dir' and i.size <= 100000:
                        sum += i.size
                        # print(i)
                print(sum)

            def findUnusedSpace(self, currentTotal, reserve):
                print('dir to delete...')
                toDeleteDirs = []
                for i in self.fs.values():
                    if i.type == 'dir' and (self.fsSize - (currentTotal - i.size) > reserve):
                        toDeleteDirs.append(i.size)

                toDeleteDirs.sort()
                print(toDeleteDirs)


        basicComputer = Computer('handheld eniac')
        # open file for reading
        filename = './inputs/7/input.txt'
        with open(filename,'r') as f:
            line_count = 0
            command = []
            output = []
            print(f'\nparsing console....')
            for line in f:
                line_count += 1
                line.strip()
                line = line.split()
                if (line[0]=='$'): # command
                    if (len(command) > 0):
                        basicComputer.parseConsoleOutput(command, output)
                    line.pop(0)
                    command = line
                    output = []
                else:
                    output.append(line)
            basicComputer.parseConsoleOutput(command, output)

        # basicComputer.printFs()    
        basicComputer.computeDirSizes()
        basicComputer.printSpecialSizes()

        rootFsEntry = basicComputer.fs['/']

        basicComputer.findUnusedSpace(rootFsEntry.size, 30000000)
        print(f'\nline count {line_count}')
    def runDay08():
        print('Greetings, boss!')

        def get_subsection_max_id(section, max_size):
            for idx, el in enumerate(section):
                if el >= max_size:
                    return idx+1
            return len(section)

        # open file for reading
        filename = './inputs/8/input.txt'
        with open(filename,'r') as f:
            line_count = 0           
            tree_rows = []
            print(f'\ntree setup:')
            for line in f:
                line = line.strip()
                line_count += 1
                n = 1 # chunk length
                chunks = [int(line[i:i+1]) for i in range(0, len(line), n)]
                tree_rows.append(chunks)
                print(line)
            
            count = 0
            scenic_counts = []
            for y in range(0, len(tree_rows), 1):
                row = tree_rows[y]
                # print(f'{y}: {row}')
                for x in range(0, len(row), 1):
                    column =  [rowx[x] for rowx in tree_rows]
                    tree = row[x]
                    # print(f'{column}')
                    # look left
                    sectionLeft = row[:x]
                    sectionRight = row[x+1:]
                    sectionUp = column[:y]
                    sectionDown = column[y+1:]
                    if (len(sectionLeft)==0 or max(sectionLeft) < tree):
                        count += 1
                    elif (len(sectionRight)==0 or max(sectionRight) < tree):
                        count += 1
                    elif (len(sectionDown)==0 or max(sectionDown) < tree):
                        count += 1
                    elif (len(sectionUp)==0 or max(sectionUp) < tree):
                        count += 1

                    sectionLeftRev = sectionLeft[::-1]
                    sectionUpRev = sectionUp[::-1]
                    l = get_subsection_max_id(sectionLeftRev, tree)
                    r = get_subsection_max_id(sectionRight, tree)
                    d = get_subsection_max_id(sectionDown, tree)
                    u = get_subsection_max_id(sectionUpRev, tree)
                    scenic_count = l * r * d * u
                    #scenic_counts[scenic_count] = f'x: {x} y: {y}'
                    scenic_counts.append(scenic_count)
                    # if (x == 1):
                    #     print(f'{sectionLeft} << {tree} >> {sectionRight}')
                    # if (y == 1):
                    #     print(f'{sectionDown} << {tree} >> {sectionUp}')
            scenic_counts.sort()
            print(f'count: {count}')
            print(f'scenic_counts: {scenic_counts}')

        print(f'\nline count {line_count}')
    def runDay09():
        move = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }
        def update_tail_position(head_position, tail_position, head_prev_position):
            if abs(head_position[0] - tail_position[0]) <= 1\
               and abs(head_position[1] - tail_position[1]) <= 1:
               return tail_position
            
            new_x = tail_position[0]
            if (head_position[0]>tail_position[0]):
                new_x += 1
            elif (head_position[0]<tail_position[0]):
                new_x -= 1
            new_y = tail_position[1]
            if (head_position[1]>tail_position[1]):
                new_y += 1
            elif (head_position[1]<tail_position[1]):
                new_y -= 1
            return (new_x, new_y, tail_position[2])

        def print_rope(rope, tail_positions):
            s = ''
            for y in range(300, -5, -1):
                s = s + f'{"{0: >3}".format(y)} '
                for x in range(-30, 231, 1):
                    found = False
                    for k in rope:
                        if k[0]==x and k[1]==y:
                            s = s + f'{k[2]}'
                            found = True
                            break
                    if not found and (x, y, 'T') in tail_positions.keys():
                        s = s + '#'
                    elif not found:
                        s = s + '.'
                s = s + '\n'
            print(s)    
                    
        print('Greetings, boss!')

        rope = []
        rope.append((0, 0, 'H'))
        rope.append((0, 0, '1'))
        rope.append((0, 0, '2'))
        rope.append((0, 0, '3'))
        rope.append((0, 0, '4'))
        rope.append((0, 0, '5'))
        rope.append((0, 0, '6'))
        rope.append((0, 0, '7'))
        rope.append((0, 0, '8'))
        rope.append((0, 0, 'T'))

        # open file for reading
        filename = './inputs/9/input.txt'
        tail_positions = dict()
        print_rope(rope, tail_positions)
        with open(filename,'r') as f:
            line_count = 0           
            for line in f:
                line_count += 1

                line = line.strip()
                line = line.split()
                direction = line[0]
                
                for i in range(int(line[1])):
                    knot_move = move[direction]
                    knot_this = rope[0]
                    knot_this_new = (knot_this[0]+knot_move[0], knot_this[1]+knot_move[1], knot_this[2])
                    rope[0] = knot_this_new
                    upper_knot_prev = knot_this
                    upper_knot = knot_this_new
                    for knot_i in range(1, len(rope)):
                        knot_this = rope[knot_i]
                        knot_this_new = update_tail_position(upper_knot, knot_this, (upper_knot_prev[0], upper_knot_prev[1], knot_this[2]))
                        rope[knot_i] = knot_this_new
                        upper_knot_prev = knot_this
                        upper_knot = knot_this_new
                        knot_move = (upper_knot[0] - upper_knot_prev[0], upper_knot[1] - upper_knot_prev[1])
                        # print_rope(rope, tail_positions)
            
                    # print(f'input: {line}: {rope[0]}')
                    tail_positions[rope[len(rope)-1]]=1

                print_rope(rope, tail_positions)
 
        print_rope(rope, tail_positions)
        print(len(tail_positions.keys()))
        print(f'line count {line_count}')
    def runDay10():
        print('Greetings, boss!')

        class Instruction:
            # load instruction
            def __init__(self, itype, input, registers):
                self.itype = itype
                self.input = input
                self.registers = registers
                
                # noop takes one cycle to complete. It has no other effect.
                if (self.itype == 'noop'):
                    self.duration = 1
                # addx V takes two cycles to complete. After two cycles,
                # the X register is increased by the value V. (V can be negative.)
                elif (self.itype == 'addx'):
                    self.duration = 2
            def __str__(self):
                return f"{self.type}: {self.duration} {self.input}"
            # execute instructions
            def execute(self):
                self.duration -= 1
                if (self.itype == 'noop'):
                    pass
                elif (self.itype == 'addx'):
                    if (self.duration == 0):
                        self.registers['X'] += int(self.input)
                return self.duration <= 0 # True if finished

        class Computer:
            def __init__(self, name, program):
                self.name = name
                self.program = program
                self.registers = {'X': 1}
                self.inst_p = 0
                self.clock = 0
                self.checksum = 0
                self.screen = ''
                self.screen_pos = 0
                self.screen_line_pos = 0
                self.current_instr = None

            def run(self):
                while(self.inst_p < len(self.program)):
                    self.clock += 1
                    self.countChecksums()
                    self.printScreen()
                    self.executeInstruction()
            
            def countChecksums(self):
                if self.clock == 20 or\
                    self.clock == 60 or\
                    self.clock == 100 or\
                    self.clock == 140 or\
                    self.clock == 180 or\
                    self.clock == 220:
                    print(f'clock: {self.clock}: {self.registers} {self.clock * self.registers["X"]}')
                    self.checksum += self.clock * self.registers["X"]
    
            def executeInstruction(self):
                line = self.program[self.inst_p]
                line = line.split()
                itype = line[0]
                input = line[1] if len(line) > 1 else None
                if (self.current_instr == None):
                    self.current_instr = Instruction(itype, input, self.registers)
                finished = self.current_instr.execute()
                if finished:
                    del self.current_instr
                    self.current_instr = None
                    self.inst_p += 1

            def printScreen(self):
                # CRT: 40 wide and 6 high.
                output = '.'
                sprite_mid = self.registers['X']
                pixel_drawn = self.screen_line_pos
                if sprite_mid == pixel_drawn or\
                   sprite_mid+1 == pixel_drawn or \
                   sprite_mid-1 == pixel_drawn:
                   output = '#'  
                self.screen += output
                self.screen_pos += 1
                self.screen_line_pos += 1
                
                if self.screen_pos % 40 == 0:
                    self.screen += '\n'
                    self.screen_line_pos = 0
                if self.screen_pos % (40 * 6) == 0:
                    print(self.screen)
                
        # open file for reading
        filename = './inputs/10/input.txt'
        with open(filename,'r') as f:
            lines = f.readlines()
            print(f'line count {len(lines)}')
        
            sophisticatedComputer = Computer('handheld eniac', lines)
            sophisticatedComputer.run()
            print(sophisticatedComputer.checksum)
    def runDay11():
        class Monkey:
            
            def __init__(self, name, items, operation, test, iftrue, iffalse):
                self.name = name
                self.items = items
                self.operation = operation
                self.test = test
                self.iftrue = iftrue
                self.iffalse = iffalse
                self.inspections = 0

            def __str__(self):
                return f"{self.name}: {self.items} insp: {self.inspections} {self.operation} {self.test} {self.iftrue} {self.iffalse}"
            
        print('Greetings, boss!')
        monkeys = []
        
        # open file for reading
        filename = './inputs/11/input.txt'
        with open(filename,'r') as f:
            while(True):
                monkeyLine = f.readline()
                if not monkeyLine:
                    break
                reg_monkey = re.search("Monkey (\d+):", monkeyLine)
                reg_sitems = re.search("Starting items: (.+)", f.readline())
                reg_opertn = re.search("Operation: new = (.+)", f.readline())
                reg_testss = re.search("Test: divisible by (\d+)", f.readline())
                reg_iftrue = re.search("If true: throw to monkey (\d+)", f.readline())
                reg_ifflse = re.search("If false: throw to monkey (\d+)", f.readline())
                f.readline() # empty line
                monkey = Monkey(reg_monkey.group(1),\
                            [int(x) for x in reg_sitems.group(1).split(',')],\
                            reg_opertn.group(1),\
                            int(reg_testss.group(1)),\
                            int(reg_iftrue.group(1)),\
                            int(reg_ifflse.group(1)))
                print(monkey)
                monkeys.append(monkey)    
        print(f'monkey count {len(monkeys)}')
        max_worry = 1
        for monkey in monkeys:
            max_worry *= monkey.test
        print(f'monkey max_worry {max_worry}')

        for i_round in range(1, 10001):
            # if (i_round % 100 == 0):
            print(f'round {i_round} ----------------')
            
            for monkey in monkeys:
                for inspected_item in monkey.items:
                    old = inspected_item
                    worry_level = eval(monkey.operation)
                    # worry_level =int(worry_level / 3)
                    worry_level = worry_level % max_worry

                    monkey.inspections += 1
                    if worry_level % monkey.test == 0:
                    # if is_divisible(worry_level, monkey.test):
                        monkeys[monkey.iftrue].items.append(worry_level)
                    else:
                        monkeys[monkey.iffalse].items.append(worry_level)
                monkey.items.clear()

            activity = []
            for monkey in monkeys:
                activity.append(monkey.inspections)
                # print(monkey)
            print(f'activity: {activity}')
            activity.sort(reverse=True)
            print(f'sorted: {activity}')
            print(f'monkey business: {activity[0] * activity[1]}')
    def runDay12():
        class Node:
            def __init__(self, position, height, parent, cost):
                self.position = position
                self.height = height
                self.parent = parent
                self.children = []
                self.direction = ''
                self.cost = cost
                self.processed = False

            def __str__(self):
                return f"{self.position}: {self.height} cost: {self.cost}"
            
            def evalNextStep(self, next_pos, real_height, height, nodes):
                if (real_height is not None):
                    diff = ord(real_height) - ord(self.height)
                    if (diff <= 1):
                        node = Node(next_pos, height, self, self.cost + 1)  
                        if (node.position in nodes):
                            old_node = nodes[node.position]
                            if (old_node.cost > node.cost):
                                nodes[node.position] = node
                        else:
                            nodes[node.position] = node

            def lookAround(self, grid, nodes):
                size = { 'y': len(grid), 'x': len(grid[0]) }
                y = self.position[0]
                x = self.position[1]
                self.processed = True

                if (self.height == 'E'):
                    return

                up = None if y == 0 else grid[y-1][x]
                down = None if y == (size['y']-1) else grid[y+1][x]
                left = None if x == 0 else grid[y][x-1]
                right = None if x == (size['x']-1) else grid[y][x+1]

                r_up = 'z' if up == 'E' else up
                r_down = 'z' if down == 'E' else down
                r_left = 'z' if left == 'E' else left
                r_right = 'z' if right == 'E' else right

                r_up = 'a' if up == 'S' else r_up
                r_down = 'a' if down == 'S' else r_down
                r_left = 'a' if left == 'S' else r_left
                r_right = 'a' if right == 'S' else r_right

                self.evalNextStep((y-1, x), r_up, up, nodes)
                self.evalNextStep((y+1, x), r_down, down, nodes)
                self.evalNextStep((y, x-1), r_left, left, nodes)
                self.evalNextStep((y, x+1), r_right, right, nodes)
                

        print('Greetings, boss!')
        
        grid = []
        
        # open file for reading
        filename = './inputs/12/input.txt'
        with open(filename,'r') as f:
            for line in f:
                line = line.strip()
                row = [i for i in line]
                grid.append(row)
           
            # print('char grid ------------------')
            # for y in range(0, len(grid)):
            #     for x in range(0, len(grid[0])):
            #         print(f'{grid[y][x]}', end='')
            #     print('')

            print('evaluating ------------------')

            costs = []
            nodes = {}
            for y, row in enumerate(grid):
                for x, col in enumerate(row):
                    if col == 'a':
                        print(f'searching {y}-{x}...')

                        startNode = Node((y, x), 'a', None, 0)
                        # nodes = {}
                        nodes[startNode.position] = startNode
                    
                        stuff_to_process = True
                        while (stuff_to_process):
                            stuff_to_process = False
                            keyCopy = list(nodes.keys())
                            for key in keyCopy:
                                node = nodes[key]
                                if not node.processed:
                                    stuff_to_process = True
                                    node.lookAround(grid, nodes)

                        for node in nodes.values():
                            if node.height == 'E':
                                print(f'{node.height}: {node.position} {node.cost}')
                                costs.append(node.cost)
            costs.sort()
            print(costs)
        print('done.')
    def runDay13():
        print('Greetings, boss!')

        def parse(input, output):
            reg_bracket = re.search("^\[(.*)\]$", input)
            inside = reg_bracket.group(1)
            reg_list = regex.findall("\[(?:[^\]\[]*(?R)?)*+\]|\d+", inside)
            for item in reg_list:
                if item.isnumeric():
                    output.append(int(item))
                else:
                    output.append([])
                    parse(item, output[len(output)-1])

        def compare (litem, ritem):
            if (isinstance(litem, numbers.Number) and isinstance(ritem, list)):
                litem = [litem]
            elif (isinstance(litem, list) and isinstance(ritem, numbers.Number)):
                ritem = [ritem]

            if (isinstance(litem, numbers.Number) and isinstance(ritem, numbers.Number)):
                if litem < ritem:
                    return 'in order'
                elif litem > ritem:
                    return 'NOT in order' # damn the constants!
                else:
                    return 'next item'
            elif (isinstance(litem, list) and isinstance(ritem, list)):
                if len(litem) == 0 and len(ritem) == 0:
                    return 'next item'
                elif len(litem) == 0: # If the left list runs out of items first, the inputs are in the right order
                    return 'in order'
                else:
                    for i, i_litem in enumerate(litem):
                        # If the right list runs out of items first, the inputs are not in the right order
                        if i >= len(ritem):
                            return 'NOT in order'
                        i_ritem = ritem[i]

                        res = compare(i_litem, i_ritem)
                        if res == 'in order' or res == 'NOT in order':
                            return res

                    if len(litem) < len(ritem):
                        return 'in order'
            return 'next item'
            

        # open file for reading
        filename = './inputs/13/input.txt'
        with open(filename,'r') as f:
            line_count = 0
            index = 1
            sumOfIndices = 0
            
            # part 2 divider packets
            all_packets = []
            divider_list1 = []
            parse("[[2]]", divider_list1)
            all_packets.append(divider_list1)

            divider_list2 = []
            parse("[[6]]", divider_list2)
            all_packets.append(divider_list2)

            while(True):
                left = f.readline()
                if not left:
                    break
                
                print(f'----- packet {index}: -----------------')
                listleft = []
                parse(left, listleft)
                all_packets.append(listleft)

                listright = []
                right = f.readline()
                parse(right, listright)
                all_packets.append(listright)

                f.readline()
                
                # part 1
                res = compare(listleft, listright)
                print(res)
                if res == 'in order':
                    sumOfIndices += index
                index += 1
            
            print(f'sumOfIndices {sumOfIndices}')
            print(f'line count {line_count}')

            # part 2
            reordered_indices = list(range(0, len(all_packets)))

            not_in_order = True
            while(not_in_order):
                not_in_order = False
                for i in range (0, len(reordered_indices)-1):
                    listleft = all_packets[reordered_indices[i]]
                    listright = all_packets[reordered_indices[i+1]]
                    res = compare(listleft, listright)
                    if res == 'NOT in order': # swap
                        tmp = reordered_indices[i]
                        reordered_indices[i] = reordered_indices[i+1]
                        reordered_indices[i+1] = tmp
                        not_in_order = True

            print('lets get results')
            for i in range (0, len(reordered_indices), 1): 
                print(all_packets[reordered_indices[i]])
            
            print(f'position of [[2]]: {reordered_indices.index(0)+1} and [[6]]: {reordered_indices.index(1)+1}')
            print(f'decoder key {(reordered_indices.index(0)+1) * (reordered_indices.index(1)+1)}')
    def runDay14():
        print('Greetings, boss!')

        def print_cave(cave, floor_y, min_limits, max_limits):
            # update limits
            for node in cave:
                if (node[0] < min_limits[0]):
                    min_limits = (node[0], min_limits[1])
                if (node[1] < min_limits[1]):
                    min_limits = (min_limits[0], node[1])
                if (node[0] > max_limits[0]):
                    max_limits = (node[0], max_limits[1])
                if (node[1] > max_limits[1]):
                    max_limits = (max_limits[0], node[1])

            cave_row = ''
            for y in range(min_limits[1], max_limits[1]+1):
                for x in range(min_limits[0], max_limits[0]+1):
                    if (x, y) in cave:
                        cave_row += cave[(x,y)]
                    elif(y == floor_y):
                        cave_row += '='
                    else:
                        cave_row += '.'
                cave_row += '\n'
            print(cave_row)
        
        # open file for reading
        filename = './inputs/14/simple_input.txt'
        start = time.time()
        with open(filename,'r') as f:
            line_count = 0           
            paths = []
            
            # load paths
            for line in f:
                line = line.strip()
                line_count += 1
                path = line.split('->')
                path = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in path]
                paths.append(path)
                # print(f'path: {path}')
            
            # get path max dimensions
            pipe = (500, 0)
            min_limits = (None, None)
            max_limits = (None, None)
            for path in paths:
                for node in path:
                    if (min_limits[0] is None or node[0] < min_limits[0]):
                        min_limits = (node[0], min_limits[1])
                    if (min_limits[1] is None or node[1] < min_limits[1]):
                        min_limits = (min_limits[0], node[1])
                    if (max_limits[0] is None or node[0] > max_limits[0]):
                        max_limits = (node[0], max_limits[1])
                    if (max_limits[1] is None or node[1] > max_limits[1]):
                        max_limits = (max_limits[0], node[1])

            print(f'pipe: {pipe}')
            print(f'min_limits: {min_limits}')
            print(f'max_limits: {max_limits}')
                    
            # setup cave - unfortunately it is a bit transposed :(
            cave = {}
            cave[pipe] = 'o'
            floor_y = max_limits[1] + 2
            max_limits = (max_limits[0], floor_y)
            print_cave(cave, floor_y, min_limits, max_limits)
            
            # setup rocks
            for path in paths:
                for i in range(0, len(path)-1):
                    segment_from = path[i]
                    segment_to = path[i+1]
                    # print(f'from: {segment_from} to: {segment_to}')
                
                    # should not go diagnoally...
                    inc = 1 if segment_from[0] <= segment_to[0] else -1
                    for x in range(segment_from[0], segment_to[0] + inc, inc):
                        # print(x, segment_from[1])
                        cave[(x, segment_from[1])] = '#'
                    inc = 1 if segment_from[1] <= segment_to[1] else -1
                    for y in range(segment_from[1], segment_to[1] + inc, inc):
                        # print(segment_from[0], y)
                        cave[(segment_from[0]), y] = '#'
            print_cave(cave, floor_y, min_limits, max_limits)
                        
            # animate pipe - damn the transposed cave!
            grain_count = 0
            while(True):
                sand = (pipe[0], pipe[1])
                sand_not_settled = True
                grain_count += 1
                while(sand_not_settled):
                    sand_not_settled = False
                    
                    # if (sand[1]+1 == floor_y): # check limits for part 1
                    #     sand_not_settled = True
                    #     break
                    if (sand[0], sand[1] + 1) not in cave and (sand[1] + 1 < floor_y): # empty below
                        sand = (sand[0], sand[1]+1)
                        sand_not_settled = True
                    elif (sand[0]-1, sand[1] + 1) not in cave and (sand[1] + 1 < floor_y):  # empty below and left
                        sand = (sand[0]-1, sand[1]+1)
                        sand_not_settled = True
                    elif (sand[0]+1, sand[1] + 1) not in cave and (sand[1] + 1 < floor_y):  # empty below and right
                        sand = (sand[0]+1, sand[1]+1)
                        sand_not_settled = True
                    elif (sand == pipe): # check limits for part 2
                        sand_not_settled = True
                        break
                    else:
                        cave[sand] = 'o'
                # print_cave(cave, floor_y, min_limits, max_limits)

                if (sand_not_settled):
                    break
            
            print_cave(cave, floor_y, min_limits, max_limits)

            end = time.time()
            print(f'time: {end - start}')
            print(f'grain count: {grain_count}')
            print(f'\nline count {line_count}')        
    def runDay15():
        print('Greetings, boss!')

        def draw_grid(sensors, beacons, exclusions):
            s = ''
            for y in range (-2, 23):
                s += '\n'
                for x in range (-2, 26):
                    if (x, y) in sensors:
                        s+='S'
                    elif (x, y) in beacons:
                        s+='B'
                    elif (x, y) in exclusions:
                        s+=exclusions[(x, y)]
                    else:
                        s+= '.'
            print(s)
        
        # open file for reading
        filename = './inputs/15/input.txt'
        with open(filename,'r') as f:
            
            lines = f.readlines()
            sensors = {}
            beacons = {}

            for line in lines:
               reg_line = re.search("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", line)
               sensor_x = reg_line.group(1)
               sensor_y = reg_line.group(2)
               beacon_x = reg_line.group(3)
               beacon_y = reg_line.group(4)
               sensors[(int(sensor_x), int(sensor_y))] = (int(beacon_x), int(beacon_y))
               beacons[(int(beacon_x), int(beacon_y))] = 'B'
        
            # print(f'sensors: {sensors}')
            # print(f'beacons: {beacons}')

            x_search_max = 4000000
            y_search_max = 4000000
            exclusions = {}
            candidates = {}
            count = 0

            for s_pos, b_pos in sensors.items():
                # go over entire exclusion zone
                manh_dist = abs(b_pos[0] - s_pos[0]) + abs(b_pos[1] - s_pos[1])
                count += 1
                print(count)

                # draw entire exclusion
                # y_search = 20
                # for x in range(-manh_dist, manh_dist+1):
                #     for y in range(-(manh_dist-abs(x)), manh_dist-abs(x)+1):
                #         ex_pos = (s_pos[0] + x, s_pos[1]+y)
                #         if ex_pos not in sensors and ex_pos not in beacons:
                #             exclusions[ex_pos] = '#'

                # part one
                # y_search = 2000000
                # for x in range(s_pos[0]-manh_dist, s_pos[0]+manh_dist+1):
                #     scan_pos = (x, y_search)
                #     if (abs(scan_pos[0] - s_pos[0]) + abs(scan_pos[1] - s_pos[1]) <= manh_dist):
                #         if (scan_pos not in sensors and scan_pos not in beacons):
                #             exclusions[scan_pos] = '#'

                # part two - go over edges
                for x in range(max(0, s_pos[0]-manh_dist-1), min(x_search_max, s_pos[0]+manh_dist+2)):
                    y1 = s_pos[1] -(manh_dist-abs(x-s_pos[0])) - 1
                    y2 = s_pos[1] + manh_dist-abs(x-s_pos[0]) + 1
                    if (y1 >= 0 and y1 <= y_search_max):
                        candidate = (x, y1) 
                        far_enough = True
                        for s2_pos, b2_pos in sensors.items():
                            manh_dist2 = abs(b2_pos[0] - s2_pos[0]) + abs(b2_pos[1] - s2_pos[1])
                            cand_dist2 = abs(candidate[0] - s2_pos[0]) + abs(candidate[1] - s2_pos[1])
                            if (cand_dist2 <= manh_dist2):
                                far_enough = False
                                break
                        if(far_enough):
                            candidates[candidate] = '#'

                    if (y2 >= 0 and y2 <= y_search_max):
                        candidate = (x, y2) 
                        far_enough = True
                        for s2_pos, b2_pos in sensors.items():
                            manh_dist2 = abs(b2_pos[0] - s2_pos[0]) + abs(b2_pos[1] - s2_pos[1])
                            cand_dist2 = abs(candidate[0] - s2_pos[0]) + abs(candidate[1] - s2_pos[1])
                            if (cand_dist2 <= manh_dist2):
                                far_enough = False
                                break
                        if(far_enough):
                            candidates[candidate] = '#'

                print(f'canditate length: {len(candidates)}')
                
                
            print(f'canditates: {candidates}')
            # just for debug
            # draw_grid(sensors, beacons, exclusions)
            
            print(f'line count {len(lines)}')
            print(f'ex_count count {len(exclusions)}')
    def runDay16():
        def dijkstra(source, valves):
            dist = {}
            prev = {}
            q = {}
            for valve_name in valves: 
                dist[valve_name] = math.inf
                prev[valve_name] = None
                q[valve_name] = True
            dist[source] = 0

            while len(q) > 0:
                # u ← vertex in Q with min dist[u]
                # remove u from Q
                min = 1000000
                u_name = ''
                for q_name in q:
                    if dist[q_name] < min:
                        min = dist[q_name]
                        u_name = q_name
                del q[u_name]

                u = valves[u_name]
                for v in u.leads_to:
                    if v in q:
                        alt = dist[u_name] + 1
                        if alt < dist[v]:
                            dist[v] = alt
                            prev[v] = u_name

            return prev

        class Tunnels:
            def __init__(self):
                self.node_count = 0
                self.sub_tree_cache = {}
                self.results = {}
                self.evstates = ''

        class Valve:
            def __init__(self, name, rate, leads_to, index):
                self.name = name
                self.rate = rate
                self.leads_to = leads_to
                self.index = index
                self.edges = []
            def __str__(self):
                return f"{self.name}[{self.index}]: {self.rate} leads_to: {self.leads_to}"                       

        class Node:
            def get_max(ttime, name, valves, vstates, tunnels, tr) -> int:
                if (ttime >= 26):
                    old = tunnels.results.get(vstates)
                    if (old is None or (old is not None and tr > old)):
                        tunnels.results[vstates] = tr
                    return tr

                key = f'{ttime}-{name}-{vstates}-{tr}' # self.total_release
                
                cached = tunnels.sub_tree_cache.get(key)
                if (cached is not None):
                    return cached 

                if (vstates == tunnels.evstates):
                    tunnels.sub_tree_cache[key] = tr
                    return tr

                valve = valves[name]
                options = []
                if (vstates[valve.index] == '0' and valve.rate != 0): # closed
                    new_vstates = vstates[:(valve.index)] + '1' + vstates[(valve.index + 1):]
                    new_tr = tr + (26 - ttime) * valve.rate
                    val = Node.get_max(ttime+1, name, valves, new_vstates, tunnels, new_tr)
                    options.append(val)
                
                for edge in valve.edges:
                    next_valve_name = edge[0]
                    my_cost = edge[1]
                    val = Node.get_max(ttime+my_cost, next_valve_name, valves, vstates, tunnels, tr)
                    options.append(val)

                res = max(options)
                
                tunnels.sub_tree_cache[key] = res

                return res
 
        print('Greetings, boss!')
        
        # open file for reading
        filename = './inputs/16/input.txt'
        with open(filename,'r') as f:
            index = 0
            p_index = 0
            valves = {}
            primary_valves = {}
            for line in f:
                line = line.strip()
                
                reg_line = re.search("^Valve (.{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", line)
                name = reg_line.group(1)
                rate = int(reg_line.group(2))
                leads_to = [i.strip() for i in reg_line.group(3).split(',')]
                valves[name] = Valve(name, rate, leads_to, index)
                if rate > 0 or name == 'AA':
                    primary_valves[name] = Valve(name, rate, [], p_index)
                    p_index += 1
                index += 1
            
            for name_from in primary_valves:
                paths = dijkstra(name_from, valves)
                for name_to in primary_valves:
                    if (name_from == name_to):
                        continue
                    # print(f'searching path name_to {name_to} -> name_from {name_from}')
                    cost = 0
                    path_s = f'{name_to} >> '
                    next = paths[name_to]
                    while(next):
                        cost += 1
                        path_s += f'{next} >> '
                        if next in primary_valves:
                            break
                        next = paths[next]
                    if (next == None):
                        print(f'UNEXPECTED')
                    if (next == name_from):
                        valve_to = primary_valves[name_to]
                        valve_to.edges.append((name_from, cost))
                        # print(f'path exists: name_to {name_to} -> name_from {name_from}: cost {cost} path: {path_s}')
                    else:
                        pass
                        # print(f'NO PATH: name_to {name_to} -> name_from {name_from}: cost {cost} path: {path_s}')

            # string of all valve states is closed '0' in the beginning                    
            p_valve_states = [str(0) for v in primary_valves]
            p_valve_states_s = ''.join(p_valve_states)

            # expected states is all nonzero rate are open '1'
            expected_p_valve_states = [(str(1) if primary_valves[v].rate > 0 else str(0)) for v in primary_valves]
            expected_p_valve_states_s = ''.join(expected_p_valve_states)
      
            start = time.time()
            tunnels = Tunnels()
            tunnels.evstates = expected_p_valve_states_s

            # part one
            gmax = Node.get_max(1, 'AA', primary_valves, p_valve_states_s, tunnels, 0)
            print(f'max: {gmax} [{filename}]')

            # part two
            sum_max = 0
            for my_res in tunnels.results:
                for el_res in tunnels.results:
                    my_res_i = int(my_res,2)
                    el_res_i = int(el_res,2)
                    if (my_res_i & el_res_i == 0):
                        sum = tunnels.results[my_res] + tunnels.results[el_res]
                        if (sum > sum_max): 
                            sum_max = sum
                        # print(f'result: {my_res} {el_res} sum: {sum}')
            
            print(f'max sum: {sum_max}')
            
            end = time.time()
            print(f'time: {end - start}')
            
        print('done.')
    def runDay17():
        print('Greetings, boss!')
        
        def draw_cave(cave, c_width, rock, rock_offset):
            s = ''
            for i in range(0, (c_width * 40) if len(cave) > (c_width * 40) else len(cave)):
                if i >= rock_offset and ((i - rock_offset) < len(rock) and rock[i - rock_offset] == 1):
                    s += '@'
                elif cave[i] == 1:
                    s += '#' 
                elif cave[i] == 0:
                    s += '.'
                if (i+1) % c_width == 0:
                    s += '\n'
            print(s)
        
        # open file for reading
        filename = './inputs/17/input.txt'
        with open(filename,'r') as f:
            
            start = time.time()
            
            # load wind blowing directions
            lines = f.readlines()
            horizontal_push = lines[0].strip()
            
            # prepare cave and rock definitions
            cave_row_template =    [int(s) for s in list('100000001')]   
            cave_bottom_template = [int(s) for s in list('111111111')]
            rock_templates =     [([int(s) for s in list('1111')], 1),
                                  ([int(s) for s in list('010000000111000000010')], 3),
                                  ([int(s) for s in list('001000000001000000111')], 3),
                                  ([int(s) for s in list('1000000001000000001000000001')], 4),
                                  ([int(s) for s in list('11000000011')], 2)]
            
            # generate cave
            c_width = len(cave_row_template)
            # c_height = 7
            HEIGHT_BUFFER = 7
            cave = cave_row_template.copy()
            cave += cave_row_template.copy()
            cave += cave_row_template.copy()
            cave += cave_row_template.copy()
            cave += cave_row_template.copy()
            cave += cave_row_template.copy()
            cave += cave_row_template.copy()
            cave += cave_bottom_template.copy()
            draw_cave(cave, c_width, [], 0)

            tower_height = 0
            rock_count = 2022 # part 1
            rock_count = 1000000000000 # part 2

            pattern = {}
            i_rock = 0
            iteration = 0
            while (i_rock < rock_count):
                i_rock_mod = i_rock % len(rock_templates)
                rock_tpl = rock_templates[i_rock_mod]
                rock_height = rock_tpl[1]
                rock_shape = rock_tpl[0]
                rock_offset = 3 + (c_width * (4-rock_height))

                # draw_cave(cave, c_width, rock_shape, rock_offset)
                moving = True
                while(moving):
                    # test move sideways
                    iteration_mod = iteration % len(horizontal_push)
                    dir = horizontal_push[iteration_mod]
                    move = (1 if dir=='>' else -1)
                    iteration += 1 
                    test_offset = rock_offset + move
                    for i in range(len(rock_shape)):
                        if rock_shape[i] & cave[i + test_offset] == 1:
                            moving = False
                            break
                    
                    if moving:
                        rock_offset += move
            
                    # draw_cave(cave, c_width, rock_shape, rock_offset)

                    # test move down
                    moving = True
                    test_offset = rock_offset + c_width
                    for i in range(len(rock_shape)):
                        if rock_shape[i] & cave[i + test_offset] == 1:
                            moving = False
                            break
                    if moving:
                        rock_offset += c_width
                        # draw_cave(cave, c_width, rock_shape, rock_offset)
                    else:
                        rock_offset_h = rock_offset // c_width
                        
                        # write rock to cave
                        for i in range(len(rock_shape)):
                            if rock_shape[i] | cave[i + rock_offset] == 1:
                                cave[i + rock_offset] = 1
                        
                        # check row where we have stopped 
                        sectionX = ''.join(map(str,cave[rock_offset_h*c_width : rock_offset_h*c_width+c_width]))
                        
                        # if not HEIGHT_BUFFER row buffer, enlarge cave
                        for hx in range (rock_offset_h, HEIGHT_BUFFER):
                            cave = cave_row_template.copy() + cave
                            tower_height += 1
                        # draw_cave(cave, c_width, [], 0)

                        # if we have stopped with first flat rock as #.####..# 
                        # this MUST be the top of the tower
                        if (i_rock_mod == 0 and int(sectionX, 2) == 377):
                            if rock_offset_h >= HEIGHT_BUFFER:
                                exit(-1)
                            if (iteration_mod in pattern):
                                previous = pattern[iteration_mod]
                                height_diff = tower_height - previous[0]
                                rock_diff = i_rock - previous[1]
                                if (previous[2] is not None \
                                    and previous[2] != height_diff \
                                    and previous[3] != rock_diff):
                                    exit(-1) # panic!
                                pattern[iteration_mod] = (tower_height, i_rock, height_diff, rock_diff) 
                                print(f'found matching iteration {iteration_mod}: {height_diff}, {rock_diff}')
                                
                                if (i_rock + rock_diff < rock_count):
                                    iters = (rock_count - i_rock) // rock_diff
                                    tower_height += height_diff * iters
                                    i_rock += rock_diff * iters
                                    pattern.pop(iteration_mod)
                            else:
                                pattern[iteration_mod] = (tower_height, i_rock, None, None) 
                        break                
                i_rock += 1
                     
            # draw_cave(cave, c_width, tower_height, [], 0)    
            print(f'tower_heigh: {tower_height}')
            end = time.time()
            print(f'time: {end - start}')
    def runDay18():
        print('Greetings, boss!')
        
        def look_around(current, space, parent_type, mins, maxs):
            space[current] = parent_type # mark position in space with same color
            # groups[parent_type][current] = parent_type
            scan = [(current[0]+1, current[1], current[2])]
            scan.append((current[0]-1, current[1], current[2]))
            scan.append((current[0], current[1]+1, current[2]))
            scan.append((current[0], current[1]-1, current[2]))
            scan.append((current[0], current[1], current[2]+1))
            scan.append((current[0], current[1], current[2]-1))
            for s in scan:
                if s[0] < mins[0] or s[0] > maxs[0] or\
                   s[1] < mins[1] or s[1] > maxs[1] or\
                   s[2] < mins[2] or s[2] > maxs[2]:
                    continue

                if s not in space:
                    look_around(s, space, parent_type, mins, maxs)
        
        # open file for reading
        filename = './inputs/18/input.txt'
        with open(filename,'r') as f:
            
            start = time.time()
            
            lines = f.readlines()
            
            SOLID_SPACE = 0
            FREE_SPACE = 1
            UNCLAIMED_SPACE = 2
            space = {}
            for line in lines:
                dm = line.strip().split(',')
                space[int(dm[0]), int(dm[1]), int(dm[2])] = SOLID_SPACE
                print(f'cube: {dm}')

            open_faces = 0
            # print(f'grid: {grid}')
            keys = space.keys()
            minx = min(list(zip(*keys))[0]) - 1
            maxx = max(list(zip(*keys))[0]) + 1
            miny = min(list(zip(*keys))[1]) - 1
            maxy = max(list(zip(*keys))[1]) + 1
            minz = min(list(zip(*keys))[2]) - 1
            maxz = max(list(zip(*keys))[2]) + 1

            space_size = (maxx - minx + 1) * (maxy - miny + 1) * (maxz - minz + 1)
            print(f'space size {space_size}: {maxx - minx + 1} x {maxy - miny + 1} x {maxz - minz + 1}')
            
            for cube in space:
                x = cube[0]
                y = cube[1]
                z = cube[2]
                # groups[1][cube] = 1
                open_faces += (0 if ((x+1, y, z) in space) else 1)
                open_faces += (0 if ((x-1, y, z) in space) else 1)
                open_faces += (0 if ((x, y+1, z) in space) else 1)
                open_faces += (0 if ((x, y-1, z) in space) else 1)
                open_faces += (0 if ((x, y, z+1) in space) else 1)
                open_faces += (0 if ((x, y, z-1) in space) else 1)

            starter = (minx, miny, minz)
            space[starter] = FREE_SPACE
            process_list = [starter]

            while(len(process_list) > 0):
                cubes_to_process = process_list.copy()
                process_list.clear()
                for current in cubes_to_process:
                    # look around
                    scan = []
                    scan.append((current[0]+1, current[1], current[2]))
                    scan.append((current[0]-1, current[1], current[2]))
                    scan.append((current[0], current[1]+1, current[2]))
                    scan.append((current[0], current[1]-1, current[2]))
                    scan.append((current[0], current[1], current[2]+1))
                    scan.append((current[0], current[1], current[2]-1))
                    for s in scan:
                        # avoid outer space
                        if s[0] < minx or s[0] > maxx or\
                           s[1] < miny or s[1] > maxy or\
                           s[2] < minz or s[2] > maxz:
                            continue
                        # avoid solid cubes
                        if (s in space and space[s] == SOLID_SPACE):
                            continue
                        # unmarked space neightboring with our cube
                        if (s not in space):
                            space[s] = FREE_SPACE
                            process_list.append(s)
                        
            groups = {}
            groups[SOLID_SPACE] = 0
            groups[FREE_SPACE] = 0
            groups[UNCLAIMED_SPACE] = 0
            unclaimed_space = {}
            for x in range(minx, maxx + 1):
                for y in range(miny, maxy + 1):
                    for z in range(minz, maxz + 1):
                        cube = (x, y, z)
                        if (cube in space):
                            color = space[cube]
                            groups[color] += 1
                        else:
                            groups[UNCLAIMED_SPACE] += 1
                            unclaimed_space[cube] = UNCLAIMED_SPACE
                            
            internal_open_faces = 0
            for cube in unclaimed_space:
                x = cube[0]
                y = cube[1]
                z = cube[2]
                # groups[1][cube] = 1
                internal_open_faces += (0 if ((x+1, y, z) in unclaimed_space) else 1)
                internal_open_faces += (0 if ((x-1, y, z) in unclaimed_space) else 1)
                internal_open_faces += (0 if ((x, y+1, z) in unclaimed_space) else 1)
                internal_open_faces += (0 if ((x, y-1, z) in unclaimed_space) else 1)
                internal_open_faces += (0 if ((x, y, z+1) in unclaimed_space) else 1)
                internal_open_faces += (0 if ((x, y, z-1) in unclaimed_space) else 1)

            end = time.time()
            for gi in groups:
                g = groups[gi]
                print(f'group {gi}: {g}')   

            print(f'open_faces: {open_faces}')
            print(f'internal_open_faces: {internal_open_faces}')
            print(f'lines: {len(lines)}')
            print(f'time: {end - start}')
    def runDay19():
        print('Greetings, boss!')
        
        def search_dfs(time, robot_counts, resource_counts, blueprint, cache):
            TIME_LIMIT = 32
            if(time > TIME_LIMIT):
                return resource_counts["geode"]
            
            key = f"{time}-{robot_counts['ore']}-{robot_counts['clay']}-{robot_counts['obsidian']}-{robot_counts['geode']}-{resource_counts['ore']}-{resource_counts['clay']}-{resource_counts['obsidian']}"
            # key = f"{time}-{robot_counts['ore']}-{robot_counts['clay']}-{robot_counts['obsidian']}-{robot_counts['geode']}-{resource_counts['ore']}"
            
            cached = cache.get(key)
            if(cached is not None):
                return cached
            
            options = []
            # spend resources - to build ore robots
            if (resource_counts["ore"] >= blueprint["ore_robot_costs"] and\
                time + 1 < TIME_LIMIT and\
                # robot_counts["ore"] < blueprint["max_ore_cost"]):
                (TIME_LIMIT - time) * robot_counts["ore"] + resource_counts["ore"] < ((TIME_LIMIT - time) * blueprint["max_ore_cost"])):
                # we build ore robot
                new_resource_counts = resource_counts.copy()
                new_robot_counts = robot_counts.copy()
                
                new_robot_counts["ore"] += 1
                new_resource_counts["ore"] -= blueprint["ore_robot_costs"] 
                
                new_resource_counts["ore"] += robot_counts["ore"]
                new_resource_counts["clay"] += robot_counts["clay"]
                new_resource_counts["obsidian"] += robot_counts["obsidian"]
                new_resource_counts["geode"] += robot_counts["geode"]

                res = search_dfs(time + 1, new_robot_counts, new_resource_counts, blueprint, cache)
                options.append(res)

            if (resource_counts["ore"] >= blueprint["clay_robot_costs"] and\
                time + 1 < TIME_LIMIT and\
                # robot_counts["clay"] < blueprint["max_clay_cost"]):
                (TIME_LIMIT - time) * robot_counts["clay"] + resource_counts["clay"] < ((TIME_LIMIT - time) * blueprint["max_clay_cost"])):
                # we build clay robot
                new_resource_counts = resource_counts.copy()
                new_robot_counts = robot_counts.copy()
                
                new_robot_counts["clay"] += 1
                new_resource_counts["ore"] -= blueprint["clay_robot_costs"] 
                
                new_resource_counts["ore"] += robot_counts["ore"]
                new_resource_counts["clay"] += robot_counts["clay"]
                new_resource_counts["obsidian"] += robot_counts["obsidian"]
                new_resource_counts["geode"] += robot_counts["geode"]

                res = search_dfs(time + 1, new_robot_counts, new_resource_counts, blueprint, cache)
                options.append(res)

            if (resource_counts["ore"] >= blueprint["obsidian_robot_ore_costs"] and\
                resource_counts["clay"] >= blueprint["obsidian_robot_clay_costs"] and\
                time < TIME_LIMIT and\
                # robot_counts["obsidian"] < blueprint["max_obsidian_cost"]):
                (TIME_LIMIT - time) * robot_counts["obsidian"] + resource_counts["obsidian"] < ((TIME_LIMIT - time) * blueprint["max_obsidian_cost"])):
                
                # we build obsidian robot
                new_resource_counts = resource_counts.copy()
                new_robot_counts = robot_counts.copy()
                
                new_robot_counts["obsidian"] += 1
                new_resource_counts["ore"] -= blueprint["obsidian_robot_ore_costs"] 
                new_resource_counts["clay"] -= blueprint["obsidian_robot_clay_costs"] 
                
                new_resource_counts["ore"] += robot_counts["ore"]
                new_resource_counts["clay"] += robot_counts["clay"]
                new_resource_counts["obsidian"] += robot_counts["obsidian"]
                new_resource_counts["geode"] += robot_counts["geode"]

                res = search_dfs(time + 1, new_robot_counts, new_resource_counts, blueprint, cache)
                options.append(res)
            
            if (resource_counts["ore"] >= blueprint["geode_robot_ore_costs"] and\
                resource_counts["obsidian"] >= blueprint["geode_robot_obsidian_costs"] and\
                time < TIME_LIMIT):
                # we build geode robot
                new_resource_counts = resource_counts.copy()
                new_robot_counts = robot_counts.copy()
                
                new_robot_counts["geode"] += 1
                new_resource_counts["ore"] -= blueprint["geode_robot_ore_costs"] 
                new_resource_counts["obsidian"] -= blueprint["geode_robot_obsidian_costs"] 
                
                new_resource_counts["ore"] += robot_counts["ore"]
                new_resource_counts["clay"] += robot_counts["clay"]
                new_resource_counts["obsidian"] += robot_counts["obsidian"]
                new_resource_counts["geode"] += robot_counts["geode"]

                res = search_dfs(time + 1, new_robot_counts, new_resource_counts, blueprint, cache)
                options.append(res)
            

            # we build NO robot
            new_resource_counts = resource_counts.copy()
            new_robot_counts = robot_counts.copy()
                
            new_resource_counts["ore"] += robot_counts["ore"]
            new_resource_counts["clay"] += robot_counts["clay"]
            new_resource_counts["obsidian"] += robot_counts["obsidian"]
            new_resource_counts["geode"] += robot_counts["geode"]

            res = search_dfs(time + 1, new_robot_counts, new_resource_counts, blueprint, cache)
            options.append(res)

            max_val = max(options)
            cache[key] = max_val
            return max_val

        def analyse_blueprint(id, blueprint):
            
            robot_counts = {}
            robot_counts["ore"] = 1
            robot_counts["clay"] = 0
            robot_counts["obsidian"] = 0
            robot_counts["geode"] = 0
            
            resource_counts = {}
            resource_counts["ore"] = 0
            resource_counts["clay"] = 0
            resource_counts["obsidian"] = 0
            resource_counts["geode"] = 0

            blueprint["max_ore_cost"] = max(blueprint["ore_robot_costs"],\
                                            blueprint["clay_robot_costs"],\
                                            blueprint["obsidian_robot_ore_costs"],\
                                            blueprint["geode_robot_ore_costs"])
            blueprint["max_clay_cost"] = blueprint["obsidian_robot_clay_costs"]
            blueprint["max_obsidian_cost"] = blueprint["geode_robot_obsidian_costs"]

            cache = {}

            res = search_dfs(1, robot_counts, resource_counts, blueprint, cache)
            # search_strategy(robot_counts, resource_counts, blueprint)

            print(f'max: {res}')
            return int(id) * res

        # open file for reading
        filename = './inputs/19/input_2.txt'
        with open(filename,'r') as f:
         
            start = time.time() 
            lines = f.readlines()
            
            blueprints = {}
            for line in lines:                
                reg = re.search("^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$", line)
                
                blueprint = {}
                blueprint["id"] = int(reg.group(1))
                blueprint["ore_robot_costs"] = int(reg.group(2))
                blueprint["clay_robot_costs"] = int(reg.group(3))
                blueprint["obsidian_robot_ore_costs"] = int(reg.group(4))
                blueprint["obsidian_robot_clay_costs"] = int(reg.group(5))
                blueprint["geode_robot_ore_costs"] = int(reg.group(6))
                blueprint["geode_robot_obsidian_costs"] = int(reg.group(7))
                
                print(f'blueprint: {blueprint}')
                blueprints[blueprint["id"]] = blueprint

            total_quality = 0
            for id in blueprints:
                blueprint = blueprints[id]
                print(f'analysing blueprint {id}')
                total_quality += analyse_blueprint(id, blueprint)
                
            end = time.time()
            print(f'lines: {len(lines)}')
            print(f'time: {end - start}')
            print(f'total_quality: {total_quality}')
    def runDay20():
        print('Greetings, boss!')
        
        def get_vals(values, indices):
            return ", ".join(str(values[i]) for i in indices)
        
        def mix(values, indices, i):
            v = values[i]
            if v < 0:
                v = ( -1 * (abs(v) % (len(values)-1)) + len(values) - 1 ) 
            if v < 0:
                exit(-1)
            oi = indices.index(i)
            ni = (oi + v) % (len(values) - 1)
            indices.insert(ni + (1 if ni > oi else 0), i)
            vallll = indices.pop(oi + 1 if (ni < oi) else oi)
            # print(get_vals(values, indices))
            if vallll != i:
                exit(-1)

        # open file for reading
        filename = './inputs/20/input.txt'
        with open(filename,'r') as f:
         
            start = time.time() 
            lines = f.readlines()

            decryption_key = 811589153

            values = []
            for line in lines:                
                value = decryption_key * int(line.strip())
                values.append(value)
            indices = list(range(0, len(values)))

            print(get_vals(values, indices))

            # the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            for i in range(0, len(values)):
                mix(values, indices, i)
            
            print(get_vals(values, indices))

            mixed = []
            for i in range(0, len(values)):
                mixed.append(values[indices[i]])

            # print(mixed)
            index_of_zero = mixed.index(0)
            print(f'index of 0: {index_of_zero}')

            v1 = mixed[(1000 + index_of_zero) % len(values)]
            v2 = mixed[(2000 + index_of_zero) % len(values)]
            v3 = mixed[(3000 + index_of_zero) % len(values)]
            out = v1 + v2 + v3
                
            end = time.time()
            print(f'time: {end - start}')
            print(f'lines: {len(lines)}')
            print(f'input: {len(values)}')
            print(f'coords: {out}')
    def runDay21():
        print('Greetings, boss!')
        
        # open file for reading
        filename = './inputs/21/input.txt'
        with open(filename,'r') as f:
         
            start = time.time() 
            lines = f.readlines()

            monkeys = {}
            for line in lines:                
                
                reg = re.search("^(.+): (.*)$", line)
                name = reg.group(1)
                value = reg.group(2)
                monkeys[name] = value
            
            print(monkeys)

            eval_input = monkeys["root"]
            
            stuff_to_replace = True
            while(stuff_to_replace):
                stuff_to_replace = False
                for m in monkeys:
                    if eval_input.find(m) > -1:
                        stuff_to_replace = True
                        replacement_str = f'({monkeys[m]})'
                        eval_input = eval_input.replace(m, replacement_str)

            eval_input_left = eval_input.split('==')[0] #str(simplify())
            eval_input_right = eval_input.split('==')[1]
            eval_input_right = str(int(eval(eval_input_right)))
            eval_input_left = str(simplify(eval_input_left))
            eval_input = eval_input_left + " == " + eval_input_right
            
            end = time.time()
            print(f'time: {end - start}')
            print(f'lines: {len(lines)}')
            print(f'result: {eval_input}')
    def runDay22():
        print('Greetings, boss!')
        
        heading = {
            0: (1, 0),
            90: (0, -1),
            180: (-1, 0),
            270: (0, 1)
        }

        out = {
            0: 0,
            90: 3,
            180: 2,
            270: 1
        }

        def draw_board(rm, cm, board, highlight = (0,0), markers = {}):
            s = '\n -- board: --\n'
            for r in range(1, rm + 1):
                for c in range(1, cm + 1):
                    if (c, r) in markers:
                        s += markers[(c, r)]
                    elif (c, r) == highlight:
                        s += 'X'
                    elif (c, r) in board:
                        s += board[(c, r)]['type']
                    else:
                        s += ' '
                s += '\n'
            print(s)

        def find_free_path_limit(tile_pos, board, diff, c_max, r_max, move):
            nxt = tile_pos
            crn = (nxt[0], nxt[1])
            while(move >= 0):
                move -= 1
                crn = (nxt[0], nxt[1])
                nxt = ((nxt[0] + diff[0] - 1) % c_max + 1, (nxt[1] + diff[1] - 1) % r_max + 1)
                # draw_board(r_max, c_max, board, nxt)
                    
                nxt_tile = board.get(nxt)
                if(nxt_tile is None):
                    # draw_board(r_max, c_max, board, nxt)
                    while (nxt not in board):
                        nxt = ((nxt[0] + diff[0] - 1) % c_max + 1, (nxt[1] + diff[1] - 1) % r_max + 1)
                    nxt_tile = board.get(nxt)
                
                if nxt_tile['type'] == '.':
                    continue
                elif nxt_tile['type'] == '#':
                    break
            return (crn, '#', None)

        def find_free_path_limit_part2(tile_pos, direction, board, c_max, r_max, move, edges, command):
            nxt = tile_pos
            crn = (nxt[0], nxt[1])
            diff = heading[direction]
            while(move > 0):
                print(command)
                # draw_board(r_max, c_max, board, crn)
                # input("Press Enter to continue...")

                if (crn, direction) in edges:
                    #  print('hell yeah')
                    edge_change = edges[crn, direction]
                    nxt = (edge_change['to'][0], edge_change['to'][1])
                    nxt_tile = board.get(nxt)
                    if nxt_tile['type'] == '.': # only if moving to another cube side, change the direction
                        direction = edge_change['dir']
                        diff = heading[direction]
                else:
                    nxt = ((nxt[0] + diff[0]), (nxt[1] + diff[1]))
                
                nxt_tile = board.get(nxt)
                if nxt_tile['type'] == '#':
                    break
                crn = (nxt[0], nxt[1])
                move -= 1
                
            return (crn, '#', direction)

        start = time.time() 

        # open file for reading
        filename = './inputs/22/edges.txt'
        with open(filename,'r') as f:
         
            edges_s = f.readlines()

        # open file for reading
        filename = './inputs/22/input.txt'
        with open(filename,'r') as f:
         
            lines = f.readlines()

            # read the board
            board = {}
            r = 0
            c_max = 1
            initial_pos = None
            for line in lines:                
                r += 1
               
                if line == '\n':
                    break
                
                c = 1
                for i in line:
                    if i == '\n':
                        continue
                    elif i == ' ':
                        pass
                    elif i == '.':
                        board[(c, r)] = { 'type': '.'}
                        if initial_pos is None:
                            initial_pos = (c, r)
                    elif i == '#':
                        board[(c, r)] = { 'type': '#'}
                    if (c > c_max):
                        c_max = c
                    c += 1
            r_max = r - 1
            
            # read the path
            path_s = lines[-1]
            path = []
            reg_list = regex.findall("(-?\d+|[R,L])", path_s)
            for item in reg_list:
                path.append(item)

            # read edges
            edges = {}
            markers = {}
            for edge_s in edges_s:
                parts = edge_s.strip().split(',')
                start_c_fr = int(parts[0])
                start_c_to = int(parts[1])
                start_r_fr = int(parts[2])
                start_r_to = int(parts[3])
                dir_orig = int(parts[4])
                end_c_fr = int(parts[5])
                end_c_to = int(parts[6])
                end_r_fr = int(parts[7])
                end_r_to = int(parts[8])
                dir_change = int(parts[9])
                mark = parts[10]
                if start_c_fr == start_c_to: # column is constant
                    from_range = range(start_r_fr, start_r_to+1) if start_r_to > start_r_fr else range(start_r_fr, start_r_to-1, -1)
                else: # row is constant
                    from_range = range(start_c_fr, start_c_to+1) if start_c_to > start_c_fr else range(start_c_fr, start_c_to-1, -1)

                if end_c_fr == end_c_to: # column is constant
                    to_range = range(end_r_fr, end_r_to+1) if end_r_to > end_r_fr else range(end_r_fr, end_r_to-1, -1)
                else: # row is constant
                    to_range = range(end_c_fr, end_c_to+1) if end_c_to > end_c_fr else range(end_c_fr, end_c_to-1, -1)

                for item in zip(from_range, to_range):
                    from_pos = (start_c_to, item[0]) if start_c_fr == start_c_to else (item[0], start_r_to)
                    to_pos = (end_c_to, item[1]) if end_c_fr == end_c_to else (item[1], end_r_to)
                    
                    edges[ from_pos, dir_orig ] = { 'to': to_pos, 'dir': dir_change}
                    markers[from_pos] = mark

            draw_board(r_max, c_max, board, (0, 0), markers)

            # process path
            position = initial_pos
            direction = 0
            for command in path:
                h = heading[direction]
                # print(command)
                if command.isnumeric():
                    move = int(command)
                    p = find_free_path_limit(position, board, h, c_max, r_max, move)  
                    position = p[0]
                    # draw_board(r_max, c_max, board, position)
                elif command == 'R':
                    direction -= 90
                elif command == 'L':
                    direction += 90
                direction = direction % 360
                
            res = out[direction] + 1000 * position[1] + 4 * position[0]
            print(f'res part 1: {res}')

            # process path part 2
            position = initial_pos
            direction = 0
            for command in path:
                print(command)
                if command.isnumeric():
                    move = int(command)
                    p = find_free_path_limit_part2(position, direction, board, c_max, r_max, move, edges, command)
                    position = p[0]
                    direction = p[2]
                    # draw_board(r_max, c_max, board, position)
                elif command == 'R':
                    direction -= 90
                elif command == 'L':
                    direction += 90
                direction = direction % 360
                
            res = out[direction] + 1000 * position[1] + 4 * position[0]
            print(f'res part 2: {res}')

            end = time.time()
            # print(f'path: {path}')
            print(f'time: {end - start}')
            print(f'lines: {len(lines)}')
    def runDay23():
        print('Greetings, boss!')
        
        def draw_grove(elves, x_dim, y_dim):
            s = '\n-- grove: --\n'
            for y in range(y_dim[0], y_dim[1] + 1):
                for x in range(x_dim[0], x_dim[1] + 1):         
                    if (x, y) in elves:
                        s += '#'
                    else:
                        s += '.'
                s += '\n'
            print(s)

        def look_direction(direction, elves):
            if direction == 'N' and\
                (e_p[0]-1, e_p[1]-1) not in elves and\
                (e_p[0],   e_p[1]-1) not in elves and\
                (e_p[0]+1, e_p[1]-1) not in elves:
                return (e_p[0],   e_p[1]-1)
            elif direction == 'S' and\
                (e_p[0]-1, e_p[1]+1) not in elves and\
                (e_p[0],   e_p[1]+1) not in elves and\
                (e_p[0]+1, e_p[1]+1) not in elves:
                return (e_p[0],   e_p[1]+1)
            elif direction == 'W' and\
                (e_p[0]-1, e_p[1]-1) not in elves and\
                (e_p[0]-1, e_p[1]) not in elves and\
                (e_p[0]-1, e_p[1]+1) not in elves:
                return (e_p[0]-1, e_p[1])
            if direction == 'E' and\
                (e_p[0]+1, e_p[1]-1) not in elves and\
                (e_p[0]+1, e_p[1]) not in elves and\
                (e_p[0]+1, e_p[1]+1) not in elves:
                return (e_p[0]+1, e_p[1])
            return None


        # open file for reading
        filename = './inputs/23/input.txt'
        with open(filename,'r') as f:
         
            start = time.time() 
            lines = f.readlines()

            elves = {}
            x_dim = (0, len(lines[0]) - 1)
            y_dim = (0, len(lines) - 1 )
            for y, line in enumerate(lines):                
                for x, col in enumerate(line.strip()):
                    if col == '#':
                        elves[x, y] = None


            # draw_grove(elves, x_dim, y_dim)

            directions = [ 'N', 'S', 'W', 'E']
            dir_i = 0

            moving = True
            round = 1
            while(moving):
                moving = False
                print(f'round [{round}] current direction: {directions[dir_i]}')
                
                for e_p in elves:
                    # If no other Elves are in one of those eight positions, the Elf does not do anything during this round
                    if (e_p[0]+1, e_p[1]+1) not in elves and\
                       (e_p[0]+1, e_p[1]) not in elves and\
                       (e_p[0]+1, e_p[1]-1) not in elves and\
                       (e_p[0], e_p[1]+1) not in elves and\
                       (e_p[0], e_p[1]-1) not in elves and\
                       (e_p[0]-1, e_p[1]+1) not in elves and\
                       (e_p[0]-1, e_p[1]) not in elves and\
                       (e_p[0]-1, e_p[1]-1) not in elves:
                       continue

                    # propose new positions
                    for look_i in range(0, len(directions)):
                        look_dir = directions[(look_i + dir_i) % len(directions)]
                        proposed = look_direction(look_dir, elves)
                        if proposed is not None:
                            elves[e_p] = proposed
                            break

                  
                # get all proposed positions counts
                all_proposed = {}
                for e_p in elves:
                    if elves[e_p] is not None:
                        proposed = elves[e_p]
                        if proposed in all_proposed:
                            all_proposed[proposed] += 1
                        else:
                            all_proposed[proposed] = 1
                
                # move elves
                new_elves = {}
                for e_p in elves:
                    if elves[e_p] is None:
                        new_elves[e_p] = None # just copy
                    elif all_proposed[elves[e_p]] == 1:
                        new_elves[elves[e_p]] = None # move to new position 
                        moving = True
                    elif all_proposed[elves[e_p]] > 1:
                        new_elves[e_p] = None # just copy # If two or more Elves propose moving to the same position, none of those Elves move.
                    else:
                        exit(-1)

                elves = new_elves
                x_dim = (0,0)
                y_dim = (0,0)
                for e_p in elves:
                    x_dim = (min(x_dim[0], e_p[0]), max(x_dim[1], e_p[0]))
                    y_dim = (min(y_dim[0], e_p[1]), max(y_dim[1], e_p[1]))

                # draw_grove(elves, x_dim, y_dim)
                print(f'empty tiles: {(x_dim[1] - x_dim[0] + 1) * (y_dim[1] - y_dim[0] + 1) - len(elves)}')
                dir_i = (dir_i + 1) % len(directions)
                round += 1 
            
            end = time.time()
            print(f'time: {end - start}')
            print(f'lines: {len(lines)}')
    def runDay24():
        print('Greetings, boss!')
        
        def compute_board(time, blizzards, size):
            board = {}
            for bl in blizzards:
                pos = (bl[0], bl[1])
                if bl[2] == '>': # moving right
                    pos = ((bl[0] + time) % size[0], (bl[1]))
                elif bl[2] == '<': # moving left
                    pos = ((bl[0] - time) % size[0], (bl[1]))
                elif bl[2] == 'v': # moving down
                    pos = ((bl[0]), (bl[1] + time) % size[1])
                elif bl[2] == '^': # moving up
                    pos = ((bl[0]), (bl[1] - time) % size[1])

                if pos in board and  type(board[pos]) == int:
                    board[pos] += 1
                elif pos in board:
                    board[pos] = 2
                else:
                    board[pos] = bl[2]
            return board

        def draw_board(time, board, entry, exit, size, p):
            s = '\n'
            for chr in range(0, size[0]):
                if ((chr, -1) == p):
                    s += 'E'
                elif ((chr, -1) == entry):
                    s += '.'
                else:
                    s += '#'

            s += '\n'
            for y in range(0, size[1]):
                for x in range(0, size[0]):
                    b = board.get((x,y))
                    if (x,y) == p:
                        s += 'E'
                    elif b is None:
                        s += '.'
                    else:
                        s += str(b)
                s += '\n'

            for chr in range(0, size[0]):
                if ((chr, size[1]) == p):
                    s += 'E'
                elif ((chr, size[1]) == exit):
                    s += '.'
                else:
                    s += '#'
            
            s += '\n'

            print(f'minute: {time}')
            print(s)

        def bfs(time, start, blizzards, end):
            processing = [(time, start[0], start[1])]
            cache = {}
            b_cache = {}
            # do bfs
            while(len(processing) > 0):
                
                # maybe also take time % repeating of blizzards
                current = processing.pop(0)
                tm = current[0]
                p = (current[1], current[2])

                key = f'{tm}'
                board = b_cache.get(key)
                if (board is not None):
                    pass
                else:
                    board = compute_board(tm, blizzards, size)
                    b_cache[key] = board
                    # print(len(b_cache))
                
                # draw_board(tm, board, entry, exit, size, p)
                # input()

                if (p[0], p[1] + 1) == end:
                    return tm
                if (p[0], p[1] - 1) == end:
                    return tm

                key = f'{tm}-{p}'
                el = cache.get(key)
                if (el is not None):
                    continue
                cache[key] = True

                # look down
                if ((p[0], p[1] + 1) == end or
                    (p[1]+1 < size[1] and ((p[0], p[1]+1)) not in board)):
                    processing.append((tm+1, p[0], p[1]+1))
                # look right
                if (p[1] >= 0 and p[1] < size[1] and p[0]+1 < size[0] and ((p[0]+1, p[1])) not in board):
                    processing.append((tm+1, p[0]+1, p[1]))
                # look up
                if ((p[0], p[1] - 1) == end or
                    (p[1]-1 >= 0 and ((p[0], p[1]-1)) not in board)):
                    processing.append((tm+1, p[0], p[1]-1))
                # look left
                if (p[1] >= 0 and p[1] < size[1] and p[0]-1 >= 0 and ((p[0]-1, p[1])) not in board):
                    processing.append((tm+1, p[0]-1, p[1]))
                # wait
                if ((p[0], p[1]) not in board):
                    processing.append((tm+1, p[0], p[1]))


        # open file for reading
        filename = './inputs/24/input.txt'
        with open(filename,'r') as f:
         
            start = time.time() 
            lines = f.readlines()

            blizzards = []
            entry = (0,0)
            exit = (0,0)
            size = (0,0)

            for y, line in enumerate(lines):                
                line = line.strip()
                if y == 0: # entry line
                    x = line.find('.')
                    entry = (x-1, y-1)
                    size = (len(line) - 2, len(lines) - 2)
                elif y == len(lines) - 1: # exit line
                    x = line.find('.')
                    exit = (x-1, y-1)
                
                for x, chr in enumerate(line):
                    if chr in ['>', '<', '^', 'v']:
                        blizzards.append((x-1, y-1, chr))
            

            min_time = bfs(1, entry, blizzards, exit)   
            print(f'min_time: {min_time}')

            min_time2 = bfs(min_time, exit, blizzards, entry)   
            print(f'min_time: {min_time2 - min_time}')

            min_time3 = bfs(min_time2, entry, blizzards, exit)   
            print(f'min_time: {min_time3 - min_time2}')

            end = time.time()
            print(f'time: {end - start}')
            print(f'lines: {len(lines)}')
    def runDay25():
        print('Greetings, boss!')
        m = {
            "2": 2,
            "1": 1,
            "0": 0,
            "-": -1,
            "=": -2,
        }
        r = {
            4: "2",
            3: "1",
            2: "0",
            1: "-",
            0: "="
        }
        def snafu_to_decimal(snafu_str):
            value = 0
            for idx, snafu_digit in enumerate(snafu_str[::-1]):
                # print(f'snafu_digit: {snafu_digit} -> {m[snafu_digit]} power: {5 ** (idx)}')
                value += m[snafu_digit] * 5 ** (idx)
            # print(snafu_str, '->', value)
            return value

        def decimal_to_snafu(decimal_amnt):
            s_str = ''
            MAX_DIGITS = 20
            decimal_amnt += (5**MAX_DIGITS) // 2
            for idx in range (0, MAX_DIGITS): # number of snafu digits
                digit = ((decimal_amnt) % (5**(idx+1))) // (5**idx)
                s_str = str(r[digit]) + s_str
                decimal_amnt -= digit
           
            return s_str
        
        # open file for reading
        filename = './inputs/25/input.txt'
        with open(filename,'r') as f:
         
            start = time.time() 
            lines = f.readlines()

            decimal_sum = 0
            for line in lines:                
                decimal_sum += snafu_to_decimal(line.strip())

            snafu_sum = decimal_to_snafu(decimal_sum)

            for i in range(1, 501):
                ss = decimal_to_snafu(i)
                dd = snafu_to_decimal(ss)           
                if i != dd:
                    print(f'i: {i}, snafu: {ss}, dec: {dd}, [{dd==i}]')
                    break

            end = time.time()
            print(f'time: {end - start}')
            print(f'lines: {len(lines)}')
            print(f'result: {snafu_sum}')           

if __name__ == '__main__':
    Aoc202201.runDay25()

