import json  # Importing the JSON module to read/write JSON files
import os    # Importing os module to interact with the file system

# Small explanation at the start:
# This is a smart home lighting system that allows users to manage room lights.
# The user can add rooms to presets, toggle the lights, delete rooms or presets, and the data is saved to a JSON file.

# Load existing data from the JSON file, if available
def load_data():
    # Check if the JSON file exists
    if os.path.exists("smart_home_data.json"):
        # Open the JSON file and load the data into a Python dictionary
        with open("smart_home_data.json", "r") as file:
            return json.load(file)
    # If no data exists, return an empty dictionary
    return {}

# Save the current data into the JSON file
def save_data(data):
    # Open the JSON file in write mode and dump the data (presets, rooms, light status) into it
    with open("smart_home_data.json", "w") as file:
        json.dump(data, file, indent=4)  # indent=4 ensures that the JSON is nicely formatted

# Function to add a room to a preset
def add_room(preset_data):
    while True:
        # Prompt the user to enter the name of the room
        room = input("Enter room name (or type 'done' to finish): ")
        
        # Exit the loop if the user types 'done'
        if room == 'done':
            break
        
        # Check if the room already exists in the preset
        if room not in preset_data:
            # If not, add the room to the preset with the light status set to "OFF"
            preset_data[room] = "OFF"
            print(f"Room '{room}' added successfully.")
        else:
            print(f"Room '{room}' already exists.")  # If the room exists, notify the user

# Function to toggle the light of a specific room within a preset
def toggle_light(presets):
    print("\nAvailable Presets:")
    # Display a list of all available presets
    for i, preset in enumerate(presets.keys(), 1):
        print(f"{i}. {preset}")
    
    # Let the user choose a preset to toggle the light from
    preset_choice = int(input("Select preset number to toggle light from: "))
    selected_preset = list(presets.keys())[preset_choice - 1]  # Get the selected preset
    
    print(f"\nRooms and Light Statuses in Preset '{selected_preset}':")
    # Display all rooms in the selected preset and their current light status
    for room, status in presets[selected_preset].items():
        print(f"Room: {room}, Light: {status}")

    # Ask the user to input the room name to toggle the light
    room_name = input("Enter room name to toggle light: ")
    if room_name in presets[selected_preset]:
        # Toggle the light status (if it's "OFF", turn it "ON", otherwise turn it "OFF")
        current_status = presets[selected_preset][room_name]
        new_status = "ON" if current_status == "OFF" else "OFF"
        presets[selected_preset][room_name] = new_status
        print(f"Room '{room_name}' light toggled to {new_status}.")
    else:
        # If the room doesn't exist in the selected preset, notify the user
        print(f"Room '{room_name}' not found in preset '{selected_preset}'.")

# Function to delete a preset from the system
def delete_preset(presets):
    print("\nAvailable Presets:")
    # Display a list of available presets for the user to choose from
    for i, preset in enumerate(presets.keys(), 1):
        print(f"{i}. {preset}")
    
    # Let the user select the preset they want to delete
    preset_choice = int(input("Select preset number to delete: "))
    selected_preset = list(presets.keys())[preset_choice - 1]  # Get the selected preset
    
    # Ask for confirmation before deleting
    confirm = input(f"Are you sure you want to delete preset '{selected_preset}'? (yes/no): ").lower()
    if confirm == 'yes':
        # If confirmed, delete the preset from the dictionary
        del presets[selected_preset]
        print(f"Preset '{selected_preset}' deleted successfully.")
        # Save the updated data to the JSON file
        save_data(presets)

# Function to delete a room from a specific preset
def delete_room_from_preset(presets):
    print("\nAvailable Presets:")
    # Display a list of available presets for the user to choose from
    for i, preset in enumerate(presets.keys(), 1):
        print(f"{i}. {preset}")
    
    # Let the user select the preset from which they want to delete a room
    preset_choice = int(input("Select preset number to delete room from: "))
    selected_preset = list(presets.keys())[preset_choice - 1]  # Get the selected preset
    
    print(f"\nRooms in Preset '{selected_preset}':")
    # List all the rooms in the selected preset
    for room in presets[selected_preset].keys():
        print(f"Room: {room}")

    while True:
        # Let the user specify which room(s) they want to delete
        room_to_delete = input("Enter room name to delete (or type 'done' to finish): ")
        
        if room_to_delete == 'done':
            break  # Exit the loop if the user types 'done'
        
        if room_to_delete in presets[selected_preset]:
            # If the room exists, delete it from the preset
            del presets[selected_preset][room_to_delete]
            print(f"Room '{room_to_delete}' deleted from preset '{selected_preset}'.")
        else:
            # If the room is not found, notify the user
            print(f"Room '{room_to_delete}' not found in preset '{selected_preset}'.")
    # Save the updated data to the JSON file after deleting rooms
    save_data(presets)

# Main function to manage the smart home lighting system
def smart_home_lighting_system():
    # Load existing presets and data from the JSON file
    presets = load_data()

    while True:
        # Display the main menu with options for the user
        print("\nSmart Home Lighting System")
        print("1. Add Room")
        print("2. Toggle Light")
        print("3. Delete Preset")
        print("4. Delete Room from Preset")
        print("5. Exit")
        
        # Prompt the user to select an option
        choice = input("Enter your choice: ")

        if choice == '1':
            # If the user selects "Add Room", prompt for preset name and add a room
            print("\nAdding a room:")
            preset_name = input("Enter preset name to add room to: ")
            if preset_name not in presets:
                # If the preset doesn't exist, create it
                presets[preset_name] = {}
                print(f"Preset '{preset_name}' created.")
            # Call the add_room function to add rooms to the preset
            add_room(presets[preset_name])
            # Save the updated data to the JSON file
            save_data(presets)
        elif choice == '2':
            # If the user selects "Toggle Light", call the toggle_light function
            print("\nToggle light:")
            toggle_light(presets)
        elif choice == '3':
            # If the user selects "Delete Preset", call the delete_preset function
            print("\nDeleting preset:")
            delete_preset(presets)
        elif choice == '4':
            # If the user selects "Delete Room from Preset", call the delete_room_from_preset function
            print("\nDelete room from preset:")
            delete_room_from_preset(presets)
        elif choice == '5':
            # If the user selects "Exit", break the loop and exit the program
            print("\nExiting...")
            break
        else:
            # If the user enters an invalid choice, prompt them to try again
            print("\nInvalid choice. Please try again.")

# Run the program
smart_home_lighting_system()
