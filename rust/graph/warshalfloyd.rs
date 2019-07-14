const INF: i64 = 1 << 61;
use std::cmp::min;


struct GraphWarshalFloyd {
    edges: Vec<Vec<i64>>,
    n: usize
}

impl GraphWarshalFloyd {
    fn new(n: usize) -> Self {
        GraphWarshalFloyd {
            edges: vec![vec![INF; n]; n],
            n: n
        }
    }

    fn add_costs(&mut self, from: usize, to: usize, cost: i64, directed: bool) {
        if directed {
            self.edges[from][to] = cost;
        } else {
            self.edges[from][to] = cost;
            self.edges[to][from] = cost;
        }
    }

    fn warshalfloyd(&self) -> (bool, Vec<Vec<i64>>) {
        // (true, dist) なら負の閉路を含む
        let mut dist: Vec<Vec<i64>> = vec![vec![INF; self.n]; self.n];
        for i in 0..self.n {
            for j in 0..self.n {
                dist[i][j] = self.edges[i][j]
            }
        }
        for i in 0..self.n {
            for j in 0..self.n {
                for k in 0..self.n {
                    if (dist[j][i] != INF) & (dist[i][k] != INF) {
                        dist[j][k] = min(dist[j][k], dist[j][i]+dist[i][k])
                    }
                }
            }
        }
        let mut has_negative_cycle = false;
        for i in 0..self.n {
            if dist[i][i] < 0 {
                has_negative_cycle = true;
            }
            dist[i][i] = 0;
        }
        return (has_negative_cycle, dist)
    }
}