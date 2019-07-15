import random, math

# randomly create a 2-dimensional quantum state
def random_quantum_state():
	first_entry = random.randrange(101)
	first_entry = first_entry/100
	first_entry = first_entry**0.5 
	if random.randrange(2) == 0: 
		first_entry = -1 * first_entry
	second_entry = 1 - (first_entry**2)
	second_entry = second_entry**0.5
	if random.randrange(2) == 0: 
		second_entry = -1 * second_entry
	return [first_entry,second_entry]
	
# randomly create a 2-dimensional quantum state	
def random_quantum_state2():
	angle_degree = random.randrange(360)
	angle_radian = math.pi * angle_degree / 180
	return [math.cos(angle_radian),math.sin(angle_radian)]	
	
# finding the angle of a 2-dimensional quantum state
def angle_quantum_state(x,y):
	angle_radian = math.acos(x) # radian of the angle with state |0>
	angle_degree = 360*angle_radian/(2*math.pi) # degree of the angle with state |0>
	# if the second amplitude is negative, 
	#     then angle is (-angle_degree)
	#     or equivalently 360 + (-angle_degree)
	if y<0: angle_degree = 360-angle_degree # degree of the angle
	# else degree of the angle is the same as degree of the angle with state |0>
	return angle_degree	
	
def oracle1(circuit,quantum_reg,number):
    # prepare ancilla qubit
    # circuit.x(quantum_reg[2])
    # circuit.h(quantum_reg[2])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number < 2):
        circuit.x(quantum_reg[1])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[2])
    if(number < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    # put ancilla qubit back into state |0>
    # circuit.h(quantum_reg[2])
    # circuit.x(quantum_reg[2])

def oracle2(circuit,quantum_reg,number):
    # prepare ancilla qubit
    circuit.x(quantum_reg[4])
    circuit.h(quantum_reg[4])

    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number < 4):
        circuit.x(quantum_reg[2])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[3])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[4])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[3])
    if(number < 4):
        circuit.x(quantum_reg[2])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])

    # put ancilla qubit back into state |0>
    circuit.h(quantum_reg[4])
    circuit.x(quantum_reg[4])

def oracle3(circuit,quantum_reg,number):
    # prepare ancilla qubit
    circuit.x(quantum_reg[6])
    circuit.h(quantum_reg[6])

    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%8 < 4):
        circuit.x(quantum_reg[2])
    if(number < 8):
        circuit.x(quantum_reg[3])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[6])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])
    if(number < 8):
        circuit.x(quantum_reg[3])
    if(number%8 < 4):
        circuit.x(quantum_reg[2])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])

    # put ancilla qubit back into state |0>
    circuit.h(quantum_reg[6])
    circuit.x(quantum_reg[6])

def diffusion1(circuit,quantum_reg):
    #step 1
    # circuit.x(quantum_reg[2])
    # circuit.h(quantum_reg[2])
    
    #step 2
    circuit.h(quantum_reg[1])
    circuit.h(quantum_reg[0])
    circuit.x(quantum_reg[1])
    circuit.x(quantum_reg[0])

    #step 3
    circuit.ccx(quantum_reg[1],quantum_reg[0],quantum_reg[2])

    #step 4
    circuit.x(quantum_reg[1])
    circuit.x(quantum_reg[0])
    circuit.h(quantum_reg[1])
    circuit.h(quantum_reg[0])

    #step 5
    # circuit.h(quantum_reg[2])
    # circuit.x(quantum_reg[2])
    
    #step 6
    circuit.z(quantum_reg[0])
    circuit.x(quantum_reg[0])
    circuit.z(quantum_reg[0])
    circuit.x(quantum_reg[0])

def diffusion2(circuit,quantum_reg):
    circuit.x(quantum_reg[4])
    circuit.h(quantum_reg[4])

    for i in range(3):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])

    circuit.ccx(quantum_reg[1],quantum_reg[0],quantum_reg[3])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[4])
    circuit.ccx(quantum_reg[1],quantum_reg[0],quantum_reg[3])

    for i in range(3):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])

    circuit.h(quantum_reg[4])
    circuit.x(quantum_reg[4])
    
    circuit.z(quantum_reg[0])
    circuit.x(quantum_reg[0])
    circuit.z(quantum_reg[0])
    circuit.x(quantum_reg[0])

def diffusion3(circuit,quantum_reg):
    circuit.x(quantum_reg[6])
    circuit.h(quantum_reg[6])

    for i in range(4):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])

    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[6])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])

    for i in range(4):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])

    circuit.h(quantum_reg[6])
    circuit.x(quantum_reg[6])
    
    circuit.z(quantum_reg[0])
    circuit.x(quantum_reg[0])
    circuit.z(quantum_reg[0])
    circuit.x(quantum_reg[0])