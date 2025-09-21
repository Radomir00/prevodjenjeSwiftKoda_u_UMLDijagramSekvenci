class Service { func fetch() {} }
class Controller {
  func run() {
    let s = Service()
    s.fetch()
  }
}
