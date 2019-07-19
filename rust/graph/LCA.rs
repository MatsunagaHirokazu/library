// TODO: verify AOJ: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C
const INF: usize = 1 << 61;

struct LCA {
    n: usize,
    logn: usize,
    edges: Vec<Vec<usize>>,
    parent: Vec<Vec<usize>>,
    depth: Vec<usize>
}

impl LCA {
    fn new(n: usize) -> Self {
        let logn = ((n as f32).log2().ceil() as usize) + 1;
        LCA {
            n,
            logn,
            edges: vec![Vec::new(); n],
            parent: vec![vec![INF; n]; logn],
            depth: vec![0; n]
        }
    }

    fn add_costs(&mut self, from: usize, to: usize) {
        self.edges[to].push(from);
        self.edges[from].push(to);
    }

    fn initialize(&mut self, root: usize) {
        self.dfs(root, INF, 0);
        for i in 0..self.logn-1 {
            for k in 0..self.n {
                let p = self.parent[i][k];
                if p != INF {
                    self.parent[i+1][k] = self.parent[i][p]
                }
            }
        }
    }

    fn dfs(&mut self, from: usize, to: usize, dep: usize) {
        self.parent[0][from] = to;
        self.depth[from] = dep;
        for i in  0..self.edges[from].len() {
            let edge = self.edges[from][i];
            if edge != to {
                self.dfs(edge, from, dep+1)
            }
        }
    }

    fn get_lca(&mut self, mut u: usize, mut v: usize) -> usize {
        if self.depth[u] > self.depth[v] {
            std::mem::swap(&mut u, &mut v);
        }
        let dep_diff = self.depth[v] - self.depth[u];
        for i in 0..self.logn {
            if (dep_diff >> i & 1) != 0 {
                v = self.parent[i][v]
            }
        }
        if u == v {return u;}
        for i in (0..self.logn).rev() {
            if self.parent[i][u] != self.parent[i][v] {
                u = self.parent[i][u];
                v = self.parent[i][v];
            }
        }
        return self.parent[0][u]
    }
}