from enum import Enum


class SyntaxFormat(Enum):
    port_sharing = "[<host_ipv4>:]<host_port>[-<end_port>][:<container_port>[-<end_port>]][:<proto>]"
    desktop_config = "[blue]proto[:ip[:port]][/blue]"
    volume = "/path/on/host/:/path/in/container/[blue][:ro|rw][/blue]"

    def __str__(self) -> str:
        return self.value
