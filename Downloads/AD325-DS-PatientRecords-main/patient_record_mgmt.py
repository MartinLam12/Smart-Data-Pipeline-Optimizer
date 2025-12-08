from binary_search_tree import Node, BinarySearchTree
import csv
import graphviz


class PatientRecord:
    # Holds all the information for a single patient
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

class PatientRecordManagementSystem:
    def __init__(self):
        # Create self.bst = BinarySearchTree()
        self.bst = BinarySearchTree()
    
    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        # Create PatientRecord, create Node, insert into BST
        patient_record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        node = Node(patient_id, patient_record)
        self.bst.insert(node)
    
    def search_patient_record(self, patient_id):
        # Use self.bst.search()
        node = self.bst.search(patient_id)
        if node is None:
            # Return the PatientRecord
            return None 
        else:
            # Not found
            return node.value
    
    def delete_patient_record(self, patient_id):
        # Use self.bst.remove()
        self.bst.remove(patient_id)
    
    def display_all_records(self):
        # Use inorder traversal, print each patient
        for node in self.bst.inorder_traversal(self.bst.root):
            patient = node.value
            print(f"Patient ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Diagnosis: {patient.diagnosis}, "
                  f"Blood Pressure: {patient.blood_pressure}, Pulse: {patient.pulse}, Body Temperature: {patient.body_temperature}")
    
    def build_tree_from_csv(self, file_path):
        # Read CSV, add each patient
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # Each row has: [PatientID, Name, Age, Diagnosis, BloodPressure, Pulse, BodyTemperature]
                patient_id = int(row[0])      # Convert ID from string to int
                name = row[1]                 # Patient name stays as a string
                age = int(row[2])             # Age stored as an int
                diagnosis = row[3]            # Diagnosis as a string
                blood_pressure = row[4]       # Blood pressure string like "120/80"
                pulse = int(row[5])           # Pulse converted to int
                body_temperature = float(row[6])  # Temperature stored as float
                # Insert this patient into the BST
                self.add_patient_record(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
    
    def visualize_tree(self):
        # Create a Graphviz Digraph object to visualize the BST
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        return dot

    
    def _add_nodes(self, dot, node):
        # Recursively add nodes and edges to the Graphviz Digraph
        if node:
            # Each node is labeled with the patient ID and patient name
            dot.node(str(node.key), f"{node.key}: {node.value.name}")
            # If there is a left child, draw an edge and recurse down the left subtree
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            # If there is a right child, draw an edge and recurse down the right subtree
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)


