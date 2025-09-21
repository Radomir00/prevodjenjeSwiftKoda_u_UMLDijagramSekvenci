class Service {
    func fetch() { /* ... */ }
}

class ViewController {
    func load() {
        let s = Service()
        s.fetch()
    }
}

func globalFunc() {
    print("Hello")
}

