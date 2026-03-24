from pathlib import Path
from rosbags.rosbag2 import Writer
from rosbags.highlevel import AnyReader

src = Path("demo.bag")
dst = Path("demo_ros2")

with AnyReader([src]) as reader:
    with Writer(dst, version=9) as writer:
        conn_map = {}
        for conn in reader.connections:
            conn_map[conn.id] = writer.add_connection(conn.topic, conn.msgtype, typestore=reader.typestore)
        for conn, timestamp, rawdata in reader.messages():
            writer.write(conn_map[conn.id], timestamp, rawdata)