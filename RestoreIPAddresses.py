class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        self.findIps(s, [], ips)
        return ips

    def findIps(self, s, path, ips):
        if not s and len(path) == 4:
            ips.append('.'.join(path))
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.findIps(s[i:], path + [s[:i]], ips)
                elif i == 2 and s[0] != '0':
                    self.findIps(s[i:], path + [s[:i]], ips)
                elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                    self.findIps(s[i:], path + [s[:i]], ips)
