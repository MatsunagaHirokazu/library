const INF: i64 = 1 << 61;
use std::collections::BinaryHeap;

struct Graph {
    edges: Vec<Vec<(usize, i64)>>, // adjacent list
    n: usize
}

impl Graph {
    fn new(n: usize) -> Self {
        Graph {
            edges: vec![Vec::new(); n],
            n: n
        }
    }

    fn add_costs(&mut self, from: usize, to: usize, cost: i64, directed: bool) {
        if directed {
            self.edges[from].push((to, cost));
        } else {
            self.edges[from].push((to, cost));
            self.edges[to].push((from, cost));
        }

    }

    fn dijkstra_search(&self, start: usize) -> (Vec<i64>, Vec<usize>) {
        let mut dist: Vec<i64> = vec![INF; self.n]; // Dijkstraなのでi64ではなくusizeの方がいいかも
        let mut visited: Vec<bool> = vec![false; self.n];
        let mut prev: Vec<usize> = vec![INF as usize; self.n]; //nodeを格納するのにusizeでないの気持ち悪い
        dist[start] = 0;
        let mut que: BinaryHeap<(i64, usize)> = BinaryHeap::new();
        que.push((0, start));
        while let Some((_, v)) = que.pop() {
            if visited[v] {
                continue
            }
            visited[v] = true;
            for edge in &self.edges[v] {
                let (u, cost) = *edge;
                if visited[u] {
                    continue
                }
                if dist[u] > dist[v] + cost {
                    dist[u] = dist[v] + cost;
                    prev[u] = v;
                    que.push(( -dist[u], u));
                }
            }
        }
        return (dist, prev)
    }

    fn dijkstra_shortest_path(&self, start: usize, goal: usize) -> Vec<usize> {
        let (dist, prev) = self.dijkstra_search(start);
        let mut shortest_path: Vec<usize>= vec![];
        let mut node = goal;
        while node != INF {
            shortest_path.push(node);
            node = prev[node];
        }
        shortest_path.reverse();
        return shortest_path
    }
}