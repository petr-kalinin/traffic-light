class DummySetter:
    def __init__(self):
        self.state = (False, False, False)

    def __call__(self, red, yellow, green):
        old_state = self.state[:]
        self.state = (red, yellow, green)
        if old_state != self.state:
            print("Dummy: ", self.state)
