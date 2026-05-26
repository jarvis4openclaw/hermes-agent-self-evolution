#!/usr/bin/env python3
import os

# Read the API key from .env file
with open('/home/wahid/.hermes/.env') as f:
    for line in f:
        if 'ANTHROPIC_API_KEY' in line:
            key = line.split('=', 1)[1].strip()
            print(f'Key length: {len(key)}')
            print(f'Key value: {key[:20]}...' if len(key) > 20 else f'Key value: {key}')
            print(f'Contains asterisks: {"*" in key}')
            
            if key and len(key) > 20 and '*' not in key:
                from anthropic import Anthropic
                client = Anthropic(api_key=key)
                msg = client.messages.create(model='claude-haiku-3-5', max_tokens=10, messages=[{'role': 'user', 'content': 'test'}])
                print('API works!')
            else:
                print('API key is masked or invalid - need plaintext key')
            break