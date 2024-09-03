import sys
import threading as tr
from hash import hash_key
from peer import Peer
from time import sleep
from listen import serve
from user_action import run
from bootstrap import connect

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("missing socket")
    else:
        user = Peer(hash_key(sys.argv[1] + ":" + sys.argv[2]),
                    sys.argv[1] + ":" + sys.argv[2])

        serving = tr.Thread(target=serve, args=[user], daemon=True)
        serving.start()

        connect(user)
        sleep(1)

        while True:
            run(user)
