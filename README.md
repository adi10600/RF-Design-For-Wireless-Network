# RF-Design-For-WWLAN-Network
It's a Wireless and communication project in which RF design for WWLAN network is implemented in python language

## Implementation Detail
The WWLAN (Wireless Wide Local Area Network) Simulator is a Python application built to simulate a wireless network environment. It includes features such as device addition, network simulation, dynamic user location updates, and graphical representation of network features.

## How It Works

### Planning Phase: Wave Propagation Model
The planning phase focuses on modeling wave propagation in the wireless network.
The simulator considers factors like signal attenuation and interference during this phase.

### Design Phase: Channel Assignment, Handoff Strategies, Architecture Standards

Channel assignment strategies are designed to allocate channels to devices efficiently.
Handoff strategies are implemented to manage device transitions between cells seamlessly.
Architecture standards, such as 802.1x, are considered for network security.

### Development Phase: Device Specifications

Specifications for devices are chosen, defining their types, initial locations, and other relevant characteristics.
Python classes model the devices, cells, channel assignment, handoff management, and authentication protocols.

### Implementation Phase: WWLAN Simulator in Python

The entire WWLAN simulator is implemented using Python, leveraging object-oriented programming principles.
The simulator class includes methods for network simulation, device signal strength calculations, channel assignment, and authentication.

### Graphical User Interface (GUI) Integration

A GUI is added to enhance the user experience, allowing users to interact with the simulator easily.
Users can add devices, simulate the network, and dynamically update device locations through the GUI.

### Simulation Results Display

Simulation results, including signal strength, channel usage, current cell, handoff thresholds, authentication protocols, and user authentication status, are displayed in a tabular format.
The GUI provides a user-friendly representation of the network features after each simulation.


### User Interaction and Modification

Users can add devices with specified characteristics through the GUI.
Dynamic updates to device locations are supported, enabling users to observe the impact on the network in real-time.

## Requirements
Python 3.x
Tkinter (usually included with Python installations)

## Running the Application
1. Clone the repository: git clone https://github.com/your-username/WWLAN-Simulator.git
2. Navigate to the project directory:
