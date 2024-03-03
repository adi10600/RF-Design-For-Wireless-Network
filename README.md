# RF-Design-For-WWLAN-Network
It's a Wireless and communication project in which RF design for WWLAN network is implemented in python language

## Implementation Detail
The WWLAN (Wireless Wide Local Area Network) Simulator is a Python application built to simulate a wireless network environment. It includes features such as device addition, network simulation, dynamic user location updates, and graphical representation of network features.

## How It Works

### Planning Phase: Wave Propagation Model
- The planning phase focuses on modeling wave propagation in the wireless network.
- The simulator considers factors like signal attenuation and interference during this phase.

### Design Phase: Channel Assignment, Handoff Strategies, Architecture Standards

- Channel assignment strategies are designed to allocate channels to devices efficiently.
- Handoff strategies are implemented to manage device transitions between cells seamlessly.
- Architecture standards, such as 802.1x, are considered for network security.

### Development Phase: Device Specifications

- Specifications for devices are chosen, defining their types, initial locations, and other relevant characteristics.
- Python classes model the devices, cells, channel assignment, handoff management, and authentication protocols.

### Implementation Phase: WWLAN Simulator

- The entire WWLAN simulator is implemented using Python, leveraging object-oriented programming principles.
- The simulator class includes methods for network simulation, device signal strength calculations, channel assignment, and authentication.

### Graphical User Interface (GUI) Integration

- A GUI is added to enhance the user experience, allowing users to interact with the simulator easily.
- Users can add devices, simulate the network, and dynamically update device locations through the GUI.

### Simulation Results Display

- Simulation results, including signal strength, channel usage, current cell, handoff thresholds, authentication protocols, and user authentication status, are displayed in a tabular format.
- The GUI provides a user-friendly representation of the network features after each simulation.


### User Interaction and Modification

- Users can add devices with specified characteristics through the GUI.
- Dynamic updates to device locations are supported, enabling users to observe the impact on the network in real-time.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)

## Running the Application
1. Clone the repository: git clone https://github.com/your-username/WWLAN-Simulator.git
2. Navigate to the project directory: cd RF_Design
3. Install the required packages: pip install -r requirements.txt
4. Run the application: python main.py
5. On GUI, add users by giving some unique id (1,2,3..) with their locations and click on add user button
6. After adding user, set handoff threshold and type cell ranges (in metres) with comma like I have used 3 cells then you have to type (30,40,50)
7. Then, Click on simulate Network
8. If you want to see the behaviour of the network on changing location of particular user then type user id then type new locations and then click on update location.
9. Updation in signal strength, handoff given to cell all will be shown on the GUI.

## Additional Notes
- Ensure that you have Python installed on your machine.
- If Tkinter is not included with your Python installation, you may need to install it separately.
- Feel free to explore and modify the code to suit your specific requirements.
- For any issues or improvements, please open an issue on the GitHub repository.

## License
This project is licensed under the [MIT License](LICENSE)- see the LICENSE file for details.
