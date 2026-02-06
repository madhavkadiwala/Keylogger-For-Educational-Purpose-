print("=== Educational Keylogger Demo ===")
print("⚠ This program logs ONLY what you type here")
print("Type 'EXIT' to stop logging\n")

log_file = open("keylog.txt", "a")

while True:
    text = input("Type here: ")

    if text.upper() == "EXIT":
        print("Logging stopped.")
        break

    log_file.write(text + "\n")

log_file.close()
