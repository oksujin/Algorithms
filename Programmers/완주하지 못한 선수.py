# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3#
def solution(participant, completion):
    completion_count = {}
    for i in completion : 
        try : completion_count[i] += 1
        except : completion_count[i] = 1
    # print(completion_count, "\n")
    
    answer = ''
    for j in participant :
        # print(j)
        try : 
            # print("check", completion_count[j])
            completion_count[j] -= 1
            if completion_count[j] < 0 :
                answer = j
                break
        except : 
            answer = j
            break
    # print(completion_count, "\n")

    return answer