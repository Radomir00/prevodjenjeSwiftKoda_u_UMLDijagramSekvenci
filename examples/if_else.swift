class PayPal { func pay(amount: Int) { } }
class Card   { func pay(amount: Int) { } }

class Checkout {
    func doPay(useCard: Bool) {
        if useCard {
            let c = Card()
            c.pay(amount: 100)
        } else {
            let p = PayPal()
            p.pay(amount: 100)
        }
    }
}
let ch = Checkout()
ch.doPay(useCard: true)
