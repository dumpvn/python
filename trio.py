# coding=utf-8

async def proxy_one_way(source, sink):
	while True:
		data = await source.receive_some(1024)
		if not data:
			await sink.send_eof()
			break
		await sink.send_all(data)
