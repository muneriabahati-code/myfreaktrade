import socket
import sys
from config import HOST

# 1. Safety Check: Did the user provide the port and message?
if len(sys.argv) < 3:
    print("🚨 ERROR: Missing arguments.")
    print("💡 Usage: python client.py <PORT> <MESSAGE>")
    print("💡 Example: python client.py 65432 BUY")
    sys.exit(1)

# Grab the arguments from the terminal
PORT = int(sys.argv[1])
MESSAGE = sys.argv[2].upper() # Force uppercase so the server always reads 'BUY' or 'SELL'

def send_signal():
    try:
        # 2. Create socket with a timeout so it doesn't freeze your terminal
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3.0) 
        
        # 3. Connect and send
        client.connect((HOST, PORT))
        # sendall() is safer than send() for ensuring the whole message goes through
        client.sendall(MESSAGE.encode('utf-8')) 
        
        print(f"✅ SUCCESS: Sent '{MESSAGE}' to {HOST}:{PORT}")
        
    except ConnectionRefusedError:
        print(f"🚨 CONNECTION FAILED: Is your socket server actually running on port {PORT}?")
    except Exception as e:
        print(f"🚨 ERROR: {e}")
    finally:
        # 4. Always close the connection
        client.close()

if __name__ == "__main__":
    send_signal()
