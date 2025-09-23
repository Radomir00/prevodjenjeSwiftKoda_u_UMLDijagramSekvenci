class Cache { func get(key: String) { } }
class Service { func load(key: String) { } }

class Controller {
    var cache: Cache? = nil
    func run() {
        cache?.get(key: "u1")       
        let s = Service()
        s.load(key: "u1")
    }
}
let c = Controller()
c.run()
