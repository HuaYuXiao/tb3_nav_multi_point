# TurtleBot3-burger: Navigation to Multiple Points

南方科技大学《EE346移动机器人导航》期末项目

## 基本指令

```bash
roscore
```

```bash
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

```bash
export TURTLEBOT3_MODEL=burger
```

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/mmap.yaml
```

```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
