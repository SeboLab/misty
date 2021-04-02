class Asset:
    def __init__(self, robot_ip):
        self.ip = robot_ip

        Publisher("/audio/list")
        Publisher("/audio")
        Publisher("/images/list")
        Publisher("/images")
        Publisher("/videos")
