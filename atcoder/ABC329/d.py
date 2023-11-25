def main(candidate_num: int, votes_num: int, votes: list) -> None:
    voting_result = {}
    ans = votes[0]
    
    for vote in votes:
        if vote in voting_result:
            voting_result[vote] += 1
        else:
            voting_result[vote] = 1
        
        prev = voting_result[ans]
        curt = voting_result[vote]
        
        if prev == curt:
            ans = min(ans, vote)
        elif prev < curt:
            ans = vote
        
        print(ans)
        
if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    main(N, M, A)
