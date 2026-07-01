FROM osrf/ros:humble-desktop-full

ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# ------------------------------------------------------------------------------
# Create non-root user
# ------------------------------------------------------------------------------

RUN if ! id -u ${USER_UID} >/dev/null 2>&1; then \
    groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd -m -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} ${USERNAME}; \
    fi

RUN apt-get update && \
    apt-get install -y sudo && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}

# ------------------------------------------------------------------------------
# ROS Environment
# ------------------------------------------------------------------------------

RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc

# ------------------------------------------------------------------------------
# System Packages
# ------------------------------------------------------------------------------

RUN sudo apt-get update && sudo apt-get install -y \
    git \
    vim \
    nano \
    curl \
    wget \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    python3-jsonschema

# ------------------------------------------------------------------------------
# TurtleBot3 + Navigation
# ------------------------------------------------------------------------------

RUN sudo apt-get install -y \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-turtlebot3 \
    ros-humble-turtlebot3-gazebo \
    ros-humble-slam-toolbox

# ------------------------------------------------------------------------------
# Python packages
# ------------------------------------------------------------------------------

RUN pip3 install --no-cache-dir \
    openai \
    pydantic \
    jsonschema

# ------------------------------------------------------------------------------
# Initialize rosdep
# ------------------------------------------------------------------------------

RUN sudo rosdep init || true
RUN rosdep update

# ------------------------------------------------------------------------------
# Workspace
# ------------------------------------------------------------------------------

RUN mkdir -p /home/${USERNAME}/ros2_ws/src

WORKDIR /home/${USERNAME}/ros2_ws

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]