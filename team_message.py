import pyautogui
import pygetwindow as gw
import time

# List of names to whom the message will be sent
names = ["John Doe", "Frank Steve", "Michael Giff"]

# Message to send
message = "Hello! This is a test message."

# Function to focus on the Microsoft Teams window
def focus_teams_window():
    # Find the Teams window
    teams_windows = [w for w in gw.getWindowsWithTitle("Microsoft Teams") if w.isActive or w.isMaximized or w.isMinimized]
    if teams_windows:
        teams_window = teams_windows[0]
        teams_window.activate()  # Bring the Teams window to the foreground
        time.sleep(1)  # Wait for the window to come into focus
    else:
        print("Microsoft Teams window not found. Please ensure Teams is open.")
        exit()

# Function to select the second search result using down arrow and enter
def select_second_search_result():
    pyautogui.press('down')  # Press the down arrow to highlight the first search result
    time.sleep(1)  # Wait for the selection to take effect
    pyautogui.press('down')  # Press the down arrow again to highlight the second search result
    time.sleep(1)  # Wait for the selection to take effect
    pyautogui.press('enter')  # Press enter to open the chat
    time.sleep(2)  # Wait for the chat to open

# Function to send a message to a person on Teams
def send_message(name, message):
    # Focus on the Teams window
    focus_teams_window()

    # Search for the person in Teams
    pyautogui.hotkey('ctrl', 'e')  # Shortcut to focus on the search bar
    time.sleep(2)  # Wait for the search bar to activate
    pyautogui.typewrite(name)  # Type the name
    time.sleep(2)  # Wait for search results to appear

    # Select the second search result
    select_second_search_result()

    # Type and send the message
    pyautogui.typewrite(message)
    pyautogui.press('enter')  # Send the message
    time.sleep(2)  # Wait to ensure the message is sent

# Main script to send messages to multiple people
for name in names:
    send_message(name, message)

print("Messages sent successfully!")
