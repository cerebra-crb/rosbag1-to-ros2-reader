# rosbag1-to-ros2-reader

Convert ROS1 `.bag` files to ROS2 format using `convert.py` and read messages in Python with `read_ros2.py`.

## Usage

1. Convert ROS1 bag to ROS2:

```bash
python convert.py
```
this will generate a ROS2 bag folder demo_ros2.

2. Read ROS2 bag:

```bash
python read_ros2.py
```
Output
```
/chatter 42 std_msgs__msg__String(data='o world', __msgtype__='std_msgs/msg/String')
/chatter 43 std_msgs__msg__String(data='o again', __msgtype__='std_msgs/msg/String')
/diagnostics 43 std_msgs__msg__String(data='nostics', __msgtype__='std_msgs/msg/String')
