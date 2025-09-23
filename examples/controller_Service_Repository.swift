class Repository {
    func fetch(id: Int) { /* ... */ }
}
class Service {
    let repo = Repository()
    func getUser(id: Int) {
        repo.fetch(id: id)
    }
}
class Controller {
    func run() {
        let s = Service()
        s.getUser(id: 42)
    }
}
let c = Controller()
c.run()
