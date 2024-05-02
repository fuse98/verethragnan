import sys
import getopt
from typing import List
from proxy_setters import BaseProxySetter, UbuntuSystemProxySetter 
from config.base import ProxyConfig


def main(argv):

    # create required configs

    getopt.getopt()
    argv



    config = ProxyConfig()

    





    # create proxy setters
    proxy_setters: List[BaseProxySetter] = []






    # set proxies
    for proxy_setter in proxy_setters:
        proxy_setter.set_proxy()


if __name__ == '__main__':
    main(sys.argv[1:])

