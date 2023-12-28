# TurtleBot3-burger: Navigation and Find Pillar

南方科技大学《EE346移动机器人导航》课程实验

![HitCount](https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2FHuaYuXiao%2Ftb3-Navigation-and-Find-Pillar.json%3Fcolor%3Dpink)
![Static Badge](https://img.shields.io/badge/ROS-melodic-22314E?logo=ros)
![Static Badge](https://img.shields.io/badge/Ubuntu-20.04-E95420?logo=ubuntu)
![Static Badge](https://img.shields.io/badge/Python-3.11.5-3776AB?logo=python)

## View on YouTube

https://youtu.be/5aUDObaqrCE


## 基本指令

主机上

```bash
roscore
```

从机上

```bash
export ROS_MASTER_URI=http://192.168.3.142:11311
```

```bash
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

主机上

```bash
export TURTLEBOT3_MODEL=burger
```

```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/mmap.yaml
```


## 团队贡献

郝熙哲：寻找柱子算法
华羽霄：路径规划导航
