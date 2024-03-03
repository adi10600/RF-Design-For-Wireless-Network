import tkinter as tk
from tkinter import ttk
import random
import math

class Device:
    def __init__(self, device_type, location):
        self.device_type = device_type
        self.location = location
        self.signal_strength = 0
        self.channel = None
        self.authenticated = False
        self.current_cell = None

    def calculate_signal_strength(self, other_device):
        distance = math.sqrt((self.location[0] - other_device.location[0])**2 + (self.location[1] - other_device.location[1])**2)
        if distance > 0:
            self.signal_strength = random.uniform(30, 100) - 20 * math.log10(distance)
        else:
            self.signal_strength = 30

class Cell:
    def __init__(self, center, range):
        self.center = center
        self.range = range

    def is_within_range(self, location):
        distance = math.sqrt((self.center[0] - location[0])**2 + (self.center[1] - location[1])**2)
        return distance <= self.range

class ChannelAssignment:
    def __init__(self):
        self.available_channels = [1, 6, 11]

    def assign_channel(self, device):
        device.channel = random.choice(self.available_channels)

class HandoffManagement:
    def __init__(self, handoff_threshold):
        self.handoff_threshold = handoff_threshold

    def perform_handoff(self, device, other_device, cells):
        for cell in cells:
            if cell.is_within_range(device.location):
                device.current_cell = cells.index(cell) + 1

            if cell.is_within_range(other_device.location):
                other_device.current_cell = cells.index(cell) + 1

        if device.signal_strength < self.handoff_threshold and other_device.signal_strength > self.handoff_threshold:
            device.channel = other_device.channel

class Authentication8021x:
    def __init__(self):
        self.protocol = "802.1x"
        self.user_credentials = {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3'}

    def authenticate_device(self, device, username, password):
        if username in self.user_credentials and password == self.user_credentials[username]:
            device.authenticated = True

class WWLANSimulator:
    def __init__(self, handoff_threshold=60, cell_ranges=(30, 30, 30)):
        self.devices = []
        self.cells = [Cell(center=(0, 0), range=cell_ranges[0]),
                      Cell(center=(50, 0), range=cell_ranges[1]),
                      Cell(center=(0, 50), range=cell_ranges[2])]
        self.channel_assignment = ChannelAssignment()
        self.handoff_management = HandoffManagement(handoff_threshold)
        self.authentication = Authentication8021x()

    def add_device(self, device):
        self.devices.append(device)

    def simulate_network(self):
        for device in self.devices:
            for other_device in self.devices:
                if device != other_device:
                    device.calculate_signal_strength(other_device)

            self.channel_assignment.assign_channel(device)

            for other_device in self.devices:
                if device != other_device:
                    self.handoff_management.perform_handoff(device, other_device, self.cells)

            self.authentication.authenticate_device(device, username='user1', password='pass1')

    def get_network_features(self):
        features = []
        for device in self.devices:
            features.append({
                "Device Type": device.device_type,
                "Location": device.location,
                "Signal Strength": f"{device.signal_strength:.2f}",
                "Channel": device.channel,
                "Current Cell": device.current_cell,
                "Handoff Threshold": self.handoff_management.handoff_threshold,
                "Authentication Protocol": self.authentication.protocol,
                "Authenticated": device.authenticated
            })
        return features

class WWLANApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WWLAN Simulator")

        self.simulator = WWLANSimulator()

        # GUI components
        self.device_label = ttk.Label(root, text="Device Type:")
        self.device_type_entry = ttk.Entry(root)
        self.location_label = ttk.Label(root, text="Location (x, y):")
        self.location_entry = ttk.Entry(root)
        self.add_device_button = ttk.Button(root, text="Add Device", command=self.add_device)

        self.handoff_threshold_label = ttk.Label(root, text="Handoff Threshold:")
        self.handoff_threshold_entry = ttk.Entry(root)
        self.cell_ranges_label = ttk.Label(root, text="Cell Ranges (comma-separated):")
        self.cell_ranges_entry = ttk.Entry(root)
        self.simulate_button = ttk.Button(root, text="Simulate Network", command=self.simulate_network)

        self.results_label = ttk.Label(root, text="Simulation Results:")
        self.tree = ttk.Treeview(root, columns=("Device Type", "Location", "Signal Strength", "Channel", "Current Cell", "Handoff Threshold", "Authentication Protocol", "Authenticated"), show="headings")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, width=150, anchor="center")  # Adjust the width as needed

        self.update_user_label = ttk.Label(root, text="Update User Location:")
        self.update_user_entry = ttk.Entry(root)
        self.update_location_label = ttk.Label(root, text="New Location (x, y):")
        self.update_location_entry = ttk.Entry(root)
        self.update_location_button = ttk.Button(root, text="Update Location", command=self.update_location)

        # Grid layout
        self.device_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.device_type_entry.grid(row=0, column=1, padx=5, pady=5)
        self.location_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.location_entry.grid(row=1, column=1, padx=5, pady=5)
        self.add_device_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.handoff_threshold_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.handoff_threshold_entry.grid(row=3, column=1, padx=5, pady=5)
        self.cell_ranges_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.cell_ranges_entry.grid(row=4, column=1, padx=5, pady=5)
        self.simulate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.results_label.grid(row=6, column=0, columnspan=2, pady=10)
        self.tree.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.update_user_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.update_user_entry.grid(row=8, column=1, padx=5, pady=5)
        self.update_location_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.update_location_entry.grid(row=9, column=1, padx=5, pady=5)
        self.update_location_button.grid(row=10, column=0, columnspan=2, pady=10)

    def add_device(self):
        device_type = self.device_type_entry.get()
        location_str = self.location_entry.get()
        location = tuple(map(int, location_str.split(',')))
        new_device = Device(device_type, location)
        self.simulator.add_device(new_device)
        print(f"Device added: {device_type} at location {location}")

    def simulate_network(self):
        handoff_threshold = int(self.handoff_threshold_entry.get())
        cell_ranges = [int(range) for range in self.cell_ranges_entry.get().split(',')]
        self.simulator.handoff_management.handoff_threshold = handoff_threshold
        self.simulator.cells = [Cell(center=(0, 0), range=cell_ranges[0]),
                                Cell(center=(50, 0), range=cell_ranges[1]),
                                Cell(center=(0, 50), range=cell_ranges[2])]
        self.simulator.simulate_network()
        features = self.simulator.get_network_features()
        self.display_results(features)

    def update_location(self):
        try:
            device_index = int(self.update_user_entry.get())
            new_location_str = self.update_location_entry.get()
            new_location = tuple(map(int, new_location_str.split(',')))
            
            if 1 <= device_index <= len(self.simulator.devices):
                self.simulator.devices[device_index - 1].location = new_location
                print(f"Location updated for Device {device_index} to {new_location}")
                self.simulate_network()
                features = self.simulator.get_network_features()
                self.display_results(features)
            else:
                print("Invalid device ID. Please enter a valid User ID.")
        except ValueError:
            print("Invalid input. Please enter valid device index and location.")

    def display_results(self, features):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for feature in features:
            self.tree.insert("", "end", values=(feature["Device Type"],
                                                feature["Location"],
                                                feature["Signal Strength"],
                                                feature["Channel"],
                                                feature["Current Cell"],
                                                feature["Handoff Threshold"],
                                                feature["Authentication Protocol"],
                                                feature["Authenticated"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = WWLANApp(root)
    root.mainloop()

