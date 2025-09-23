class Logger { func write(msg: String) { } }
class Repo {
    let log = Logger()
    func findAll() { log.write(msg: "SELECT *") }
}
class Service {
    let repo = Repo()
    func list() { repo.findAll() }
}
class Controller {
    func run() {
        let s = Service()
        s.list()
    }
}
let c = Controller()
c.run()
