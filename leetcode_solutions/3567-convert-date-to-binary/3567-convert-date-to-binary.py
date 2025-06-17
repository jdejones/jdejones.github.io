class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return f"{bin(datetime.datetime.strptime(date, '%Y-%m-%d').year)[2:]}-{bin(datetime.datetime.strptime(date, '%Y-%m-%d').month)[2:]}-{bin(datetime.datetime.strptime(date, '%Y-%m-%d').day)[2:]}"
