import asyncio
from nats.aio.client import Client as NATS
class NatsSubscriber:
    def __init__(self, nats_url: str, subject: str):
        self.nats_url = nats_url
        self.subject = subject
        self.nc = NATS()

    async def connect(self):
        print(f"Connecting to NATS at {self.nats_url}...")
        await self.nc.connect(servers=[self.nats_url])
        print("Connected to NATS!")

    async def subscribe(self):
        async def message_handler(msg):
            print(f"Received message: {msg.data.decode()}")

        print(f"Subscribing to subject: {self.subject}")
        await self.nc.subscribe(self.subject, cb=message_handler)

    async def close(self):
        print("Closing connection to NATS...")
        await self.nc.close()
        print("Connection closed.")

# Test the subscriber
async def test_subscriber():
    subscriber = NatsSubscriber(nats_url="nats://localhost:4222", subject="test.subject")
    await subscriber.connect()
    await subscriber.subscribe()
    print("Listening for messages...")
    await asyncio.sleep(10)  # Keep the subscriber running for 10 seconds
    await subscriber.close()

if __name__ == "__main__":
    asyncio.run(test_subscriber())
