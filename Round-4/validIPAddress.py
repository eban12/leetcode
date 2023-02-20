class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIpv4(ip):
            for part in ip:
                if (part.startswith('0') and len(part) > 1) or not part.isnumeric() or int(part) > 255:
                    return False
            return True
        
        def isIpv6(ip):
            for part in ip:
                if not 1 <= len(part) <= 4 or not all(c in string.hexdigits for c in part):
                    return False
            return True
        
        ipv4 = queryIP.split('.')
        if len(ipv4) == 4 and isIpv4(ipv4):
            return "IPv4"
        
        ipv6 = queryIP.split(':')
        if len(ipv6) == 8 and isIpv6(ipv6):
            return "IPv6"
        
        return "Neither"
