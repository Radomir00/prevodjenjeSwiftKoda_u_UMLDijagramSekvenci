class Repo { func save() {} }
class VC {
  func load() {
    for i in 0...2 {
      let r = Repo()
      r.save()
    }
    if true {
      print("yes")
    } else {
      print("no")
    }
  }
}
