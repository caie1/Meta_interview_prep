class Solution(object):
    def validIPAddress(self, IP):
        """
        :type queryIP: str
        :rtype: str
        """
        ## Time:O(N) Space: O(1)
        def _checkForIPv4():
            splitIP = IP.split('.')
            for val in splitIP:
                if not val or len(val) > 3:
                    return 'Neither'
                if (val[0] == '0' and len(val) > 1) or not val.isdigit() or int(val) > 255:
                    return 'Neither'
            return 'IPv4'
        def _checkForIPv6():
            splitIP = IP.split(':')
            hexdecimal = {'0','1','2','3','4','5','6','7','8','9', 'a','b','c','d','e','f','A','B','C','D','E','F'}
            for val in splitIP:
                if not val or len(val) > 4:
                    return 'Neither'
                for ch in val:
                    if ch not in hexdecimal:
                        return 'Neither'
            return 'IPv6'
        if not IP:
            return 'Neither'
        if IP.count('.') == 3:
            return _checkForIPv4()
        elif IP.count(':') == 7:
            return _checkForIPv6()
        else:
            return 'Neither'
