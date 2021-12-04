class RunTask:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        print(f"{self.message}... ", end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Done")
