const INF: usize = 1 << 61;
use std::collections::VecDeque;
use std::cmp::min;


struct Dinic {
    n: usize,
    edges: Vec<Vec<(usize, i64, i64)>>, // adjacent list
    level: Vec<i64>,
    iter: Vec<usize>
}

impl Dinic {
    fn new(n: usize) -> Self {
        Dinic {
            n,
            edges: vec![Vec::new(); n],
            level: vec![0; n],
            iter: vec![0; n]
        }
    }

    fn add(&mut self, from: usize, to: usize, cap: i64, directed: bool) {
        // edge[from]: to, cap, cost, rev(逆辺)
        if directed {
            let rev_from: i64 = self.edges[to].len() as i64;
            self.edges[from].push((to, cap, rev_from));
            let rev_to: i64 = self.edges[from].len() as i64;
            self.edges[to].push((from, 0, rev_to-1));
        } else {
            // TODO: must be verified
            let rev_from: i64 = self.edges[to].len() as i64;
            self.edges[from].push((to, cap, rev_from));
            let rev_to: i64 = self.edges[from].len() as i64;
            self.edges[to].push((from, 0, rev_to-1));
            self.edges[to].push((from, cap, rev_to));
            let rev_from: i64 = self.edges[to].len() as i64;
            self.edges[from].push((to, 0, rev_from-1));
        }
    }

    fn bfs(&mut self, start: usize) {
        self.level = vec![-1; self.n];
        self.level[start] = 0;
        let mut que: VecDeque<usize> = VecDeque::new();
        que.push_back(start);
        while let Some(v) = que.pop_front() {
            for i in 0..self.edges[v].len() {
                let e = self.edges[v][i];
                if e.1 > 0 && self.level[e.0] < 0 {
                    self.level[e.0] = self.level[v] + 1;
                    que.push_back(e.0);
                }
            }
        }
    }

    fn dfs(&mut self, v: usize, t: usize, f: usize) -> usize {
        if v == t {return f}
        for i in self.iter[v]..self.edges[v].len() {
            self.iter[v] = i;
            let e = self.edges[v][i];
            if e.1 > 0 && self.level[v] < self.level[e.0] {
                let d = self.dfs(e.0, t, min(f, e.1 as usize));
                if d > 0 {
                    self.edges[e.0][e.2 as usize].1 += d as i64;
                    self.edges[v][i].1 -= d as i64;
                    return d
                }
            }
        }
        return 0
    }

    fn max_flow(&mut self, start: usize, goal: usize) -> usize {
        let mut flow = 0;
        loop {
            self.bfs(start);
            if self.level[goal] < 0 {
                return flow
            }
            self.iter = vec![0; self.n];
            let mut f = self.dfs(start, goal, INF);
            while f > 0  {
                flow += f;
                f = self.dfs(start, goal, INF);
            }
        }
    }
}