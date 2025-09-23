class AccountService {
    func withdraw(amount: Int) -> Bool { return true }
    func audit() { }
}
class Controller {
    func run() {
        let svc = AccountService()
        svc.withdraw(amount: 100)
        if true { svc?.withdraw(amount: 1) } else { self.audit() }
    }
}
let c = Controller()
c.run()
