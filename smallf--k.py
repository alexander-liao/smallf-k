import sys

def BFinterpret(commands):
	print(''.join('+-,.<>[]'[command] for command in commands))
	tape = [0]
	pointer = 0
	index = 0
	while index < len(commands):
		if commands[index] == 0:
			tape[pointer] += 1
		elif commands[index] == 1:
			tape[pointer] -= 1
		elif commands[index] == 2:
			tape[pointer] = sys.stdin.read(1)
		elif commands[index] == 3:
			print(chr(tape[pointer]), end = '')
		elif commands[index] == 4:
			pointer -= 1
			while pointer < 0:
				tape.insert(0, 0)
				pointer += 1
		elif commands[index] == 5:
			pointer += 1
			while pointer >= len(tape):
				tape.append(0)
		elif commands[index] == 6 and not tape[pointer]:
			brackets = 1
			while brackets:
				index += 1
				if commands[index] == 6:
					brackets += 1
				elif commands[index] == 7:
					brackets -= 1
			index += 1
		elif commands[index] == 7 and tape[pointer]:
			brackets = 1
			while brackets:
				index -= 1
				if commands[index] == 6:
					brackets -= 1
				elif commands[index] == 7:
					brackets += 1
		index += 1
	print()

def interpret(code):
	command = 0
	commands = []
	for char in code:
		if ord(char) % 2:
			command = (command + 1) % 8
		else:
			commands.append(command)
	BFinterpret(commands)

if sys.argv[1:]:
	with open(sys.argv[1], 'r') as f:
		interpret(f.read)
else:
	while True:
		interpret(input())
