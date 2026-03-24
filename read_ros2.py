from pathlib import Path
from rosbags.highlevel import AnyReader

bag_path = Path("demo_ros2")

with AnyReader([bag_path]) as reader:
    for connection, timestamp, rawdata in reader.messages():
        msg = reader.deserialize(rawdata, connection.msgtype)
        print(connection.topic, timestamp, msg)