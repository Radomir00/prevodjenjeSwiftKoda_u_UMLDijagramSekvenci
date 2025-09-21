class Service { func fetch() {} ; static func sharedFetch() {} }

class Controller {
  func selfCall() { self.selfCall() }
  func run() {
    let s = Service()
    s.fetch()
    Service.sharedFetch()
    print("done")
  }
}
