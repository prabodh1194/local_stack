A test bench for sqs.

1. Bring up localstack
   ```bash
   docker-compose up
   ```
2. create queue using
   ```bash
   python sqs_create_queue.py
   ```
3. send 10 messages to this queue
   ```bash
   python sqs_producer.py
   ```
4. consume all 10 messages from this queue
   ```bash
   python sqs_consumer.py
   ```