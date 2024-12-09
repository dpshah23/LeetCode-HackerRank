class Solution(object):
   
    def isArraySpecial(self, arr, qry):
        q_len = len(qry)
        result = [False] * q_len
        arr_len = len(arr)
        parity_count = [0] * arr_len

        for i in range(1, arr_len):
            if arr[i] % 2 == arr[i - 1] % 2:
                parity_count[i] = 1 + parity_count[i - 1]
            else:
                parity_count[i] = parity_count[i - 1]

        for i in range(q_len):
            start, end = qry[i]
            result[i] = (parity_count[end] - parity_count[start] == 0)

        return result
