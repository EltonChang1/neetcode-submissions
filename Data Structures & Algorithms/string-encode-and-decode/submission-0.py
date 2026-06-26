class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for j in strs:
            encoded_string += str(len(j))+"#"+j
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        
        while i < len(s):
            end_of_int_length = i
            while s[end_of_int_length] != "#":
                end_of_int_length += 1
            length_of_string = int(s[i:end_of_int_length])
            start_of_string = end_of_int_length + 1
            end_of_string = start_of_string + length_of_string
            each_string = s[start_of_string:end_of_string]

            decoded_string.append(each_string)
            i = end_of_string

        return decoded_string

        
            
