#[allow(dead_code)]
struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
    size: Vec<usize>,
}

#[allow(dead_code)]
impl UnionFind {
    fn new(n: usize) -> UnionFind {
        let mut p = vec![0; n];
        for i in 0..n {
            p[i] = i;
        }
        return UnionFind {
            parent: p,
            rank: vec![0; n],
            size: vec![1; n],
        };
    }

    fn find(&mut self, x: usize) -> usize {
        if x == self.parent[x] {
            x
        } else {
            let p = self.parent[x];
            let pr = self.find(p);
            self.parent[x] = pr;
            pr
        }
    }

    fn same(&mut self, a: usize, b: usize) -> bool {
        self.find(a) == self.find(b)
    }

    fn unite(&mut self, a: usize, b: usize) {
        let a_root = self.find(a);
        let b_root = self.find(b);
        if self.rank[a_root] > self.rank[b_root] {
            self.parent[b_root] = a_root;
            self.size[a_root] += self.size[b_root];
        } else {
            self.parent[a_root] = b_root;
            self.size[b_root] += self.size[a_root];
            if self.rank[a_root] == self.rank[b_root] {
                self.rank[b_root] += 1;
            }
        }
    }

    fn get_size(&mut self, x: usize) -> usize {
        let root = self.find(x);
        self.size[root]
    }
}
