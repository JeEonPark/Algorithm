n, m, k = input().split()

team_without_k = min([int(int(n)/2), int(m)])

n_can_join = team_without_k * 2
m_can_join = team_without_k

n_without_k = int(n) - n_can_join
m_without_k = int(m) - m_can_join


if n_without_k + m_without_k >= int(k):
    print(team_without_k)
else:
    k = int(k) - (n_without_k + m_without_k)
    print(team_without_k - (int((k-1)/3)+1))
    
