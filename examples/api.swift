class Network { func request(path: String) { } }
class Api {
    let net = Network()
    func getUsers() { net.request(path: "/users") }
}
class App {
    func start() {
        let api = Api()
        api.getUsers()
    }
}
let app = App()
app.start()
