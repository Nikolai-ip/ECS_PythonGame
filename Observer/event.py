class Event:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, handler):
        self.subscribers.append(handler)

    def unsubscribe(self, handler):
        self.subscribers.remove(handler)

    def notify(self, *args, **kwargs):
        for handler in self.subscribers:
            handler(*args, **kwargs)