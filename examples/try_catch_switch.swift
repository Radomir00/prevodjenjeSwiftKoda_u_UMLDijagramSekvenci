class Network { func request() throws {} }
class Controller {
  func run() {
    let net = Network()
    do { try net.request() } catch { print("failed") }
    let code = 2
    switch code { case 1: print("ONE"); case 2: print("TWO"); default: print("OTHER") }
  }
}
