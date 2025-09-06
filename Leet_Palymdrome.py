def pal(n):
    copy_no = n
    inverted_no = 0
    while copy_no != 0:
        temp_last_digit = copy_no % 10
        copy_no = copy_no // 10
        inverted_no = inverted_no * 10 + temp_last_digit

    if inverted_no == n:
        print(f"{n} is a palindrome!")
    else:
        print(f"{n} is not a palindrome! Here it is in reverse: {inverted_no}")

no = int(input("Enter a number"))
pal(no)
