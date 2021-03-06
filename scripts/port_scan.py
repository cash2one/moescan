# coding=utf-8

'''
Scan targets' ports using nmap.
'''
import nmap
from lib import exploit


class Exploit(exploit.BaseExploit):
    protocol = 'tcp'

    def help(self):
        print('Port scan use python-nmap')
        print('extra_arg: ')
        print('-' * 30)
        print('arg: arguments of nmap')

    def exploit(self):
        n = nmap.PortScanner()
        print('Scan {} ports: {}'.format(self.target, self.port))
        arg = self.extra_arg.get('arg') if not self.extra_arg.get('arg') is None else '-sV -Pn'
        result = n.scan(hosts=self.target, ports=self.port, arguments=arg)
        print(result)
        # TODO: qwq
