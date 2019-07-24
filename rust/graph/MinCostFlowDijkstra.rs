const INF: i64 = 1 << 61;
use std::collections::BinaryHeap;
use std::cmp::min;

struct Graph {
    edges: Vec<Vec<(usize, i64, i64, i64)>>, // adjacent list
    n: usize
}

impl Graph {
    fn new(n: usize) -> Self {
        Graph {
            edges: vec![Vec::new(); n],
            n,
        }
    }

    fn add(&mut self, from: usize, to: usize, cap: i64, cost: i64, directed: bool) {
        // edge[from]: to, cap, cost, rev(逆辺)
        if directed {
            let rev_from: i64 = self.edges[to].len() as i64;
            self.edges[from].push((to, cap, cost, rev_from));
            let rev_to: i64 = self.edges[from].len() as i64;
            self.edges[to].push((from, 0, -cost, rev_to-1));
        } else {
            // TODO: must be verified
            let rev_from: i64 = self.edges[to].len() as i64;
            self.edges[from].push((to, cap, cost, rev_from));
            let rev_to: i64 = self.edges[from].len() as i64;
            self.edges[to].push((from, 0, -cost, rev_to-1));
            self.edges[to].push((from, cap, cost, rev_to));
            let rev_from: i64 = self.edges[to].len() as i64;
            self.edges[from].push((to, 0, -cost, rev_from-1));
        }
    }

    fn min_cost_flow(&mut self, start: usize, goal: usize, mut flow: i64) -> i64 {
        let mut res: i64 = 0;
        let mut potential: Vec<usize> = vec![0; self.n];
        let mut prev_vertex: Vec<usize> = vec![0; self.n];
        let mut prev_edge: Vec<usize> = vec![0; self.n];

        while flow > 0 {
            let mut dist: Vec<i64> = vec![INF; self.n];
            dist[start] = 0;
            let mut que: BinaryHeap<(i64, i64)> = BinaryHeap::new();
            que.push((0, start as i64));

            while let Some((k, v)) = que.pop() {
                let v: usize = -v as usize;
                if dist[v] < -k { continue }
                for (i, edge) in self.edges[v].iter().enumerate() {
                    let (to, cap, cost, _) = *edge;
                    if (cap > 0) & (dist[to] as i64 > dist[v] as i64 + cost + potential[v] as i64 - potential[to] as i64) {
                        dist[to] = dist[v] as i64 + cost + potential[v] as i64 - potential[to] as i64;
                        prev_vertex[to] = v;
                        prev_edge[to] = i;
                        que.push((-dist[to], -(to as i64)));
                    }
                }
            }

            if dist[goal] == INF {
                return -1
            }
            for i in 0..self.n {
                potential[i] += dist[i] as usize;
            }

            let mut d = flow;
            let mut v = goal;
            while v != start {
                d = min(d, self.edges[prev_vertex[v]][prev_edge[v]].1);
                v = prev_vertex[v];
            }

            flow -= d;
            res += d * (potential[goal] as i64);
            let mut v = goal;
            while v != start {
                self.edges[prev_vertex[v]][prev_edge[v]].1 -= d;
                let e = self.edges[prev_vertex[v]][prev_edge[v]];
                self.edges[v][e.3 as usize].1 += d;
                v = prev_vertex[v];
            }
        }
        return res
    }
}