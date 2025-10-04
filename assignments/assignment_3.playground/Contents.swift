import UIKit

struct Product {
    var id: Int
    var name: String
    var price: Double
    let category = Category.allCases.count
    var description: String
    
    enum Category: String, CaseIterable {
        case outwear
        case headwear
        case tshirts
        case pants
        case shirts
        case shoes
        case skirts
    }
}
