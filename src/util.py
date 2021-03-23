import time
import requests
import subprocess as sp


def ping_ip(ip, timeout):
    """Continuously ping an IP until a timeout period.

    Returns True if the IP is up within that duration
    """
    ping_cmd = "ping -c 1 -w .1".split(" ")
    ping_cmd.append(ip)
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            response = sp.run(
                ping_cmd, timeout=timeout, stdout=sp.PIPE, stderr=sp.PIPE, check=True
            )
            if "1 received" in str(response.stdout):
                return True
        except sp.TimeoutExpired:
            continue
    return False


def ros_msg_to_json(msg):
    json = dict()
    for field in dir(msg):
        if field.startswith("_") or "serialize" in field:
            continue

        words = [word.capitalize() for word in field.split("_")]
        camel_case_field = "".join(words)

        json[camel_case_field] = getattr(msg, field)
    return json


def post(ip, endpoint, json):
    requests.post("http://" + ip + "/api/" + endpoint, json=json)