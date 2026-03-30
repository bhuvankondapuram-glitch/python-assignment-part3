try:
    # Create and write notes
    with open("python_notes.txt", "w") as f:
        f.write("Python is easy to learn.\nFile handling is useful.")

    # Force an error (to create error_log.txt)
    print(10 / 0)

except Exception as e:
    with open("error_log.txt", "w") as err:
        err.write(str(e))
