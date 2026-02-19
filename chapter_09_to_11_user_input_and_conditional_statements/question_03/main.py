traffic_signal_color : str = input("Enter the color of road traffic signal: ")

if traffic_signal_color == "Red":
    print("Must stop")
elif traffic_signal_color == "Yellow":
    print("Ready to move")
elif traffic_signal_color == "Green":
    print("Move now")