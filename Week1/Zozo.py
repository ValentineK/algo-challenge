class Solution:
    def numUniqueEmails(self, array):
        dataSet = set()
        for email in array:
            a,b = email.split('@')
            if '+' in a:
                a = a.split('+')[0]
            a   = a.replace('.','')
            dataSet.add( (a,b) )
        return len(dataSet)
