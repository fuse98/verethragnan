from config import ProxyConfig
from  abc import ABC, abstractmethod


class BaseProxySetter(ABC):
    
    def __init__(self, config: ProxyConfig) -> None:
        self.config = config

    @abstractmethod
    def set_proxy(self):
        pass
