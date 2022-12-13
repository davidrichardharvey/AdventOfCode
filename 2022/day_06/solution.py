with open("input.txt") as file:
    datastream = file.readline().strip()

def start_of_packet_marker(datastream):
    for i in range(len(datastream) - 3):
        marker = datastream[i:i+4]
        if len(marker) == len(set(list(marker))):
            return i + 4

print(start_of_packet_marker(datastream))

# Part 2

def start_of_message_marker(datastream):
    n = 14
    for i in range(len(datastream) - (n - 1)):
        marker = datastream[i:i+n]
        if len(marker) == len(set(list(marker))):
            return i + n

print(start_of_message_marker(datastream))