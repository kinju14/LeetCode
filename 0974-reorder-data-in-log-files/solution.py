class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []

        for log in logs:
            if log.split()[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)

        letterLogs.sort(key = lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
        
        return letterLogs + digitLogs
