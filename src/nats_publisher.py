import asyncio
from nats.aio.client import Client as NATS

class NatsPublisher:
    def __init__(self, nats_url: str, subject: str):
        self.nats_url = nats_url
        self.subject = subject
        self.nc = NATS()

    async def connect(self):
        print(f"Connecting to NATS at {self.nats_url}...")
        await self.nc.connect(servers=[self.nats_url])
        print("Connected to NATS!")

    async def publish(self, message: str):
        print(f"Publishing message: {message}")
        await self.nc.publish(self.subject, message.encode())

    async def close(self):
        print("Closing connection to NATS...")
        await self.nc.close()
        print("Connection closed.")

# Test the publisher
async def test_publisher():
    publisher = NatsPublisher(nats_url="nats://localhost:4222", subject="test.subject")
    await publisher.connect()
    await publisher.publish("Hello, NATS!")
    await publisher.close()

if __name__ == "__main__":
    asyncio.run(test_publisher())
