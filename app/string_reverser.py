class StringReverser:
    def reverse_string(input):
        input.replace(' world', '')
        reverse = ""
        for i in range(len(input)):
            reverse = reverse + input[len(input) - i - 1]
        return reverse