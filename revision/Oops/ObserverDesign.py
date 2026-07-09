class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, video_name):
        print(f"{self.name} received notification : {video_name}")

class YoutubeChannel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def upload(self, video_name):

        print(f"\nUploading : {video_name}\n")

        for subscriber in self.subscribers:
            subscriber.update(video_name)

channel = YoutubeChannel()

s1 = Subscriber("Abhay")
s2 = Subscriber("Admin")
s3 = Subscriber("Kush")

channel.subscribe(s1)
channel.subscribe(s2)
channel.subscribe(s3)

channel.upload("Python OOP")