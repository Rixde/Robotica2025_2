import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robousr/robotica-2025-2/ROS2_Dev/install/node_topics_py'
