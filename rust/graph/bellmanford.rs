const INF: i64 = 1 << 61;


// adjacent list
struct Graph {
    edges: Vec<(usize, usize, i64)>, // adjacent list
    n: usize
}

impl Graph {
    fn new(n: usize) -> Self {
        Graph {
            edges: vec![],
            n: n
        }
    }

    fn add_costs(&mut self, from: usize, to: usize, cost: i64, directed: bool) {
        if directed {
            self.edges.push((from, to, cost));
        } else {
            self.edges.push((from, to, cost));
            self.edges.push((to, from, cost));
        }
    }

    fn bellmanford_search(&self, start: usize) -> Vec<i64> {
        let mut dist: Vec<i64> = vec![INF; self.n];
        dist[start] = 0;
        loop {
            let mut update: bool = false;
            for edge in &self.edges {
                let (from, to, cost) = *edge;
                if (dist[from] != INF) & (dist[to] > dist[from] + cost) {
                    dist[to] = dist[from] + cost;
                    update = true;
                }
            }
            if !update {
                break;
            }
        }
        return dist
    }

    fn bellmanford_search_negative_cycle(&self, start: usize) -> (bool, Vec<i64>) {
        // (true, dist) なら負の閉路を含む
        let mut dist: Vec<i64> = vec![INF; self.n];
        dist[start] = 0;
        for i in 0..self.n {
            for &(from, to, cost) in &self.edges{
                if (dist[from] != INF) & (dist[to] > dist[from] + cost) {
                    dist[to] = dist[from] + cost;
                    if i == self.n - 1{
                        return (true, dist);
                    }
                }
            }
        }
        return (false, dist);
    }
}

//adjacent matrix
struct Graph {
    edges: Vec<Vec<(usize, i64)>>, // adjacent matrix
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

    fn bellmanford_search(&self, start: usize) -> Vec<i64> {
        let mut dist: Vec<i64> = vec![INF; self.n];
        dist[start] = 0;
        let mut update: bool = true;
        while update {
            update = false;
            for from in 0..self.n {
                for edge in &self.edges[from] {
                    let (to, cost) = *edge;
                    if dist[to] > dist[from] + cost {
                        dist[to] = dist[from] + cost;
                        update = true;
                    }
                }
            }
        }
        return dist
    }

    fn bellmanford_search_negative_cycle(&self, start: usize) -> (bool, Vec<i64>) {
        // (true, dist) なら負の閉路を含む
        let mut dist: Vec<i64> = vec![INF; self.n];
        dist[start] = 0;
        let mut counter = 0;
        let mut update: bool = true;
        while update {
            update = false;
            for from in 0..self.n {
                for edge in &self.edges[from] {
                    let (to, cost) = *edge;
                    if (dist[from] != INF) & (dist[to] > dist[from] + cost) {
                        dist[to] = dist[from] + cost;
                        update = true;
                        counter += 1;
                    }
                }
            }
            if counter >= self.n * self.n {
                return (true, dist);
            }
        }
        return (false, dist);
    }
}