class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        time_instance = {}

        for src, dst, t in meetings:
            if t not in time_instance:
                time_instance[t] = defaultdict(list)
            time_instance[t][src].append(dst)
            time_instance[t][dst].append(src)

        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        for t in sorted(time_instance.keys()):
            visit = set()
            for src in time_instance[t]:
                if src in secrets:
                    dfs(src, time_instance[t])

        return list(secrets)