from dotenv import load_dotenv
load_dotenv()
import time
import os
import concurrent.futures
from uuid import uuid4
from datetime import datetime

import json
import boto3

MAX_MESSAGES = 500_000

sqs = boto3.client('sqs', endpoint_url='http://localhost:4566')


def main(queue, thread):  
    count = 0
    start = time.perf_counter()
    print(f'Starting thread {thread}')
    for x in range(MAX_MESSAGES):
        try:
            sqs.send_message(
                QueueUrl=queue,
                MessageBody=json.dumps({
                    'id': f'thread-{thread}#message-{x}',
                    'date': datetime.now().isoformat(),
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}',
                    f'{str(uuid4())}': f'{str(uuid4())}'
                    
                })
            )
        except Exception as e:
            print(e)
        count += 1
        
        if count % 1_000 == 0:
            print(f'Thread: {num} Message: {count}')
        
    print(f'Thread: {thread} Took: {round(time.perf_counter() - start,1)} seconds')

if __name__ == "__main__":  
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for num in range(8):
            sqs.create_queue(QueueName=f'decouple-{num}')
            queue = f'http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/decouple-{num}'
            executor.submit(main, queue, num)
