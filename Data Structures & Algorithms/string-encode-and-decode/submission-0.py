class Solution:

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_result = ""
        for s in strs:
            # Format: <length_of_string> + <delimiter> + <string>
            # Example: "hello" -> "5#hello"
            encoded_result += f"{len(s)}#{s}"
        return encoded_result

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        result = []
        i = 0
        
        while i < len(s):
            # Find where the length prefix ends
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # Step past the '#' delimiter
            start_of_str = j + 1
            end_of_str = start_of_str + length
            
            # Extract the actual string and add it to our list
            result.append(s[start_of_str:end_of_str])
            
            # Move the pointer to the start of the next encoded block
            i = end_of_str
            
        return result

# --- How to instantiate and run it correctly outside the class ---
sol = Solution()

input_list = ["lint", "code", "love", "you"]
encoded_string = sol.encode(input_list)
print("Encoded:", repr(encoded_string))  # Output: '4#lint4#code4#love3#you'

decoded_list = sol.decode(encoded_string)
print("Decoded:", decoded_list)          # Output: ['lint', 'code', 'love', 'you']
