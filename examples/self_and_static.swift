class Service { static func shared() {} }
class Controller {
  func run() {
    self.run()
    Service.shared()
  }
}
