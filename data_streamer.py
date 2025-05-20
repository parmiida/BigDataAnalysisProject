import socket
import time

CSV_FILE = "timeseries.csv"
SPARK_HOST = "localhost"
SPARK_PORT = 9999
INTERVAL = 0.01  # 10 milliseconds interval

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Spark application
sock.connect((SPARK_HOST, SPARK_PORT))

with open(CSV_FILE, 'r') as file:
    # Skip the header line
    next(file)

    for line in file:
        # Send each line to the Spark application
        sock.sendall(line.encode('utf-8'))

        # Calculate the next timestamp when the message should be sent
        next_timestamp = time.time() + INTERVAL

        # Wait until the next timestamp is reached
        while time.time() < next_timestamp:
            pass

# Close the socket connection
sock.close()

