 1. Introduction: 
This project is a Smart Home Lighting System, which provides users with an easy way to manage lighting 
in their home through customizable presets. The application allows users to add rooms, toggle lights, and 
delete presets or rooms while saving configurations in a persistent JSON file for future use. 
 
2. Design Choices: 
• Data Structure: The data is structured as a dictionary, with presets as keys and rooms as values 
(also dictionaries with room names as keys and light statuses as values). This allows for easy 
addition, removal, and modification of rooms and presets. 
• JSON File for Persistence: The use of a JSON file allows the system to save configurations 
between sessions. When the application starts, it loads the JSON file to retrieve any existing 
presets and room configurations. 
• Modular Design: The system is broken into functions, each handling a specific task (e.g., loading 
data, adding rooms, toggling light status). This modular approach makes the code more readable 
and maintainable. 
 
3. System Architecture: 
The system follows a command-line interface (CLI) design: 
1.Main Menu: Displays options to the user and captures input. 
2.Functions for Managing Presets and Rooms: 
• load_data() – Loads data from the JSON file. 
• save_data(data) – Saves updated data back to the JSON file. 
• add_room(preset_data) – Adds new rooms to a preset. 
• toggle_light(presets) – Toggles the light status (ON/OFF) for rooms. 
• delete_preset(presets) – Deletes an entire preset. 
• delete_room_from_preset(presets) – Deletes a room from a preset. 
3.Error Handling: Each function checks if the provided preset or room exists before proceeding with the 
action, ensuring that the program doesn't crash from invalid input. 
 
4. Data Structures: 
The main data structure used in the program is a dictionary: 
• Presets: Each preset is represented by a dictionary key (e.g., "Living Room Preset"). 
• Rooms within a preset: Each preset's value is another dictionary, where keys are room names 
(e.g., "Living Room", "Kitchen") and values are light statuses (e.g., "ON", "OFF"). 
Example data stored in smart_home_data.json: 
 
5. Functions Overview: 
 
load_data(): 
• Loads the saved configuration from smart_home_data.json (if it exists). 
• Returns the data as a dictionary. 
 
Save_data(data): 
• Saves the provided dictionary data to smart_home_data.json. 
 
add_room(preset_data): 
• Prompts the user to input room names and adds those rooms to a specified preset. 
 
toggle_light(presets): 
• Toggles the light status for rooms in a selected preset. 
 
delete_preset(presets): 
• Deletes a chosen preset after confirmation. 
 
delete_room_from_preset(presets): 
• Deletes selected rooms from a chosen preset. 
 
6. Challenges Faced and Solutions: 
 
Handling Invalid Input: 
• Issue: Users might provide invalid preset names or room names. 
• Solution: Implemented error handling that checks if the specified preset or room exists before 
performing the action. If not, an error message is shown, and the user is prompted to provide a 
valid input. 
 
Data Persistence: 
• Issue: Ensuring that changes to the preset configurations are saved and loaded correctly. 
• Solution: Used the json module to read and write data to a file (smart_home_data.json), ensuring 
persistence between sessions. 
 
User Interface: 
• Issue: Making the command-line interface simple and user-friendly. 
• Solution: Kept the menu options clear and provided prompts to guide the user through each step, 
along with error messages when necessary. 
 
7. Future Enhancements: 
• Graphical User Interface (GUI): Transitioning from CLI to a GUI would improve usability, 
especially for non-technical users. 
• Remote Control Integration: Integrating the system with mobile apps or smart home devices like 
Alexa or Google Home could enhance the control experience. 
• More Complex Presets: Allow users to create more advanced presets, including scheduling lights 
to turn on or off at specific times.

How to Use the Application:  
Once the application starts, you will see the main menu with options to:  
  
1. Add Rooms: This option lets you add new rooms to a preset. You will be prompted to provide the 
preset name and the rooms you want to add.  
2. Toggle Light: Allows you to toggle the light status (ON/OFF) of a room within a preset. You’ll 
need to select the preset and room to toggle.  
3. Delete Preset: Removes an entire preset from the system. You will be asked to confirm before 
deletion.  
4. Delete Room from Preset: Lets you delete a specific room from a preset. You can remove rooms 
one by one until you choose to stop.  
5. Exit: Exits the program.  
  
  
  Example Walkthrough:  
    Step 1: Add Rooms  
After selecting Option 1 (Add Room), you'll be prompted to input a preset name (e.g., "Living 
Room Preset").  
Next, you'll enter the names of rooms to be added to the preset (e.g., "Living Room", "Kitchen", 
etc.).  
   Step 2: Toggle Light  
Select Option 2 (Toggle Light).  
Choose a preset from the available list.  
Pick a room from the preset, and toggle the light status (ON/OFF).  
   Step 3: Delete Preset  
Select Option 3 (Delete Preset).  
Choose the preset you want to delete from the available list.  
Confirm the deletion.  
   Step 4: Delete Room from Preset  
Select Option 4 (Delete Room from Preset).  
Choose the preset from which you want to delete rooms.  
Select one or more rooms to delete, and the system will remove them.  
   Step 5: Exit  
Once you're done, select Option 5 (Exit) to close the program.  
Data Storage:  
The system saves all presets, rooms, and light statuses in a JSON file (smart_home_data.json). 
When the program is restarted, it will load the data from this file and display the current 
configurations.  
