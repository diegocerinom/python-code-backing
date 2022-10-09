import asyncio
import time
import logging
import socket

logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(name)s | %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 8080

async def handle_event(reader, writer):
    try:
        received = await reader.read(1024)
        response = 'OK'
        client_address = writer.get_extra_info('peername')

        logging.info(f'[server] received: {received.decode()!r} from {client_address!r}')
        print(f'[server] received: {received.decode()!r} from {client_address!r}')
        start_time = time.time()

        writer.writer(response.encode())
        await writer.drain()

        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f'[server] response: {response} to {client_address!r}')
        print(f'[server] response: {response} from {client_address!r}')

        writer.close()

    except Exception as e:
        logging.error('[server]', exc_info=True)

async def main():
    try:
        server = await asyncio.start_server(handle_event, ip_address, port)

        server_address = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        logging.info(f'[server] serving on {server_address}')
        print(f'[server] serving on {server_address}')

        async with server:
            await server.serve_forever()

    except Exception as e:
        logging.error('[server]', exc_info=True)

if __name__ == '__main__':
    asyncio.run(main())