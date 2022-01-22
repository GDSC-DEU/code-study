#1 try
def solution(phone_book):
    book_len = len(phone_book)
                   
    answer = True
                   
    for i in range(1,book_len):
        if phone_book[0] in phone_book[i]:
            answer = False
            break
    
    return answer


#2 try
def solution(phone_book):
    book_len = len(phone_book)
    first_num = phone_book[0]
    phone_book.pop(0)
    first_num_len = len(first_num)
    
    book_len = len(phone_book)
    answer = True
                   
    for i in range(book_len):
        if first_num == phone_book[i][:first_num_len]:
            answer = False
            break
    
    return answer

#3 try
def solution(phone_book):
    phone_book.sort()
    answer = True
    phone_book_len = len(phone_book)
        
    for i in range(phone_book_len-1):
        test = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:test]:
            answer = False
            break
    
    return answer