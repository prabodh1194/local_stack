A test bench for sqs.

1. create queue using
   ```bash
   python sqs_create_queue.py
   ```
2. send 10 messages to this queue
   ```bash
   python sqs_producer.py
   ```
3. consume all 10 messages from this queue
   ```bash
   python sqs_consumer.py
   ```