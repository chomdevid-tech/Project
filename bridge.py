import threading
import time
from ids import MiniIdps
from sniffer import EVENT_QUEUE, start_sniffer

# Initialize IDS
ids = MiniIdps()

# Thread that continuously processes events from the queue
def event_loop():
    while True:
        try:
            event = EVENT_QUEUE.get()
            if event is None:  # sentinel stop signal
                break

            ids.manage_event(event)  # matches your IDS function name

            EVENT_QUEUE.task_done()

        except Exception as e:
            print("[Event Loop Error]", e)

        time.sleep(0.001)  # avoid CPU spike


# Function that starts the event loop + sniffer
def start_event_bridge():
    # Start background event loop thread
    t = threading.Thread(target=event_loop, daemon=True)
    t.start()
    return t  # main.py will control the thread if needed
