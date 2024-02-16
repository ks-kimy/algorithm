T= 10


def palindrome_words(matrix):
    count =0
    for i in range(8):
        for j in range(8-text_length+1):
            words = matrix[i][j:j+text_length]
            if words == words[::-1]:
                count +=1
    for j in range(8):
        for i in range(8-text_length+1):
            words2 =''.join([matrix[k][j] for k in range(i,i+text_length)])
            # join 은 문자열 매서드이다. 이터러블 객체의 각각의 요소들을 문자열로 만들어준다.
            if words2 == words2[::-1]:
                count += 1
    return count
for tc in range(T):
    text_length = int(input())
    matrix = [input() for _ in range(8)]
    # print(matrix)
    result = palindrome_words(matrix)
    print(f'#{tc+1} {result}')