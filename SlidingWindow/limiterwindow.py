from collections import defaultdict, deque


class RateLimiter:
    DEFAULT_LIMIT = 10

    def __init__(self, window_seconds: int):
        self.window = window_seconds
        self.clientConfig: dict[str, int] = {}
        self.clients: dict[str, deque[int]] = defaultdict(deque)

    def registerClient(self, client_config: dict[str, int]):
        self.clientConfig.update(client_config)

    def is_allowed(self, client_id: str, timestamp: int) -> bool:
        if client_id not in self.clientConfig:
            raise ValueError(f"Client '{client_id}' is not registered")

        window = self.clients[client_id]
        cutoff = timestamp - self.window
        
        # evict old
        while window and window[0] < cutoff:
            window.popleft()

        if len(window) < self.clientConfig.get(client_id, self.DEFAULT_LIMIT):
            window.append(timestamp)
            return True
        
        return False
    

if __name__ == '__main__':
    # enterprise clientA gets 3 req/10s, standard clientB gets 1 req/10s
    rl = RateLimiter(10)
    rl.registerClient({"clientA": 3})
    rl.registerClient({"clientB": 6})

    # client_config={"clientA": 3, "clientB": 1},
    requests = [
        ("clientA", 1),   # allowed  (1st)
        ("clientA", 5),   # allowed  (2nd)
        ("clientA", 9),   # allowed  (3rd)
        ("clientA", 11),  # blocked  (3 in window [1..11])
        ("clientA", 12),  # allowed  (window slides: [5,9,12], drops t=1)
        ("clientB", 11),  # allowed  (clientB is independent)
    ]

    for client_id, ts in requests:
        result = rl.is_allowed(client_id, ts)
        print(f"client={client_id} t={ts:>3} -> {'ALLOW' if result else 'BLOCK'}")
